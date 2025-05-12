import random
newList = []
fileName = input("输入文件名，输入为空则默认为“file.txt”。（此后可以随时使用“.menu”菜单指令修改文件名）")
if(fileName == ""):
    fileName = "file.txt"
print("当前单词表内容如下：")
f = open(fileName, 'a+')
content = f.readlines()
f.close()
# Display the file's content line by line.
temp = True
for line in content:
    print(line, end="")
    if (temp):
        new = [line]
        temp = False
    else:
        new.append(line)
        newList.append(new)
        temp = True

decition = True
while (decition):
    flag = input("为单词表添加单词（a), 或者重新设置单词表（w）吗？")[0]
    if(flag == 'w'):
        flag = input("将会清空所选的单词表文件，确认吗？(按Y确认)")[0]
    elif(flag != 'a'):
        flag = 'r'
        decition = False
    else:
        decition = False
    if(flag == 'Y'):
        flag = 'w'
        newList = []
        decition = False

f = open(fileName, flag)
if (flag != 'r'):
    newline = input("输入单词列表，格式：‘abandon 抛弃’以空格区分拼写和词义，以分行区分单词。输入为空停止。")
    while (newline != ""):
        l = len(newline)
        temp = True
        for i in range(l):
            if (temp and (newline[i] == ' ' or newline[i] == ',')):
                spl = i
                temp = False
        if (temp):
            newline = input("未找到分割点，该行数据无效，请继续输入单词列表。")
        else:
            
            f.write(newline[0:spl])
            f.write(newline[(spl + 1):l])
            newList.append([newline[0:spl], newline[(spl + 1):l]])
            newline = input("继续输入单词列表。")
    f.close
    f = open(fileName, 'r')


correct = 0
count = 0
newline = "111"
while (newline != ""):
    print("接下来开始听写。输入为空停止并计分")
    n = random.randrange(0, len(newList))
    m = random.randrange(0, 2) 
    print(newList[n][m])
    newline = input()
    if (newline == newList[n][1-m]):
        correct += 1
    elif(newline == ""):
        print("结束，")
        count -= 1
    else:
        print("正确答案：", newList[n][1-m])
    count += 1

print("得分：", correct, "/", count)
input()

