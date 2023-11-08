from worker import Worker

class Delivery(Worker):
    def __init__(self, name, surname, salary, duty):
        super().__init__(name, surname, salary, "Delivery")
        self.duty = duty

    def get_duty(self):
        return self.duty

    def set_duty(self, new_duty):
        self.duty = new_duty

    def display_info(self):
        return f"ID: {self.get_id()}, Name: {self.name}, Surname: {self.surname}, Department: {self.department}, Duty: {self.duty}"

