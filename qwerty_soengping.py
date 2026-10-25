import turtle

t = turtle.Turtle()
t.speed(0)
t.ht()

qwe = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
row_c = len(qwe)
hg_c, vg_c = 9, row_c - 1
hor_gap, ver_gap, hor_off, ver_off = 60, 60, -300, 0

le_pos = {}
t.color('red')
for i in range(row_c):
    for j in range(len(qwe[i])):
        le = qwe[i][j]
        x, y = (j + float(i) / row_c) * hor_gap, float(vg_c - i) * ver_gap
        le_pos[le] = x, y
        t.pu()
        t.goto(x + hor_off, y + ver_off)
        t.pd()
        t.write(le, align='center')

sy_list = ['aai', ('aamaap', 'aap'), ('aanaat', 'aat'), 'aau', 'ai', ('amap', 'ap'), ('anat', 'at'), ('angaangakaak', 'ak'), 'au',
           ('ekikenging', 'ik'), ('eoiui', 'ui'), ('eononeotot', 'ot'), ('init', 'it'), ('imip', 'ip'), 'iu', ('oekoeng', 'oek'), 'oi', ('okong', 'ok'), ('ukung', 'uk'), ('unyunutyut', 'ut')]

sy_pos = {}
sy_bl, sy_tr = (hg_c * hor_gap, vg_c * ver_gap), (0, 0)
for sy in sy_list:
    sy = sy[0] if type(sy) is tuple else sy
    x, y = 0, 0
    for le in sy:
        x, y = x + le_pos[le][0], y + le_pos[le][1]
    x, y = x / len(sy), y / len(sy)
    sy_pos[sy] = x, y
    sy_bl, sy_tr = (min(sy_bl[0], x), min(sy_bl[1], y)), (max(sy_tr[0], x), max(sy_tr[1], y))

hor_ra, ver_ra = (hg_c * hor_gap) / (sy_tr[0] - sy_bl[0]), (vg_c * ver_gap) / (sy_tr[1] - sy_bl[1])
t.color('black')
for sy in sy_list:
    sy, ab = sy if type(sy) is tuple else (sy, sy)
    x, y = sy_pos[sy]
    t.pu()
    t.goto((x - sy_bl[0]) * hor_ra + hor_off, (y - sy_bl[1]) * ver_ra + ver_off)
    t.pd()
    t.write(ab, align='center')