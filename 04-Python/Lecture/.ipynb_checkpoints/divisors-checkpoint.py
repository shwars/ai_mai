# print('Input number:')
x = int(input())
z = 2
while x>1:
    if x%z==0:
        print(z, end=' ')
        x = x//z
    else:
        z+=1
