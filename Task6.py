class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Пример использования
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 100
print(f"{temp.fahrenheit}°F = {temp.celsius}°C")
