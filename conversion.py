co = float(input('Quantos pesos te restaram? '))
pe = float(input('Quantos sols te restaram? '))
br = int(input('Quantos reais te restaram? '))
usd = (co*0.00026) + (pe*0.27) + (br*0.20)
print(usd)