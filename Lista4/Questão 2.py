# CES-22: Programação Orientada à Objeto
# Professor: Yano
# Código utilizado para Questão 2 da Lista 4 de Python
# Escrito por Lucas do Vale Bezerra, COMP-22

import six
from abc import ABCMeta

# Classe abstrata de Pizzas
@six.add_metaclass(ABCMeta)
class Abstract_Pizza(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.02*self.get_cost()


class Mussarela_Pizza(Abstract_Pizza):
   
   def get_cost(self):
      return 1.00
   
   def get_ingredients(self):
      return 'queijo'

# Decorador da Classe abstrata
@six.add_metaclass(ABCMeta)
class Abstract_Pizza_Decorator(Abstract_Pizza):
   
   def __init__(self,decorated_pizza):
      self.decorated_pizza = decorated_pizza
   
   def get_cost(self):
      return self.decorated_pizza.get_cost()
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients()

# Tipos de ingredientes da Pizza
class Tomate(Abstract_Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Abstract_Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost()
   
   def get_ingredients(self):
	   return self.decorated_pizza.get_ingredients() + ', tomate'

class Cebola(Abstract_Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Abstract_Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 0.25
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients() + ', cebola'

class Calabresa(Abstract_Pizza_Decorator):
   
   def __init__(self,decorated_pizza):
      Abstract_Pizza_Decorator.__init__(self,decorated_pizza)
   
   def get_cost(self):
      return self.decorated_pizza.get_cost() + 0.75
   
   def get_ingredients(self):
      return self.decorated_pizza.get_ingredients() + ', calabresa'

# Testando a implementação
pizza = Mussarela_Pizza()
pizza_calabresa = Calabresa(pizza)


minhaPizza = Mussarela_Pizza()
print('Ingredientes: '+minhaPizza.get_ingredients()+
   '; Custo: '+str(minhaPizza.get_cost())+'; Taxa = '+str(minhaPizza.get_tax()))

minhaPizza = Calabresa(minhaPizza)
print('Ingredientes: '+minhaPizza.get_ingredients()+
   '; Custo: '+str(minhaPizza.get_cost())+'; Taxa = '+str(minhaPizza.get_tax()))

minhaPizza = Cebola(minhaPizza)
print('Ingredientes: '+minhaPizza.get_ingredients()+
   '; Custo: '+str(minhaPizza.get_cost())+'; Taxa = '+str(minhaPizza.get_tax()))

minhaPizza = Tomate(minhaPizza)
print('Ingredientes: '+minhaPizza.get_ingredients()+
   '; Custo: '+str(minhaPizza.get_cost())+'; Taxa = '+str(minhaPizza.get_tax()))