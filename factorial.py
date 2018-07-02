# def n_factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result *=i
#         print(i,result)
#     return result
#
# print(n_factorial(3))
#
# def factorial_r(n):
#     if n==0:
#         return 1
#     else:
#         return factorial_r(n-1)*n
# print(factorial_r(5))

def alphabet():
    if len('')==1:
        return ''
    else:
        result=[]
        for letter