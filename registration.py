class RegistrationManager:
    def __init__(self):
        self.students = []

    def register_student(self, student):
        if not student.name.strip():
            return "Error: Student name is required."

        if not student.registration_number.strip():
            return "Error: Registration number is required."

        if not student.workshop.strip():
            return "Error: Workshop selection is required."

        for existing_student in self.students:
            if existing_student.registration_number == student.registration_number:
                return "Error: Registration number already exists."

        self.students.append(student)
        return "Registration successful!"

    def display_participants(self):
        if not self.students:
            print("\nNo participants registered yet.")
            return

        print("\n--- Registered Participants ---")

        for student in self.students:
            print(student.display())