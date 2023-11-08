import csv
from worker import Worker, Delivery, NonDelivery

class WorkerDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.read_employees()

    def read_employees(self):
        with open(self.filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                if len(row) == 5:
                    name, surname, salary, department, extra_field = row
                    salary = int(salary.strip())
                    if department == 'Delivery':
                        Delivery(name, surname, salary, extra_field)
                    elif department == 'Non-Delivery':
                        NonDelivery(name, surname, salary, extra_field)

    def add_worker(self, worker):
        with open(self.filename, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            if isinstance(worker, Delivery):
                csv_writer.writerow([worker.name, worker.surname, worker.salary, "Delivery", worker.get_duty()])
            elif isinstance(worker, NonDelivery):
                csv_writer.writerow([worker.name, worker.surname, worker.salary, "Non-Delivery", worker.get_job_title()])

        if worker not in Delivery._workers and worker not in NonDelivery._workers:
            Worker._workers.append(worker)

    def find_workers_by_name(self, search_name):
        matching_workers = []
        for worker in (Delivery._workers + NonDelivery._workers):
            if worker.name == search_name:
                matching_workers.append(worker)
        return matching_workers

    def sort_workers_by_criteria(self, criteria):
        all_workers = Delivery._workers + NonDelivery._workers
        if criteria == "за зарплатою":
            all_workers.sort(key=lambda x: x.salary, reverse=True)

        return all_workers

    def display_sorted_workers(self, criteria):
        sorted_workers = self.sort_workers_by_criteria(criteria)
        for worker in sorted_workers:
            print(worker.display_info())

if __name__ == "__main__":
    db = WorkerDatabase('employees.csv')

    new_delivery_worker = Delivery("John", "Doe", 60000, "Driver")
    new_non_delivery_worker = NonDelivery("Alice", "Smith", 70000, "HR Manager")

    db.add_worker(new_delivery_worker)
    db.add_worker(new_non_delivery_worker)

    found_workers = db.find_workers_by_name("Ihor")
    if found_workers:
        print("Знайдені працівники:")
        for worker in found_workers:
            print(f"ID: {worker.get_id()}, Ім'я: {worker.name}, Прізвище: {worker.surname}, Відділ: {worker.department}")
    else:
        print("Працівники не знайдені")

    print("Сортування за зарплатою:")
    db.display_sorted_workers("за зарплатою")

