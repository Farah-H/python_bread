# creating Factory class
class Factory:
    
    # make dough function takes water & bread and returns dough. 
    def make_dough(self, water_string, bread_string):
        # makes sure if the input is not 'water' and 'bread'
        if water_string == 'water' and bread_string == 'bread':
            return 'dough'
        
    # make naan function takes outcome of make_dough function and makes naan with it
    def make_naan(self,water_string, bread_string):
        # works if make_dough returned dough
        if self.make_dough(water_string, bread_string) == 'dough':
            return 'naan'

