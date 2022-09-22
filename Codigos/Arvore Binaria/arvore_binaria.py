class NoArvore:

    def __init__(self,info):
        self.info=info
        self.esq=None
        self.dir=None

    def getInfo(self):
        return self.info

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def setEsq(self,esq):
        self.esq=esq

    def setDir(self,dir):
        self.dir=dir

class Arvore:

    def __init__(self):
        self.raiz=None

    def montaArvore(self,x):
        if self.raiz is None:
            no = NoArvore(x)
            self.raiz = no
        q = None
        p = self.raiz

        while p and p.getInfo() != x:
            q = p
            if x < p.getInfo():
                p = p.getEsq()
            else:
                p = p.getDir()
        if p:
            print(f'Info ja cadastrada')
            return
        p = NoArvore(x)
        if x < q.getInfo():
            q.setEsq(p)
        else:
            q.setDir(p)

    def preOrder(self,p):
        if p:
            print(f'No visitado em preOrderm: {p.getInfo()}')
            self.preOrder(p.getEsq())
            self.preOrder(p.getDir())

    def inOrder(self,p):
        if p:
            self.inOrder(p.getEsq())
            print(f'No visitado inOrder: {p.getInfo()}')
            self.inOrder(p.getDir())

    def posOrder(self,p):
        if p:
            self.posOrder(p.getEsq())
            self.posOrder(p.getDir())
            print(f'No visitado posOrder: {p.getInfo()}')
    #CONSTRUIR UMA FUNCAO PARA PERCORRER A ARVORE MOSTRANDO OS ELEMENTOS EM ORDEM DECRESCENTE




arv = Arvore()
arv.montaArvore(20)
arv.montaArvore(30)
arv.montaArvore(10)
arv.montaArvore(11)
arv.montaArvore(25)
arv.montaArvore(23)
arv.montaArvore(26)

arv.preOrder(arv.raiz)
arv.inOrder(arv.raiz)
arv.posOrder(arv.raiz)



