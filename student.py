class Student:
    def __init__(self, name, registration_number, workshop):
        self.__name = name
        self.__registration_number = registration_number
        self.__workshop = workshop

    @property
    def name(self):
        return self.__name

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def workshop(self):
        return self.__workshop

    def display(self):
        return (
            f"Name: {self.name} | "
            f"Registration No: {self.registration_number} | "
            f"Workshop: {self.workshop}"
        )