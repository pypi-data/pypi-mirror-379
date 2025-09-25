"""This module implements tables, the central place for accessing and manipulating documents."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import TYPE_CHECKING, Any, cast

from bear_dereth.lru_cache import LRUCache
from bear_dereth.query._protocol import QueryProtocol

from .models import Document

if TYPE_CHECKING:
    from .common import DataShape
    from .models import Storage


def to_type[T, T2](tbl: dict, t: Callable[..., T], t2: Callable[..., T2], unique: set[Any]) -> list[T]:
    """Convert documents in a table to a specific type, filtering by unique IDs in a set.

    Args:
        tbl: the table containing documents
        t: a callable that converts a document and its ID to type T
        t2: a callable that converts a document ID to type T2
        unique: a set of unique document IDs to filter by

    Returns:
        a list of documents of type T
    """
    return [t(doc, t2(doc_id)) for doc_id, doc in tbl.items() if doc_id in unique]


class Table:
    """Represents a single table.

    It provides methods for accessing and manipulating documents.

    Query Cache:

        As an optimization, a query cache is implemented using a
        :class:`~tinydb.utils.LRUCache`. This class mimics the interface of
        a normal ``dict``, but starts to remove the least-recently used entries
        once a threshold is reached.

        The query cache is updated on every search operation. When writing
        data, the whole cache is discarded as the query results may have
        changed.

    Customization:

        For customization, the following class variables can be set:

        - ``document_class`` defines the class that is used to represent
          documents,
        - ``id_class`` defines the class that is used to represent
          document IDs,
        - ``query_cache_class`` defines the class that is used for the query
          cache
        - ``default_query_cache_capacity`` defines the default capacity of
          the query cache

    Args:
        storage: the storage instance to use
        name: the name of the table
        cache_size: the maximum number of queries to cache
        persist_empty: whether to persist an empty table to the storage
    Returns:
        a new table instance
    """

    document_class = Document
    id_class = int
    query_cache_class = LRUCache
    default_query_cache_capacity = 10

    def __init__(
        self,
        storage: Storage,
        name: str,
        cache_size: int = default_query_cache_capacity,
        persist_empty: bool = False,
    ) -> None:
        """Create a table instance."""
        self._storage: Storage = storage
        self._name: str = name
        self._query_cache = self.query_cache_class[QueryProtocol, list[self.document_class]](capacity=cache_size)

        self._next_id = None
        if persist_empty:
            self._update_table(lambda table: table.clear())

    def __repr__(self):
        args: list[str] = [
            f"name={self.name!r}",
            f"total={len(self)}",
            f"storage={self._storage}",
        ]
        return "<{} {}>".format(type(self).__name__, ", ".join(args))

    @property
    def name(self) -> str:
        """Get the table name."""
        return self._name

    @property
    def storage(self) -> Storage:
        """Get the table storage instance."""
        return self._storage

    def insert(self, document: Mapping | Any) -> int:
        """Insert a new document into the table.

        Args:
            document: the document to insert
        Returns:
            the inserted document's ID
        """
        if not isinstance(document, Mapping):
            raise TypeError("Document is not a Mapping")

        if isinstance(document, self.document_class):
            doc_id: int = document.doc_id
            self._next_id = None  # We also reset the stored next ID so the next insert won't re-use document IDs by accident when storing an old value
        else:
            doc_id = self._get_next_id()

        def updater(table: dict) -> None:
            if doc_id in table:
                raise ValueError(f"Document with ID {doc_id!s} already exists")
            table[doc_id] = dict(document)

        self._update_table(updater)
        return doc_id

    def insert_multiple(self, documents: Iterable[Mapping]) -> list[int]:
        """Insert multiple documents into the table.

        Args:
            documents: an iterable of documents to insert
        Returns:
            a list containing the inserted documents' IDs
        """
        doc_ids: list[int] = []

        def updater(table: dict) -> None:
            for document in documents:
                if not isinstance(document, Mapping):
                    raise TypeError("Document is not a Mapping")

                if isinstance(document, self.document_class):
                    if document.doc_id in table:
                        raise ValueError(f"Document with ID {document.doc_id!s} already exists")

                    doc_id: int = document.doc_id
                    doc_ids.append(doc_id)
                    table[doc_id] = dict(document)
                    continue

                doc_id = self._get_next_id()
                doc_ids.append(doc_id)
                table[doc_id] = dict(document)

        self._update_table(updater)
        return doc_ids

    def all(self) -> list[Document]:
        """Get all documents stored in the table.

        Returns:
            list of all documents using iterator and list constructor
        """
        return list(iter(self))

    def search(self, cond: QueryProtocol) -> list[Document]:
        """Search for all documents matching a 'where' cond.

        :param cond: the condition to check against
        :returns: list of matching documents
        """
        cached_results = self._query_cache.get(cond)
        if cached_results is not None:
            return cached_results[:]
        table: dict[str, DataShape] = self._read_table()
        matched_docs: set[str] = {str(doc_id) for doc_id, doc in table.items() if cond(doc)}
        docs = to_type(table, self.document_class, self.id_class, matched_docs)

        if cond.is_cacheable:
            self._query_cache[cond] = docs[:]  # Update the query cache
        return docs

    def get(
        self,
        cond: QueryProtocol | None = None,
        doc_id: int | None = None,
        doc_ids: list | None = None,
    ):
        """Get exactly one document specified by a query or a document ID.

        However, if multiple document IDs are given then returns all
        documents in a list.

        Returns ``None`` if the document doesn't exist.

        Args:
            cond: the condition to check against
            doc_id: the document ID to look for
            doc_ids: a list of document IDs to look for
        Returns:
            the matching document, a list of documents or None
        """
        table: dict[str, DataShape] = self._read_table()
        if doc_id is not None:
            raw_doc: DataShape | None = table.get(str(doc_id), None)
            if raw_doc is None:
                return None
            return self.document_class(raw_doc, doc_id)

        if doc_ids is not None:
            doc_ids_set: set[str] = {str(doc_id) for doc_id in doc_ids}
            return to_type(table, self.document_class, self.id_class, doc_ids_set)

        if cond is not None:
            for doc_id_, doc in table.items():
                if cond(doc):
                    return self.document_class(doc, self.id_class(doc_id_))

            return None

        raise RuntimeError("You have to pass either cond or doc_id or doc_ids")

    def contains(self, cond: QueryProtocol | None = None, doc_id: int | None = None) -> bool:
        """Check whether the database contains a document matching a query or an ID.

        If ``doc_id`` is set, it checks if the db contains the specified ID.

        Args:
            cond: the condition to check against
            doc_id: the document ID to look for
        Returns:
            whether a matching document exists
        """
        if doc_id is not None:
            return self.get(doc_id=doc_id) is not None

        if cond is not None:
            return self.get(cond) is not None

        raise RuntimeError("You have to pass either cond or doc_id")

    def update(
        self,
        fields: Mapping | Callable[[Mapping], None],
        cond: QueryProtocol | None = None,
        doc_ids: Iterable[int] | None = None,
    ) -> list[int]:
        """Update all matching documents to have a given set of fields.

        Args:
            fields: the fields to update or a function that performs the update
            cond: the condition to check against
            doc_ids: a list of document IDs
        Returns:
            a list containing the updated document's ID
        """

        def perform_update(table: dict, doc_id: int) -> None:
            if callable(fields):
                fields(table[doc_id])
            else:
                table[doc_id].update(fields)

        if doc_ids is not None:
            updated_ids = list(doc_ids)

            def updater(table: dict) -> None:
                for doc_id in updated_ids:
                    perform_update(table, doc_id)

            self._update_table(updater)
            return updated_ids

        if cond is not None:
            updated_ids = []

            def updater(table: dict) -> None:
                _cond: QueryProtocol = cond
                for doc_id in list(table.keys()):
                    if _cond(table[doc_id]):
                        updated_ids.append(doc_id)
                        perform_update(table, doc_id)

            self._update_table(updater)
            return updated_ids

        updated_ids: list[int] = []

        def updater(table: dict) -> None:
            for doc_id in list(table.keys()):
                updated_ids.append(doc_id)
                perform_update(table, doc_id)

        self._update_table(updater)
        return updated_ids

    def update_multiple(
        self,
        updates: Iterable[tuple[Mapping | Callable[[Mapping], None], QueryProtocol]],
    ) -> list[int]:
        """Update all matching documents to have a given set of fields.

        :returns: a list containing the updated document's ID
        """

        def perform_update(fields: Any, table: dict, doc_id: int) -> None:
            if callable(fields):
                fields(table[doc_id])  # Update documents by calling the update function provided by the user
            else:
                table[doc_id].update(fields)  # Update documents by setting all fields from the provided data

        updated_ids: list[int] = []

        def updater(table: dict) -> None:
            tbl_keys = list(table.keys())
            for doc_id in tbl_keys:
                for fields, cond in updates:
                    if cond(table[doc_id]):
                        updated_ids.append(doc_id)
                        perform_update(fields, table, doc_id)

        # Perform the update operation (see _update_table for details)
        self._update_table(updater)

        return updated_ids

    def upsert(self, document: Mapping, cond: QueryProtocol | None = None) -> list[int]:
        """Update documents, if they exist, insert them otherwise.

        Note: This will update *all* documents matching the query. Document
        argument can be a tinydb.table.Document object if you want to specify a
        doc_id.

        Args:
            document: the document to insert or update
            cond: the condition to check against
        Returns:
            a list containing the inserted or updated document's ID
        """
        if isinstance(document, self.document_class) and hasattr(document, "doc_id"):
            doc_ids: list[int] | None = [document.doc_id]
        else:
            doc_ids = None

        if doc_ids is None and cond is None:
            # Make sure we can actually find a matching document
            raise ValueError(
                "If you don't specify a search query, you must specify a doc_id. Hint: use a table.Document object."
            )

        try:
            updated_docs: list[int] | None = self.update(document, cond, doc_ids)  # Perform the update operation
        except KeyError:
            updated_docs = None  # This happens when a doc_id is specified, but it's missing

        if updated_docs:  # If documents have been updated: return their IDs
            return updated_docs

        # There are no documents that match the specified query -> insert the
        # data as a new document
        return [self.insert(document)]

    def remove(
        self,
        cond: QueryProtocol | None = None,
        doc_ids: Iterable[int] | None = None,
    ) -> list[int]:
        """Remove all matching documents.

        :param cond: the condition to check against
        :param doc_ids: a list of document IDs
        :returns: a list containing the removed documents' ID
        """
        if doc_ids is not None:
            # This function returns the list of IDs for the documents that have
            # been removed. When removing documents identified by a set of
            # document IDs, it's this list of document IDs we need to return
            # later.
            # We convert the document ID iterator into a list, so we can both
            # use the document IDs to remove the specified documents and
            # to return the list of affected document IDs
            removed_ids: list[int] = list(doc_ids)

            def updater(table: dict) -> None:
                for doc_id in removed_ids:
                    table.pop(doc_id)

            self._update_table(updater)  # Perform the remove operation

            return removed_ids

        if cond is not None:
            removed_ids = []

            # This updater function will be called with the table data
            # as its first argument. See ``Table._update`` for details on this
            # operation
            def updater(table: dict) -> None:
                # We need to convince MyPy (the static type checker) that
                # the ``cond is not None`` invariant still holds true when
                # the updater function is called
                _cond = cast("QueryProtocol", cond)

                # We need to convert the keys iterator to a list because
                # we may remove entries from the ``table`` dict during
                # iteration and doing this without the list conversion would
                # result in an exception (RuntimeError: dictionary changed size
                # during iteration)
                for doc_id in list(table.keys()):
                    if _cond(table[doc_id]):
                        removed_ids.append(doc_id)  # Add document ID to list of removed document IDs
                        table.pop(doc_id)  # Remove document from the table

            self._update_table(updater)  # Perform the remove operation
            return removed_ids
        raise RuntimeError("Use truncate() to remove all documents")

    def truncate(self) -> None:
        """Truncate the table by removing all documents."""
        self._update_table(lambda table: table.clear())  # Update the table by resetting all data
        self._next_id = None  # Reset document ID counter

    def count(self, cond: QueryProtocol) -> int:
        """Count the documents matching a query.

        Args:
            cond: the condition to check against
        Returns:
            the number of matching documents
        """
        return len(self.search(cond))

    def clear_cache(self) -> None:
        """Clear the query cache."""
        self._query_cache.clear()

    def __len__(self) -> int:
        """Count the total number of documents in this table."""
        return len(self._read_table())

    def __iter__(self) -> Iterator[Document]:
        """Iterate over all documents stored in the table.

        Returns:
            An iterator that yields all documents in the table.
        """
        for doc_id, doc in self._read_table().items():  # Iterate all documents and their IDs
            yield self.document_class(doc, self.id_class(doc_id))

    def _get_next_id(self) -> int:
        """Return the ID for a newly inserted document."""
        if self._next_id is not None:  # If we already know the next ID
            next_id: int = self._next_id
            self._next_id = next_id + 1
            return next_id

        # Determine the next document ID by finding out the max ID value
        # of the current table documents

        table: dict[str, DataShape] = self._read_table()

        if not table:  # If the table is empty, set the initial ID
            next_id = 1
            self._next_id = next_id + 1
            return next_id

        max_id: int = max(self.id_class(i) for i in table)
        next_id = max_id + 1

        # The next ID we will return AFTER this call needs to be larger than
        # the current next ID we calculated
        self._next_id = next_id + 1

        return next_id

    def _read_table(self) -> dict[str, DataShape]:
        """Read the table data from the underlying storage.

        Documents and doc_ids are NOT yet transformed, as
        we may not want to convert *all* documents when returning
        only one document for example.
        """
        tables: DataShape | None = self._storage.read()

        if tables is None:
            return {}  # The database is empty

        try:
            table: dict[str, Any] = tables[self.name]  # Retrieve the current table's data
        except KeyError:
            return {}  # The table does not exist yet, so it is empty
        return table

    def _update_table(self, updater: Callable[[dict[int, DataShape]], None]) -> None:
        """Perform a table update operation.

        The storage interface used here only allows to read/write the
        complete database data, but not modifying only portions of it. Thus,
        to only update portions of the table data, we first perform a read
        operation, perform the update on the table data and then write
        the updated data back to the storage.

        As a further optimization, we don't convert the documents into the
        document class, as the table data will *not* be returned to the user.

        Args:
            updater: A callable that takes the table data as its only
                     argument and performs the update operation on it.
        """
        tables: DataShape | None = self._storage.read()
        if tables is None:
            tables = {}  # The database is empty

        try:
            raw_table: dict[str, Any] = tables[self.name]
        except KeyError:
            raw_table = {}  # The table does not exist yet, so it is empty

        table: dict[int, Any] = {self.id_class(doc_id): doc for doc_id, doc in raw_table.items()}
        updater(table)

        # Convert the document IDs back to strings.
        # This is required as some storages (most notably the JSON file format)
        # don't support IDs other than strings.
        tables[self.name] = {str(doc_id): doc for doc_id, doc in table.items()}
        self._storage.write(tables)  # Write the newly updated data back to the storage
        self.clear_cache()  # Clear the query cache, as the table contents have changed


__all__ = ["Document", "Table"]
