# MesaMaster

Este proyecto ofrece un sistema sencillo de gestión de reservas para un
restaurante. La lógica de reservas se encuentra encapsulada en la clase
`ReservationSystem` y cada reserva se modela mediante el dataclass
`Reservation`, lo que facilita la reutilización y la posibilidad de realizar
pruebas unitarias.

## Uso rápido

```bash
python reservation.py
```

El script ejecutará un pequeño ejemplo de creación y cancelación de
reservas. Para integrar la lógica en otras aplicaciones basta con importar la
clase `ReservationSystem` desde `reservation.py`.
