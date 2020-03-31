class Details():
    def __init__(self,num_people_1d,fig_size):
        self.num_people_1d = num_people_1d
        self.total_people = self.num_people_1d**2
        
        self.fig_size = fig_size
        
        self.x_length = self.fig_size[0]/num_people_1d
        self.y_length = self.fig_size[0]/num_people_1d