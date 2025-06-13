import mysql.connector
from datetime import datetime

# Variável global para reutilizar a conexão
conexao = None

def obtemConexao(servidor, usuario, senha, bd):
    global conexao
    if conexao is None:
        conexao = mysql.connector.connect(
            host=servidor,
            user=usuario,
            password=senha,
            database=bd
        )
    return conexao

def fechaConexao():
    global conexao
    if conexao:
        conexao.close()
        conexao = None

def insercao_registro(nome, data_formatada, L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte):
    comando = """
        INSERT INTO registros
        (nome, data, litros_agua, kwh_energia, kg_residuos, porcentagem_reciclada, transporte)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome, data_formatada, L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte)
    conexao = obtemConexao("172.16.12.14", "BD240225249", "Jjzly3", "BD240225249")
    cursor = conexao.cursor()
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()

def visualizar_registros_por_data(data_formatada):
    comando = """
        SELECT nome, data, litros_agua, kwh_energia, kg_residuos, porcentagem_reciclada, transporte
        FROM registros
        WHERE data = %s
    """
    conexao = obtemConexao("172.16.12.14", "BD240225249", "Jjzly3", "BD240225249")
    cursor = conexao.cursor()
    cursor.execute(comando, (data_formatada,))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def atualizar_registro(nome, data_formatada, L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte):
    comando = """
        UPDATE registros
        SET litros_agua = %s,
            kwh_energia = %s,
            kg_residuos = %s,
            porcentagem_reciclada = %s,
            transporte = %s
        WHERE nome = %s AND data = %s
    """
    valores = (L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte, nome, data_formatada)
    conexao = obtemConexao("172.16.12.14", "BD240225249", "Jjzly3", "BD240225249")
    cursor = conexao.cursor()
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()

def excluir_registro(nome, data_formatada):
    comando = "DELETE FROM registros WHERE nome = %s AND data = %s"
    conexao = obtemConexao("172.16.12.14", "BD240225249", "Jjzly3", "BD240225249")
    cursor = conexao.cursor()
    cursor.execute(comando, (nome, data_formatada))
    conexao.commit()
    cursor.close()

#---------------------------------------------------------------------------------------

print("PROGRAMA PARA CALCULAR SUSTENTABILIDADE PESSOAL")

while True:
    print("")
    print("----------------------------------------------")
    print("|                   Menu                     |")
    print("----------------------------------------------")
    print("|  1 - Inserir novo monitoramento            |")
    print("|  2 - Visualizar monitoramentos por data    |")
    print("|  3 - Atualizar um monitoramento existente  |")
    print("|  4 - Excluir um monitoramento              |")
    print("|  5 - Sair                                  |")
    print("----------------------------------------------")

    escolha = input("Digite a opção (1/2/3/4/5): ")

    if escolha == "1":
        nome = input("Digite o seu nome: ")

        while True:
            data_usuario = input("Digite a data do monitoramento (aaaa/mm/dd): ")
            try:
                data_formatada = datetime.strptime(data_usuario, "%Y/%m/%d").strftime("%Y/%m/%d")
                break
            except ValueError:
                print("Formato de data inválido!")

        def solicitar_float(mensagem):
            while True:
                try:
                    valor = float(input(mensagem).replace(",", "."))
                    if valor < 0:
                        print("Valor não pode ser menor que 0.")
                    else:
                        return valor
                except ValueError:
                    print("Valor inválido!")

        L_de_agua = solicitar_float("Quantos litros de água foram consumidos? ")
        kwh = solicitar_float("Quanto kWh de energia elétrica você consumiu? ")
        kg_de_residuos = solicitar_float("Quantos kg de resíduos não recicláveis você gerou? ")
        porcentagem_de_residuos = solicitar_float("Qual a porcentagem de resíduos reciclados? ")

        meios_transporte = {
            1: "transporte público", 2: "bicicleta", 3: "caminhada",
            4: "carro", 5: "carro elétrico", 6: "carona compartilhada", 7: "moto"
        }

        print("\nMeios de transporte disponíveis:")
        for numero, descricao in meios_transporte.items():
            print(f"{numero} - {descricao}")

        while True:
            try:
                transporte = int(input("Escolha o meio de transporte pelo número (1 a 7): "))
                if transporte in meios_transporte:
                    break
                else:
                    print("Valor deve estar entre 1 e 7.")
            except ValueError:
                print("Valor inválido! Digite um número entre 1 e 7.")


        insercao_registro(nome, data_formatada, L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte)

        # Sustentabilidade
        print("\nClassificação de Sustentabilidade:")
        if L_de_agua < 150:
            print("Água: 🟢 Alta")
        elif L_de_agua <= 200:
            print("Água: 🟡 Moderada")
        else:
            print("Água: 🔴 Baixa")

        if kwh < 5:
            print("Energia: 🟢 Alta")
        elif kwh <= 10:
            print("Energia: 🟡 Moderada")
        else:
            print("Energia: 🔴 Baixa")

        if porcentagem_de_residuos > 50:
            print("Resíduos: 🟢 Alta")
        elif porcentagem_de_residuos >= 20:
            print("Resíduos: 🟡 Moderada")
        else:
            print("Resíduos: 🔴 Baixa")

        if transporte in [1, 2, 5]:
            print("Transporte: 🟢 Alta")
        elif transporte == 6:
            print("Transporte: 🟡 Moderada")
        else:
            print("Transporte: 🔴 Baixa")

    elif escolha == "2":
        data_usuario = input("Digite a data que deseja consultar (aaaa/mm/dd): ")
        try:
            data_formatada = datetime.strptime(data_usuario, "%Y/%m/%d").strftime("%Y/%m/%d")
            registros = visualizar_registros_por_data(data_formatada)
            if registros:
                print(f"\nRegistros em {data_formatada}:")
                for r in registros:
                    print(f"- {r[0]}: Água={r[2]}L, Energia={r[3]}kWh, Resíduos={r[4]}kg, % Reciclado={r[5]}%, Transporte={r[6]}")
            else:
                print("Nenhum registro encontrado.")
        except ValueError:
            print("Formato de data inválido.")

    elif escolha == "3" or escolha == "4":
        data_usuario = input("Digite a data do registro (aaaa/mm/dd): ")
        try:
            data_formatada = datetime.strptime(data_usuario, "%Y/%m/%d").strftime("%Y/%m/%d")
            registros = visualizar_registros_por_data(data_formatada)
            if not registros:
                print("Nenhum registro encontrado para essa data.")
                continue

            print("\nRegistros disponíveis:")
            for i, r in enumerate(registros):
                print(f"{i + 1} - {r[0]}")

            indice = input("Escolha o número do registro para continuar: ")
            if not indice.isdigit() or not (1 <= int(indice) <= len(registros)):
                print("Número inválido.")
                continue

            registro = registros[int(indice) - 1]
            nome = registro[0]

            if escolha == "3":
                def atualizar_campo(texto, valor_antigo, tipo=float):
                    entrada = input(f"{texto} [{valor_antigo}]: ").strip()
                    if entrada == "":
                        return valor_antigo
                    try:
                        return tipo(entrada.replace(",", ".")) if tipo == float else tipo(entrada)
                    except ValueError:
                        print("Entrada inválida! Mantendo valor antigo.")
                        return valor_antigo

                novo_L = atualizar_campo("Novo consumo de água", registro[2])
                novo_kwh = atualizar_campo("Novo consumo de energia", registro[3])
                novo_res = atualizar_campo("Novo total de resíduos", registro[4])
                nova_pct = atualizar_campo("Nova % reciclado", registro[5])
                novo_transp = atualizar_campo("Novo transporte (1-7)", registro[6], int)

                atualizar_registro(nome, data_formatada, novo_L, novo_kwh, novo_res, nova_pct, novo_transp)
                print("Registro atualizado com sucesso!")

            elif escolha == "4":
                excluir_registro(nome, data_formatada)
                print("Registro excluído com sucesso!")

        except ValueError:
            print("Formato de data inválido.")

    elif escolha == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")

fechaConexao()