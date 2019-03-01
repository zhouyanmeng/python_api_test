#1  1-10相加
sum=0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum+=i
print("1-10相加的和:",sum)
print("1.1*********************")
sum=0
for i in range(11):##range(0,11,1)-->0,1,2,3,4,5,6,7,8,9
    sum+=i
print("1-10相加的和:",sum)
print("1.2*********************")

a=[1,2,3,4,5,6,7,8,9,10]
sum=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
print("1-10相加的和:",sum)
print("1.3*********************")

i=0
while 1:
    if i<=10:
        sum+=i
        i+=1
        continue
    else:
        break
print("1-10相加的和:",sum)


##1,2,3,4组成不同的4位数
count=0
for a in range(1,5):
    for b in range(1, 5):
        for c in range(1, 5):
            if(a!=b and b!=c and a!=c):
                count+=1
                #print("符合条件的值是：", a * 100 + b * 10 + c)
                print( a * 100 + b * 10 + c,end='  ')
print()
print("符合的个数是：",count)


#3冒泡排序
#小的排在前面，大的排在后面
#相邻2个数进行比较
a=[1,7,4,89,34,2]

a.sort()
print(a)
print("******************")

##冒泡排序循环次数：执行n-1次
for i in range(len(a)-1):#0,1,2,3,4,5 索引值   ###循环次数n-1
    ##下面的for循环的作用是完成每一次相邻2个数据的比较，并且完成比较完交换
    for j in range(len(a)-1):
        if a[j] > a[j+1]:###j=0,j+1=1
            a[j],a[j+1]=a[j+1],a[j]
print(a)


a=2
b=4
a,b=b,a ###交换值，赋值运算
print('a:',a)
print('b:',b)

a,b=1,2  ##连续赋值
print('a:',a)
print('b:',b)


