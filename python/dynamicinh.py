class Dog:
    def sounds(self):
        print('bow bow')
class Cat:
    def sounds(self):
        print('meow meow')
def call(obj):
    obj.sounds()
C=Cat()
call(C)

D=Dog
call(D)
              
