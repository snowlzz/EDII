def sequencial(v,x):
    for i in range(len(v)):
        if x==v[i]:
            return i
    return -1

def sequencial_ordenado(v,x):
    for i in range(len(v)):
        if v[i]>x:
            return -1
        if v[i]==x:
            return i

    return -1


def busca_binaria(vet,n,chave):
    li=0
    lf=n-1
    while(li<=lf):
        meio=(li+lf)//2
        if chave == vet[meio]:
            return meio
        elif chave < vet[meio]:
            lf=meio-1
        else:
            li=meio+1

    return -1

def busca_binaria_rec(vet,chave,li,lf):
    if li > lf:
        return -1
    meio=(li+lf) // 2

    if chave==vet[meio]:
        return meio
    elif chave < vet[meio]:
        return busca_binaria_rec(vet, chave, li, lf-1)
    else:
        return busca_binaria_rec(vet, chave, meio+1, lf)


v2=[10,20,30,40,50,60,70,80,90]
a=20
pos=busca_binaria(v2,len(v2),a)

if pos==-1:
    print(f'elemento {a} nao encontrado')
else:
    print(f'elemento {a} encontrado na posicao {pos}')


v=[10,5,8,9,12,3,4]
v1=[10,20,30,40,50,60,70,80,90]

x=120

#pos=sequencial(v,x)
pos=sequencial_ordenado(v1,x)

if pos==-1:
    print(f'\nElemento {x} nao encontrado no vetor')
else:
    print(f'Elemento {x} encontrado na posicao {pos} do vetor')
