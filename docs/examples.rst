The IRepository Interface
-------------------------

The ``IRepository`` interface provides a template for implementing basic CRUD operations in repository classes. It uses generics to allow for flexibility in working with different entity types while maintaining type safety:

.. code-block:: python

    from abc import ABC, abstractmethod
    from typing import Generic, List, TypeVar

    T = TypeVar("T")

    class IRepository(ABC, Generic[T]):
        @abstractmethod
        def get(self, id: str) -> T:
            pass

        @abstractmethod
        def save(self, entity: T) -> T:
            pass

        @abstractmethod
        def find_all(self) -> List[T]:
            pass

        @abstractmethod
        def delete(self, id: str):
            pass

Extending the IRepository interface
-----------------------------------

To create a custom repository interface, you can extend the generic ``IRepository`` interface and add any domain-specific methods that are needed. For example, here's how you can define a custom repository interface for the ``Vehicle`` entity:

.. code-block:: python

    from typing import List
    from abc import ABC, abstractmethod
    from motorbusiness.domain.model.vehicle.vehicle import Vehicle
    from ddd.infrastructure.repository.irepository import IRepository

    class IVehicleRepository(IRepository[Vehicle], ABC):
        @abstractmethod
        def find_with_colors(self, colors: List[str]) -> List[Vehicle]:
            """
            Find vehicles by a list of colors.

            :param colors: List of colors to search for.
            :return: List of vehicles with the specified colors.
            """
            pass

In this example, the ``IVehicleRepository`` interface extends ``IRepository[Vehicle]`` to indicate that it is a repository for ``Vehicle`` entities. The ``find_with_colors`` method is an abstract method that must be implemented by any concrete class that inherits from ``IVehicleRepository``. This method is designed to return a list of ``Vehicle`` instances that match any of the specified colors.


Using InMemoryRepositoryBase
-----------------------------

Here's an example demonstrating how to subclass `InMemoryRepositoryBase` for the `Vehicle` entity:

.. code-block:: python

    from typing import List
    from ddd.infrastructure.repository.in_memory.in_memory_repository_base import InMemoryRepositoryBase
    from motorbusiness.domain.model.vehicle.ivehicle_repository import IVehicleRepository
    from motorbusiness.domain.model.vehicle.vehicle import Vehicle

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
    from motorbusiness.domain.model.vehicle.ivehicle_repository import IVehicleRepository
    from motorbusiness.domain.model.vehicle.vehicle import Vehicle

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
