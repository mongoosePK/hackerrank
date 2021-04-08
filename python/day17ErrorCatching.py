# day17.py 
# william pulkownik
# practice throwing and propagating errors

# define Calculator class below. Calculator contains one method, 
# which exponentially multiplies two integers n,p such that n**p
# and throws an exception if either input are negative 
# and returns an error message

class Calculator:
    # def __init__(self, n=0, p=0):
    #     self.n = n
    #     self.p = p
    
    def power(self, n,p):
        assert n >= 0 and p >= 0, "n and p should be non-negative"
        return n ** p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   