class MockMetadata:
    """Minimal metadata facade mirroring cassandra.cluster.Metadata."""

    def __init__(self, state):
        self._state = state

    @property
    def keyspaces(self):
        return {
            name: MockKeyspaceMetadata(name, info)
            for name, info in self._state.keyspaces.items()
        }

    def get_keyspace(self, name):
        return self.keyspaces.get(name)

    def refresh(self):
        return self


class MockKeyspaceMetadata:
    """Represents keyspace metadata."""

    def __init__(self, name, info):
        self.name = name
        self.durable_writes = info.get("durable_writes", True)
        self.replication_strategy = info.get("replication", {})
        self.tables = {
            table_name: MockTableMetadata(name, table_name, table_info)
            for table_name, table_info in info.get("tables", {}).items()
        }
        self.user_types = info.get("types", {})
        self.views = {
            view_name: MockMaterializedViewMetadata(name, view_name, view_info)
            for view_name, view_info in info.get("views", {}).items()
        }

    def table(self, name):
        return self.tables.get(name)

    def view(self, name):
        return self.views.get(name)


def _resolve_primary_key_info(primary_key):
    if isinstance(primary_key, dict):
        partition = primary_key.get("partition", [])
        clustering = primary_key.get("clustering", [])
        combined = primary_key.get("all") or (partition + clustering)
        return partition, clustering, combined
    partition = list(primary_key[:1])
    clustering = list(primary_key[1:])
    return partition, clustering, list(primary_key)


class MockTableMetadata:
    """Represents table metadata."""

    def __init__(self, keyspace_name, table_name, table_info):
        self.keyspace = keyspace_name
        self.name = table_name
        schema = table_info.get("schema", {})
        self.columns = {
            column_name: MockColumnMetadata(column_name, column_type)
            for column_name, column_type in schema.items()
        }
        partition_names, clustering_names, primary_names = (
            _resolve_primary_key_info(table_info.get("primary_key", []))
        )
        self.partition_key = [
            self.columns[col] for col in partition_names if col in self.columns
        ]
        self.clustering_key = [
            self.columns[col] for col in clustering_names if col in self.columns
        ]
        self.primary_key = [
            self.columns[col] for col in primary_names if col in self.columns
        ]
        self.clustering_orders = table_info.get("clustering_orders", {})
        for column_name, column in self.columns.items():
            if column_name in self.clustering_orders:
                column.clustering_order = self.clustering_orders[column_name]
            else:
                column.clustering_order = None
        self.indexes = [
            {
                "name": idx.get("name"),
                "column": idx.get("column"),
            }
            for idx in table_info.get("indexes", []) or []
        ]
        self.options = table_info.get("options", {})

    def column(self, name):
        return self.columns.get(name)


class MockMaterializedViewMetadata:
    """Represents materialized view metadata."""

    def __init__(self, keyspace_name, view_name, view_info):
        self.keyspace = keyspace_name
        self.name = view_name
        self.base_table = view_info.get("base_table")
        self.base_keyspace = view_info.get("base_keyspace", keyspace_name)
        self.where_clause = view_info.get("where_clause")
        self.primary_key = view_info.get("primary_key", [])
        self.options = view_info.get("options", {})


class MockColumnMetadata:
    """Represents column metadata."""

    def __init__(self, name, cql_type):
        self.name = name
        self.cql_type = cql_type
        self.typestring = cql_type
        self.clustering_order = None


__all__ = [
    "MockMetadata",
    "MockKeyspaceMetadata",
    "MockTableMetadata",
    "MockMaterializedViewMetadata",
    "MockColumnMetadata",
]
