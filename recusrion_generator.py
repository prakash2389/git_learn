
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

# print(fact(8))

def gener(n):
    for i in range(1,n):
        yield (fact(i))

gen = gener(10)

for i in gen:
    print(i)



