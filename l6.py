class Firearms:
    className = 'Firearms'
    objectsCount = 0

    def __init__(self, name):
        self._name = name

        Firearms.objectsCount = Firearms.objectsCount + 1

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n


    def info(self):
        print(self._name)


class Assaultrifle(Firearms):
    className = 'Assaultrifle'

    def __init__(self, name, cartridges, speed, range, caliber):
        super().__init__(name)
        self._cartridges = cartridges
        self._speed = speed
        self._range = range
        self.caliber = caliber

    def get_cartridges(self):
        return self._cartridges

    def set_cartridges(self, cartridges):
        if cartridges > 0:
            self._cartridges = cartridges
        else:
            self._cartridges = 0.1

    def speed(self):
        return self._speed

    def range(self):
        return self._range

    def set_caliber(self, caliber):
        if caliber > 0:
            self.caliber = caliber
        else:
            self.caliber = 1

    def seconds(self):
        print(f'Магазин опустеет за: {self._speed * 60} сек')

    def ratio(self):
        print(f'Соотношение скорострельности к дальности стрельбы: {self._speed / self._range} ')

    def info(self):
        super().info()
        print(f'Тип: {Assaultrifle.className}')
        print(f"Количество патронов в магазине: {self._cartridges} ")
        print(f'Скорострельность: {self._speed} в/мин')
        print(f'Дальность стрельбы: {self._range} м')
        print(f"Калибр (мм): {self.caliber}")



b = Firearms("Объект класса " + Firearms.className)
b.info()


print('\n')

f = Assaultrifle('штурмовая винтовка', 20, 800, 500, 5.56)
f2 = Assaultrifle('снайперская винтовка', 10, 30, 1200, 7.62)


f.info()
f.ratio()
f.seconds()

f2.info()
f2.ratio()
f2.seconds()



print(f'Objects count: {Firearms.objectsCount}')