from T1_week_06 import display_options
from T1_week_06 import display_attractions
from T1_week_06 import display_booking_days

def process_booking():
    print("\n--- Booking Details ---")
    total_cost = 0

    num_adults = int(input("Enter the number of adult tickets: "))
    num_childern = int(input("Enter the number of child tickets: "))
    num_seniors = int(input("Enter the number of senior tickets: "))
    num_families = int(input("Enter the number of family tickets: "))
    num_groups = int(input("Enter the number of people in group bookings (6 or more): "))

    num_lion_feeding = int(input("Enter the number of people for lion feeding: "))
    num_penguin_feeding = int(input("Enter the number of people for penguin feeding: "))

    two_day_ticket = input("Are you booking for two days? (yes/no): ").lower()

    total_cost += num_adults * (30 if two_day_ticket == "yes" else 20)
    total_cost += num_childern * (18 if two_day_ticket == "yes" else 12)
    total_cost += num_seniors * (24 if two_day_ticket == "yes" else 16)
    total_cost += num_families * (90 if two_day_ticket == "yes" else 60)
    total_cost += num_groups * (22.50 if two_day_ticket == "yes" else 15)

    total_cost += num_lion_feeding * 2.50
    total_cost += num_penguin_feeding * 2.00

    print(f"\nTotal Cost: ${total_cost:.2f}")
    booking_number = generate_booking_number()
    print(f"Booking Number: {booking_number}")

def generate_booking_number():
    global booking_counter
    booking_counter += 1
    return f"WPB{booking_counter:04d}"

def main():
    print("Welcome to the WildLife Paek Ticket Booking System!\n")
    display_options()
    display_attractions()
    display_booking_days()

    while True:
        process_booking()
        cont = input("\nDo you want to make another booking? (yes/no): ").lower()

        if cont != "yes":
            break

if __name__ == "__main__":
    booking_counter = 0
    main()