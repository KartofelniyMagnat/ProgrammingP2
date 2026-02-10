class Employee:
    def __init__(self, name: str, base_salary: int):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self) -> float:
        return float(self.base_salary)


class Manager(Employee):
    def __init__(self, name: str, base_salary: int, bonus_percent: int):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self) -> float:
        return self.base_salary * (1 + self.bonus_percent / 100.0)


class Developer(Employee):
    def __init__(self, name: str, base_salary: int, completed_projects: int):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self) -> float:
        return self.base_salary + 500.0 * self.completed_projects


class Intern(Employee):
    pass


parts = input().split()
role = parts[0]

if role == "Manager":
    name = parts[1]
    base_salary = int(parts[2])
    bonus_percent = int(parts[3])
    emp = Manager(name, base_salary, bonus_percent)

elif role == "Developer":
    name = parts[1]
    base_salary = int(parts[2])
    completed_projects = int(parts[3])
    emp = Developer(name, base_salary, completed_projects)

elif role == "Intern":
    name = parts[1]
    base_salary = int(parts[2])
    emp = Intern(name, base_salary)

else:
    raise ValueError("Unknown employee type")

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")