import argparse
import sys
import time
import os

# Using a constant makes the code more readable and maintainable
SECONDS_PER_HOUR = 3600

def parse_arguments():
    """Parses command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description='A script to repeat intentions hourly from a file or direct input.',
        epilog='If no arguments are provided, the script will prompt for them interactively.'
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--file', type=str, help='The file containing the intention.')
    group.add_argument('--intent', type=str, help='The intention string.')
    
    def positive_int(value):
        """Helper function to validate positive integers for argparse."""
        try:
            ivalue = int(value)
            if ivalue <= 0:
                raise argparse.ArgumentTypeError(f"must be a positive integer, not '{value}'")
            return ivalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"invalid integer value: '{value}'")
    
    parser.add_argument('--repeats', type=positive_int, help='Number of times the intention is actioned per hour.')
    parser.add_argument('--duration', type=positive_int, help='Total duration in seconds for the script to run.')
    
    return parser.parse_args()

def read_intention_from_file(filename):
    """Reads and returns the content of a file, exiting on error."""
    try:
        with open(filename, 'r', encoding='utf-8', errors='replace') as f:
            return f.read().strip()
    except (IOError, OSError) as e:
        # Errors are printed to stderr, which is standard practice
        print(f"Error: Could not read file '{filename}'. Reason: {e}", file=sys.stderr)
        sys.exit(1)

def format_time_hms(seconds):
    """Formats seconds into a clear HH:MM:SS string."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def get_interactive_inputs():
    """Interactively prompts the user for necessary inputs if not provided via CLI."""
    details = {}
    
    while True:
        user_input = input("Enter the intention string or a filename: ").strip()
        if not user_input:
            print("Input cannot be empty.")
            continue
        if os.path.isfile(user_input):
            details['file'] = user_input
            break
        else:
            details['intent'] = user_input
            break
            
    while 'repeats' not in details:
        try:
            repeats = int(input("Number of repeats per hour: ").strip())
            if repeats > 0:
                details['repeats'] = repeats
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while 'duration' not in details:
        try:
            duration = int(input("Duration in seconds: ").strip())
            if duration > 0:
                details['duration'] = duration
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    return details

def run_intention_repeater(intention, duration, repeats, source_name):
    """Main loop to handle the timing and repetition of the intention."""
    start_time = time.time()
    end_time = start_time + duration
    
    # Schedule the first repetition for the start time.
    # This method prevents "timing drift" by always scheduling based on the
    # previous *scheduled* time, not the actual time the loop ran.
    next_repetition_time = start_time 

    print("\nServitor connection established. Starting intention cycles...")
    try:
        while True:
            current_time = time.time()
            if current_time >= end_time:
                break

            # --- Core Intention Repetition Trigger ---
            if current_time >= next_repetition_time:
                # Provide feedback to the user that a cycle is starting.
                print(f"\n[Cycle at {time.strftime('%H:%M:%S')}] Focusing intention {repeats} times...")
                
                # THIS IS THE RESTORED CORE LOGIC:
                # The act of repeatedly assigning the intention string to a variable
                # in memory is the "work" being performed.
                active_intention = None
                for _ in range(repeats):
                    active_intention = intention
                
                print("Cycle complete.")
                
                # Schedule the next run exactly one hour from the last scheduled time.
                next_repetition_time += SECONDS_PER_HOUR

            # --- Live Status UI Update ---
            remaining_seconds = max(0, end_time - current_time)
            timer_str = format_time_hms(remaining_seconds)
            status_line = f"Source: {source_name} | Repeats: {repeats}/hr | Time Remaining: {timer_str}"
            
            # Print status on the same line and pad with spaces to prevent artifacts
            sys.stdout.write('\r' + status_line.ljust(80)) 
            sys.stdout.flush()
            
            # Sleep for a short interval before the next status update
            time.sleep(1)

        print("\n\nDuration completed. Servitor connection closed.")

    except KeyboardInterrupt:
        print("\n\nScript interrupted by user. Exiting gracefully.")

def main():
    """The main entry point of the script."""
    print("ServitorConnect CLI v1.5.0")
    print("by AnthroHeart/Anthro Teacher/Thomas Sweet\n")
    
    args = parse_arguments()
    
    # If no arguments were given, switch to interactive mode
    if len(sys.argv) == 1:
        user_details = get_interactive_inputs()
        file = user_details.get('file')
        intent = user_details.get('intent')
        repeats = user_details.get('repeats')
        duration = user_details.get('duration')
    else:
        file = args.file
        intent = args.intent
        repeats = args.repeats
        duration = args.duration

    # After args are parsed, ensure we have values for everything, prompting if necessary
    if not (file or intent):
        print("Error: An intention or file must be provided.", file=sys.stderr)
        sys.exit(1)
    if not repeats:
        repeats = int(input("Number of repeats per hour: ").strip())
    if not duration:
        duration = int(input("Duration in seconds: ").strip())

    # Determine the intention and its source ONCE to avoid redundant logic
    if file:
        intention_value = read_intention_from_file(file)
        source = f"File ('{file}')"
    else:
        intention_value = intent
        source = "Direct Input"
    
    print("Configuration:")
    print(f"  - Source: {source}")
    print(f"  - Intention: '{intention_value}'")
    print(f"  - Repeats per Hour: {repeats}")
    print(f"  - Total Duration: {format_time_hms(duration)}")

    run_intention_repeater(intention_value, duration, repeats, source)

if __name__ == "__main__":
    main()