class User:
    def __init__(self, user_id=0, name="", email="", password=""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password


class Complaint:
    def __init__(self, complaint_id, details):
        self.complaint_id = complaint_id
        self.details = details
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status


class System:
    def __init__(self):
        self.users = {}
        self.user_complaints = {}
        self.next_user_id = 1
        self.next_complaint_id = 1

    def register_user(self, name, email, password):
        new_user = User(self.next_user_id, name, email, password)
        self.users[new_user.user_id] = new_user
        print(f"User registered successfully! User ID: {new_user.user_id}")
        self.next_user_id += 1

    def login_user(self, email, password):
        for user in self.users.values():
            if user.email == email and user.check_password(password):
                print(f"Login successful! Welcome {user.name}")
                return user.user_id
        print("Login failed! Invalid credentials.")
        return -1

    def submit_complaint(self, user_id, details):
        if user_id in self.users:
            new_complaint = Complaint(self.next_complaint_id, details)
            if user_id not in self.user_complaints:
                self.user_complaints[user_id] = []
            self.user_complaints[user_id].append(new_complaint)
            print(f"Complaint submitted successfully! Complaint ID: {new_complaint.complaint_id}")
            self.next_complaint_id += 1
        else:
            print("Invalid user ID! Please register first.")

    def view_complaints(self, user_id):
        if user_id in self.user_complaints:
            complaints = self.user_complaints[user_id]
            if not complaints:
                print("No complaints found for this user.")
                return
            for complaint in complaints:
                print(f"Complaint ID: {complaint.complaint_id} | Details: {complaint.details} | Status: {complaint.status}")
        else:
            print("No complaints found for this user.")

    def update_complaint_status(self, user_id, complaint_id, new_status):
        if user_id in self.user_complaints:
            for complaint in self.user_complaints[user_id]:
                if complaint.complaint_id == complaint_id:
                    complaint.update_status(new_status)
                    print(f"Complaint status updated to: {new_status}")
                    return
            print("Complaint not found.")
        else:
            print("Invalid user ID!")


def main():
    system = System()
    while True:
        print("\n1. Register\n2. Login\n3. Submit Complaint\n4. View Complaints\n5. Update Complaint Status\n6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            system.register_user(name, email, password)

        elif choice == 2:
            email = input("Enter email: ")
            password = input("Enter password: ")
            user_id = system.login_user(email, password)

        elif choice == 3:
            user_id = int(input("Enter your user ID: "))
            complaint_details = input("Enter complaint details: ")
            system.submit_complaint(user_id, complaint_details)

        elif choice == 4:
            user_id = int(input("Enter your user ID: "))
            system.view_complaints(user_id)

        elif choice == 5:
            user_id = int(input("Enter user ID: "))
            complaint_id = int(input("Enter complaint ID: "))
            new_status = input("Enter new status: ")
            system.update_complaint_status(user_id, complaint_id, new_status)

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
