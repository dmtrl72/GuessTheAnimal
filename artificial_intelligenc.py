from binary_tree import *

class ArtificialIntelligenc:
   def __init__(self):
       self._animal_bd_=BinaryTree()
       self._animal_bd_.create_root("Кот")

   def exist_question(self):
       return not self._animal_bd_.is_leaf()

   def ask(self):
       return  self._animal_bd_.get_current_data()

   def next_question(self,answer):
        if answer: self._animal_bd_.goto_right()
        else:      self._animal_bd_.goto_left()

   def learn(self,a,q):
        self._animal_bd_.add_left(self._animal_bd_.get_current_data())
        self._animal_bd_.add_right(a)
        self._animal_bd_.set_current_data(q)

   def start(self):
       self._animal_bd_.goto_first()
