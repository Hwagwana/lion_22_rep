import random
import time

lunch = ["짜장면","짬뽕","볶음밥","중국냉면"]

while True:
    print(lunch)
    food = input("음식 추가(q로 종료) : ")
    if(food=="q"):
        break
    else:
        lunch.append(food)

lunch_set = set(lunch)

while True:
    print(lunch_set)
    food = input("음식 제거(q로 종료) : ")
    if(food=="q"):
        break
    else:
        lunch_set = lunch_set - set([food])

for x in range(5):
    print(5-x)
    time.sleep(1)

print(random.choice(list(lunch_set)))