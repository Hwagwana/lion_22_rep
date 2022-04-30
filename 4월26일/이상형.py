qalist = {}

while True:
    question = input("질문 : ")
    if(question=="q"):
        break
    else:
        qalist[question] = ""

for x in qalist:
    print(x)
    answer = input("답변 : ")
    qalist[x] = answer

print(qalist)