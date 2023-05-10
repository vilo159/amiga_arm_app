from .connections import *
import configurator as config

class Friction_Load:

    def __init__(self):
        self.config_data = config.get('sensors', {})
        self.friction = 0.0
        self.friction_adc = 0.0
        try:
            self.slope = self.config_data['Friction Load']['slope']
            self.intercept = self.config_data['Friction Load']['intercept']
        except:
            self.slope = 1.0
            self.intercept = 0.0

    def get_data(self, adc_out = 0):
        try:
            if adc_out == 1:
                self.friction_adc = FRICTION_CHAN.value
                return self.friction_adc
            else:
                self.friction = (FRICTION_CHAN.value * self.slope) + self.intercept
                return self.friction
        except:
            if adc_out == 1:
                return self.friction_adc
            else:
                return self.friction
