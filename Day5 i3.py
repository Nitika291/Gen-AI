"""Design a base class Employee with attributes like name, department, and salary. Define a method display_info that prints the employee details. Create subclasses Manager and Engineer inheriting from Employee. Add specific attributes and methods to Manager (e.g., manage_team) and Engineer (e.g., work_on_project)."""
# Base class Employee
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:.2f}")


# Subclass Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, name, department, salary, team_members):
        super().__init__(name, department, salary)
        self.team_members = team_members

    def manage_team(self):
        print(f"{self.name} is managing their team of {len(self.team_members)} members.")

    def display_info(self):
        super().display_info()
        print("Team Members:")
        for member in self.team_members:
            print(member)


# Subclass Engineer inheriting from Employee
class Engineer(Employee):
    def __init__(self, name, department, salary, project):
        super().__init__(name, department, salary)
        self.project = project

    def work_on_project(self):
        print(f"{self.name} is working on the {self.project} project.")

    def display_info(self):
        super().display_info()
        print(f"Project: {self.project}")


# Example usage
if __name__ == "__main__":
    manager = Manager("Nitika", "Management", 100000, ["Nitika", "Jyoti"])
    manager.display_info()
    manager.manage_team()

    engineer = Engineer("Jyoti", "Engineering", 110000, "AI Development")
    engineer.display_info()
    engineer.work_on_project()
