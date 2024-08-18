import turtle

t = turtle.Turtle()
t.speed(0)
t.ht()

qwe = ['1234567890', 'qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']

le_pos = {}
for i in range(4):
    for j in range(10):
        le = qwe[i][j]
        x, y = j + 0.5, float(i)
        le_pos[le] = (x, y)

sy_list = ['aau', 'aai', 'aan', 'aat', 'aam', 'aap', 'au', 'ai', 'an', 'at', 'am', 'ap', 'aangang', 'aakak',
           'eoiui', 'eonon', 'eotot', 'oeng', 'oek', 'yunun', 'yutut', 'ung', 'uk', 'iu', 'in', 'it', 'im', 'ip', 'ingeng', 'ik', 'ek', 'oi', 'ong', 'ok']

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

ab = {'aangang': 'ang', 'aakak': 'ak',
      'eoiui': 'ui', 'eonon': 'on', 'eotot': 'ot', 'yunun': 'un', 'yutut': 'ut', 'ingeng': 'ing'}
for sy in sy_list:
    sp = sy_pos[sy]
    t.pu()
    t.goto(col[sp[0]] * 30 - 300, (2 - row[sp[1]]) * 30)
    t.pd()
    t.write(ab.get(sy, sy), align='center')