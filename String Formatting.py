number=int(input()
bin1=bin(number)
bin1_fl=bin1[2:]
length=(len(bin1_fl))+1
if (1<=number and number<=99):
        for i in range(1,number+1):
            #decimal
            print(str(i).rjust(length),end="")
            #octal
            octal=oct(i)
            octal_fl=octal[2:]
            print(str(octal_fl).rjust(length),end="")
            #hexadcimal
            hexa=hex(i)
            hexa_fl=hexa[2:]
            hexa_fl=hexa_fl.capitalize()
            print(str(hexa_fl).rjust(length),end="")
            #binary
            binary=bin(i)
            binary_fl=binary[2:]
            print(str(binary_fl).rjust(length))



            
            