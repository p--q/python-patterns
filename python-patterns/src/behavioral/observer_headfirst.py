#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
class WeatherData:  # Subject
    def __init__(self):
        self._observers = list()    
    def registerObserver(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)    
    def removeObserver(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)  
    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self)  
    def measurementsChanged(self):
        self.notifyObservers()
    def setMeasurements(self,temperature,humidity,pressure):  # 測定値を取得する。
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity
    def getPressure(self):
        return self.pressure
class CurrentConditionsDisplay:  # Observer
    def update(self,subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.display()
    def display(self):
        print("Current conditions: {}F degrees and {}% humidity".format(self.temperature, self.humidity))
class ForecastDisplay:  # Observer
    def __init__(self):
        self.currentPressure = 29.92   
    def update(self,subject):
        self.lastPressure = self.currentPressure
        self.currentPressure = subject.pressure
        self.display()
    def display(self):
        print("Forecast: ");
        if self.currentPressure > self.lastPressure:
            print("Improving weather on the way!")
        elif self.currentPressure == self.lastPressure:
            print("More of the same");
        elif self.currentPressure < self.lastPressure:
            print("Watch out for cooler, rainy weather")
class StatisticsDisplay:  # Observer
    def __init__(self):
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0     
    def update(self,subject):
        self.tempSum += subject.temperature
        self.numReadings += 1
        if subject.temperature > self.maxTemp:
            self.maxTemp = subject.temperature
        if subject.temperature < self.minTemp:
            self.minTemp = subject.temperature
        self.display()
    def display(self):
        print("Avg/Max/Min temperature = {}/{}/{}".format(self.tempSum/self.numReadings, self.maxTemp, self.minTemp))
class HeatIndexDisplay:  # Observer
    def __init__(self):
        self.heatIndex = 0.0     
    def update(self,subject):
        self.heatIndex = self.computeHeatIndex(subject.temperature,subject.humidity)
        self.display()
    def computeHeatIndex(self,t,rh):
        return (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) - (0.0000000000481975 * (t * t * t * rh * rh * rh))
    def display(self):
        print("Heat index is {}".format(self.heatIndex))    
if __name__ == '__main__':
    weatherData = WeatherData()  # Subject 

    currentDisplay = CurrentConditionsDisplay()  # Observer
    statisticsDisplay = StatisticsDisplay()  # Observer
    forecastDisplay = ForecastDisplay()  # Observer
    heatIndexDisplay = HeatIndexDisplay()  # Observer 

    weatherData.registerObserver(currentDisplay)  # Register an Observer
    weatherData.registerObserver(statisticsDisplay)
    weatherData.registerObserver(forecastDisplay)
    weatherData.registerObserver(heatIndexDisplay)   

    # Input test data
    weatherData.setMeasurements(80, 65, 30.4)
    print()
    weatherData.setMeasurements(82, 70, 29.2)
    print()
    weatherData.setMeasurements(78, 90, 29.2)
