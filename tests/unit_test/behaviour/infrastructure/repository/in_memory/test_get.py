from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.in_memory.repository import \
    InMemoryVehicleRepository
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestGet(UnitTestCase):
    def test_returns_when_entity_with_id_exists(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle = Vehicle(id="test-id", color="red")
        vehicle_repository.save(vehicle)

        # act
        vehicle = vehicle_repository.get(id="test-id")

        # assert
        self.assertIsNotNone(vehicle)
        self.assertEqual("test-id", vehicle.id)

    def test_returns_none_when_entity_with_id_dont_exist(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        # act
        vehicle = vehicle_repository.get(id="test-id")

        # assert
        self.assertIsNone(vehicle)
