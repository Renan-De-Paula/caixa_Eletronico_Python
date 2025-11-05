# Variáveis iniciais
opcao = -1              # Variável de controle da opção do menu
saldo_total = 10000     # Saldo inicial do usuário

# Loop infinito para manter o menu rodando até o usuário escolher sair
while True:
    # Exibição do cabeçalho do sistema
    print("-" * 30)
    print(f"          \033[32mBanco OnFlux\033[m")
    print("-" * 30)

    # Menu de opções
    print("""
    ==================
    \033[34mSelecione a Opção\033[m
    ==================
    [\033[34m1\033[m] Sacar
    [\033[34m2\033[m] Extrato
    [\033[34m3\033[m] Depositar
    [\033[34m0\033[m] Sair
    """)

    # Entrada do usuário
    opcao = int(input("\033[34mQual opção deseja:\033[m "))

    # Caso usuário queira sair do programa
    if opcao == 0:
        print("""
    ==============================
       Operação Encerrada
    Obrigado por usar nosso Banco!
    ==============================
        """)
        break  # Interrompe o loop e encerra o programa

    # Opção de saque
    elif opcao == 1:
        print("""
=====================
\033[32mQual valor quer Sacar\033[m
=====================
        """)

        saque = float(input("Ex: (R$0.00): R$ "))
        
        # Subtraindo o valor sacado do saldo total
        saldo_total -= saque
        
        # Exibindo o valor sacado e saldo restante
        print(f"""
\033[34mVocê sacou:\033[m \033[32mR${saque:.2f}\033[m
Saldo: \033[32mR${saldo_total:.2f}\033[m
        """)

    # Opção de extrato
    elif opcao == 2:
        print("""
    ===============
    \033[34mExtrato atual:\033[m
    ===============
        """)
        print(f"Saldo: \033[32mR${saldo_total:.2f}\033[m")

    # 💰 Opção de depósito
    elif opcao == 3:
        print("""
    ===============
    \033[34mValor do Depósito:\033[m
    ===============
        """)
        
        deposito = float(input("Qual valor do Depósito: R$ "))
        
        # Somando o valor depositado ao saldo
        saldo_total += deposito
        
        print(f"""
    \033[34mVocê depositou:\033[m \033[32mR${deposito:.2f}\033[m
    Saldo: \033[32mR${saldo_total:.2f}\033[m
        """)

    # Opção inválida
    else:
        print("\033[31mOpção inválida! Tente novamente.\033[m")