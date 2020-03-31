from person import Person
from virus import Virus
from display import Display
from details import Details
from population import Population

import random
num_people_1d = 10

simul_details = Details(num_people_1d = num_people_1d,fig_size = (1,1))
virus_strain1 = Virus()
pop = Population(details_instance = simul_details,virus_strain=virus_strain1)

number_people = num_people_1d**2-1
for i in range(number_people):
    pop.add_person()
pop.add_neighbors()
starting_person = random.randint(0,number_people-1)
print('The starting person is %d' % starting_person)

pop.persons[starting_person].become_infected(virus_strain1)
current_infected = pop.get_infected_table()
current_dead = pop.get_dead_table()

simul_display = Display(details_instance=simul_details)
simul_display.create_plot()

total = 100
for iter in range(total):
    infected_people = pop.get_infected_count()
    dead_people = pop.get_dead_count()
    print('The iteration we are on is %d with %d infected' %(iter,infected_people))
    simul_display.update_plot(current_infected,current_dead)
    
    pop.spread_infection(current_infected)
    current_infected=pop.get_infected_table()
    pop.kill_infected(current_infected)
    current_dead = pop.get_dead_table()
    
    if infected_people+dead_people > number_people:
        print('All individuals are infected or dead!')
        break
