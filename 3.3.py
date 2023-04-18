colors_1= {'A','E','I','O','U','L','N','S','T','R','А','В','Е','И','Н','О','Р','С','Т'}
colors_2={'D','G','Д','К','Л','М','П','У'}
colors_3= {'B','C','M','P','Б','Г','Ё','Ь','Я'}
colors_4={'F','H','V','W','Y','Й','Ы'}
colors_5={'K','Ж','З','Х','Ц','Ч'}
colors_8={'J','X','Ш','Э','Ю'}
colors_10={'Q','Z','Ф','Щ','Ъ'}
word = str(input('Введите слово: ')).upper()
count =0
for i in range(len(word)):
  if word[i] in set(colors_1):
    count +=1
  elif word[i] in set(colors_2):
    count +=2
  elif word[i] in set(colors_3):
    count +=3
  elif word[i] in set(colors_4):
    count +=4
  elif word[i] in set(colors_5):
    count +=5
  elif word[i] in set(colors_8):
    count +=8
  elif word[i] in set(colors_10):
    count +=10
print(f'Стоимость введенного слова: {count}')