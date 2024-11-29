
import csv
import serial
import time


# Configure the serial port
serial_port = ('COM5')  # Change to your port, e.g., 'COM3' for Windows
baud_rate = 9600              # Set the baud rate to match the device

filename = "sit_down_4.csv"

try:
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    print(f"Connected to {serial_port} at {baud_rate} baud rate")

    # Continuously read from the serial port
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        while True:
            if ser.in_waiting > 0:  # Check if there's any data waiting to be read
                data = ser.readline().decode('utf-8').strip()
                #print(f"Received: {data}")
                values = data.split(',')
                writer.writerow(values)

        # Optional delay to avoid high CPU usage
        time.sleep(0.1)

except serial.SerialException as e:
    print(f"Could not open serial port {serial_port}: {e}")
except KeyboardInterrupt:
    print("Program interrupted. Closing serial port.")
finally:
    # Close the serial port when done
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
