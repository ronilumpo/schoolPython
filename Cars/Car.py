class Car:
  
  __slots__ = ("__make", "__model", "__year", "__mileage")
  
  def __init__(self, make, model, year, mileage):
    self.__make = make
    self.__model = model
    self.__year = year
    self.mileage = mileage
  
  @property  
  def make(self):
    return self.__make
  
  @property
  def model(self):
    return self.__model
  
  @property  
  def year(self):
    return self.__year  
  
  @property
  def mileage(self):
    return self.__mileage
  
  @mileage.setter
  def mileage(self, x):
    self.__mileage = x
    
  def __str__(self):
    return "Make: {}\nModel: {}\nYear: {}\nMileage: {}\n".format(self.__make, self.__model, self.__year, self.__mileage)
    
  def __lt__(self, other):
    if self.__make != other.__make:
      return self.__make < other.__make
    elif self.__model != other.__model:
      return self.__model < other.__model
    elif self.__year != other.__year:
      return self.__year < other.__year
    else:
      return self.__mileage < other.__mileage
    
  def __eq__(self, other):
    return self.__make == other.__make and self.__model == other.__model and self.__year == other.__year