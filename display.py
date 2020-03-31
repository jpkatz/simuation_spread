import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Display():
    def __init__(self,details_instance):
        self.size_x,self.size_y = details_instance.fig_size
        self.length_1d = details_instance.num_people_1d
        
        
        self.x_length = details_instance.x_length
        self.y_length = details_instance.y_length
        
    def create_plot(self,plot_size = (5,5)):
        self.fig = plt.figure(figsize = plot_size)
        self.ax = self.fig.subplots()
        
        canvas = patches.Rectangle((0,0),1,1,fill=True,
                           edgecolor='none',facecolor='g')
        self.ax.add_patch(canvas)

     
        
    #This function needs its matrices transposed, will deal with later 
    def update_plot(self,infected_table=None,kill_table = None): 
        infected_table = list(map(list, zip(*infected_table)))
        kill_table = list(map(list, zip(*kill_table)))
        for i,row in enumerate(infected_table):
            for j,col in enumerate(row):
                #current_truth = truth_table[i][j]
                # current_truth = col
                infected_person = col
                dead_person = kill_table[i][j]
                if dead_person:
                    coord = i*self.x_length,j*self.y_length
                    square = patches.Rectangle(coord,
                                       self.x_length,self.y_length,
                                       fill=True,
                                       edgecolor = 'none',
                                       facecolor = 'r')
                    self.ax.add_patch(square)
                if infected_person and not dead_person:
                    coord = i*self.x_length,j*self.y_length
                    square = patches.Rectangle(coord,
                                       self.x_length,self.y_length,
                                       fill=True,
                                       edgecolor = 'none',
                                       facecolor = 'y')
                    self.ax.add_patch(square)
        plt.show()
        plt.pause(0.1)