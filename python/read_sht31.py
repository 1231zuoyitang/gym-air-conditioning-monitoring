import serial
import csv
from datetime import datetime

port = 'COM9'
baudrate = 9600

ser = serial.Serial(port, baudrate, timeout=2)

with open('temperature_humidity_log.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    if f.tell() == 0:
        writer.writerow(['timestamp', 'temperature_C', 'humidity_percent'])

    print('Start logging data... Press Ctrl+C to stop.')

    try:
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()

            if line:
                print('Received:', line)
                parts = line.split(',')

                if len(parts) == 2:
                    try:
                        temperature = float(parts[0])
                        humidity = float(parts[1])
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        writer.writerow([timestamp, temperature, humidity])
                        f.flush()

                        print(f'Saved: {timestamp}, {temperature}, {humidity}')
                    except ValueError:
                        print('Invalid data:', line)

    except KeyboardInterrupt:
        print('Logging stopped.')

    finally:
        ser.close()
