s = input()
s = s.lower()
s = s.replace('a', '')
s = s.replace('e', '')
s = s.replace('o', '')
s = s.replace('u', '')
s = s.replace('i', '')
s = s.replace('y', '')
s1 = '.'
s = s1. join(s)
print('.' + s)
