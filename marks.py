with open('dataset_3363_4.txt', 'r') as stroka:
    string = stroka.read().split()

name = []
ave = []
ave_math = 0
ave_phy = 0
ave_rus = 0

for i in range(len(string)):
    name.append(string[i].split(';')) #создаем новый список, где содержимое каждого i-ого элемента делаем строками

for k in range(0, len(name)):

    math1 = int(name[k][1]) #берем каждый предмет каждого ученика
    phy1 = int(name[k][2])
    rus1 = int(name[k][3])

    ave_mark = ((math1 + phy1 + rus1) / 3) #считаем средний балл каждого ученика
    print(ave_mark)

    ave_math += math1 #накапливает все оценки по каждому предмету
    ave_phy += phy1
    ave_rus += rus1


ave_math2 = (ave_math) / (len(name)) #считаем среднее баллы по каждому предмету
ave.append(ave_math2)
ave_phy2 = (ave_phy) / (len(name))
ave.append(ave_phy2)
ave_rus2 = (ave_rus) / (len(name))
ave.append(ave_rus2)

print(ave)