print('欢迎使用本程序,by Excust---')
_pi = 3.14
keep_running = True
while keep_running:
    mode = input('输入模式,长方形面积输1,圆面积输2，长方体体积输入3,球体积输入4,梯形面积输入5,退出输0\n模式:')
    mode = int(mode)
    if mode == 0:
        break
    elif mode == 1:
        a = input('长：')
        b = input('宽:')
        a = float(a)
        b = float(b)
        print('面积为：', float(a * b))
        keep_running = input('输入1继续，回车退出\n继续吗：')
    elif mode == 2:
        r = input('半径:')
        print('面积:', (float(r) ** 2) * _pi)
        keep_running = input('输入1继续，回车退出\n继续吗：')
    elif mode == 3:
        a = 0
        b = 0
        c = 0
        a = input('长：')
        b = input('宽：')
        h = input('高：')
        print('体积:', float(a) * float(b) * float(h))
        keep_running = input('输入1继续，回车退出\n继续吗：')
    elif mode == 4:
        r = 0
        r = input('球半径：')
        print('球体积：', (4 / 3) * _pi * (float(r) ** 3))
        keep_running = input('输入1继续，回车退出\n继续吗：')
    elif mode == 5:
        a = 0
        b = 0
        h = 0
        a = input('上底：')
        b = input('下底：')
        h = input('高 :')
        print('面积：', ((float(a) * float(b)) / 2) * float(h))
        keep_running = input('输入1继续，回车退出\n继续吗：')
else:
    print('感谢使用本程序')
print('感谢使用本程序')