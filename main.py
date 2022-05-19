from sensors.measures import Measures

# This main class is made for testing purposes
if __name__ == '__main__':
    for i in range(5):
        print(Measures().get_temperature())
        print(Measures().get_power())
        print(Measures().get_load())
