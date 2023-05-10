#from sensors.Temperature import Temperature
# from sensors.Humidity import Humidity
from sensors.Location import Location
from sensors.X_Load import X_Load
from sensors.Y_Load import Y_Load
from sensors.Friction_Load import Friction_Load
from sensors.IMU import IMU
from sensors.Height import HeightPoT
import datetime
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Sensor:

    def __init__(self):
        self.REAL_DATA = True
        self.keys = ["Temperature","Humidity","Location","Time","X Load","Y Load","Friction Load","IMU Angle", "Load Cell Height"]
        self.temp = 0.0 #Temperature()
        self.hum = 0.0 #Humidity()
        self.location = Location()
        self.x_load = X_Load()
        self.y_load = Y_Load()
        self.friction_load = Friction_Load()
        self.imu_angle = IMU()
        self.load_cell_height = HeightPoT()
        self.time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.sensor_data = {}
        self.cpu_time = 0
        self.temp_fake = 0
        self.hum_fake = 0
        self.loc_fake = 0
        self.x_fake = 0
        self.y_fake = 0
        self.friction_fake = 0
        self.imu_fake = 0

    def get_header_data(self):
        self.sensor_data["Location"] = self.location.get_data()

    def get_sensor_data(self, adc_out = 0):
        self.sensor_data["X Load"] = round(self.x_load.get_data(adc_out),4)
        self.sensor_data["Y Load"] = round(self.y_load.get_data(adc_out),4)
        self.sensor_data["Friction Load"] = round(self.friction_load.get_data(adc_out),3)
        self.sensor_data["IMU Angle"] = round(self.imu_angle.get_data(adc_out),3)
        self.sensor_data["Load Cell Height"] = round(self.load_cell_height.get_data(adc_out),2)
        return self.sensor_data

    def clear_gps_memory(self):
        self.location.update_gps_location()

    def get_sensor_keys(self):
        return self.keys

if __name__ == "__main__":
    sensor = Sensor()
    print("\n **********Beginning Sensor Test********** \n")
    print("Sensor Data: ")
    data_array = sensor.get_sensor_data()
    for key in sensor.get_sensor_keys():
        print(key, data_array[key])
    print("\n **********Ending Sensor Test********** \n")
