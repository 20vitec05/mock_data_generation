import threading
import psycopg2
import random
from datetime import datetime

def generate_mock():
  temperature = random.uniform(20.0, 30.0)
  humidity = random.uniform(40.0, 60.0)
  pressure = random.uniform(980.0, 1020.0)
  wind_speed = random.uniform(0.0, 20.0)
  return temperature, humidity, pressure, wind_speed

def log_to_db(connection, temperature, humidity, pressure, wind_speed):
    ts = datetime.now()
    connection.execute(
        "INSERT INTO measurements (ts, temperatue, pressure, wind_speed) VALUES (%s, %s, %s, %s)",
        (ts, temperature, pressure, wind_speed)
    )
    threading.Timer(1, log_to_db).start()

def main():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="your_db",
        user="your_user",
        password="your_password"
    )
    conn.autocommit = True
    with conn.cursor() as cur:
      log_to_db(cur,*generate_mock())
      
print(datetime.now())
