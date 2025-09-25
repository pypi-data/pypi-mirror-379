import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#读取数据
df1 = pd.read_csv('Oranges_Grapefruit_100.csv')

# 绘图函数
def plot_perceptron(W, df):
    colors = {'orange':'orange', 'grapefruit':'blue'}
    plt.ion() # 开启交互模式
    plt.clf() # 清空图像
    plt.scatter(df['diameter'], df['weight'], c=[colors[name] for name in df['name']])
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label=name, markerfacecolor=color, markersize=10) for name, color in colors.items()])
    x = np.linspace(0, 15, 100)
    y = -(W[0] + W[1]*x) / W[2]
    plt.plot(x, y)
    plt.draw()
    plt.pause(0.01) # 暂停

#激活函数
def activation_fn(x):
    print(x)
    return 1 if x >= 0 else 0

#预测
def predict(W, x):
    z = np.dot(W, x)
    return activation_fn(z)

#训练
def fit(Data, Label, lr, epochs):
    W = np.zeros(Data.shape[1] + 1)
    for _ in range(epochs):
        for i in range(Label.size):
            x = np.insert(Data[i], 0, 1) # 在数据前插入1作为偏置项
            y = predict(W, x)
            e = Label[i] - y
            W += lr * e * x
        plot_perceptron(W, df1)
    return W

# 数据预处理
Data = df1[['diameter', 'weight']].values
Label = df1['name'].apply(lambda x: 1 if x == 'orange' else 0).values

#---------------在此修改学习率与训练轮次-------------------
learning_rate=0.1
epochs=300
#---------------在此修改学习率与训练轮次-------------------

# 训练感知机
W = fit(Data, Label, learning_rate, epochs)

plot_perceptron(W, df1)
print('训练完成')
# 输出最终W的斜率与截距
print('斜率：', -W[1]/W[2])
print('截距：', -W[0]/W[2])

# 测试准确率
def test(Data, Label, W):
    correct = sum(predict(W, np.insert(x, 0, 1)) == y for x, y in zip(Data, Label))
    return correct / Label.size

print('最终推理正确率：', test(Data, Label, W))

# 用户输入预测
print('请参考csv文件输入果物的直径和重量，用空格隔开如6 150')
while True:
    x = [1] + list(map(float, input('输入数据完成推理：').split()))
    prediction = predict(W, x)
    print('orange' if prediction == 0 else 'grapefruit')

