# 1kg = 2.2046226218488 lbs
t = 2.2046226218488
weight = int(input("Enter you weight: "))
unit = input("lbs (L) or kg (K)? ").upper()
if unit == 'L':
  print(f'Your weight is {weight / t}kg')
elif unit == 'K':
  print(f'Your weight is {weight * t}lbs')
else:
  print('Please enter K for kg or L for lbs!')
