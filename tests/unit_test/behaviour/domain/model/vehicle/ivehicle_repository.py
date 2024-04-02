from abc import abstractmethod
from typing import List

from ddd.infrastructure.repository.irepository import IRepository
from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle


class IVehicleRepository(IRepository[Vehicle]):
    @abstractmethod
    def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
        pass
