# -------------------------------------------------------------
# Equipment Booking System for Bright Minds Academy
# -------------------------------------------------------------

Equipment_List = []
Bookings_List = []


# -------------------------------------------------------------
# Add New Equipment
# -------------------------------------------------------------
def add_equipment():
    print("\nAdd New Equipment")
    name = input("Enter the name of equipment (e.g. Laptop1, ProjectorA): ").strip()

    if name == "":
        print("ERROR: Equipment name cannot be empty.")
        return

    if name in Equipment_List:
        print(f"ERROR: '{name}' already exists.")
        return

    Equipment_List.append(name)
    print(f"Equipment '{name}' added successfully.")


# -------------------------------------------------------------
# Record Booking
# -------------------------------------------------------------
def record_booking():
    print("\nRecord a Booking")

    equipment = input("Enter equipment: ").strip()
    student = input("Enter student: ").strip()
    booking_date = input("Enter date (YYYY-MM-DD): ").strip()

    # Check equipment exists
    if equipment not in Equipment_List:
        print(f"ERROR: Cannot book '{equipment}' because it is not in the system.")
        return

    # Check for double booking
    for booking in Bookings_List:
        if booking["equipment"] == equipment and booking["date"] == booking_date:
            print(f"ERROR: {equipment} is already booked on {booking_date}.")
            return

    # Add booking
    new_booking = {
        "equipment": equipment,
        "student": student,
        "date": booking_date
    }

    Bookings_List.append(new_booking)
    print(f"Booking recorded: {equipment} for {student} on {booking_date}")


# -------------------------------------------------------------
# View All Bookings
# -------------------------------------------------------------
def show_bookings():
    print("\nAll Booking Records:")

    if not Bookings_List:
        print("No bookings recorded.")
        return

    for b in Bookings_List:
        print(f"- {b['equipment']} booked by {b['student']} on {b['date']}")


# -------------------------------------------------------------
# View Booking Status by Equipment
# -------------------------------------------------------------
def view_equipment_status():
    print("\nEquipment Booking Status:")

    if not Equipment_List:
        print("No equipment recorded.")
        return

    for item in Equipment_List:
        print(f"\nEquipment {item}:")
        found = False

        for b in Bookings_List:
            if b["equipment"] == item:
                print(f"   - Booked by {b['student']} on {b['date']}")
                found = True

        if not found:
            print("   - No bookings yet.")


# -------------------------------------------------------------
# Search Bookings
# -------------------------------------------------------------
def search_bookings():
    print("\nSearch Bookings")
    keyword = input("Enter a keyword (student, equipment, or date): ").strip().lower()

    results = []

    for b in Bookings_List:
        if (keyword in b["student"].lower() or
            keyword in b["equipment"].lower() or
            keyword in b["date"].lower()):
            results.append(b)

    if not results:
        print(f"No bookings found for '{keyword}'.")
    else:
        print(f"\nSearch results for '{keyword}':")
        for r in results:
            print(f"- {r['equipment']} booked by {r['student']} on {r['date']}")


# -------------------------------------------------------------
# MAIN MENU (This makes the programme RUN)
# -------------------------------------------------------------
def main_menu():
    while True:
        print("\n--- Bright Minds Academy Booking System ---")
        print("1. Add Equipment")
        print("2. Record Booking")
        print("3. View All Bookings")
        print("4. Search Bookings")
        print("5. View Equipment Status")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            record_booking()
        elif choice == "3":
            show_bookings()
        elif choice == "4":
            search_bookings()
        elif choice == "5":
            view_equipment_status()
        elif choice == "6":
            print("Exiting system. Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1–6.")

# -------------------------------------------------------------
# Example Usage (Preloaded Data)
# -------------------------------------------------------------
Equipment_List = ["Laptop1", "ProjectorA", "Tablet3"]

Bookings_List = [
    {"equipment": "ProjectorA", "student": "Clement", "date": "2020-07-30"},
    {"equipment": "Laptop1", "student": "Beda", "date": "2026-02-13"},
    {"equipment": "Tablet3", "student": "Julien", "date": "2025-01-21"}
]

# -------------------------------------------------------------
# Start the programme
# -------------------------------------------------------------
main_menu()
