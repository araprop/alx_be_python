task  = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == "yes":
            result = f"Reminder '{task}' is a high priority task requires immediate attention today!"
            print(result)
        else:
            print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to work on it soon.")

    case 'low':
        if time_bound == "no":
            result = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to work on it soon.")

