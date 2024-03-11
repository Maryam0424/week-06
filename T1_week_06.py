def display_options():
    print("Ticket Options: ")
    print("1. Ond-day Ticket: ")
    print("  a. One adult - $20.00")
    print("  b. One child - $12.00")
    print("  c. One senior - $16.00")
    print("  d. Family ticket - $60.00")
    print("  e. Group of six or more - $15.00 per person")
    
    print("2. Two-day Ticket: ")
    print("  a. One adult - $30.00")
    print("  b. One child - $18.00")
    print("  c. One senior - $24.00")
    print("  d. Family ticket - $90.00")
    print("  e. Group of six or more - $22.50 per person")

def display_attractions():
    print("\nExtra Attractions: ")
    print("1. Lion feeding - $2.50 per person")
    print("2. Penguin feeding - $2.00 per person")
    print("3. Evening barbecue (only available with two-day tickets)- $5.00 per person")

def display_booking_days():
    print("\nDays Available for Booking: ")
    days = ["Monday", "Tuesday", "Wednesday", "Thusrday", "Friday", "saturday", "Sunday"]
    for i, day in enumerate(days, start = 1):
        print(f"{i}. {day}")

def main():
    print("Welcome to the WildLife Park Ticket Booking System!\n")
    display_options()
    display_attractions()
    display_booking_days

if __name__ == "__main__":
    main()