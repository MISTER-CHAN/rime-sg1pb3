import turtle

t = turtle.Turtle()
t.speed(0)
t.ht()

qwe = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
hor_gap, ver_gap, hor_off, ver_off = 60, 90, -300, 0

le_pos = {}
t.color('red')
for i in range(3):
    for j in range(len(qwe[i])):
        le = qwe[i][j]
        x, y = (j + i * 0.5 / 3) * hor_gap, (2 - float(i)) * ver_gap
        le_pos[le] = x, y
        t.pu()
        t.goto(x + hor_off, y + ver_off)
        t.pd()
        t.write(le, align='center')

sy_list = ['aau', 'aai', 'aanaat', 'aamaap', 'au', 'ai', 'anat', 'amap', 'aangaakangak',
           'eoiui', 'eoneotonot', 'oengoek', 'yunyutunut', 'unguk', 'iu', 'init', 'imip', 'ingikengek', 'oi', 'ongok']

sy_pos = {}
sy_bl, sy_tr = (9 * hor_gap, 2 * ver_gap), (0, 0)
for sy in sy_list:
    x, y = 0, 0
    for le in sy:
        x, y = x + le_pos[le][0], y + le_pos[le][1]
    x, y = x / len(sy), y / len(sy)
    sy_pos[sy] = x, y
    sy_bl, sy_tr = (min(sy_bl[0], x), min(sy_bl[1], y)), (max(sy_tr[0], x), max(sy_tr[1], y))

hor_ra, ver_ra = (9 * hor_gap) / (sy_tr[0] - sy_bl[0]), (2 * ver_gap) / (sy_tr[1] - sy_bl[1])
ab = {'aanaat': 'aat', 'aamaap': 'aap', 'anat': 'at', 'amap': 'ap', 'aangaakangak': 'ak',
      'eoiui': 'ui', 'eoneotonot': 'ot', 'oengoek': 'oek', 'yunyutunut': 'ut', 'unguk': 'uk', 'init': 'it', 'imip': 'ip', 'ingikengek': 'ik', 'ongok': 'ok'}
t.color('black')
for sy in sy_list:
    x, y = sy_pos[sy]
    t.pu()
    t.goto((x - sy_bl[0]) * hor_ra + hor_off, (y - sy_bl[1]) * ver_ra + ver_off)
    t.pd()
    t.write(ab.get(sy, sy), align='center')