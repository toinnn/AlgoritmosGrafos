
def inserirEmListaPorElem(lis,elemKey,newElem):
    for n, i in enumerate(lis):
        if i == elemKey:
            lis[n] = newElem

class nume :
    def __init__(self,num):
        self.valor=num

    def __str__(self):
        return self.valor

tk1=[nume(1),nume(4),nume(2),nume(3),nume(4)]
tk2=[nume(4),nume(2),nume(3),nume(5)]

lis=list()
lis.append(tk1)
lis.append(tk2)
print(lis)

inserirEmListaPorElem(lis,tk1,tk1+tk2)

"""for n,i in enumerate(lis) :
    if i== tk1 :
        lis[n]=tk1+tk2
"""

lis.remove(tk2)
print(lis)
print(tk1)
