# Ещё больше разделяем интерфейс и код
from artificial_intelligence import *

ai=ArtificialIntelligence()
exit_game=False;
while not exit_game:
    print("Загадай животное. Готов?")
    ans=int(input("(Да-1, Нет-0)"))
    ai.start()
    while ai.exist_question():
        print(ai.ask)
        ans=bool(input("(Да-1, Нет-0)"))
        ai.next_question(ans)
    print("Это", ai.ask() + "? (Да-1, Нет-0)")
    ans=int(input())
    if ans: print("Я победил!!! AI --- рулит!")
    else:
        a=input("Кто это? ");
        q=input("Задай вопрос, ответом ДА, на который будет " + a +", а ответом НЕТ ---" + ai.ask() + ". ");
        ai.learn(a,q)
    exit_game=not int(input("Хочешь сыграть ещё? (Да-1, Нет-0)"))

