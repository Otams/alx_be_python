# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match case to provide a base reminder based on priority
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unrecognized priority level"

# Modify the message based on time sensitivity
if time_bound == "yes":
    reminder = base + " that requires immediate attention today!"
else:
    reminder = base + ". Consider completing it when you have free time."

# Print the final reminder (single line)
print("Reminder:", reminder)
