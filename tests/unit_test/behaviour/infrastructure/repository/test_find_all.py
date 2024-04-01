from abc import ABC

from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.datastore.datastore_emulator_mixin import \
    DatastoreEmulatorMixin
from unit_test.behaviour.infrastructure.repository.datastore.vehicle_repository import \
    DatastoreVehicleRepository
from unit_test.behaviour.infrastructure.repository.in_memory.vehicle_repository import (
    InMemoryVehicleRepository,
)
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestFindAllBase(UnitTestCase, ABC):
    def setUp(self):
        self.vehicle_repository = None

    def test_returns_all(
        self,
    ):
        # arrange
        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_2 = Vehicle(id="test-id-2", color="green")
        self.vehicle_repository.save(vehicle_1)
        self.vehicle_repository.save(vehicle_2)

        # act
        all_vehicles = self.vehicle_repository.find_all()

        # assert
        self.assertIsNotNone(all_vehicles)
        self.assertEqual(2, len(all_vehicles))
        self.assertEqual([vehicle_1, vehicle_2], all_vehicles)


class TestFindAllInMemory(TestFindAllBase):
    def setUp(self):
        self.vehicle_repository = InMemoryVehicleRepository()


class TestFindAllDatastore(TestFindAllBase, DatastoreEmulatorMixin):
    def setUp(self):
        self.vehicle_repository = DatastoreVehicleRepository(client=self.datastore_client)
