"""
    现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
    但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致
    罗恩 23 35 44
    哈利 60 77 68 88 90
    赫敏 97 99 89 91 95 90
    马尔福 100 85 90
    希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件
"""
f = open(file="score.txt", mode="r", encoding="utf-8")
data = f.readlines()
li = list()

# 文件转list
for val in data:
    li.append(val.splitlines()[0].split(" "))

# str转int
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j].isdigit():
            li[i][j] = int(li[i][j])

# 计算成绩和
result = list()
for val in li:
    sum = 0
    for i in range(1, len(val)):
        sum += val[i]
    result.append([val[0], sum])

# 写入文件
f = open(file="result.txt", mode="w+", encoding="utf-8")
for val in result:
    name = val[0]
    score = str(val[1])
    f.write(name + " " + score + "\n")

f.flush()
f.close()