import random

passwords={
1:"S", 2:"q", 3:"o", 4:"P", 5:"5",
6:"b", 7:"A", 8:"W", 9:"g", 10:"010",
11:"B", 12:"L", 13:"f", 14:"y", 15:"313",
16:"z", 17:"m", 18:"N", 19:"å", 20:"010",
21:"ö", 22:"ä", 23:"R", 24:"B", 25:"10",
26:"Y", 27:"h", 28:"k", 29:"e", 30:"201",
31:"c", 32:"l", 33:"u", 34:"o", 35:"13",
36:"v", 37:"x", 38:"t", 39:"Å", 40:"12"

}

r=int(random.randint(1,40))
r1=int(random.randint(1,40))
r2=int(random.randint(1,40))
r3=int(random.randint(1,40))
r4=int(random.randint(1,40))
r5=int(random.randint(1,40))
r6=int(random.randint(1,40))
r7=int(random.randint(1,40))
r8=int(random.randint(1,40))
r9=int(random.randint(1,40))
r10=int(random.randint(1,40))
r11=int(random.randint(1,40))
r12=int(random.randint(1,40))
r13=int(random.randint(1,40))
r14=int(random.randint(1,40))

rs=(passwords[r])
rs1=(passwords[r1])
rs2=(passwords[r2])
rs3=(passwords[r3])
rs4=(passwords[r4])
rs5=(passwords[r5])
rs6=(passwords[r6])
rs7=(passwords[r7])
rs8=(passwords[r8])
rs9=(passwords[r9])
rs10=(passwords[r10])
rs11=(passwords[r11])
rs12=(passwords[r12])
rs13=(passwords[r13])
rs14=(passwords[r14])

data=int(input("How many letters and numbers 5, 10 or 15: "))
data1=str(input("Name for your password: "))
data2=str(input("Password text file name is?(DONT PUT .txt or .something to the end!): "))
f=open(data2 + ".txt","w")

if data==5:
    f.write(str(data1 + ":" + "\n" + rs + rs1 + rs2 + rs3 + rs4))
    f.close()
    print("Password saved to text file")
elif data==10:
    f.write(str(data1 + ":" + "\n" + rs + rs1 + rs2 + rs3 + rs4 + rs5 + rs6 + rs7 + rs8 + rs9))
    f.close()
    print("Password saved to text file")
elif data==15:
    f.write(str(data1 + ":" + "\n" + rs + rs1 + rs2 + rs3 + rs4 + rs5 + rs6 + rs7 + rs8 + rs9 + rs10 + rs11 + rs12 + rs13 + rs14))
    f.close()
    print("Password saved to text file")
else:
    print("5, 10 or 15")
    pass
