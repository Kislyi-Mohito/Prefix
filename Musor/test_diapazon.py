f_out = open('codesFT.txt', 'r', encoding="utf-8")
f_in = open('kods_1.txt', 'w', encoding="utf-8")
x = 0
z = 0
count = 0
for line in f_out:
    count += 1
    if count >1:
        z = line.split(';')

        x = z[2].split(',')
        for i in x:
            z[1] == i
            f_in.write(z[0] + ';' + z[1] +';'+i + ';' +z[3] )
            print(z[0] + ';' + z[1] +';'+i + ';' +z[3])

f_in.close()
f_out.close()
