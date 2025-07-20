from dataclasses import dataclass


@dataclass
class RestaurantConfig:
    """Configuration parameters for reservation rules."""

    open_hour: int = 12
    close_hour: int = 22
    max_capacity: int = 20


@dataclass
class Reservation:
    """Represents a single reservation."""

    name: str
    time: int
    people: int


class ReservationSystem:
    """Simple reservation management for a restaurant."""

    def __init__(self, config: RestaurantConfig | None = None):
        """Create a new reservation system with the given configuration."""
        # Allow custom configuration; fallback to defaults if none provided.
        self.config: RestaurantConfig = config or RestaurantConfig()
        # Store each booking as Reservation instances
        self.bookings: list[Reservation] = []

    def make_reservation(self, name, time, people):
        """Create a reservation if the request is valid and there is space."""
        if people <= 0:
            return "Error: Number of people must be positive"
        if time < self.config.open_hour or time > self.config.close_hour:
            return (
                f"Error: Time must be between {self.config.open_hour} "
                f"and {self.config.close_hour}"
            )
        if not self.check_availability(time, people):
            return "No availability"

        self.bookings.append(Reservation(name, time, people))
        return f"Reservation for {name} at {time}:00 for {people} people added"

    def check_availability(self, time, people):
        """Return True if the requested reservation fits into the schedule."""
        total_people = sum(
            res.people for res in self.bookings if res.time == time
        )
        return total_people + people <= self.config.max_capacity

    def cancel(self, name):
        """Cancel a reservation by client name."""
        for i, booking in enumerate(self.bookings):
            if booking.name == name:
                self.bookings.pop(i)
                return "Reservation cancelled"
        return "Reservation not found"


def main():
    """Demonstrates basic usage of the ReservationSystem class."""
    # Example of system using default configuration
    system = ReservationSystem()

    print(system.make_reservation("John", 18, 4))
    print(system.make_reservation("Alice", 18, 17))

    print(system.bookings)
    print(system.cancel("John"))
    print(system.bookings)


if __name__ == "__main__":
    main()
