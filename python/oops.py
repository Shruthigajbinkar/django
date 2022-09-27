#oops

class Square:
    def __init__(self,l,w,h):
        self.length=l
        self.width=w
        self.height=h

    def getvolume(self):
        volume=self.length*self.width*self.height

        return volume

obj1=Square(20,40,60)
volume=obj1.getvolume()
print(volume)

        
    
