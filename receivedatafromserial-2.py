import serial
import os
from datetime import datetime

# Open the serial port
ser = serial.Serial('COM3', 115200)  # Replace 'COM1' with the appropriate port and '9600' with the baud rate

# Specify the directory for saving the file
save_directory = 'F:\_Downloads'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Generate the file name using the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"data_{current_datetime}.txt"
file_path = os.path.join(save_directory, file_name)

# Open the text file for writing
file = open(file_path, 'w')

try:
    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode().strip()

        # Get the current timestamp
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        # Print the timestamp and data to the terminal
        print(f"{timestamp} {data}")

        # Save the timestamp and data to the text file
        file.write(f"{timestamp} {data}\n")

except KeyboardInterrupt:
    # Close the serial port and text file
    ser.close()
    file.close()
