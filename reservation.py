from dataclasses import dataclass


class ReservationError(Exception):
    """Base class for reservation related errors."""


class InvalidReservationError(ReservationError):
    """Raised when a reservation request is not valid."""


class NoAvailabilityError(ReservationError):
    """Raised when there is no space for the requested reservation."""


class ReservationNotFoundError(ReservationError):
    """Raised when attempting to cancel a non-existent reservation."""


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

    def make_reservation(self, name: str, time: int, people: int) -> Reservation:
        """Create a reservation if the request is valid and there is space."""
        if people <= 0:
            raise InvalidReservationError("Number of people must be positive")
        if time < self.config.open_hour or time > self.config.close_hour:
            raise InvalidReservationError(
                f"Time must be between {self.config.open_hour} and {self.config.close_hour}"
            )
        if not self.check_availability(time, people):
            raise NoAvailabilityError("No availability")

        reservation = Reservation(name, time, people)
        self.bookings.append(reservation)
        return reservation

    def check_availability(self, time, people):
        """Return True if the requested reservation fits into the schedule."""
        total_people = sum(
            res.people for res in self.bookings if res.time == time
        )
        return total_people + people <= self.config.max_capacity

    def cancel(self, name: str) -> Reservation:
        """Cancel a reservation by client name."""
        for i, booking in enumerate(self.bookings):
            if booking.name == name:
                return self.bookings.pop(i)
        raise ReservationNotFoundError("Reservation not found")


def main():
    """Demonstrates basic usage of the ReservationSystem class."""
    system = ReservationSystem()

    try:
        res = system.make_reservation("John", 18, 4)
        print(f"Added reservation: {res}")
        res = system.make_reservation("Alice", 18, 17)
        print(f"Added reservation: {res}")
    except ReservationError as exc:
        print(f"Reservation error: {exc}")

    print(system.bookings)
    try:
        cancelled = system.cancel("John")
        print(f"Cancelled reservation for {cancelled.name}")
    except ReservationError as exc:
        print(f"Cancellation error: {exc}")

    print(system.bookings)


if __name__ == "__main__":
    main()
