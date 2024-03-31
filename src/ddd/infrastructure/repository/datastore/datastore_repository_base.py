from typing import List, TypeVar

from ddd.infrastructure.repository.irepository import IRepository

T = TypeVar("T")


class DatastoreRepositoryBase(IRepository[T]):
    def get(self, id: str) -> T:
        raise NotImplementedError()

    def save(self, entity: T) -> T:
        raise NotImplementedError()

    def find_all(self) -> List[T]:
        raise NotImplementedError()

    def delete(self, id: str):
        raise NotImplementedError()
