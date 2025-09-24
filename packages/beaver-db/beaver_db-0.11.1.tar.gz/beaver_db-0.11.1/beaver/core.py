import sqlite3
import threading

from .dicts import DictManager
from .lists import ListManager
from .channels import ChannelManager
from .collections import CollectionManager
from .queues import QueueManager


class BeaverDB:
    """
    An embedded, multi-modal database in a single SQLite file.
    This class manages the database connection and table schemas.
    """

    def __init__(self, db_path: str, timeout:float=30.0):
        """
        Initializes the database connection and creates all necessary tables.

        Args:
            db_path: The path to the SQLite database file.
        """
        self._db_path = db_path
        # Enable WAL mode for better concurrency between readers and writers
        self._conn = sqlite3.connect(self._db_path, check_same_thread=False, timeout=timeout)
        self._conn.execute("PRAGMA journal_mode=WAL;")
        self._conn.row_factory = sqlite3.Row
        self._channels: dict[str, ChannelManager] = {}
        self._channels_lock = threading.Lock()
        # Add a cache and lock for CollectionManager singletons
        self._collections: dict[str, CollectionManager] = {}
        self._collections_lock = threading.Lock()

        # Initialize the schemas
        self._create_all_tables()

    def _create_all_tables(self):
        """Initializes all required tables in the database file."""
        with self._conn:
            self._create_pubsub_table()
            self._create_list_table()
            self._create_collections_table()
            self._create_fts_table()
            self._create_trigrams_table()
            self._create_edges_table()
            self._create_versions_table()
            self._create_dict_table()
            self._create_priority_queue_table()
            self._create_ann_indexes_table()
            self._create_ann_pending_log_table()
            self._create_ann_deletions_log_table()
            self._create_ann_id_mapping_table()

    def _create_ann_indexes_table(self):
        """Creates the table to store the serialized base ANN index."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS _beaver_ann_indexes (
                collection_name TEXT PRIMARY KEY,
                index_data BLOB,
                base_index_version INTEGER NOT NULL DEFAULT 0
            )
            """
        )

    def _create_ann_pending_log_table(self):
        """Creates the log for new vector additions."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS _beaver_ann_pending_log (
                collection_name TEXT NOT NULL,
                str_id TEXT NOT NULL,
                PRIMARY KEY (collection_name, str_id)
            )
            """
        )

    def _create_ann_deletions_log_table(self):
        """Creates the log for vector deletions (tombstones)."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS _beaver_ann_deletions_log (
                collection_name TEXT NOT NULL,
                int_id INTEGER NOT NULL,
                PRIMARY KEY (collection_name, int_id)
            )
            """
        )

    def _create_ann_id_mapping_table(self):
        """Creates the table to map string IDs to integer IDs for Faiss."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS _beaver_ann_id_mapping (
                collection_name TEXT NOT NULL,
                str_id TEXT NOT NULL,
                int_id INTEGER PRIMARY KEY AUTOINCREMENT,
                UNIQUE(collection_name, str_id)
            )
            """
        )

    def _create_priority_queue_table(self):
        """Creates the priority queue table and its performance index."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_priority_queues (
                queue_name TEXT NOT NULL,
                priority REAL NOT NULL,
                timestamp REAL NOT NULL,
                data TEXT NOT NULL
            )
            """
        )
        self._conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_priority_queue_order
            ON beaver_priority_queues (queue_name, priority ASC, timestamp ASC)
            """
        )

    def _create_dict_table(self):
        """Creates the namespaced dictionary table."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_dicts (
                dict_name TEXT NOT NULL,
                key TEXT NOT NULL,
                value TEXT NOT NULL,
                expires_at REAL,
                PRIMARY KEY (dict_name, key)
            )
        """
        )

    def _create_pubsub_table(self):
        """Creates the pub/sub log table."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_pubsub_log (
                timestamp REAL PRIMARY KEY,
                channel_name TEXT NOT NULL,
                message_payload TEXT NOT NULL
            )
        """
        )
        self._conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_pubsub_channel_timestamp
            ON beaver_pubsub_log (channel_name, timestamp)
        """
        )

    def _create_list_table(self):
        """Creates the lists table."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_lists (
                list_name TEXT NOT NULL,
                item_order REAL NOT NULL,
                item_value TEXT NOT NULL,
                PRIMARY KEY (list_name, item_order)
            )
        """
        )

    def _create_collections_table(self):
        """Creates the main table for storing documents and vectors."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_collections (
                collection TEXT NOT NULL,
                item_id TEXT NOT NULL,
                item_vector BLOB,
                metadata TEXT,
                PRIMARY KEY (collection, item_id)
            )
        """
        )

    def _create_fts_table(self):
        """Creates the virtual FTS table for full-text search."""
        self._conn.execute(
            """
            CREATE VIRTUAL TABLE IF NOT EXISTS beaver_fts_index USING fts5(
                collection,
                item_id,
                field_path,
                field_content,
                tokenize = 'porter'
            )
        """
        )

    def _create_trigrams_table(self):
        """Creates the table for the fuzzy search trigram index."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_trigrams (
                collection TEXT NOT NULL,
                item_id TEXT NOT NULL,
                field_path TEXT NOT NULL,
                trigram TEXT NOT NULL,
                PRIMARY KEY (collection, field_path, trigram, item_id)
            )
            """
        )
        self._conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_trigram_lookup
            ON beaver_trigrams (collection, trigram, field_path)
            """
        )

    def _create_edges_table(self):
        """Creates the table for storing relationships between documents."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_edges (
                collection TEXT NOT NULL,
                source_item_id TEXT NOT NULL,
                target_item_id TEXT NOT NULL,
                label TEXT NOT NULL,
                metadata TEXT,
                PRIMARY KEY (collection, source_item_id, target_item_id, label)
            )
        """
        )

    def _create_versions_table(self):
        """Creates a table to track the version of each collection for caching."""
        self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS beaver_collection_versions (
                collection_name TEXT PRIMARY KEY,
                version INTEGER NOT NULL DEFAULT 0
            )
        """
        )

    def close(self):
        """Closes the database connection."""
        if self._conn:
            # Cleanly shut down any active polling threads before closing
            with self._channels_lock:
                for channel in self._channels.values():
                    channel.close()
            self._conn.close()

    # --- Factory and Passthrough Methods ---

    def dict(self, name: str) -> DictManager:
        """Returns a wrapper object for interacting with a named dictionary."""
        if not isinstance(name, str) or not name:
            raise TypeError("Dictionary name must be a non-empty string.")

        return DictManager(name, self._conn)

    def list(self, name: str) -> ListManager:
        """Returns a wrapper object for interacting with a named list."""
        if not isinstance(name, str) or not name:
            raise TypeError("List name must be a non-empty string.")

        return ListManager(name, self._conn)

    def queue(self, name: str) -> QueueManager:
        """Returns a wrapper object for interacting with a persistent priority queue."""
        if not isinstance(name, str) or not name:
            raise TypeError("Queue name must be a non-empty string.")

        return QueueManager(name, self._conn)

    def collection(self, name: str) -> CollectionManager:
        """
        Returns a singleton CollectionManager instance for interacting with a
        document collection.
        """
        if not isinstance(name, str) or not name:
            raise TypeError("Collection name must be a non-empty string.")

        # Use a thread-safe lock to ensure only one CollectionManager object is
        # created per name. This is crucial for managing the in-memory state
        # of the vector index consistently.
        with self._collections_lock:
            if name not in self._collections:
                self._collections[name] = CollectionManager(name, self._conn)
            return self._collections[name]

    def channel(self, name: str) -> ChannelManager:
        """
        Returns a singleton Channel instance for high-efficiency pub/sub.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Channel name must be a non-empty string.")

        # Use a thread-safe lock to ensure only one Channel object is created per name.
        with self._channels_lock:
            if name not in self._channels:
                self._channels[name] = ChannelManager(name, self._conn, self._db_path)
            return self._channels[name]
