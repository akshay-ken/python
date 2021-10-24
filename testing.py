class Animal:
    def __init__(self,fur_color):
        self.fur_color = fur_color

    def eat(self):
        print('I am eating')
    def chase(self,name='prey'):
        print(f'I am chasing a {name}')

    def get_a_fur_color(self):
        print(self.fur_color)
    
class HouseAnimal(Animal):
    def __init__(self, fur_color):
        super().__init__(fur_color)
    def speak(self):
        print('speaking')
    def chase(self, name='other animal'):
        super().chase(name)
        print(f'chased the {name}')

newanmial = HouseAnimal('orange')
print(newanmial.chase())
print(newanmial.get_a_fur_color())