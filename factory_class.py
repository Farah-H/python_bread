class Factory:
    
    def make_dough(self, water_string, bread_string):
        if water_string == 'water' and bread_string == 'bread':
            return 'dough'
        
    
    def make_naan(self,water_string, bread_string):
        if self.make_dough(water_string, bread_string) == 'dough':
            return 'naan'

