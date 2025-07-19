task = input("Enter your task: ")

# Prompt for task's priority
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
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    if priority == 'high': # Only high priority time-bound tasks require immediate attention today
        reminder_message += " that requires immediate attention today!"
    elif priority == 'medium':
        reminder_message += " and is time-bound. Plan accordingly."
    elif priority == 'low':
        reminder_message += ". It is time-bound, but can be done when you have free time."
    else: # For unrecognized priority that is time-bound
        reminder_message += " and is time-bound. Please review its urgency."
else: # If not time-bound
    if priority == 'low':
        reminder_message += ". Consider completing it when you have free time."
    elif priority == 'medium':
        reminder_message += ". It can be completed at your convenience."
    elif priority == 'high':
        reminder_message += ". Ensure it's completed soon, even if not strictly time-bound today."
    # If priority is unrecognized, the initial message already covers it.

# Output the customized reminder
print(reminder_message)