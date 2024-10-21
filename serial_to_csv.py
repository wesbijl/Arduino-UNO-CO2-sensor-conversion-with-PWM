import serial
import csv
import time

# Establish serial communication with Arduino
arduino_port = 'COM3' 
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

# Create a unique CSV file name with a timestamp
file_name = time.strftime('co2_data_%Y-%m-%d_%H-%M-%S.csv')
csv_file = open(file_name, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'CO2 Concentration (ppm)'])

try:
    while True:
        # Read a line of serial data from Arduino
        serial_data = ser.readline().decode().strip()

        # Get the current time for the timestamp
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Extract CO2 concentration value from the serial data
        if "CO2 concentration:" in serial_data:
            co2_value = serial_data.split(":")[1].strip().split()[0]  # Extracts the numerical value or "ovf"

            # Check if the value is not "ovf"
            if co2_value != "ovf":
                # Write the timestamp and CO2 concentration to CSV
                csv_writer.writerow([current_time, co2_value])
                csv_file.flush()  # Ensure immediate writing to file

except KeyboardInterrupt:
    pass

# Close the CSV file and serial connection
csv_file.close()
ser.close()
