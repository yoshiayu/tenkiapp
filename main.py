import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams['font.size'] = 14

fig, ax = plt.subplots(facecolor='aqua', figsize=(15, 10))

ax.plot(['月', '火', '水', '木', '金', '土', '日'], [
    19, 20, 20, 22, 24, 25, 20], label='最高気温', marker='o', color='b')
ax.plot(['月', '火', '水', '木', '金', '土', '日'], [
        11, 10, 10, 12, 14, 15, 13], label='最低気温', marker='^', color='r')
ax.set_xlabel('曜日')
ax.set_ylabel('気温', rotation='horizontal')
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.set_title('茨城県5月1週目')
ax.grid()
ax.legend()
