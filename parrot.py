class parrot:
    species='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot('blu','14')
woo=parrot('woo','16')
print('Blu is a {}'.format(blu.species))
print('Woo is a {}'.format(woo.species))
print('{} is a {} years old'.format(blu.name,blu.age))
print('{} is a {} years old'.format(blu.name,blu.age))