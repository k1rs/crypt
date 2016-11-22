file = open("input.txt", 'r')

str_1 = file.readline().rstrip().decode("hex")
str_2 = file.readline().rstrip()

str_1 = str_1 #Delete \n in raw data and decode HEX
str_2 = str_2.decode("hex")

print "HEX decoded source string one: " + str_1
print "HEX decoded source string two: " + str_2

a = list(str_1)
b = list(str_2)
c = list(str_1) #Because i do not know how to do blank list with no limits

i = 0 #counter
lenght = len(str_2)

while i != lenght:
    c[i] = chr(ord(a[i])^ord(b[i]))
    i = i + 1
c = "".join(c)
print "Decrypted secret message:  " + c
print "HEX encoded secret message:  " + c.encode("hex")
