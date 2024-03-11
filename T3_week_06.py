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
    
    if num_groups >= 6 and total_cost > num_groups * (15 if two_day_ticket == "yes" else 22.50):
        print("It mighr be more cost-effective to book individual tickets instead of a group booking.")

    elif num_adults >= 2 and num_childern >= 3 and total_cost > (num_families + num_groups) * (60 if two_day_ticket == "yes" else 90):
        print("It might be more cost_effective to book family tickets instead of individual adult and child tickets.")
        
    elif num_adults >= 2 and num_childern >= 3 and total_cost > (num_adults + num_childern) * (20 if two_day_ticket == "yes" else 30):
        print("It might be more cost_effective to book individual tickets instead of a family ticket.")
    
def main():
    print("Welcome to the WildLife Paek Ticket Booking System!\n")
    process_booking()

if __name__ == "__main__":
    main()