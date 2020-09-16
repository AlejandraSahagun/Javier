class Products:

    # default constructor 
    def __init__(self, name, due_date): 
        self.name = name
        self.due_date = due_date
    
    def print_product(self): 
        return self.name + ', ' + self.due_date