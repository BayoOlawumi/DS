class country:
    def __init__(self,name,currency,population):
        self.name =name
        self.currency =currency
        self.population =population
        self.peace = True
        self.lockdown =False

    def protest(self):
        self.peace = False
        

    def go_on_strike(self):
        self.lockdown =True

nigeria = country('Nigeria','Naira', 200)
nigeria.protest()
if nigeria.peace == False:
    print("God help us in Nigeria")



ghana =country('Ghana','CEDIS', 60)
ghana.go_on_strike()
if ghana.peace == False:
    print("God help us in Ghana")