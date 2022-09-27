#abstarction
class Animal(ABC):

    @abstarctmethod
    def sounds(self):
        pass
class Dog(Animal):
    def sounds(self):
        print('bow bow')

class Cat(Animal):
    def sounds(self):
        print('meow meow')
C=Cat()
C.sounds()

D=Dog()
D.sounds()
