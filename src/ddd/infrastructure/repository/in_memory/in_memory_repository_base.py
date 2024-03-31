from typing import Dict, List, TypeVar
from threading import Lock
import copy

from ddd.infrastructure.repository.irepository import IRepository

T = TypeVar('T')


class InMemoryRepositoryBase(IRepository[T]):
    def __init__(self):
        self._entities: Dict[str, T] = {}
        self._lock = Lock()

    def get(self, id: str) -> T:
        with self._lock:
            entity = self._entities.get(id)
            return copy.deepcopy(entity) if entity else None

    def save(self, entity: T) -> T:
        if not entity.id:
            raise AttributeError("The entity needs to have an ID.")
        with self._lock:
            # Assuming the entity has an 'id' attribute
            self._entities[entity.id] = copy.deepcopy(entity)
            return copy.deepcopy(entity)

    def find_all(self) -> List[T]:
        with self._lock:
            return [copy.deepcopy(entity) for entity in self._entities.values()]

    def delete(self, id: str):
        with self._lock:
            if id not in self._entities:
                raise KeyError(f"No entity found with ID: '{id}'")
            del self._entities[id]
