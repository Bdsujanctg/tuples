class ferrari():
    def adv(self):
        print("Ferrari is faster than Lamborghini")
    def adv2(self):
        print("Ferraris are generally cheaper than Lamborghini")
    def disadv(self):
        print("Ferraris are not weather friendly")
class lamborghini():
    def adv(self):
        print("Lamborghinis are good for both city and highway driving.")
    def adv2(self):
        print("Lamborghinis are easier to handle in wet or slippery conditions")
    def disadv(self):
        print("On average, Lamborghinis cost more than Ferraris.")  
obj_fer=ferrari()
obj_lam=lamborghini()
for cars in (obj_fer,obj_lam):
  cars.adv()
  cars.adv2()
  cars.disadv()