import math
class Calculator:
    def __init__(self, data):
        self.data = sorted(data)
        self._calc_stats()
        
    def _calc_stats(self):  
        self.length = self._length()
        self.mean = self._mean()  
        self.median = self._median()
        self.variance = self._variance()
        self.stand_dev = self._stand_dev()

    def add_data(self, data):
        self.data.extend
        self._calc_stats()
   
    def remove_data(self, data):
        self.data.[x for x in self.data if x not in new_data]
        self._calc_stats()
    


    def _length(self):
        return  len(self.data)
    
    def _mean(self):
        return  sum(self.data)/len(self.data)

    def _median(self):
        n = len(self.data)
        s = sorted(self.data)
        med = (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None    
        return  med
    
    def _variance(self):
        x = [n - self.mean for n in self.data]
        z = [i**2 for i in x ]
        av = sum(z)/len(z)
        return  av
    
    def _stand_dev(self):
        sd = math.sqrt(self._variance())
        return sd

data = [1,56,77,90,103,476,889]
calc = Calculator(data)
print(calc.length)
print(calc.mean)
print(calc.median)
print(calc.variance)
print(calc.stand_dev)


