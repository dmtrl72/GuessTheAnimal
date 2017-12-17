# Структура данных, поля данных, курсоры на левых сыновей, курсоры на правых сыновей
class BinaryTree:
   _data_=[]
   _left_=[]
   _right_=[]
   _root_=-1
   _current_=-1

empty_tree()

# Сделать пустым
def empty_tree():
    _data_    = []
    _left_    = []
    _right_   = []
    _root_    = -1
    _current_ = -1

# Встать в начало
def goto_first():
    _root_ = _current_

# Проверить, есть ли левый сын
def is_right_empty():
    return _right_[_current_] == -1


# Проверить, есть ли правый сын
def is_left_empty():
    return _left_[_current_] == -1


# Переместиться к левому сыну
def goto_left():
    global _current_
    if not is_left_empty():
        _current_=_left_[_current_]


# Переместиться к правому сыну
def goto_right():
    global _current_
    if not is_right_empty():
         _current_=_right_[_current_]


# Это лист?
def is_leaf():
    return is_left_empty and is_right_empty


# Добавить, левого сына, если его ещё нет.
def add_left(left_data):
    if is_left_empty():
        _data_.append(left_data)
        _left_.append(-1)
        _right_.append(-1)
        _left_[_current_] = len(_data_) - 1
        return True
    return False


# Добавить, правого сына, если его ещё нет.
def add_right(left_data):
    if is_right_empty():
        _data_.append(left_data)
        _left_.append(-1)
        _right_.append(-1)
        _right_[_current_] = len(_data_) - 1
        return True
    return False


# Заменить текущее поле данных
def add_current_data(cur_data):
    _data_[_current_] = cur_data


# Получить список полей данныъх
def get_data():
    return _data_


# Получить список курсоров на левых сыновей
def get_left():
    return _left_


# Получить список курсоров на правых сыновей
def get_right():
    return _right_


# Получить список полей данныъх
def set_data(list_data):
    _data_ = list_data


# Получить список курсоров на левых сыновей
def set_left(list_dleft):
    _data_ = list_left


# Получить список курсоров на правых сыновей
def set_right():
    _data_ = list_right
