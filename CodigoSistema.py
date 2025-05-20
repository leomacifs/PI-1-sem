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

#Solicita nome do usuário
nome=input("Digite o seu nome: ")

from datetime import datetime
digitou_corretamente=False
while not digitou_corretamente:
    # Solicita a data ao usuário
    data_usuario = input("Digite a data atual (no formato aaaa/mm/dd): ")

    # Tenta converter a entrada para o formato correto
    try:
        # Verifica se a data está no formato correto
        data_formatada = datetime.strptime(data_usuario, "%Y/%m/%d").strftime("%Y/%m/%d")
        print("Data formatada:", data_formatada)
        break  # Sai do laço se a data for válida
    except ValueError:
        # Se o formato estiver errado, avisa o usuário e pede novamente
        print("Formato de data inválido! Por favor, use o formato aaaa/mm/dd.")
    else: 
            digitou_corretamente=True     

digitou_corretamente=False
while not digitou_corretamente:
    try:    # LITROS DE ÁGUA
        L_de_agua=float(input("Quantos litros de água foram consumidos hoje? ").replace(",", "."))
    except ValueError:
        print("O valor deve ser numérico! Tente novamente!")
    else:
        if L_de_agua<0:
            print("O valor não pode ser menor que 0! Tente novamnete.")
        else: 
            digitou_corretamente=True

digitou_corretamente=False
while not digitou_corretamente:
    try:    # ENERGIA ELÉTRICA
        kwh=float(input("Quanto kWh de energia elétrica você consumiu hoje?").replace(",", "."))
    except ValueError:
        print("O valor deve ser numérico! Tente novamente.")
    else:
        if kwh<0:
            print("O valor não pode ser menor que 0! Tente novamente!")
        else: 
            digitou_corretamente=True

digitou_corretamente=False
while not digitou_corretamente:
    try:      # KG DE RESÍDUOS
        kg_de_residuos=float(input("Quantos kg de resíduos não recicláveis você gerou hoje?").replace(",", "."))
    except ValueError:
        print("O valor deve ser numérico! Tente novamente!")
    else:
        if kg_de_residuos<0:
            print("O valor não pode ser menor que 0! Tente novamente.")
        else:
            digitou_corretamente=True

digitou_corretamente=False
while not digitou_corretamente:
    try:      #  % DE RESIDUOS
        porcentagem_de_residuos=float(input("Qual a porcentagem de resíduos reciclados no total?" ).replace(",", "."))
    except ValueError:
        print("O valor deve ser numérico! Tente novamente!")
    else:
        if porcentagem_de_residuos<0:
            print("O valor não pode ser menor que 0! Tente novamente.")
        else:
            digitou_corretamente=True


# TRANSPORTE
meios_transporte = {
    1: "transporte público",
    2: "bicicleta",
    3: "caminhada",
    4: "carro",
    5: "carro elétrico",
    6: "carona compartilhada",
    7: "moto"
}

digitou_corretamente = False

while not digitou_corretamente:
    try:
        transporte = int(input("Qual o meio de transporte (1-transporte público, 2-bicicleta, 3-caminhada, 4-carro, 5-carro elétrico, 6-carona compartilhada, 7-moto) você usou hoje? "))
    except ValueError: 
        print("O valor deve ser um número inteiro! Tente novamente.")
    else:
        if transporte not in meios_transporte:
            print("O valor deve estar entre 1 e 7! Tente novamente!")
        else:
            digitou_corretamente = True

print(f"Você escolheu: {meios_transporte[transporte]}.")

# CLASSIFICAÇÂO DE SUSTENTABILIDADE

# PARA ÁGUA
if L_de_agua <150:
    print("Seu consumo de água resultou em: 🟢 Alta Sustentabilidade 🟢")        
elif L_de_agua>= 150 and L_de_agua <=200:
    print("Seu consumo de água resultou em: 🟡 Moderada Sustentabilidade 🟡")
else:
    print("Seu consumo de água resultou em: 🔴 Baixa Sustentabilidade 🔴")

 # PARA ENERGIA
if kwh <5:
    print("O seu gasto de energia resultou em: 🟢 Alta Sustentabilidade 🟢")        
elif kwh>= 5 and kwh <=10:
    print("O seu gasto de energia resultou em: 🟡 Moderada Sustentabilidade 🟡")
