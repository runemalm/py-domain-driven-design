from abc import ABC

import pytest

from ddd.domain.model.exceptions.entity_not_found_exception import (
    EntityNotFoundException,
)
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


class TestDeleteBase(UnitTestCase, ABC):
    def setUp(self):
        self.vehicle_repository = None

    def test_deletes_when_exists(
        self,
    ):
        # arrange
        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_2 = Vehicle(id="test-id-2", color="green")
        self.vehicle_repository.save(vehicle_1)
        self.vehicle_repository.save(vehicle_2)

        # act
        self.vehicle_repository.delete(id="test-id-1")

        # assert
        all_vehicles = self.vehicle_repository.find_all()
        self.assertIsNotNone(all_vehicles)
        self.assertEqual(1, len(all_vehicles))
        self.assertEqual([vehicle_2], all_vehicles)

    def test_raises_when_no_entity_with_that_id_exists(
        self,
    ):
        # arrange
        vehicle_1 = Vehicle(id="test-id-1", color="red")
        self.vehicle_repository.save(vehicle_1)

        # act + assert
        with pytest.raises(
            EntityNotFoundException, match="No entity found with ID: 'non-existing-id'"
        ):
            self.vehicle_repository.delete(id="non-existing-id")


class TestDeleteInMemory(TestDeleteBase):
    def setUp(self):
        self.vehicle_repository = InMemoryVehicleRepository()


class TestDeleteDatastore(TestDeleteBase, DatastoreEmulatorMixin):
    def setUp(self):
        self.vehicle_repository = DatastoreVehicleRepository(client=self.datastore_client)
