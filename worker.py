class Worker:
    _id_counter = 1
    _workers = []

    def __init__(self, name, surname, salary, department):
        self.__id = Worker._id_counter
        Worker._id_counter += 1
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
        Worker._workers.append(self)

    def get_id(self):
        return self.__id

    def display_info(self):
        return f"ID: {self.get_id()}, Name: {self.name}, Surname: {self.surname}, Department: {self.department}"

