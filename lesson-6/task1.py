DATA_ID = []

try:
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) >= 1 and parts[0].isdigit():
                DATA_ID.append(int(parts[0]))
except FileNotFoundError:
    print("employees.txt file not found. Creating new on first save.")


def add():
    new_data = []

    while True:
        try:
            ID = int(input("ID = "))
            if ID <= 0:
                print("ID must be positive.")
            elif ID in DATA_ID:
                print("This ID exists, enter another one.")
            else:
                DATA_ID.append(ID)
                new_data.append(str(ID))
                break
        except ValueError as e:
            print(f"ID must be an integer. {e}")

    name = input("Name = ")
    new_data.append(name)

    position = input("Position = ")
    new_data.append(position)

    while True:
        try:
            salary = int(input("Salary = "))
            if salary <= 0:
                print("Salary must be positive.")
            else:
                new_data.append(str(salary))
                break
        except ValueError as e:
            print(f"Salary must be an integer. {e}")

    try:
        with open('employees.txt', 'a') as file:
            file.write(', '.join(new_data) + '\n')
        print("Data added successfully.")
    except FileNotFoundError:
        print("employees.txt not found.")


def view():
    try:
        with open('employees.txt', 'r') as file:
            content = file.read()
            if not content.strip():
                print("No employee records found.")
            else:
                print(content)
    except FileNotFoundError:
        print("employees.txt not found.")


def search():
    try:
        ID = int(input("Search ID = "))
        if ID <= 0:
            print("ID must be positive.")
            return

        if ID in DATA_ID:
            with open('employees.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(', ')
                    if int(parts[0]) == ID:
                        print("Employee found:", ', '.join(parts))
                        return
        else:
            print("No such employee ID.")
    except ValueError:
        print("ID must be an integer.")
    except FileNotFoundError:
        print("employees.txt not found.")


def update():
    try:
        ID = int(input("Update ID = "))
        if ID <= 0:
            print("ID must be positive.")
            return

        if ID not in DATA_ID:
            print("No such employee.")
            return

        new_content = ''
        with open('employees.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                if int(parts[0]) == ID:
                    parts[1] = input("New Name = ")
                    parts[2] = input("New Position = ")
                    while True:
                        try:
                            salary = int(input("New Salary = "))
                            if salary > 0:
                                parts[3] = str(salary)
                                break
                            else:
                                print("Salary must be positive.")
                        except ValueError as e:
                            print("Salary must be an integer.")
                new_content += ', '.join(parts) + '\n'

        with open('employees.txt', 'w') as file:
            file.write(new_content)

        print("Employee updated.")
    except ValueError:
        print("ID must be an integer.")
    except FileNotFoundError:
        print("employees.txt not found.")


def delete():
    try:
        ID = int(input("Delete ID = "))
        if ID <= 0:
            print("ID must be positive.")
            return

        if ID not in DATA_ID:
            print("No such employee.")
            return

        new_content = ''
        with open('employees.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                if int(parts[0]) != ID:
                    new_content += ', '.join(parts) + '\n'

        with open('employees.txt', 'w') as file:
            file.write(new_content)

        DATA_ID.remove(ID)
        print("Employee deleted.")
    except ValueError:
        print("ID must be an integer.")
    except FileNotFoundError:
        print("employees.txt not found.")



print("Employee Records Manager")
print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")

while True:
    try:
        command = int(input("Select option: "))

        match command:
            case 1:
                add()
            case 2:
                view()
            case 3:
                search()
            case 4:
                update()
            case 5:
                delete()
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Enter number between 1-6.")
    except ValueError:
        print("Please enter only integers (1-6).")
