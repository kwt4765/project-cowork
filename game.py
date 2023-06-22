import random

rn = random.randint(1, 5)

gn = -1


while rn != gn :
    gn = int(input("숫자 추측해 : "))

    if rn == gn :
        print("정답입니다!")
    else : 
        print("틀렸습니다! 다시 하시죠 !")