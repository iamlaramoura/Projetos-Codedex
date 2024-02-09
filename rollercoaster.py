print('Para entrar, iremos verificar sua altura e créditos.')
height = int(input('Diga sua altura em cm: '))
credit = int(input('Diga quantos créditos você tem: '))
if height >= 137 and credit >= 10:
  print('Enjoy the ride!')
elif not height >= 137 and credit >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and not credit >= 10:
  print('You don''t have enough credits.')
else:
  print('You have not met either requirement.')