from binary_tree import BinaryTree
animal_bd = BinaryTree()
# считать данныые с файла, если существует, иначе
animal_bd.create_root("Кот")
yes_no=1;
while yes_no==1:
    print("Загадай животное. Готов? (Да-1, Нет-0)")
    yes_no=int(input())
    # Проход по вопросам
    animal_bd.goto_first()
    while not animal_bd.is_leaf():
        print(animal_bd.get_current_data(),"(Да-1, Нет-0)")
        yes_no=int(input())
        if yes_no: animal_bd.goto_right()
        else:      animal_bd.goto_left()
    print("Это", animal_bd.get_current_data()+"? (Да-1, Нет-0)")
    yes_no=int(input())
    if yes_no: print("Я победил!!! AI --- рулит!")
    else:
        # Если не угадал, спросить "кто это?"
        a=input("Кто это? ");
        # узнать как отличить
        q=input("Задай вопрос, ответом ДА, на который будет "+a+", а ответом НЕТ ---"+animal_bd.get_current_data()+" ");
        # В правый лист записать новое животное, в левый лист --- сатрое, в их родителя вопрос.
        animal_bd.add_left(animal_bd.get_current_data())
        animal_bd.add_right(a)
        animal_bd.set_current_data(q)
        print(animal_bd.get_data_list())
        print(animal_bd.get_left_list())
        print(animal_bd.get_right_list())
    yes_no=int(input("Хочешь сыграть ещё? (Да-1, Нет-0)"))

    # TODO: Сохранение в файл реализовать. Считывание также.
