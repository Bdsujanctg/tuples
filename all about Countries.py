class India():
  def capital(self):
    print("New Delhi is the capital of India ")
  def language(self):
    print("Hindi is the most widely spoken language of India")
  def type(self):
    print("India is a developing country")
class USA():
  def capital(self):
    print("Washington D.C. is the capital of USA ")
  def language(self):
    print("English is the most widely spoken language of USA")
  def type(self):
    print("USA is a developed country")
obj_india=India()
obj_usa=USA()
for country in (obj_india,obj_usa):
  country.capital()
  country.language()
  country.type()
  
