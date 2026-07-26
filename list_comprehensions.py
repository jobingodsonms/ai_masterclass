#list=[i for i in range(1,51)]
#print(list) 

#list=[i*i*i for i in range(10)]
#print(list)

#list=[i for i in range(30) if i%2==1]
#print(list)

#list=["apple","banana","cherry"]
#res=[lis.upper() for lis in list]
#print(res)

#list=[12,25,8,31,40]
#pas=[ "pass" if lis>=20 else "fail" for lis in list]
#print(pas)

list=[i*i for i in range(1,51)]

l2 = [i for i in list if i % 2 == 1]

l3 = [str(i) for i in l2]
print(l3)