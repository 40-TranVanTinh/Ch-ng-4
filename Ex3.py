m=int(input("Nhập số m:"))
n=int(input("Nhập số n:"))
for i in range (1,n):
    if m<n and i%m==0:
        print(i)
    else:
        print("")