from abc import ABC

import pytest

from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.datastore.datastore_emulator_mixin import (
    DatastoreEmulatorMixin,
)
from unit_test.behaviour.infrastructure.repository.datastore.vehicle_repository import (
    DatastoreVehicleRepository,
)
from unit_test.behaviour.infrastructure.repository.in_memory.vehicle_repository import (
    InMemoryVehicleRepository,
)
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestSaveBase(UnitTestCase, ABC):
    def setUp(self):
        self.vehicle_repository = None

    def test_creates_when_dont_exist(
        self,
    ):
        # arrange
        vehicle = Vehicle(id="test-id", color="red")

        # act
        self.vehicle_repository.save(vehicle)

        found_vehicles = self.vehicle_repository.find_all()

        # assert
        self.assertEqual(1, len(found_vehicles))
        self.assertEqual(vehicle, found_vehicles[0])

    def test_updates_when_exists(
        self,
    ):
        # arrange
        vehicle = Vehicle(id="test-id", color="red")
        self.vehicle_repository.save(vehicle)
        vehicle.color = "green"

        # act
        self.vehicle_repository.save(vehicle)

        found_vehicles = self.vehicle_repository.find_all()

        # assert
        self.assertEqual(1, len(found_vehicles))
        self.assertEqual("green", found_vehicles[0].color)

    def test_raises_when_no_entity_id(
        self,
    ):
        # arrange
        vehicle = Vehicle(id=None, color="red")

        # act + assert
        with pytest.raises(AttributeError, match="The entity needs to have an ID."):
            self.vehicle_repository.save(vehicle)


class TestSaveInMemory(TestSaveBase):
    def setUp(self):
        self.vehicle_repository = InMemoryVehicleRepository()


class TestSaveDatastore(TestSaveBase, DatastoreEmulatorMixin):
    def setUp(self):
        self.vehicle_repository = DatastoreVehicleRepository(client=self.datastore_client)
