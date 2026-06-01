import random
import time


def exibir_introducao():
    print("-" * 50)
    print("      BEM-VINDO AO COMO MATAR SEU DRAGÃO!      ")
    print("-" * 50)
    print("Você é um jovem mago e enfrentará o temível Dragão de Python!")
    print("Escolha seus ataques com sabedoria para sobreviver.\n")
    time.sleep(1.5)


def jogar():
    exibir_introducao()

    # Inicialização de variáveis (ótimo ponto para explicar na apresentação)
    vida_jogador = 100
    vida_dragao = 120
    pocoes_cura = 3

    # Loop principal do jogo (enquanto ambos estiverem vivos)
    while vida_jogador > 0 and vida_dragao > 0:
        print(f"\n--- STATUS DO COMBATE ---")
        print(f"Sua Vida: {vida_jogador} | Poções de Cura: {pocoes_cura}")
        print(f"Vida do Dragão: {vida_dragao}")
        print("-" * 25)

        # Menu de opções do jogador
        print("Sua vez! Escolha sua ação:")
        print("[1] Bola de Fogo (Dano alto, precisão baixa.)")
        print("[2] Seta de Gelo (Dano médio, precisão garantida)")
        print("[3] Usar Poção de Cura (Recupera 30 de vida)")

        opcao = input("Digite o número da sua ação: ")
        print("-" * 25)

        # Lógica das ações do jogador (Condicionais)
        if opcao == "1":
            # Bola de fogo tem 70% de chance de acertar
            if random.random() < 0.578:
                dano = random.randint(20, 35)
                vida_dragao -= dano
                print(f"🔥 Sucesso! Sua Bola de Fogo causou {dano} de dano no Dragão!")
            else:
                print("❌ Você errou a Bola de Fogo!")

        elif opcao == "2":
            # Seta de gelo sempre acerta, mas dá menos dano
            dano = random.randint(12, 18)
            vida_dragao -= dano
            print(f"❄️ Certeiro! Sua Seta de Gelo causou {dano} de dano no Dragão!")

        elif opcao == "3":
            if pocoes_cura > 0:
                vida_jogador += 30
                if vida_jogador > 100:  # Limita a vida ao máximo de 100
                    vida_jogador = 100
                pocoes_cura -= 1
                print(f"💚 Você bebeu uma poção e recuperou 30 de vida! Vida atual: {vida_jogador}")
            else:
                print("🚫 Você não tem mais poções! Perdeu a vez tentando procurar uma.")

        else:
            print("🤔 Comando inválido! Você se atrapalhou com os feitiços e perdeu a vez.")

        time.sleep(1.5)

        # Verificação se o dragão morreu antes de ele contra-atacar
        if vida_dragao <= 0:
            break

        # Vez do Dragão (Inteligência Artificial básica usando aleatoriedade)
        print("\n🐉 O Dragão está se preparando para atacar...")
        time.sleep(1)

        ataque_dragao = random.choice(["morder", "sopro_fogo", "rugido"])

        if ataque_dragao == "morder":
            dano_dragao = random.randint(10, 15)
            vida_jogador -= dano_dragao
            print(f"💥 O Dragão te mordeu! Você sofreu {dano_dragao} de dano.")
        elif ataque_dragao == "sopro_fogo":
            dano_dragao = random.randint(18, 25)
            vida_jogador -= dano_dragao
            print(f"🔥 O Dragão usou o Sopro de Fogo! Você sofreu {dano_dragao} de dano.")
        elif ataque_dragao == "rugido":
            print("💨 O Dragão soltou um rugido assustador, mas você conseguiu se esquivar do golpe!")

        time.sleep(1.5)

    # Conclusão do jogo (Verificação de vencedor)
    print("\n=============================")
    if vida_jogador > 0:
        print("🏆 PARABÉNS! Você derrotou o Dragão e salvou o reino de Python!")
    else:
        print("💀 GAME OVER! O Dragão foi vitorioso. Tente novamente!")
    print("=============================")


# Executa o jogo
if __name__ == "__main__":
    jogar()