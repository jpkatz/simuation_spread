from person import Person
import random

class Population():
    def __init__(self,persons=[],details_instance =None,virus_strain=None):
        if len(persons)<1:
            print('There is no population! Adding a member')
            self.persons = persons
            self.count = 0
            self.add_person()
            
        else:
            self.persons = persons
        self.details_instance = details_instance
        self.virus_strain = virus_strain
        self.dead_persons = [[]]
            
    def add_person(self):
        if len(self.persons)<1:
            self.persons.append(Person(id=self.count,
                                  discrete_location = (0,0),
                                  infected = False)
                           )
            self.count +=1
        else:
            loc_x = self.details_instance.x_length*(self.count%self.details_instance.num_people_1d)
            loc_y = self.details_instance.y_length*((self.count - self.count%self.details_instance.num_people_1d)/self.details_instance.num_people_1d)
            person = Person(id = self.count,
                             discrete_location = (loc_x,loc_y),
                             infected = False)
            self.count +=1
            self.persons.append(person)
            
            
    def get_infected_table(self):
        truth_table = []
        current_list = []
        i = 0
        while i < self.count:
            current_list.append(self.persons[i].infected)
            i+=1
            if (i)%(self.details_instance.num_people_1d) ==0:
                truth_table.append(current_list)
                current_list = []
        if self.count%(self.details_instance.num_people_1d) !=0:
            truth_table.append(current_list)
        
        #Transpose truth_table
        # return list(map(list, zip(*truth_table)))
        return truth_table
    
    def get_dead_table(self):
        truth_table = []
        current_list = []
        i = 0
        while i < self.count:
            current_list.append(self.persons[i].dead)
            i+=1
            if (i)%(self.details_instance.num_people_1d) ==0:
                truth_table.append(current_list)
                current_list = []
        if self.count%(self.details_instance.num_people_1d) !=0:
            truth_table.append(current_list)
        
        return truth_table

      
    def kill_infected(self,infected_table):
        linear_indices = self.get_infected_indices(infected_table)
        for index in linear_indices:
            still_living = self.persons[index].do_i_live()
            if not still_living:
                self.persons[index].kill()
                self.dead_persons.append(index)
        
    def add_neighbors(self):
        #Currently returns the linear index! Compatible with persons!!
        if len(self.persons)<=1:
            return
        
        #One method:
            #Use self.count and modulos to identify neighbors
        #I believe a better method that I do not follow:
            #Use the discrete locations(more effeective to go to higher dim)
            #Using discrete location has the downside of comparing floats
            
        #Using first method
        for i in range(self.count):
            #at left boundary
            if i%self.details_instance.num_people_1d==0:
                left = -1
            else:
                left = i-1
            #at right boundary
            if (i+1)%self.details_instance.num_people_1d==0:
                right = -1
            else:
                right = i+1
            
            up = i+self.details_instance.num_people_1d
            down = i - self.details_instance.num_people_1d
            
            #First build potential neighbors
            potential_neighbors = [left,right,up,down]
            
            #Second identify if any potential neighbors don't exist
            neighbor_list = []
            for j in potential_neighbors:
                if (j >= 0) and (j<self.count):
                    neighbor_list.append(j)
                    
            #Third update the person with neighbors
            self.persons[i].neighbors = neighbor_list
    
    def spread_infection(self,infected_table):
        linear_indices = self.get_infected_indices(infected_table)
        for index in linear_indices:
            current_infected_person = self.persons[index]
            neighbors = current_infected_person.neighbors
            for neighbor in neighbors:
                if random.random()<current_infected_person.virus.IR:
                    self.persons[neighbor].become_infected(self.virus_strain)
                            
    def get_infected_count(self):
        infected_people = 0
        for person in self.persons:
            if person.infected:
                infected_people+=1
        return infected_people
    
    def get_dead_count(self):
        dead_people = 0
        for person in self.persons:
            if person.dead:
                dead_people+=1
        return dead_people
    
    def get_infected_indices(self,infected_table):
        #returns the linear indices of those infected
        linear_indices=[]
        for i,row in enumerate(infected_table):
            for j,col in enumerate(row):
                if col:
                    linear_indices.append(j+i*self.details_instance.num_people_1d)
        return linear_indices
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        