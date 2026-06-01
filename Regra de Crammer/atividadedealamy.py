# Programa para resolver sistemas 2x2 ou 3x3 usando Regra de Cramer

#no def ele estará criando uma função que calcula a matriz 2x2
def determinante_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
#return = ele devolve o valor, colocando dentro de uma lista 2x2

#segue a msm coisa no 2x2
def determinante_3x3(m):
    return (
        m[0][0]*m[1][1]*m[2][2] +
        m[0][1]*m[1][2]*m[2][0] +
        m[0][2]*m[1][0]*m[2][1]
        -
        m[0][2]*m[1][1]*m[2][0] -
        m[0][0]*m[1][2]*m[2][1] -
        m[0][1]*m[1][0]*m[2][2]
    )

#faz a magica de cramer acontecer
def substituir_coluna(matriz, coluna, novos_valores):
    nova = [linha[:] for linha in matriz]
    for i in range(len(nova)): #vai percorrer todas as linhas
        nova[i][coluna] = novos_valores[i] #troca a coluna pela lista de resultados
    return nova


def resolver_2x2():
    print("\n--- Sistema 2x2 ---")
    matriz = []
    termos = []

    for i in range(2):#repetiçao
        linha = list(map(float, input(f"Digite os coeficientes da equação {i+1} (a b): ").split())) #transforma texto em numero
        matriz.append(linha)
        termo = float(input(f"Digite o resultado da equação {i+1}: "))
        termos.append(termo)

    D = determinante_2x2(matriz)

    if D == 0:
        print("Sistema sem solução ou com infinitas soluções.")
        return

    Dx = determinante_2x2(substituir_coluna(matriz, 0, termos))
    Dy = determinante_2x2(substituir_coluna(matriz, 1, termos))

    x = Dx / D
    y = Dy / D

    print(f"\nResultado (aproximadamente):")
    print(f"x = {x:.3f}")
    print(f"y = {y:.3f}")


def resolver_3x3():
    print("\n--- Sistema 3x3 ---")
    matriz = []
    termos = []

    for i in range(3):
        linha = list(map(float, input(f"Digite os coeficientes da equação {i+1} (a b c): ").split()))
        matriz.append(linha)
        termo = float(input(f"Digite o resultado da equação {i+1}: "))
        termos.append(termo)

    D = determinante_3x3(matriz)

    if D == 0:
        print("Sistema sem solução ou com infinitas soluções.")
        return

    Dx = determinante_3x3(substituir_coluna(matriz, 0, termos))
    Dy = determinante_3x3(substituir_coluna(matriz, 1, termos))
    Dz = determinante_3x3(substituir_coluna(matriz, 2, termos))

    x = Dx / D
    y = Dy / D
    z = Dz / D

    print(f"\nResultado (aproximadamente):")
    print(f"x = {x:.3f}")
    print(f"y = {y:.3f}")
    print(f"z = {z:.3f}")


# Programa principal
print("Escolha o tipo de sistema:")
print("1 - Sistema 2x2")
print("2 - Sistema 3x3")

opcao = input("Digite a opção: ")

if opcao == "1":
    resolver_2x2()
elif opcao == "2":
    resolver_3x3()
else:
    print("Opção inválida.")