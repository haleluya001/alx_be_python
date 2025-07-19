# Prompt user for task input
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process the task based on priority using Match Case
match priority:
    case 'high':
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder_message = f"Note: '{task}' is a medium priority task"
    case 'low':
        reminder_message = f"Note: '{task}' is a low priority task"
    case _: # Default case for unrecognized priority
        reminder_message = f"'{task}' has an unrecognized priority level"

# Modify the reminder based on time sensitivity
if time_bound == 'yes':
    if priority == 'high':
        # Specific message for high priority, time-bound tasks as per example
        reminder_message += " that requires immediate attention today!"
    else:
        # Generic time-bound message for other priorities
        reminder_message += " and is time-bound."
else: # If not time-bound
    if priority == 'low':
        # Specific message for low priority, non-time-bound tasks as per example
        reminder_message += ". Consider completing it when you have free time."
    else:
        # Generic non-time-bound message for high, medium, or unrecognized priorities
        reminder_message += ". It is not time-bound."

# Output the customized reminder
print(reminder_message)

