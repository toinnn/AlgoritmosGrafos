class Aresta:

    def __init__(self, peso=0, verticeLigado1=None,verticeLigado2=None):
        self.peso = peso
        self.verticeLigado1 = verticeLigado1
        self.verticeLigado2 = verticeLigado2

    def __str__(self):
        return "Peso:{} , Vertice Ligando {} a {}".format(self.peso, self.verticeLigado1,self.verticeLigado2)


class Vertice:

    def __init__(self):
        self.aresta = list()
        self.dado = dict()

    def addDado(self, nomeDado, dado):
        self.dado[nomeDado] = dado

    def addTipoDado(self, tipoDado):
        self.dado[tipoDado] = None

    def getDado(self, key):
        return self.dado[key]

    def showKeys(self):
        return self.dado.keys()

    def addAresta(self, peso, outroVertice):
        self.aresta.append(Aresta(peso, outroVertice))
    def addArestaBidirecional(self, peso, outroVertice):
        aux=Aresta(peso,self,outroVertice)
        self.aresta.append(aux)
        outroVertice.aresta.append(aux)

    def __str__(self):

        return "{}".format(self.dado["nome"])

    def __repr__(self):
        return str(self)



class ListaAdjassencia:

    def __init__(self):
        self.lista = []

    def buscaVerticePorDado(self, nomeDado, dado):
        for aux in self.lista:
            if aux.dado[nomeDado] == dado:
                return aux

    def addVertice(self, vertice):
        self.lista.append(vertice)

    def addItemAllVertice(self, nomeDado, dado):
        for x in self.lista:
            x.addDado(nomeDado, dado)

    def addMultItemAllVertice(self, nomeDado, dado):
        for x in self.lista:
            for item in range(0, len(nomeDado)):
                x.addDado(nomeDado[item], dado[item])

    def alteraItemVertice(self, vertice, nomeDado, dado):
        vertice.addDado(nomeDado, dado)

    def criaVertice(self,DadoNome,Dado):
        aux = Vertice()
        aux.addDado(DadoNome,Dado)
        self.lista.append(aux)
        

    # NomeDadoRefer e DadoRefer devem ser listas de tamanho 2,onde primeira posicao refereci de onde sai e a segunda pra onde vai
    def criaAresta(self,NomeDadoRefer,DadoRefer,peso=0):
        if len(NomeDadoRefer)==2 and len(DadoRefer)==2 :
            aux1=None
            aux2=None
            for n in self.lista :
                if n.dado[NomeDadoRefer[0]]==DadoRefer[0] :
                    aux1=n
                if n.dado[NomeDadoRefer[1]]==DadoRefer[1] :
                    aux2=n
            aux1.addAresta(peso,aux2)
    def criaArestaNaoDirecionada(self,nomeDado1,Dado1,nomeDado2,Dado2,peso=0):
        aux1 = None
        aux2 = None
        for n in self.lista:
            if n.dado[nomeDado1] == Dado1:
                aux1 = n
            if n.dado[nomeDado2] == Dado2:
                aux2 = n
        if aux1 !=None and aux2 !=None :
            aux1.addArestaBidirecional( peso,aux2)
        else :
            print("ERRO : pelo menos um dos dados não corresponde ")

    def __str__(self):
        return "\n{}".format(self.lista)


    def __repr__(self):
        return str(self)

