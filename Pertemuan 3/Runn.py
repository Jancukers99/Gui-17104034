myfile = open("perangkat.txt")

content = myfile.read()

myfile.close()

print(content)

print(type(myfile))


#Processing File


print("Hello\nworld".splitlines())


#For loop


a = [1,2,3,4,5]

for item in a:

    print(item)


blackpink = ["Lisa", "Jennie", "Rose", "Ji-Soo"]

for anggota in blackpink:

    print(anggota)


for i in a:

    b = i + 10

    print(b)


mylist = [3,4,6,11,2,17,90]

for list in mylist:

    if list > 5:

        print(list)


temperatures = [10,-20,100]

def cel_to_fahr(celsius):

    fahrenheit = (celsius * 9/5) + 32

    return fahrenheit


for suhu in temperatures:

    print(cel_to_fahr(suhu))



#Edit File


myfile = open("pegawai.txt","w")

myfile.write("Bambang")

myfile.write("\nAnto")

myfile.write("\nLinda")

myfile.close()


#Appending text to data

myfile = open("pegawai.txt","a+")

myfile.write("\nPaijo")

myfile.seek(0)

print(myfile.read())

myfile.close()


myfile.write("Latu")

myfile.close()
