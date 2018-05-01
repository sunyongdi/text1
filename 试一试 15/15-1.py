import matplotlib.pyplot as plt

# x_value = list(range(1, 6))
x_value = list(range(1, 5001))
y_value = [x ** 3 for x in x_value]
plt.scatter(x_value, y_value, s=40)
plt.title('', fontsize=40)
plt.xlabel("value", fontsize=14)
plt.ylabel("", fontsize=14)
# plt.axis([0, 5, 1, 150])
plt.show()
