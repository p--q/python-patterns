#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
import types
class WeatherData:  # Subject
    def measurementsChanged(self):
        pass
    def setMeasurements(self,temperature,humidity,pressure):  # 測定値を取得する。
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()  # 測定値が変化したことを伝える。
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity
    def getPressure(self):
        return self.pressure
class CurrentConditionsDisplay:  # Observer
#     def __init__(self,weatherData):
    def observe(self,weatherData):
        weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
#     def observe(self,bound_method):
#         bound_method.__self__.measurementsChanged = types.MethodType(self.register(bound_method), bound_method.__self__)   
    def register(self,f):
        
        
        def g(this):
            f()
            return self.update(this)
        return g
    def update(self,this):
        self.temperature = this.temperature
        self.humidity = this.humidity
        self.display()
    def display(self):
        print("Current conditions: {}F degrees and {}% humidity".format(self.temperature, self.humidity))
class ForecastDisplay:
    def __init__(self):
#     def __init__(self,weatherData):
#         weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
        self.currentPressure = 29.92
    def observe(self,weatherData):
        weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
#     def observe(self,bound_method):
#         bound_method = types.MethodType(self.register(bound_method), bound_method.__self__)    
    def register(self,f):
        def g(this):
            f()
            return self.update(this)
        return g        
    def update(self,this):
        self.lastPressure = self.currentPressure
        self.currentPressure = this.pressure
        self.display()
    def display(self):
        print("Forecast: ");
        if self.currentPressure > self.lastPressure:
            print("Improving weather on the way!")
        elif self.currentPressure == self.lastPressure:
            print("More of the same");
        elif self.currentPressure < self.lastPressure:
            print("Watch out for cooler, rainy weather")
class StatisticsDisplay:
    def __init__(self):
#     def __init__(self,weatherData):
#         weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0
    def observe(self,weatherData):
        weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
    def register(self,f):
        def g(this):
            f()
            return self.update(this)
        return g          
    def update(self,this):
        self.tempSum += this.temperature
        self.numReadings += 1
        if this.temperature > self.maxTemp:
            self.maxTemp = this.temperature
        if this.temperature < self.minTemp:
            self.minTemp = this.temperature
        self.display()
    def display(self):
        print("Avg/Max/Min temperature = {}/{}/{}".format(self.tempSum/self.numReadings, self.maxTemp, self.minTemp))
class HeatIndexDisplay:
    def __init__(self):
#     def __init__(self,weatherData):
#         weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
        self.heatIndex = 0.0
    def observe(self,weatherData):
        weatherData.measurementsChanged = types.MethodType(self.register(weatherData.measurementsChanged), weatherData)
    def register(self,f):
        def g(this):
            f()
            return self.update(this)
        return g           
    def update(self,this):
        self.heatIndex = self.computeHeatIndex(this.temperature,this.humidity)
        self.display()
    def computeHeatIndex(self,t,rh):
        return (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) - (0.0000000000481975 * (t * t * t * rh * rh * rh))
    def display(self):
        print("Heat index is {}".format(self.heatIndex))      


if __name__ == '__main__':
    
#     def register(self):
#         callbacks = list()
#         def g(this):
#             callbacks.append(self.update(this))
#             return lambda callbacks: [fn() for fn in callbacks]
#         return g    





    weatherData = WeatherData()
#     currentDisplay = CurrentConditionsDisplay(weatherData)
#     statisticsDisplay = StatisticsDisplay(weatherData)
#     forecastDisplay = ForecastDisplay(weatherData)
#     heatIndexDisplay = HeatIndexDisplay(weatherData)


    currentDisplay = CurrentConditionsDisplay()
    statisticsDisplay = StatisticsDisplay()
    forecastDisplay = ForecastDisplay()
    heatIndexDisplay = HeatIndexDisplay()
    
    
    currentDisplay.observe(weatherData)
    statisticsDisplay.observe(weatherData)
    forecastDisplay.observe(weatherData)
    heatIndexDisplay.observe(weatherData)
    
#     weatherData = WeatherData()
#     currentDisplay.observe(weatherData)
    
    
#     forecastDisplay.update = types.MethodType(lambda :pass, forecastDisplay)
    
    
    
    weatherData.setMeasurements(80, 65, 30.4)
    print()
    weatherData.setMeasurements(82, 70, 29.2)
    print()
    weatherData.setMeasurements(78, 90, 29.2)
    
