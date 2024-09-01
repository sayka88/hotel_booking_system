# Hotel Booking System

## Project Overview

The Hotel Booking System is designed to manage hotel reservations, rooms, and guests. It allows creating, modifying, and canceling reservations, as well as managing room availability.

## Project Structure

hotel_booking_system/ │ ├── hotel/ │ ├── init.py │ ├── guest.py │ ├── hotel.py │ ├── reservation.py │ ├── room.py │ ├── tests/ │ ├── init.py │ ├── test_hotel.py │ └── test_reservation.py │ ├── README.md ├── main.py

## Classes and Their Functions

### `Room`
Represents a room in the hotel.
- **Attributes:**
  - `room_number`: Room number
  - `room_type`: Type of room (e.g., "Single", "Double", "Suite")
  - `rate_per_night`: Rate per night
  - `availability`: Room availability

- **Methods:**
  - `check_availability()`: Checks if the room is available
  - `update_availability(status)`: Updates the availability status of the room

### `SingleRoom`, `DoubleRoom`, `Suite`
Subclasses of the `Room` class representing different types of rooms.

### `Guest`
Represents a guest who makes a reservation.
- **Attributes:**
  - `name`: Guest's name
  - `contact_info`: Guest's contact information

### `Reservation`
Represents a reservation in the hotel.
- **Attributes:**
  - `reservation_id`: Reservation identifier
  - `guest`: Guest making the reservation
  - `room`: Room being reserved
  - `check_in_date`: Check-in date
  - `check_out_date`: Check-out date
  - `total_cost`: Total cost of the reservation

- **Methods:**
  - `calculate_total_cost()`: Calculates the total cost of the reservation
  - `modify_reservation(new_check_in, new_check_out)`: Modifies the check-in and check-out dates
  - `cancel_reservation()`: Cancels the reservation and updates room availability
  - `get_reservation_details()`: Returns the details of the reservation

### 'Testing'

The project uses the `unittest` module for testing functionality.

### Running Tests

To run the tests, use the following command:

```bash
python3 -m unittest discover -s tests

### Tests
test_initial_reservation: Checks the creation of a new reservation.
test_modify_reservation: Checks the modification of an existing reservation.
test_cancel_reservation: Checks the cancellation of a reservation.
test_get_reservation_details: Checks the retrieval of reservation details.

### Installation
Clone the repository and install the necessary dependencies:

git clone <URL-REPOSITORY>
cd hotel_booking_system

### Usage
To run the hotel booking system, use the main.py script.
python3 main.py

### License
This project is licensed under the MIT License.

### Author
Your Name : Yusupova Sayyara H
