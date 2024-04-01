from typing import List

from ddd.infrastructure.repository.in_memory.in_memory_repository_base import (
    InMemoryRepositoryBase,
)
from unit_test.behaviour.domain.model.vehicle.ivehicle_repository import (
    IVehicleRepository,
)
from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle


class InMemoryVehicleRepository(InMemoryRepositoryBase[Vehicle], IVehicleRepository):
    def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
        with self._lock:
            return [vehicle for vehicle in self._entities.values() if vehicle.color in colors]
