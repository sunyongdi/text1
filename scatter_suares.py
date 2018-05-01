import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolor='none', s=40)
plt.title("Square Number", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square", fontsize=14)

# 设置刻度标记的大小
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
