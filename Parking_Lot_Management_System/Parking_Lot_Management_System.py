parking_capacity = 10
occupied = 6

print("Total Parking Slots:", parking_capacity)
print("Occupied Slots:", occupied)

available = parking_capacity - occupied

print("Available Slots:", available)

cars_entering = int(input("Enter number of incoming cars: "))

if cars_entering <= available:
    occupied += cars_entering
    print("Cars Parked Successfully")
    print("Updated Occupied Slots:", occupied)
else:
    print("Parking Full! Not enough space.")

Total Parking Slots: 10
Occupied Slots: 6
Available Slots: 4
Enter number of incoming cars:  5
Parking Full! Not enough space.