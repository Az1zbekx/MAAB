import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_file_line(self):
        return f"{self.employee_id}|{self.name}|{self.position}|{self.salary}\n"

    @staticmethod
    def from_file_line(line):
        parts = line.strip().split('|')
        if len(parts) == 4:
            return Employee(parts[0], parts[1], parts[2], parts[3])
        return None


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def add_employee(self):
        print("\n--- Add New Employee ---")
        employee_id = input("Enter Employee ID: ").strip()
        if self._employee_exists(employee_id):
            print("❌ Employee ID already exists.")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()

        try:
            salary = float(input("Enter Salary: ").strip())
        except ValueError:
            print("❌ Invalid salary. Must be a number.")
            return

        emp = Employee(employee_id, name, position, salary)
        try:
            with open(self.FILE_NAME, 'a') as file:
                file.write(emp.to_file_line())
            print("✅ Employee added successfully.")
        except Exception as e:
            print(f"❌ Error saving employee: {e}")

    def view_all_employees(self):
        print("\n--- All Employee Records ---")
        if not os.path.exists(self.FILE_NAME):
            print("No employee records found.")
            return

        try:
            with open(self.FILE_NAME, 'r') as file:
                employees = [Employee.from_file_line(line) for line in file if line.strip()]
        except Exception as e:
            print(f"❌ Failed to read employee data: {e}")
            return

        if not employees:
            print("No records to display.")
            return

        # Bonus: Sorting options
        print("Sort by: 1. Name  2. Salary  3. No Sort")
        sort_choice = input("Enter choice: ").strip()
        if sort_choice == '1':
            employees.sort(key=lambda e: e.name.lower())
        elif sort_choice == '2':
            employees.sort(key=lambda e: e.salary)

        for emp in employees:
            print(emp)

    def search_employee(self):
        print("\n--- Search Employee by ID ---")
        employee_id = input("Enter Employee ID: ").strip()
        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    emp = Employee.from_file_line(line)
                    if emp and emp.employee_id == employee_id:
                        print("✅ Employee Found:")
                        print(emp)
                        return
        except Exception as e:
            print(f"❌ Failed to search employee: {e}")
            return
        print("❌ Employee not found.")

    def update_employee(self):
        print("\n--- Update Employee Info ---")
        employee_id = input("Enter Employee ID to update: ").strip()
        updated = False
        updated_lines = []

        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    emp = Employee.from_file_line(line)
                    if emp and emp.employee_id == employee_id:
                        print(f"Current Name: {emp.name}")
                        new_name = input("New Name (leave blank to keep current): ").strip() or emp.name

                        print(f"Current Position: {emp.position}")
                        new_position = input("New Position (leave blank to keep current): ").strip() or emp.position

                        print(f"Current Salary: {emp.salary}")
                        new_salary_input = input("New Salary (leave blank to keep current): ").strip()
                        try:
                            new_salary = float(new_salary_input) if new_salary_input else emp.salary
                        except ValueError:
                            print("❌ Invalid salary.")
                            return

                        emp = Employee(employee_id, new_name, new_position, new_salary)
                        updated = True
                    updated_lines.append(emp.to_file_line() if emp else line)

            with open(self.FILE_NAME, 'w') as file:
                file.writelines(updated_lines)

            print("✅ Employee updated." if updated else "❌ Employee not found.")

        except Exception as e:
            print(f"❌ Error updating employee: {e}")

    def delete_employee(self):
        print("\n--- Delete Employee ---")
        employee_id = input("Enter Employee ID to delete: ").strip()
        deleted = False
        remaining_lines = []

        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    emp = Employee.from_file_line(line)
                    if emp and emp.employee_id == employee_id:
                        deleted = True
                        continue
                    remaining_lines.append(line)

            with open(self.FILE_NAME, 'w') as file:
                file.writelines(remaining_lines)

            print("✅ Employee deleted." if deleted else "❌ Employee not found.")
        except Exception as e:
            print(f"❌ Error deleting employee: {e}")

    def _employee_exists(self, employee_id):
        try:
            if not os.path.exists(self.FILE_NAME):
                return False
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    emp = Employee.from_file_line(line)
                    if emp and emp.employee_id == employee_id:
                        return True
        except:
            return False
        return False

    def menu(self):
        while True:
            print("\n===== Employee Records Manager =====")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            match choice:
                case '1': self.add_employee()
                case '2': self.view_all_employees()
                case '3': self.search_employee()
                case '4': self.update_employee()
                case '5': self.delete_employee()
                case '6': print("👋 Goodbye!"); break
                case _: print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
