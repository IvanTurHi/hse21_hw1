f = open("Poil_contig.fa",'r')
count = 0
total_length = 0
list_of_contig = []
for i in f:
    if i.find("seq") != -1:
        count +=1
        first = i.find("_")
        last = i.rfind("_")
        total_length += int(i[first + 4:last])
        list_of_contig.append(int(i[first + 4:last]))
        #print(i[first+4:last])
        #print(i)
list_of_contig.sort(reverse=True)
print("Общее количество контигов", count)
print("Общая длина контигов", total_length)
print("Самый длинный контиг", list_of_contig[0])
#print(list_of_contig)
half_len = 0
i = 0
N50 = 0
while half_len < total_length/2:
    half_len += list_of_contig[i]
    N50 = list_of_contig[i]
    i += 1
print("N50", N50)
