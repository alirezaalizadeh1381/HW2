x = int(input())
res = 1
if x <= 1:
        print ('it is not prime')
else:
        for i in range(2,x):
                if x % i == 0:
                    res = 0
                    break
        if res == 1:
                print ('it is prime')
        else:
                print ('it is not prime')


