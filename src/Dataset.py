import datetime

class Dataset:

    def __init__(self, timestamp, x_load, y_load, friction_load, imu_angle, data_rate, limit_one, limit_two):
        self.timestamp = timestamp
        self.x_load = x_load
        self.y_load = y_load
        self.friction_load = friction_load
        self.imu_angle = imu_angle
        self.data_rate = data_rate
        self.limit_one = limit_one
        self.limit_two = limit_two
