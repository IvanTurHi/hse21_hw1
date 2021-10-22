f = open("MaxScaf.fa", 'r')
f.readline()
str = f.readline()
len_of_gep = 0
num_of_gep = 0
flag = False
for i in str:
    if i == "N":
        if flag == False:
            num_of_gep += 1
        flag = True
        len_of_gep += 1
    else:
        flag = False
print("Общая длина гэпов", len_of_gep)
print("Общее количество гэпов", num_of_gep)
