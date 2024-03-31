from unit_test.behaviour.domain.model.vehicle.vehicle import Vehicle
from unit_test.behaviour.infrastructure.repository.in_memory.repository import \
    InMemoryVehicleRepository
from unit_test.behaviour.unit_test_case import UnitTestCase


class TestFindAll(UnitTestCase):
    def test_returns_all(
        self,
    ):
        # arrange
        vehicle_repository = InMemoryVehicleRepository()

        vehicle_1 = Vehicle(id="test-id-1", color="red")
        vehicle_2 = Vehicle(id="test-id-2", color="green")
        vehicle_repository.save(vehicle_1)
        vehicle_repository.save(vehicle_2)

        # act
        all_vehicles = vehicle_repository.find_all()

        # assert
        self.assertIsNotNone(all_vehicles)
        self.assertEqual(2, len(all_vehicles))
        self.assertEqual([vehicle_1, vehicle_2], all_vehicles)
