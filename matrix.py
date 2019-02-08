a, b, c = [], [], []
s = input()
while(s != 'end'):
  b = [int(i) for i in s.split()]
  a.append(b)
  b = []
  s = input()
for i in range(len(a)):
  row = []
  for j in range(len(a[i])):
      row.append(a[(i)%len(a)][(j-1)%len(a[i])] + a[(i+1)%len(a)][(j)%len(a[i])] + a[(i-1)%len(a)][(j)%len(a[i])] + a[(i)%len(a)][(j+1)%len(a[i])])
  c.append(row)
for row in c:
	print(' '.join(str(item) for item in row))