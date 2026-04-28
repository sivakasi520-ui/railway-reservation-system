TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))
bookings = {}
booking_id = 1

while True:
    print("\n1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available seats:", available_seats)

    elif choice == "2":
        if not available_seats:
            print("No seats available")
        else:
            name = input("Enter name: ")
            age = input("Enter age: ")

            seat = available_seats.pop(0)
            bid = "B" + str(booking_id)

            bookings[bid] = {
                "name": name,
                "age": age,
                "seat": seat
            }

            print("Booked! ID:", bid, "Seat:", seat)
            booking_id += 1

    elif choice == "3":
        bid = input("Enter booking ID: ")
        if bid in bookings:
            print(bookings[bid])
        else:
            print("Not found")

    elif choice == "4":
        bid = input("Enter booking ID: ")
        if bid in bookings:
            seat = bookings[bid]["seat"]
            available_seats.append(seat)
            del bookings[bid]
            print("Cancelled")
        else:
            print("Invalid ID")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
