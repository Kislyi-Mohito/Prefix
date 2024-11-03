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
            # print(z[0] + ';' + z[1] +';'+i + ';' +z[3])

f_in.close()
f_out.close()








prefix = []
g_prefix = ''

def analis(a, b):

    i = -1
    x = ''
    a_new = '0'
    b_new = '0'


    if len(a)!= 0  and a[-1] == '0' and b[-1] == '9':
        a_new = a[:-1]
        b_new = b[:-1]

        analis(a_new,b_new)
    else:
        if len(a) == 0:
            prefix.append(g_prefix)
            # print(g_prefix)
            return
        elif len(a) == 1:
            for i in range(int(a), int(b) + 1):
                g = g_prefix
                g += str(i)
                prefix.append(g)
            return
        elif a[-1] == '0': #######################################################################################################
            a_new = a

        elif a[-1]!= '0':
            a_new = a[:-1]

            for i in range(int(a[-1]), 10):
                c = a_new + str(i)
                g = g_prefix
                g += c
                prefix.append(g)
            a_new = int('2' + a_new) + 1
            a_new = str(a_new) + '0'
            a_new = a_new[1:]
        if b[-1] == '9':######################################################################################################################
            b_new = b
        elif b[-1] != '9':
            b_new = b[:-1]
            for i in range(int(b[-1]), -1, -1):
                c = b_new + str(i)
                g = g_prefix
                g += c
                prefix.append(g)
            b_new = int('2' + b_new) - 1
            b_new = str(b_new) + '9'
            b_new = b_new[1:]

        analis(a_new, b_new)




f_in = open('kods_1.txt', 'r', encoding="utf-8")
f_out = open('kods_2.txt', 'w', encoding="utf-8")


zapis = []
z = 0
count = 0
Y = ""


for line in f_in:

    z = line.split(';')



    if ' ' in z[2]:

        z[2] = z[2][1:]
        # print(z[2])



    # print(z[2])
    if '-' in z[2]:
        di = z[2]
        d = di.split('-')
        # print(di)

        prefix = []
        g_prefix = ''


        a = d[0]
        b = d[1]
        print(a, b)





        for i in range(0, len(a)):
            if a[0] == b[0]:
                g_prefix += a[0]
                a = a[1:]
                b = b[1:]

        analis(a, b)
        # print(prefix)

        for j in prefix:
            # print(prefix)
            # print(j)
            f_out.write(z[0] + ';' + z[1] + ';' + j + ';' + z[3])
            # print(z[0] + ';' + z[1] + ';' + j + ';' + z[3] )
            # print(j)
    else:
        f_out.write(z[0] + ';' + z[1] + ';' + z[2] + ';' + z[3] )
        # print(z[0] + ';' + z[1] + ';' + z[2] + ';' + z[3] )
        # print(Y)


# f_out.write(z[0] + ';' + j + ';' + z[2] + ';' + z[3] + '\n')




f_in.close()
f_out.close()