from worker import Worker

class NonDelivery(Worker):
    def __init__(self, name, surname, salary, job_title):
        super().__init__(name, surname, salary, "Non-Delivery")
        self.job_title = job_title

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, new_job_title):
        self.job_title = new_job_title

    def display_info(self):
        return f"ID: {self.get_id()}, Name: {self.name}, Surname: {self.surname}, Department: {self.department}, Job Title: {self.job_title}"

