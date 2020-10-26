class Food:
    def __init__(self, name,klass, color, taste, quality):
        self.name =name
        self.klass = klass
        self.color = color
        self.taste = taste
        self.supplement = False
        self.quality =quality
        self.supplement_food()

    def change_taste(self, new_taste):
        self.taste = new_taste

    def supplement_food(self):
        if self.quality < 65 or self.quality > 100 :
            self.supplement = True
        if self.supplement:
            print(self.name + " is being supplemented")
        else:
            print(self.name + " is not being supplemented")
        
    
    

yam = Food('Yam', 'carbonhydrate', 'white', 'bitter', 45)
beans = Food('beans', 'protein', 'chocolate', 'sweet', 70)

