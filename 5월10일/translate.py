pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()

sentence = input("문장 : ")
target = input("목표 언어 : ")

result = translator.translate(,sentence,target)
detected = translator.detect(,sentence)

print("============결과============")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("============================")