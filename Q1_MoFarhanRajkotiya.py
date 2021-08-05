import math


num=int(input("Enter number: "))
if(num<=0):
    print("Please provide a valid positive integer")
else:
    answer =0
    for n in range(1,num+1):
        cnt = 0
        for i in range(1, (int)(math.sqrt(n)) + 1) :
            if (n % i == 0) :
                if (n / i == i) :
                    cnt = cnt + 1
                else : # Otherwise count both
                    cnt = cnt + 2
        if(cnt>3):
            answer+=1
    print(answer)
