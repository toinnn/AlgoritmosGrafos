from grafoAdjassencia import *
import copy

def inserirEmListaPorElem(lista,elemKey,newElem):
    for n, i in enumerate(lista):
        if i == elemKey:
            lista[n] = newElem


class Kruskal:

    def __init__(self, listaAdjacencia=ListaAdjassencia()):
        self.listaOriginal=listaAdjacencia
        self.lista = copy.deepcopy(listaAdjacencia)


    def arvoreGeradoraMinima(self):
        arestas=[]
        for n in self.lista.lista :#Junta todas as arestas do grafo em uma lista e apaga as instancias delas nos vértices
            arestas= arestas + n.aresta
            n.aresta=list()
        arestas=list(set(arestas))#Remove Duplicatas
        arestas.sort(key=lambda x:x.peso) #Organiza as arestas por ordem crescente de Pesos
        LisDeListas=list()
        auxV=arestas[0].verticeLigado1
        auxV.addArestaBidirecional( arestas[0].peso,arestas[0].verticeLigado2)
        conjuntoLigados=list([arestas[0].verticeLigado1,arestas[0].verticeLigado2])
        LisDeListas.append(conjuntoLigados)
        del arestas[0]
        while len(LisDeListas[0])!=len(self.lista.lista) :
            tk1=list()
            tk2=list()
            for n in LisDeListas:#Os tks estão verificando se os próximos vertices a serem ligados formam ciclo
                if arestas[0].verticeLigado1 in n :
                    tk1.extend([n,arestas[0].verticeLigado1])
                if arestas[0].verticeLigado2 in n :
                    tk2.extend([n,arestas[0].verticeLigado2])
            #Dependendo se formam ou não ciclos ele faz a operação indicada ao caso
            try:
                if tk1[0]!=tk2[0]:
                    auxV = arestas[0].verticeLigado1
                    auxV.addArestaBidirecional(arestas[0].peso, arestas[0].verticeLigado2)
                    #tk1[0]=tk1[0] + tk2[0]
                    inserirEmListaPorElem(LisDeListas,tk1[0],tk1[0]+tk2[0])
                    LisDeListas.remove(tk2[0])
                    #del arestas[0]
                #else:
                 #   del arestas[0]
            except :
                if len(tk1)==0 and len(tk2)==0:
                    auxV = arestas[0].verticeLigado1
                    auxV.addArestaBidirecional(arestas[0].peso, arestas[0].verticeLigado2)
                    conjuntoLigados = list([arestas[0].verticeLigado1, arestas[0].verticeLigado2])
                    LisDeListas.append(conjuntoLigados)
                    #del arestas[0]
                elif len(tk1)==0 :
                    auxV=arestas[0].verticeLigado1
                    auxV.addArestaBidirecional(arestas[0].peso, arestas[0].verticeLigado2)
                    #tk2[0]= tk2[0]+ auxV
                    inserirEmListaPorElem(LisDeListas,tk2[0],tk2[0]+[auxV])

                    #del arestas[0]

                elif len(tk2)==0 :
                    auxV=arestas[0].verticeLigado2
                    auxV.addArestaBidirecional(arestas[0].peso,arestas[0].verticeLigado1)
                    inserirEmListaPorElem(LisDeListas,tk1[0],tk1[0]+[auxV])

                    #del arestas[0]

            del arestas[0]

        return LisDeListas[0][0]

    def printArvore(self):
        aux=[]
        for n in self.lista.lista:
            for i in n.aresta :
                #print(i)
                aux.append(i)
            #print(n.aresta)
        aux=list(set(aux))
        for i in aux :
            print(i)








a=ListaAdjassencia()
a.criaVertice("nome","A")
a.criaVertice("nome","B")
a.criaVertice("nome","C")
a.criaVertice("nome","D")
a.criaVertice("nome","E")
a.criaVertice("nome","F")
a.criaVertice("nome","G")

a.criaArestaNaoDirecionada("nome","A","nome","B",2)
a.criaArestaNaoDirecionada("nome","A","nome","C",3)
a.criaArestaNaoDirecionada("nome","A","nome","D",3)
a.criaArestaNaoDirecionada("nome","B","nome","C",4)
a.criaArestaNaoDirecionada("nome","B","nome","E",3)
a.criaArestaNaoDirecionada("nome","C","nome","D",5)
a.criaArestaNaoDirecionada("nome","C","nome","E",1)
a.criaArestaNaoDirecionada("nome","C","nome","F",6)
a.criaArestaNaoDirecionada("nome","D","nome","F",7)
a.criaArestaNaoDirecionada("nome","E","nome","F",8)
a.criaArestaNaoDirecionada("nome","F","nome","G",9)

k=Kruskal(a)
k.arvoreGeradoraMinima()
k.printArvore()