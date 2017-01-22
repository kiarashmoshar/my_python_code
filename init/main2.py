__author__ = 'kiarash7'
class enemy:
    def __init__(self,x ):
        self.energy=x
    def get_energy(self):
        print(self.energy)


jason=enemy(5)
sandy=enemy(18)

jason.get_energy()
sandy.get_energy()