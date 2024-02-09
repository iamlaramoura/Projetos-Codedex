print('Esta será uma calculadora do seu salário com todos os descontos de INSS, VT e IRRF.')
br = float(input('Informe seu salário bruto: '))

# Cálculo INSS
if br <= 1412:
  inss = br * 0.075
elif br > 1412 and br <= 2666.68:
  inss = br * 0.09
elif br > 2666.68 and br <= 4000:
  inss = br * 0.12
elif br > 4000 and br <= 7786.02:
  inss = br * 0.14
else:
  inss = 877

# Cálculo VT
vt = br * 0.06

# Cálculo IRRF
if br >= 2826.66 and br <= 3751.05:
  irrf = br * 0.15
elif br > 3751.05 and br <= 4664.68:
  irrf = br * 0.225
elif br > 4464.68:
  irrf = br * 0.275
else:
  irrf = 0

# Resultados
liq = br - (inss + vt + irrf) 
print('\n')
print('Desconto INSS: {}'.format(inss))
print('Desconto VT: {}'.format(vt))
print('Desconto IRRF: {}'.format(irrf))
print('\n')
print('Este é o seu salário líquido: {}'.format(liq))
print('\n')