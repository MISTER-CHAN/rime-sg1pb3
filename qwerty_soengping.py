import turtle

t = turtle.Turtle()
t.speed(0)
t.ht()

qwe = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

le_pos = {}
for i in range(3):
    nc = len(qwe[i])
    w = nc / 10.0
    for j in range(nc):
        le = qwe[i][j]
        x, y = float(j) / nc * 10 + w / 2, float(i)
        le_pos[le] = (x, y)

sy_list = ['aau', 'aai', 'aanaat', 'aamaap', 'au', 'ai', 'anat', 'amap', 'aangaakangak',
           'eoiui', 'eoneotonot', 'oengoek', 'yunyutunut', 'unguk', 'iu', 'init', 'imip', 'ingikengek', 'oi', 'ongok']

sy_pos, col, row = {}, {}, {}
for sy in sy_list:
    x, y = 0, 0
    for le in sy:
        x, y = x + le_pos[le][0], y + le_pos[le][1]
    x, y = x / len(sy), y / len(sy)
    sy_pos[sy] = (x, y)
    col[x], row[y] = 0, 0

for i, k in enumerate(sorted(col)):
    col[k] = i
for i, k in enumerate(sorted(row)):
    row[k] = i

ab = {'aanaat': 'aat', 'aamaap': 'aap', 'anat': 'at', 'amap': 'ap', 'aangaakangak': 'ak',
      'eoiui': 'ui', 'eoneotonot': 'ot', 'oengoek': 'oek', 'yunyutunut': 'ut', 'unguk': 'uk', 'init': 'it', 'imip': 'ip', 'ingikengek': 'ik', 'ongok': 'ok'}
for sy in sy_list:
    sp = sy_pos[sy]
    t.pu()
    t.goto(col[sp[0]] * 30 - 300, (2 - row[sp[1]]) * 30)
    t.pd()
    t.write(ab.get(sy, sy), align='center')