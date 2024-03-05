class TaskScheduler:
    def __init__(self):
        self.schedule = [[None for _ in range(8)] for _ in range(5)]

    def add_task(self, task_name, task_duration, day=None, start_hour=None):
        if day is not None and start_hour is not None:
            if self.schedule[day][start_hour:start_hour + task_duration] == [None] * task_duration:
                self.schedule[day][start_hour:start_hour + task_duration] = [task_name] * task_duration
                print("Task '{}' scheduled on day {} starting from hour {}.".format(task_name, day, start_hour))
            else:
                print("Time range already populated with task(s):", self.schedule[day][start_hour:start_hour + task_duration])
                decision = input("Do you want to overwrite the existing task(s)? (yes/no): ")
                if decision.lower() == "yes":
                    self.schedule[day][start_hour:start_hour + task_duration] = [task_name] * task_duration
                    print("Task '{}' overwritten on day {} starting from hour {}.".format(task_name, day, start_hour))
                else:
                    print("Please specify a new time for the task.")
        else:
            for day in range(5):
                for start_hour in range(8 - task_duration + 1):
                    if self.schedule[day][start_hour:start_hour + task_duration] == [None] * task_duration:
                        self.schedule[day][start_hour:start_hour + task_duration] = [task_name] * task_duration
                        print("Task '{}' scheduled on day {} starting from hour {}.".format(task_name, day, start_hour))
                        return
            print("No available time slots for task '{}'.".format(task_name))

    def print_schedule(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        print("Schedule:")
        for i, day in enumerate(days):
            print(day + ":")
            for hour, task in enumerate(self.schedule[i]):
                if task is None:
                    print("\tHour {}: Empty".format(hour))
                else:
                    print("\tHour {}: {}".format(hour, task))


def main():
    scheduler = TaskScheduler()
    while True:
        task_name = input("Enter task name: ")
        if task_name.lower() == "done":
            break
        task_duration = int(input("Enter task duration (in hours): "))
        specific_day = input("Enter specific day (Monday-Friday) or press Enter for any day: ")
        start_hour = None
        if specific_day:
            specific_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].index(specific_day)
            start_hour = int(input("Enter starting hour: "))
        scheduler.add_task(task_name, task_duration, specific_day, start_hour)

    scheduler.print_schedule()


if __name__ == "__main__":
    main()
