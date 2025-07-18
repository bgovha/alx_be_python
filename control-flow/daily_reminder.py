task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f" '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a high priority task. Please address it soon."
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a medium priority task that should be completed today."
        else:
            reminder = f"Reminder: '{task}' is a medium priority task. Schedule time for it this week."
    case "low":
        if time_bound == "yes":
            reminder = f"Note: '{task}' is a low priority task but has a deadline today."
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time.."
    case _:
        reminder = "Invalid priority level entered. Please use high, medium, or low."
print("\n" + reminder)
