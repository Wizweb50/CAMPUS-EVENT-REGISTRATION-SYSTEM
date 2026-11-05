class Student:
    def __init__(self, name, registration_number, workshop):
        self.name = name
        self.registration_number = registration_number
        self.workshop = workshop

    def display(self):
        return (
            f"Name: {self.name} | "
            f"Registration No: {self.registration_number} | "
            f"Workshop: {self.workshop}"
        )