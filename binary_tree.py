# Структура данных: поле данных, курсор на левого сына, курсор на правого сына
class BinaryTree:
# Инициализация. Сделать пустым
    def __init__(self):
        self._data_    = []
        self._left_    = []
        self._right_   = []
        self._root_    = -1
        self._current_ = -1
        self._marker_ = -1

# Встать в начало
    def goto_first(self):
        self._current_=self._root_

# Проверить, есть ли левый сын
    def is_right_empty(self):
       return self._right_[self._current_] == -1


# Проверить, есть ли правый сын
    def is_left_empty(self):
        return self._left_[self._current_] == -1

# Переместиться к левому сыну
    def goto_left(self):
        if not self.is_left_empty():
            self._current_=self._left_[self._current_]


# Переместиться к правому сыну
    def goto_right(self):
        if not self.is_right_empty():
            self._current_=self._right_[self._current_]


# Это лист?
    def is_leaf(self):
        return self.is_left_empty() and self.is_right_empty()


# Добавить, левого сына, если его ещё нет.
    def add_left(self,left_data):
        if self.is_left_empty():
           self._data_.append(left_data)
           self._left_.append(-1)
           self._right_.append(-1)
           self._left_[self._current_] = len(self._data_) - 1
           return True
        return False

# Добавить, правого сына, если его ещё нет.
    def add_right(self,right_data):
        if self.is_right_empty():
            self._data_.append(right_data)
            self._left_.append(-1)
            self._right_.append(-1)
            self._right_[self._current_] = len(self._data_) - 1
            return True
        return False

# Создать корень
    def create_root(self,data):
        BinaryTree()
        self._root_    = 0
        self._data_.append(data)
        self._left_.append(-1)
        self._right_.append(-1)

# Заменить текущее поле данных
    def set_current_data(self,cur_data):
        self._data_[self._current_] = cur_data

# Заменить текущее поле данных
    def set_current_data(self,cur_data):
        self._data_[self._current_] = cur_data


# Получить текущее поле данных
    def get_current_data(self):
        return self._data_[self._current_]

# Получить список полей данныъх
    def get_data_list(self):
        return self._data_


# Получить список курсоров на левых сыновей
    def get_left_list(self):
        return  self._left_

# Получить список курсоров на правых сыновей
    def get_right_list(self):
        return self._right_


# Получить список полей данныъх
    def set_data_list(self,list_data):
        self._data_ = list_data


# Получить список курсоров на левых сыновей
    def set_left_list(self,list_left):
        self._left_ = list_left


# Получить список курсоров на правых сыновей
    def set_right_list(self,list_list_left):
        self._right_ = list_right


# Установить маркер на текущую позиуию
#    def set_marker(self):
#        self._marker_ = self._current_

# Перейти на маркированную позицию
    def goto_marker(self):
        self._current_=self._marker_
