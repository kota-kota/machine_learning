import numpy as np
import matplotlib.pyplot as plt

o = np.array([0.0, 0.0])    # 原点
a = np.array([0.0, 0.0])    # aベクトル
b = np.array([0.0, 0.0])    # bベクトル
ab_map = np.array([0.0, 0.0])   # aからbへの写像

def onclick(event):
    print('event.button:{} event.x:{} event.y:{} event.xdata:{} event.ydata:{}'.format(event.button, event.x, event.y, event.xdata, event.ydata))
    if event.button == 1:   # 左クリックでaベクトルを動かす
        a[0] = event.xdata
        a[1] = event.ydata
    if event.button == 3:   # 右クリックでbベクトルを動かす
        b[0] = event.xdata
        b[1] = event.ydata

    # aからbへの写像を計算
    # ab内積にbと同じ向きの単位ベクトルをかけたもの
    k = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
    ab_map[0] = k * b[0]
    ab_map[1] = k * b[1]

    # 再描画
    draw()

def draw():
    plt.clf()

    # 原点
    plt.plot(o[0], o[1], 'o', color='blue')
    # aベクトル
    plt.quiver(o[0], o[1], a[0], a[1], width=0.004, color="black", angles='xy', scale_units='xy', scale=1)
    plt.text(a[0], a[1], "a[{:.2f},{:.2f}]".format(a[0], a[1]), color = "black", size = 10)
    # bベクトル
    plt.quiver(o[0], o[1], b[0], b[1], width=0.004, color="black", angles='xy', scale_units='xy', scale=1)
    plt.text(b[0], b[1], "b[{:.2f},{:.2f}]".format(b[0], b[1]), color = "black", size = 10)
    # aからbへの写像ベクトル
    plt.quiver(o[0], o[1], ab_map[0], ab_map[1], width=0.004, color="red", angles='xy', scale_units='xy', scale=1)
    plt.text(ab_map[0], ab_map[1], "ab_map[{:.2f},{:.2f}]".format(ab_map[0], ab_map[1]), color = "black", size = 10)
    # aからbへの垂線
    plt.plot([a[0], ab_map[0]], [a[1], ab_map[1]], linestyle = "dashed")

    # タイトル
    plt.title('mapping : a -> b')

    # 軸ラベル
    plt.xlabel('X')
    plt.ylabel('Y')

    # 軸範囲
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # 描画
    plt.grid()
    plt.draw()
    plt.show()

def main():
    fig=plt.figure()
    fig.canvas.mpl_connect('button_press_event', onclick)
    draw()

if __name__ == '__main__':
    main()