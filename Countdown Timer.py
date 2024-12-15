import time

def countdown_timer(seconds):
    try:
        while seconds > 0:
            print(f"Countdown: {seconds} seconds remaining")
            time.sleep(1)  # Wait for 1 second
            seconds -= 1
        print("Time's up!")
    except KeyboardInterrupt:
        print("\nCountdown interrupted by user.")

# Get user input for countdown duration
try:
    user_input = int(input("Enter countdown duration in seconds: "))
    print("Starting countdown...")
    countdown_timer(user_input)
except ValueError:
    print("Please enter a valid number.")
