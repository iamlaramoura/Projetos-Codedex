import random

input('Make a question: ')

asw = random.randint(1, 9)
if asw == 1:
  print('Yes - definitely.')
elif asw == 2:
  print('It is decidedly so.')
elif asw == 3:
  print('Without a doubt.')
elif asw == 4:
  print('Reply hazy, try again.')
elif asw == 5:
  print('Ask again later.')
elif asw == 6:
  print('Better not tell you now.')
elif asw == 7:
  print('My sources say no.')
elif asw == 8:
  print('Outlook not so good.')
else:
  print('Very doubtful.')