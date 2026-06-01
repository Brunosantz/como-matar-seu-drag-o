# ----------------------------
# MEMÓRIA (várias instruções)
# ----------------------------

memoria = [
    "ADD 2 3",
    "SUB 10 5",
    "ADD 7 1"
]

# ----------------------------
# CICLO DE INSTRUÇÃO
# ----------------------------

for instrucao in memoria:

    print("\n========================")
    print(f"Instrução atual: {instrucao}")

    # ------------------------
    # FETCH
    # ------------------------
    print("FETCH → Buscando instrução...")
    comando = instrucao

    # ------------------------
    # DECODE
    # ------------------------
    print("DECODE → Entendendo instrução...")
    partes = comando.split()

    operacao = partes[0]
    A = int(partes[1])
    B = int(partes[2])

    print(f"Operação: {operacao}")
    print(f"Valores: {A} e {B}")

    # ------------------------
    # EXECUTE
    # ------------------------
    print("EXECUTE → Executando...")

    if operacao == "ADD":
        resultado = A + B

    elif operacao == "SUB":
        resultado = A - B

    else:
        resultado = "Erro: operação inválida"

    print(f"Resultado: {resultado}")