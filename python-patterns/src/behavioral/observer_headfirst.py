#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-
class WeatherData:  # Subject
    def setMeasurements(self,temperature,humidity,pressure):  # 測定値を取得する。
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
    def getTemperature(self):
        return self.temperature
    def getHumidity(self):
        return self.humidity
    def getPressure(self):
        return self.pressure
class CurrentConditionsDisplay:  # Observer
    def update(self,this):
        self.temperature = this.temperature
        self.humidity = this.humidity
        self.display()
    def display(self):
        print("Current conditions: {}F degrees and {}% humidity".format(self.temperature, self.humidity))
class ForecastDisplay:  # Observer
    def __init__(self):
        self.currentPressure = 29.92   
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
class StatisticsDisplay:  # Observer
    def __init__(self):
        self.maxTemp = 0.0
        self.minTemp = 200
        self.tempSum = 0.0
        self.numReadings = 0     
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
class HeatIndexDisplay:  # Observer
    def __init__(self):
        self.heatIndex = 0.0     
    def update(self,this):
        self.heatIndex = self.computeHeatIndex(this.temperature,this.humidity)
        self.display()
    def computeHeatIndex(self,t,rh):
        return (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + 0.000000000843296 * (t * t * rh * rh * rh)) - (0.0000000000481975 * (t * t * t * rh * rh * rh))
    def display(self):
        print("Heat index is {}".format(self.heatIndex))    
        
import types        
class Observe:  # Observer Broker
    def __init__(self,subject,subject_m_name):
        '''
        the Class intermediating Observer methods and a Subject method
        :param subject: a Subject instance
        :type subject: Object
        :param subject_m_name: the name of a Subject method (the observed method)
        :type subject_m_name: str
        :returns: Observer Broker instance
        :rtype: Object
        '''
        self._observer_ms = list()  # the list of Observer methods
        self.subject = subject  # the instance of the Subject
        self.subject_m_name = subject_m_name  # the name of the Subject method
        self.subject_m = getattr(self.subject, self.subject_m_name)  # the method object of the Subject method
    def register(self, observer_m):
        '''
        Register a observer method
        :param observer_m: Observer method
        :type observer_m: Method Object
        :returns: None
        :rtype: None
        '''
        if observer_m not in self._observer_ms:
            self._observer_ms.append(observer_m)
        self._observe()  # Replace the Subject method    
    def _decorator(self,f):
        '''
        Decorator of the Subject method
        :param f: the Subject method
        :type f: Method Object
        :returns: Function to be replaced with the Subject method
        :rtype: Function Object
        '''
        def g(this,*args):
            return self._execute(this,f,*args)        
        return g
    def remove(self, observer_m):
        '''
        Remove a observer method
        :param observer_m: Observer method
        :type observer_m: Method Object
        :returns: None
        :rtype: None
        '''
        if observer_m in self._observer_ms:
            self._observer_ms.remove(observer_m)
    def _observe(self):  # Subjectのメソッドをself._registerに置換する。
        '''
        Replace the Subject method
        :returns: None
        :rtype: None
        '''
        setattr(self.subject, self.subject_m_name, types.MethodType(self._decorator(self.subject_m), self.subject))
    def _execute(self,this,f,*args):  # Subjectのメソッドと入れ替わる関数。*argsは元のSubjectのメソッドの引数。
        '''
        Function to be replaced with the Subject method
        :param this: Subject
        :type this: Object
        :param f: the original Subject method
        :type f:  Method Object
        :returns: None
        :rtype: None
        '''
        f(*args)  # 置換する前のSubjectのメソッドをまず実行。
        for observer_m in self._observer_ms:  # Observerのリストにあるメソッドをすべて実行する。
            observer_m(this)    
                    
if __name__ == '__main__':
    weatherData = WeatherData()  # Subject 

    currentDisplay = CurrentConditionsDisplay()  # Observer
    statisticsDisplay = StatisticsDisplay()  # Observer
    forecastDisplay = ForecastDisplay()  # Observer
    heatIndexDisplay = HeatIndexDisplay()  # Observer 

    obs = Observe(weatherData,"setMeasurements")  # the Observed method

    obs.register(currentDisplay.update)  # Register an Observer method
    obs.register(statisticsDisplay.update)  # removeする予定がなければ、インスタンスを変数で保持しておく必要はない。登録順に実行される。
    obs.register(forecastDisplay.update)
    obs.register(heatIndexDisplay.update)   
    
    # Input test data
    weatherData.setMeasurements(80, 65, 30.4)
    print()
    weatherData.setMeasurements(82, 70, 29.2)
    print()
    weatherData.setMeasurements(78, 90, 29.2)
