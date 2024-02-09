g = 0
h = 0
r = 0
s = 0

print('--- The Sorting Hat ---')
print("\n")
print("Let's find out which of the four Houses you belong!")
print("\n")
print('Q1) Do you like Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')
print("\n")

asr = int(input('Enter answer (1-2): '))
if asr == 1:
    g += 1
    r += 1
elif asr == 2:
    h += 1
    s += 1
else:
    print('Wrong input.')
print("\n")

print('Q2) When I’m dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
print("\n")

asr = int(input('Enter answer (1-4): '))
if asr == 1:
    h = + 2
elif asr == 2:
    s = + 2
elif asr == 3:
    r = + 2
elif asr == 4:
    g = + 2
else:
    print('Wrong input.')
print("\n")

print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
print("\n")

asr = int(input('Enter answer (1-4): '))
if asr == 1:
    s = + 4
elif asr == 2:
    h = + 4
elif asr == 3:
    r = + 4
elif asr == 4:
    g = + 4
else:
    print('Wrong input.')

print("\n")
print("Gryffindor: ", g)
print("Ravenclaw:  ", r)
print("Hufflepuff: ", h)
print("Slytherin:  ", s)
print("\n")

most_points = max(g, r, h, s)

if g == most_points:
    print('You´re  🦁  Gryffindor!')
elif r == most_points:
    print('You´re  🦅   Ravenclaw!')
elif h == most_points:
    print('You´re  🦡   Hufflepuff!')
else:
    print('You´re  🐍   Slytherin!')
