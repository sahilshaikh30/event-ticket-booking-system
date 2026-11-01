# Event Ticket Booking System

A Python console application for browsing events, booking and cancelling tickets, and generating booking reports. Built as a beginner project to practice dictionaries, loops, and input handling.

## Features
- View all events with price and available seats
- Check seat availability for a specific event
- Book tickets with automatic booking IDs
- Cancel part or all of a booking, with seats restored
- Search a booking by ID
- Generate a report with total bookings, tickets, and revenue

## Tech used
- Python 3
- Standard library only (no installs needed)

## How to run
1. Make sure Python 3 is installed
2. Download or clone this repo
3. Run:
   ```
   python event_ticket_booking_system.py
   ```
4. Use the menu by typing a number from 1 to 7

## Sample events
| Event ID | Event | Price | Seats |
|---|---|---|---|
| E101 | Music Concert | ₹500 | 100 |
| E102 | Comedy Show | ₹300 | 50 |
| E103 | Tech Conference | ₹800 | 75 |

## What I practiced
- Nested dictionaries to store events and bookings
- Menu-driven programs with `while` loops
- `try/except` for invalid menu input
- Generating unique IDs and calculating totals

## Known issues
- Entering text instead of a number when booking or cancelling tickets crashes the program
- Data is stored in memory only, so bookings are lost when the program closes

## Planned improvements
- Add input validation for ticket quantities
- Save bookings to a SQLite database
- Break the code into functions
