import csv
import random
import time
from datetime import datetime

def generate_random_data(num_rows):
    rpm = random.randint(800, 7000)
    speed = random.randint(0, 200)
    return rpm, speed
def log_data(filename="telemetry_log.csv", num_rows=100):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "RPM", "Speed"])

        print(f"Logging {num_rows} rows of data to {filename}...")

        while True:
            rpm, speed = generate_random_data(num_rows)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, rpm, speed])
            print(f"Logged data: {timestamp}, RPM: {rpm}, Speed: {speed} km/h")
            time.sleep(1)  # Simulate a delay between data entries
log_data()