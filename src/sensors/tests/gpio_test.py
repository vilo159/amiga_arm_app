from connections import *

def gpio_test():
    print("\n **********Beginning GPIO Test********** \n")

    for i in range(3):
        print("Blink: ", i)
        for pin in GPIO_PINS:
            print("Value:", GPIO.input(pin), "Pin:", pin)
        sleep(.5)
        for pin in GPIO_PINS:
            print("Value:", GPIO.input(pin), "Pin:", pin)
        sleep(.5)

    print("\n **********Ending GPIO Test********** \n")


if __name__ == "__main__":
    gpio_test()
