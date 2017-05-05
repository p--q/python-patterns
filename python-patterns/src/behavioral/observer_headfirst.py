#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
class WeatherData:  # Subject
    def mesurementsChanged(self):
        pass
    def setMeasurements(self,temperature,humidity,pressure):  # 測定値を取得する。
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.mesurementsChanged()  # 測定値が変化したことを伝える。
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity
    def getPressure(self):
        return self.pressure
class CurrentConditionsDisplay:  # Observer
    def __init__(self,weatherData):
        WeatherData.mesurementsChanged = self.register(WeatherData.mesurementsChanged)

#         weatherData.mesurementsChanged = self.register(weatherData.mesurementsChanged)

    def register(self,f):
        def g(this):
            self.temperature = this.temperature
            self.humidity = this.humidity
            self.display()
        return g
    def display(self):
        print("Current conditions: {}F degrees and {}% humidity".format(self.temperature, self.humidity))
class ForecastDisplay:
    def __init__(self,weatherData):
        self.weatherData = weatherData
        self.currentPressure = 29.92
        # notify
    def update(self,temperature,humidity,pressure):
        self.lastpressure = self.currentPressure
        self.currentPressure = pressure
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
    def __init__(self,weatherData):
        self.weatherData = weatherData
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0
        # notify           
    def update(self, temp, humidity, pressure):
        self.tempSum += temp
        self.numReadings += 1
        if self.temp > self.maxTemp:
            self.maxTemp = self.temp
        if self.temp < self.minTemp:
            self.minTemp = self.temp
        self.display()
    def display(self):
        print("Avg/Max/Min temperature = " + (self.tempSum / self.numReadings) + "/" + self.maxTemp + "/" + self.minTemp)
class HeatIndexDisplay:
    def __init__(self,weatherData):
        self.weatherData = weatherData
        self.heatIndex = 0.0
        # notify
    def update(self,t,rh,pressure):
        self.heatIndex = self.computeHeatIndex(t,rh)
        self.display()
    def computeHeatIndex(self,t,rh):
        return (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) - (0.0000000000481975 * (t * t * t * rh * rh * rh))
    def display(self):
        print("Heat index is " + self.heatIndex)      
if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)
    
    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)
    
