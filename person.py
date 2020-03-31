import random

class Person():
    
    def __init__(self,id = None,discrete_location = None,infected = False):
        self.id = id
        if discrete_location:
            self.dl_x,self.dl_y = discrete_location
        else:
            raise Exception()
        self.infected = infected
        self.neighbors = []
        self.dead = False
        
    def become_infected(self,virus):
        if not self.dead:
            self.infected = True
            self.virus = virus
    
    def do_i_live(self):
        return random.random()>self.virus.MR
    
    def kill(self):
        self.dead = True
        self.infected = False