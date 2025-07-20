def make_reservation(name, time, people):
    if people <= 0:
        return "Error: Number of people must be positive"
    if time < 12 or time > 22:
        return "Error: Time must be between 12 and 22"
    print(f"Reservation for {name} at {time}:00 for {people} people")
    return "Reservation successful"


def check_availability(time, people, bookings):
    total_people = 0
    for b in bookings:
        if b[1] == time:
            total_people += b[2]
    if total_people + people > 20:
        return False
    return True


def cancel(name, bookings):
    for i in range(len(bookings)):
        if bookings[i][0] == name:
            bookings.pop(i)
            return "Reservation cancelled"
    return "Reservation not found"


# Uso de las funciones
bookings = []

print(make_reservation("John", 18, 4))
if check_availability(18, 4, bookings):
    bookings.append(["John", 18, 4])

print(make_reservation("Alice", 18, 17))
if check_availability(18, 17, bookings):
    bookings.append(["Alice", 18, 17])

print(bookings)
print(cancel("John", bookings))
print(bookings)
