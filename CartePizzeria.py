class CartePizzeria:

pizza = []

def.__init__(self)

def is_empty(self):
    if(len self.pizza == 0):
        return True
    return False

def nb_pizzas(self):
    return len(self.pizzas)

def add_pizza(self, pizza):
    self.pizzas.append(pizza)

def remove_pizza(self, name):
    for pizza in self.pizzas:
         if pizza.name == name:
                self.pizzas.remove(pizza)
            return
     raise Exception (f"La pizza '{name}' n'existe pas dans la carte.")

     