else:
    print("O seu gasto de energia resultou em: 🔴 Baixa Sustentabilidade 🔴")   

# PARA RESÍDUOS
if porcentagem_de_residuos >50:
    print("A porcentagem que você gerou de residuos não recicláveis resultou em: 🟢 Alta Sustentabilidade 🟢")        
elif porcentagem_de_residuos>= 20 and porcentagem_de_residuos <=50:
    print("A porcentagem que você gerou de residuos não recicláveis resultou em: 🟡 Moderada Sustentabilidade 🟡")
else:
    print("A porcentagem que você gerou de residuos não recicláveis resultou em: 🔴 Baixa Sustentabilidade 🔴")    
    
# PARA TRANSPORTE
if transporte==1 or transporte==2 or transporte==5:
    print("A sua opção de transporte resultou em: 🟢 Alta Sustentabilidade 🟢")        
elif transporte==6:
    print("A sua opção de transporte resultou em: 🟡 Moderada Sustentabilidade 🟡")
else:
    print("A sua opção de transporte resultou em: 🔴 Baixa Sustentabilidade 🔴")

#--------------------------------------------------------------------------------

while True:
    print("----------------------------------------------")
    print("|                   Menu                     |")
    print("----------------------------------------------")
    print("|  1 - Inserir novo monitoramento            |")
    print("|  2 - Visualizar um monitoramento existente |")
    print("|  3 - Atualizar um monitoramento existente  |")
    print("|  4 - Excluir um monitoramento              |")
    print("|  5 - Sair                                  |")
    print("----------------------------------------------")

    escolha = input("Digite a opção (1/2/3): ")

    if escolha == "1":
        insercao_registro(nome, data_formatada, L_de_agua, kwh, kg_de_residuos, porcentagem_de_residuos, transporte)
        print("Registro inserido com sucesso!")

    elif escolha == "2":
        registros = visualizar_registros_por_data(data_formatada)
        if registros:
            print("\nRegistros encontrados para a data", data_formatada)
            for registro in registros:
                print(f"Nome: {registro[0]}, Data: {registro[1]}, Água: {registro[2]}L, Energia: {registro[3]}kWh, Resíduos: {registro[4]}kg, % Reciclado: {registro[5]}%, Transporte: {registro[6]}")
        else:
            print("Nenhum registro encontrado para essa data.")

    elif escolha == "3":
        registros = visualizar_registros_por_data(data_formatada)
        registro_existente = None
        for r in registros:
            if r[0] == nome:
                registro_existente = r
                break

        if not registro_existente:
            print("Nenhum registro encontrado para esse nome e data.")
        else:
            print("\nRegistro atual:")
            print(f"Nome: {registro_existente[0]}")
            print(f"Data: {registro_existente[1]}")
            print(f"Água: {registro_existente[2]}L")
            print(f"Energia: {registro_existente[3]}kWh")
            print(f"Resíduos: {registro_existente[4]}kg")
            print(f"% Reciclado: {registro_existente[5]}%")
            print(f"Transporte: {registro_existente[6]}")

            def atualizar_campo(texto, valor_antigo, tipo=float):
                entrada = input(f"{texto} [{valor_antigo}]: ").strip()
                if entrada == "":
                    return valor_antigo
                else:
                    try:
                        return tipo(entrada.replace(",", ".")) if tipo == float else tipo(entrada)
                    except ValueError:
                        print("Entrada inválida! Mantendo valor antigo.")
                        return valor_antigo

            novo_L_de_agua = atualizar_campo("Novo consumo de água (L)", registro_existente[2])
            novo_kwh = atualizar_campo("Novo consumo de energia (kWh)", registro_existente[3])
            novo_residuos = atualizar_campo("Novo total de resíduos (kg)", registro_existente[4])
            nova_porcentagem = atualizar_campo("Nova % de resíduos reciclados", registro_existente[5])
            novo_transporte = atualizar_campo("Novo meio de transporte (1-7)", registro_existente[6], int)

            atualizar_registro(nome, data_formatada, novo_L_de_agua, novo_kwh, novo_residuos, nova_porcentagem, novo_transporte)
            print("Registro atualizado com sucesso!")

    elif escolha == "4":
        excluir_registro(nome, data_formatada)
        print("Registro excluído com sucesso!")

    elif escolha == "5":
        print("Programa encerrado.")
        break

fechaConexao()