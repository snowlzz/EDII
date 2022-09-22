def selecao (lis):
    for p in range(len(lis) - 1):
        ime = p  # armazena em ime o indice do menor elemento
        for i in range (p+1, len(lis)): # percorrer o vetor para encontrar o menor
            if lis[i] < lis[ime]:
                ime = i
        lis[p],lis[ime] = lis[ime], lis[p]
        print('\n',lis,end='')



def bolha(lis):
    for p in range(1,len(lis)):
        print(f'\nPasso: {p}')
        for i in range(len(lis)-p):
            if lis[i] > lis[i+1]:
                lis[i],lis[i+1]=lis[i+1],lis[i]
            print(lis)





def particao(x,li,ls):
    a=x[li]
    acima=ls
    abaixo=li

    while abaixo < acima:

        while x[abaixo] <= a and abaixo < ls:
            abaixo+=1

        while x[acima]>a:
            acima-=1

        if abaixo < acima:
            x[abaixo],x[acima]=x[acima],x[abaixo]

    x[li]=x[acima]
    x[acima]=a

    return acima

def quick(x,li,lf):
    if (li >= lf):
        return
    ret = particao(x,li,lf)  # retorna 5
    quick(x,li,ret-1)  # quick (x, 0, 4)
    quick(x,ret+1,lf)  # quick (x, 6, 15)



x=[12,30,15,5,4,3,70,10,2,40,50,45,25,21,23,24]
print(f'Nao ordenado: {x} \n\n')
quick(x,0,len(x)-1)
print(f'Ordenado quick: {x} \n\n')




print('\n')
vet1=[25,57,48,37,12,92,86,33]
print(vet1)
bolha(vet1)
print(f'Vetor ordenado bolha: {vet1} \n')




vet=[25,57,48,37,12,92,86,33]
print(f'{vet} - vetor nao ordenado')
print('Passos para a ordenacao')
selecao(vet)
print(f'\n\n{vet} - vetor ordenado')