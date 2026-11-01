
# ==========================================
#       EVENT TICKET BOOKING SYSTEM
# ==========================================


# Store event details using Event ID as dictionary keys
events = {
    "E101": {
        "event_name": "Music Concert",
        "ticket_price": 500,
        "available_seats": 100
    },
    "E102": {
        "event_name": "Comedy Show",
        "ticket_price": 300,
        "available_seats": 50
    },
    "E103": {
        "event_name": "Tech Conference",
        "ticket_price": 800,
        "available_seats": 75
    },
}

# Stores all customer bookings
bookings = {}

# Variables used to control the menu and generate unique booking IDs
choice = 0
next_booking_number = 1


# Keep displaying the menu until the user chooses Exit
while choice != 7:

    print("""
===== Event Ticket Booking System =====
1. View Events
2. Check Available Seats
3. Book Tickets
4. Cancel Booking
5. Search Booking
6. Booking Reports
7. Exit
""")

    # Handle invalid menu input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue


    # --------------------------------------
    # 1. VIEW ALL EVENTS
    # --------------------------------------
    if choice == 1:

        print("Available Events:")
        print("-------------------------")

        # Display details of every event
        for event_id, details in events.items():
            print(f"Event ID: {event_id}")
            print(f"Event Name: {details['event_name']}")
            print(f"Ticket Price: ₹{details['ticket_price']}")
            print(f"Available Seats: {details['available_seats']}")
            print("-------------------------")


    # --------------------------------------
    # 2. CHECK AVAILABLE SEATS
    # --------------------------------------
    elif choice == 2:

        event_id = input("Enter Event ID: ")

        # Check whether the entered Event ID exists
        if event_id in events:
            print(f"Event Name: {events[event_id]['event_name']}")
            print(f"Available Seats: {events[event_id]['available_seats']}")

        else:
            print("Event Not Found!")


    # --------------------------------------
    # 3. BOOK TICKETS
    # --------------------------------------
    elif choice == 3:

        event_id = input("Enter Event ID: ")

        # Verify that the event exists
        if event_id in events:

            ticket = int(input("Enter the number of tickets you want: "))

            # Validate ticket quantity and seat availability
            if ticket > 0 and ticket <= events[event_id]['available_seats']:

                # Reduce available seats after successful booking
                events[event_id]['available_seats'] -= ticket

                # Calculate the total booking amount
                total_price = ticket * events[event_id]["ticket_price"]

                # Generate a unique booking ID
                booking_id = f"B{next_booking_number}"
                next_booking_number += 1

                # Store booking information
                bookings[booking_id] = {
                    "event_id": event_id,
                    "event_name": events[event_id]["event_name"],
                    "ticket": ticket,
                    "total_price": total_price
                }

                # Display booking confirmation
                print(f"Booking ID: {booking_id}")
                print(f"Event Name: {events[event_id]['event_name']}")
                print(f"No of Tickets booked: {ticket}")
                print(f"Total Price: ₹{total_price}")
                print("Booking Successful!")

            else:
                print("Invalid ticket quantity or not enough seats available!")

        else:
            print("Event Not Found!")


    # --------------------------------------
    # 4. CANCEL BOOKING
    # --------------------------------------
    elif choice == 4:

        booking_id = input("Enter Booking ID: ")

        # Check whether the booking exists
        if booking_id in bookings:

            event_id = bookings[booking_id]['event_id']
            ticket = bookings[booking_id]['ticket']

            cancel_ticket = int(input("No of Ticket you want to Cancel: "))

            # Validate cancellation quantity
            if cancel_ticket > 0 and cancel_ticket <= ticket:

                # Restore cancelled seats to the event
                events[event_id]['available_seats'] += cancel_ticket

                # Update the remaining ticket quantity
                ticket -= cancel_ticket
                bookings[booking_id]['ticket'] -= cancel_ticket

                # Recalculate the booking amount
                bookings[booking_id]['total_price'] = (
                    bookings[booking_id]['ticket']
                    * events[event_id]["ticket_price"]
                )

                # Delete the booking if all tickets are cancelled
                if bookings[booking_id]['ticket'] == 0:
                    del bookings[booking_id]

                print("Booking cancellation successful!")
                print(f"Tickets cancelled: {cancel_ticket}")

            else:
                print("Invalid cancellation quantity!")

        else:
            print("Booking Not Found!")


    # --------------------------------------
    # 5. SEARCH BOOKING
    # --------------------------------------
    elif choice == 5:

        search_id = input("Enter the Booking ID: ")

        # Search for the booking using its ID
        if search_id in bookings:

            print(f"Booking ID: {search_id}")
            print(f"Event Name: {bookings[search_id]['event_name']}")
            print(f"Event ID: {bookings[search_id]['event_id']}")
            print(f"Number of Tickets: {bookings[search_id]['ticket']}")
            print(f"Total Price: {bookings[search_id]['total_price']}")

        else:
            print("Booking Not Found!")


    # --------------------------------------
    # 6. BOOKING REPORTS
    # --------------------------------------
    elif choice == 6:

        # Check whether any bookings are available
        if bookings:

            # Display details of all existing bookings
            for booking_id, details in bookings.items():

                print(f"Booking ID: {booking_id}")
                print(f"Event Name: {details['event_name']}")
                print(f"Number of Tickets: {details['ticket']}")
                print(f"Total Price: {details['total_price']}")

            # Calculate overall booking statistics
            total_bookings = len(bookings)

            # Calculate total tickets booked
            total_tickets = sum(
                details["ticket"] for details in bookings.values()
            )

            # Calculate total revenue generated
            total_revenue = sum(
                details["total_price"] for details in bookings.values()
            )

            # Display the final report
            print(f"Total Bookings: {total_bookings}")
            print(f"Total Tickets: {total_tickets}")
            print(f"Total Revenue: {total_revenue}")

        else:
            print("No bookings available!")


    # --------------------------------------
    # 7. EXIT APPLICATION
    # --------------------------------------
    elif choice == 7:

        print("Thank you for using our system!")


    # Handle menu numbers outside the available options
    else:
        print("Invalid Choice")
        