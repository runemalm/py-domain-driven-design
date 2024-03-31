from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar('T')


class DatastoreRepositoryBase(IRepository[T]):
    def get_by_id(self, id: str) -> T:
        raise NotImplementedError()

    def save(self, entity: T) -> T:
        raise NotImplementedError()

    def find_all(self) -> List[T]:
        raise NotImplementedError()

    def delete(self, id: str):
        raise NotImplementedError()
