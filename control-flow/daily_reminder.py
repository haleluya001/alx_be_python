# Prompt user for task input
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Initialize parts of the message
prefix = ""
core_description = ""
time_sensitivity_suffix = ""

# Process the task based on priority using Match Case to set prefix and core description
match priority:
    case 'high':
        prefix = "Reminder: "
        core_description = f"'{task}' is a high priority task"
    case 'medium':
        prefix = "Note: "
        core_description = f"'{task}' is a medium priority task"
    case 'low':
        prefix = "Note: "
        core_description = f"'{task}' is a low priority task"
    case _: # Default case for unrecognized priority
        prefix = "Note: " # Consistent prefix for unrecognized priority
        core_description = f"'{task}' has an unrecognized priority level"

# Determine the time-sensitivity suffix based on time_bound and priority
if time_bound == 'yes':
    if priority == 'high':
        # Specific message for high priority, time-bound tasks as per example
        time_sensitivity_suffix = " that requires immediate attention today!"
    else:
        # Generic time-bound message for other priorities
        time_sensitivity_suffix = ". This task is time-bound."
else: # If not time-bound
    if priority == 'low':
        # Specific message for low priority, non-time-bound tasks as per example
        time_sensitivity_suffix = ". Consider completing it when you have free time."
    else:
        # Generic non-time-bound message for high, medium, or unrecognized priorities
        time_sensitivity_suffix = ". This task is not time-bound."

# Output the customized reminder by combining the parts
print(f"{prefix}{core_description}{time_sensitivity_suffix}")
