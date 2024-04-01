from typing import List

from google.cloud import datastore

from ddd.infrastructure.repository.datastore.datastore_repository_base import (
    DatastoreRepositoryBase,
)
from unit_test.behaviour.domain.model.vehicle.ivehicle_repository import (
    IVehicleRepository,
)
from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle


class DatastoreVehicleRepository(DatastoreRepositoryBase[Vehicle], IVehicleRepository):
    def __init__(self, client: datastore.Client = None):
        super().__init__(kind="Vehicle", client=client)

    def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
        query = self.client.query(kind=self.kind)
        query.add_filter("color", "IN", colors)
        entities = list(query.fetch())
        return [self._from_datastore(entity) for entity in entities]

    def _from_datastore(self, entity: datastore.Entity) -> Vehicle:
        return Vehicle(id=entity.key.name, color=entity["color"])

    def _to_datastore(self, entity: Vehicle) -> dict:
        return {"color": entity.color}
