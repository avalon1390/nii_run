class Sensor:  # Баззовый класс датчиков

    def __init__(self, mac):  # Инициализация с установкой сетевого адресата - мака
        self.mac = mac
        self.data = None

    def get(self):  # Запрос показаний текущих
        return self.data

    def set(self, data, is_processing):  # установка расписания автоматической отправки показания датчика
        if is_processing:
            self.data = self.processing_data(data)
        else:
            self.data = data
        return self.data

    def processing_data(self, data):
        return data



class Temperature_sensor(Sensor):  # Класс датчика температуры

    def processing_data(self, data):
        data = "Temperature"
        return data



class Switcher(Sensor):  # Класс переключателя - электричество, газ, вода


    def processing_data(self, data): # Запуск - включить/выключить
        return not data


