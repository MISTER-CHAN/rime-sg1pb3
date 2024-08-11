import turtle

t = turtle.Turtle()
t.speed(0)
t.ht()

qwe = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

pos = {}
for i in range(3):
  nc = len(qwe[i])
  w = nc / 10.0
  for j in range(nc):
    le = qwe[i][j]
    x, y = (float(j) / nc * 10 + w / 2) * 100 - 550, (2 - i) * 200 - 300
    pos[le] = (x, y)

syList = ['aau', 'aai', ('aanaat', 'aat'), ('aamaap', 'aap'), 'au', 'ai', ('anat', 'at'), ('amap', 'ap'), ('aangaakangak', 'ak'),
         ('eoiui', 'ui'), ('eoneotonot', 'ot'), ('oengoek', 'oek'), ('yunyutunut', 'un'), ('unguk', 'uk'), 'iu', ('init', 'it'), ('imip', 'ip'), ('ingikengek', 'ik'), 'oi', ('ongok', 'ok')]

for sy in syList:
  x, y = 0, 0
  leStr, ab = sy if isinstance(sy, tuple) else (sy, sy)
  for le in leStr:
    x, y = x + pos[le][0], y + pos[le][1]
  t.pu()
  t.goto(x / len(leStr), y / len(leStr))
  t.pd()
  t.write(ab, align='center')