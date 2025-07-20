# MesaMaster

Este proyecto ofrece un sistema sencillo de gestión de reservas para un
restaurante. La lógica de reservas se encuentra encapsulada en la clase
`ReservationSystem` y cada reserva se modela mediante el dataclass
`Reservation`. Las operaciones pueden lanzar excepciones específicas en caso
de error, lo que facilita un control de flujo claro y permite la reutilización
del código en diferentes contextos.

## Uso rápido

```bash
python reservation.py
```

El script ejecutará un pequeño ejemplo de creación y cancelación de
reservas. Para integrar la lógica en otras aplicaciones basta con importar la
clase `ReservationSystem` desde `reservation.py`.

Si se desean modificar parámetros como el horario de atención o la capacidad
máxima del local, puede pasarse un objeto `RestaurantConfig` al constructor
de `ReservationSystem`:

```python
from reservation import ReservationSystem, RestaurantConfig, ReservationError

config = RestaurantConfig(open_hour=11, close_hour=23, max_capacity=30)
system = ReservationSystem(config)

try:
    reservation = system.make_reservation("Bob", 20, 2)
    print(reservation)
except ReservationError as exc:
    print(exc)
```
