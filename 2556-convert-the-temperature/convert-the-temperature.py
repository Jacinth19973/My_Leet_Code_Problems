class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr=[]
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        arr.append(Kelvin)
        arr.append(Fahrenheit)
        return arr

        