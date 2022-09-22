def metodo_contagem(x,saida):
    count=[]
    for i in range(len(x)):
        count.append(0)
        saida.append(0)

    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] < x[i]:
               count[i]=count[i]+1

    for i in range(len(x)):
        saida[count[i]]=x[i]


def metodoImparPar(x):
    continua=True
    while continua:
        continua=False
        for i in range(0,len(x)-1,2):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                continua=True
        for i in range (1,len(x)-1,2):
            if x[i] > x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
                continua=True




x    =[25,57,45,37,12,86,92,33]
saida=[]

metodo_contagem(x,saida)
print(f'valor de x: {x}')
print(f'Valor de saida: {saida}')
print(f'valor de x: {x}')
metodoImparPar(x)
print(f'valor de x - par e impar: {x}')