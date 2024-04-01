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


class TestGetBase(UnitTestCase, ABC):
    def setUp(self):
        self.vehicle_repository = None

    def test_returns_when_entity_with_id_exists(
        self,
    ):
        # arrange
        vehicle = Vehicle(id="test-id", color="red")
        self.vehicle_repository.save(vehicle)

        # act
        vehicle = self.vehicle_repository.get(id="test-id")

        # assert
        self.assertIsNotNone(vehicle)
        self.assertEqual("test-id", vehicle.id)

    def test_returns_none_when_entity_with_id_dont_exist(
        self,
    ):
        # act
        vehicle = self.vehicle_repository.get(id="test-id")

        # assert
        self.assertIsNone(vehicle)


class TestGetInMemory(TestGetBase):
    def setUp(self):
        self.vehicle_repository = InMemoryVehicleRepository()


class TestGetDatastore(TestGetBase, DatastoreEmulatorMixin):
    def setUp(self):
        self.vehicle_repository = DatastoreVehicleRepository(client=self.datastore_client)
