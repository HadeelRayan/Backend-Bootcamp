
class Robot:
    def __init__(self, name, id, main_material, price, cost_to_fix_per_day, battery_type, animal_type):
        self.name = name
        self.id = id
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.battery_type = battery_type
        self.animal_type = animal_type
        self.status = "for sale"  # Initial status

    def __str__(self):
        return f"Robot {self.name} (ID: {self.id}) - Status: {self.status}"


class Employee:
    def __init__(self, name, id, battery_type, daily_salary):
        self.name = name
        self.id = id
        self.battery_type = battery_type
        self.daily_salary = daily_salary

    def __str__(self):
        return f"Employee {self.name} (ID: {self.id}) - Daily Salary: {self.daily_salary}"


class Store:
    def __init__(self):
        self.robots = []
        self.employees = []
        self.balance = 0

    def add_robot(self, robot):
        self.robots.append(robot)

    def add_employee(self, employee):
        self.employees.append(employee)

    def sell_robot(self, robot_id):
        for robot in self.robots:
            if robot.id == robot_id and robot.status == "for sale":
                self.balance += robot.price
                robot.status = "sold"
                return f"Robot {robot.name} sold."
        return "Robot not found or not for sale."

    def repair_robot(self, robot_id):
        for robot in self.robots:
            if robot.id == robot_id:
                robot.status = "in repair"
                self.balance -= robot.cost_to_fix_per_day
                return f"Robot {robot.name} is now in repair."
        return "Robot not found."

    def calculate_daily_costs(self):
        total_salaries = sum(employee.daily_salary for employee in self.employees)
        total_repair_costs = sum(robot.cost_to_fix_per_day for robot in self.robots if robot.status == "in repair")
        self.balance -= (total_salaries + total_repair_costs)
        return f"Daily costs of {total_salaries + total_repair_costs} deducted from balance."

    def print_robots_for_sale(self):
        for_sale = [str(robot) for robot in self.robots if robot.status == "for sale"]
        return "\n".join(for_sale) if for_sale else "No robots for sale."

    def print_robots_in_repair(self):
        in_repair = [str(robot) for robot in self.robots if robot.status == "in repair"]
        return "\n".join(in_repair) if in_repair else "No robots in repair."


def main():
    robot1 = Robot("RoboDog", "001", "Steel", 1500, 100, "Lithium", "Carnivore")
    robot2 = Robot("MechaCat", "002", "Aluminum", 1200, 80, "Alkaline", "Herbivore")
    employee1 = Employee("RoboSmith", "E01", "Lithium", 200)

    store = Store()
    store.add_robot(robot1)
    store.add_robot(robot2)
    store.add_employee(employee1)

    print(store.print_robots_for_sale())  # Print robots for sale
    print(store.sell_robot("001"))  # Sell a robot
    print(store.repair_robot("002"))  # Send a robot to repair
    print(store.calculate_daily_costs())  # Calculate and deduct daily costs


if __name__ == "__main__":
    main()