import csv
import os
import getpass
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"
MANAGER_PASSWORD = "admin123"  # Change this for security


def save_attendance(emp_id, department, in_time=None, out_time=None):
    """Save attendance record to CSV"""
    today = datetime.now().strftime("%Y-%m-%d")

    records = load_attendance()
    updated_records = []
    found = False

    for row in records:
        if row[0] == emp_id and row[2] == today:
            if in_time:
                print("\n⚠️ Already checked in today!\n")
                return
            row[4] = out_time  # Update out_time
            found = True
        updated_records.append(row)

    if not found and in_time:
        updated_records.append([emp_id, department, today, in_time, ""])

    with open(ATTENDANCE_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_records)

    if in_time:
        print(f"\n✅ Employee {emp_id} checked in at {in_time}\n")
    elif out_time:
        print(f"\n✅ Employee {emp_id} checked out at {out_time}\n")


def load_attendance():
    """Load attendance from CSV"""
    if not os.path.exists(ATTENDANCE_FILE):
        return []

    with open(ATTENDANCE_FILE, mode="r") as file:
        reader = csv.reader(file)
        return list(reader)


def check_in():
    """Check-in an employee"""
    emp_id = input("Enter Employee ID (VVDN/...): ").strip().upper()
    department = input("Enter Department: ").strip().upper()

    if not emp_id.startswith("VVDN/"):
        print("\n❌ Employee ID must start with 'VVDN/'!\n")
        return
    if not department:
        print("\n❌ Department cannot be empty!\n")
        return

    in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_attendance(emp_id, department, in_time=in_time)


def check_out():
    """Check-out an employee"""
    emp_id = input("Enter Employee ID (VVDN/...): ").strip().upper()
    today = datetime.now().strftime("%Y-%m-%d")

    records = load_attendance()

    for row in records:
        if row[0] == emp_id and row[2] == today:
            if row[4]:  # Already checked out
                print("\n⚠️ Already checked out today!\n")
                return

            out_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_attendance(emp_id, row[1], out_time=out_time)
            return

    print("\n⚠️ You haven't checked in today!\n")


def view_all_attendance():
    """View all attendance records (Manager only)"""
    records = load_attendance()
    print("\n📋 All Employee Attendance Records:\n")
    print("{:<12} {:<15} {:<12} {:<20} {:<20}".format("Employee ID", "Department", "Date", "In-Time", "Out-Time"))
    print("-" * 80)

    for row in records:
        print("{:<12} {:<15} {:<12} {:<20} {:<20}".format(row[0], row[1], row[2], row[3] or "N/A", row[4] or "N/A"))

    print()


def export_attendance():
    """Export attendance records to CSV"""
    filename = f"attendance_report_{datetime.now().strftime('%Y%m%d')}.csv"
    records = load_attendance()

    if records:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Department", "Date", "In-Time", "Out-Time"])
            writer.writerows(records)

        print(f"\n✅ Attendance report saved as {filename}\n")
    else:
        print("\n⚠️ No records to export!\n")


def manager_menu():
    """Manager-specific menu"""
    password = getpass.getpass("Enter Manager Password: ").strip()

    if password != MANAGER_PASSWORD:
        print("\n❌ Incorrect Password!\n")
        return

    while True:
        print("\n📌 Manager Menu")
        print("1️⃣ View All Attendance")
        print("2️⃣ Export Attendance Report")
        print("0️⃣ Logout")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            view_all_attendance()
        elif choice == "2":
            export_attendance()
        elif choice == "0":
            print("\n👋 Logged out!\n")
            break
        else:
            print("\n❌ Invalid choice!\n")


def main():
    """Main program loop"""
    while True:
        print("\n📌 Employee Tracker Menu")
        print("1️⃣ Employee Check-In")
        print("2️⃣ Employee Check-Out")
        print("3️⃣ Manager Login")
        print("0️⃣ Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            check_in()
        elif choice == "2":
            check_out()
        elif choice == "3":
            manager_menu()
        elif choice == "0":
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice!\n")


if __name__ == "__main__":
    main()
