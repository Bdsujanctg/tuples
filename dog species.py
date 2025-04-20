class dog:
    breed="animal"
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
dog1= dog("Jack","british bulldog","9")
dog2= dog("Bear","golden retriever","2")
print('{} is a dog'.format(dog1.name))
print('{} is a dog'.format(dog2.name))
print('{} is a {} and he is {} years old'.format(dog1.name,dog1.breed,dog1.age))
print('{} is a {} and he is {} years old'.format(dog2.name,dog2.breed,dog2.age))


         