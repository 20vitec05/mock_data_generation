import psycopg2
import random
import time
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

period = float(os.getenv("PERIOD", 1))


current_temp = random.uniform(20.0, 30.0)
current_humidity = random.uniform(40.0, 60.0)
current_pressure = random.uniform(980.0, 1020.0)
current_wind = random.uniform(0.0, 20.0)

def generate_mock():
    global current_temp, current_humidity, current_pressure, current_wind
    
    step_temp = 0.1
    step_humidity = 0.5
    step_pressure = 0.2
    step_wind = 0.5
    
    current_temp += random.uniform(-step_temp, step_temp)
    current_temp = max(15.0, min(35.0, current_temp))
    
    current_humidity += random.uniform(-step_humidity, step_humidity)
    current_humidity = max(20.0, min(100.0, current_humidity))
    
    current_pressure += random.uniform(-step_pressure, step_pressure)
    current_pressure = max(950.0, min(1050.0, current_pressure))
    
    current_wind += random.uniform(-step_wind, step_wind)
    current_wind = max(0.0, min(30.0, current_wind))
    
    return current_temp, current_pressure, current_wind, current_humidity
  

def log_to_db(cursor):
    ts = datetime.now()
    temperature, humidity, pressure, wind_speed = generate_mock()
    
    cursor.execute(
        "INSERT INTO measurements (ts, temperature, pressure, wind_speed, humidity) VALUES (%s, %s, %s, %s, %s)",
        (ts, temperature, pressure, wind_speed, humidity)
    )
  
def main():
    conn = psycopg2.connect(
      host=os.getenv("DB_HOST"),
      port=os.getenv("DB_PORT"),
      dbname=os.getenv("DB_NAME"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD")
    )
    conn.autocommit = True
    with conn.cursor() as cur:
      while True:
            log_to_db(cur)
            time.sleep(period)
      
