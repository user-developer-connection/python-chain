class Car:
    # top_speed = 100
    # warning = []
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warning = []

    def __repr__(self):
        print('Printing...')
        return 'Top speed: {}, warings: {}'.format(self.top_speed, self.__warning.__len__())

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warning.append(warning_text)

    def get_warning(self):
        return self.__warning

    def drive(self):
        print('I am driving but certainly not fast than {}'.format(self.top_speed))



car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.add_warning('New Waring')
#car1.__warning.append('Test warnings')
#print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warning())

car3 = Car(250)
car3.drive()
print(car3.get_warning())