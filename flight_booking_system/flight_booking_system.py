flights = {
    "AI101": 5,
    "BA202": 3,
    "UA303": 2
}

flight_no = input("Enter flight number: ").upper()

if flight_no in flights:

    seats = int(input("Enter number of seats to book: "))

    if seats <= flights[flight_no]:
        flights[flight_no] -= seats

        print("Booking Confirmed")
        print("Remaining Seats:", flights[flight_no])

    else:
        print("Not enough seats available")

else:
    print("Flight not found")



Enter flight number:  UA303
Enter number of seats to book:  2
Booking Confirmed
Remaining Seats: 0