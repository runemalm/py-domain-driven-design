Using InMemoryRepositoryBase
-----------------------------

Here's an example demonstrating how to subclass `InMemoryRepositoryBase` for the `Vehicle` entity:

.. code-block:: python

    from typing import List
    from ddd.infrastructure.repository.in_memory.in_memory_repository_base import InMemoryRepositoryBase
    from carbusiness.domain.model.vehicle.ivehicle_repository import IVehicleRepository
    from carbusiness.domain.model.vehicle.vehicle import Vehicle

    class InMemoryVehicleRepository(InMemoryRepositoryBase[Vehicle], IVehicleRepository):
        def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
            with self._lock:
                return [vehicle for vehicle in self._entities.values() if vehicle.color in colors]

    # Creating a repository for Vehicle entities
    vehicle_repository = InMemoryVehicleRepository()

    # Adding some vehicles to the repository
    vehicle_repository.save(Vehicle(id="1", color="red"))
    vehicle_repository.save(Vehicle(id="2", color="blue"))
    vehicle_repository.save(Vehicle(id="3", color="red"))

    # Finding vehicles with the color red
    red_vehicles = vehicle_repository.find_with_colors(["red"])
    for vehicle in red_vehicles:
        print(f"Red Vehicle: ID {vehicle.id}, Color {vehicle.color}")
    # Output:
    # Red Vehicle: ID 1, Color red
    # Red Vehicle: ID 3, Color red

Using DatastoreRepositoryBase
-----------------------------

Here's an example demonstrating how to subclass `DatastoreRepositoryBase` for the `Vehicle` entity:

.. code-block:: python

    from google.cloud import datastore
    from ddd.infrastructure.repository.datastore.datastore_repository_base import DatastoreRepositoryBase
    from carbusiness.domain.model.vehicle.ivehicle_repository import IVehicleRepository
    from carbusiness.domain.model.vehicle.vehicle import Vehicle

    class DatastoreVehicleRepository(DatastoreRepositoryBase[Vehicle], IVehicleRepository):
        def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
            query = self.client.query(kind=self.kind)
            query.add_filter("color", "IN", colors)
            entities = list(query.fetch())
            return [self._from_datastore(entity) for entity in entities]

        def _from_datastore(self, entity: datastore.Entity) -> Vehicle:
            return Vehicle(id=entity.key.name, color=entity["color"])

        def _to_datastore(self, entity: Vehicle) -> dict:
            return {"color": entity.color}

    # Creating a repository for Vehicle entities
    vehicle_repository = DatastoreVehicleRepository(kind="Vehicle")

    # Adding some vehicles to the repository
    vehicle_repository.save(Vehicle(id="1", color="red"))
    vehicle_repository.save(Vehicle(id="2", color="blue"))
    vehicle_repository.save(Vehicle(id="3", color="red"))

    # Finding vehicles with the color red
    red_vehicles = vehicle_repository.find_with_colors(["red"])
    for vehicle in red_vehicles:
        print(f"Red Vehicle: ID {vehicle.id}, Color {vehicle.color}")
    # Output:
    # Red Vehicle: ID 1, Color red
    # Red Vehicle: ID 3, Color red
