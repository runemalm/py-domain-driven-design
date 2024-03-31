import pytest

from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.in_memory.repository import \
    InMemoryVehicleRepository
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestDelete(UnitTestCase):
    def test_deletes_when_exists(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_2 = Vehicle(id="test-id-2", color="green")
        vehicle_repository.save(vehicle_1)
        vehicle_repository.save(vehicle_2)

        # act
        vehicle_repository.delete(id="test-id-1")

        # assert
        all_vehicles = vehicle_repository.find_all()
        self.assertIsNotNone(all_vehicles)
        self.assertEqual(1, len(all_vehicles))
        self.assertEqual([vehicle_2], all_vehicles)

    def test_raises_when_no_entity_with_that_id_exists(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_repository.save(vehicle_1)

        # act + assert
        with pytest.raises(KeyError, match="No entity found with ID: 'non-existing-id'"):
            vehicle_repository.delete(id="non-existing-id")
