print("PROGRAMA PARA CALCULAR SUSTENTABILIDADE PESSOAL")

#Solicita nome do usuário
nome=input("Digite o seu nome: ")

from datetime import datetime
digitou_corretamente=False
while not digitou_corretamente:
    # Solicita a data ao usuário
    data_usuario = input("Digite a data atual (no formato dd/mm/aaaa): ")

    # Tenta converter a entrada para o formato correto
    try:
        # Verifica se a data está no formato correto
        data_formatada = datetime.strptime(data_usuario, "%d/%m/%Y").strftime("%d/%m/%Y")
        print("Data formatada:", data_formatada)
        break  # Sai do laço se a data for válida
    except ValueError:
        # Se o formato estiver errado, avisa o usuário e pede novamente
        print("Formato de data inválido! Por favor, use o formato dd/mm/aaaa.")
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

print("PROGRAMA ENCERRADO!")

import mysql.connector #importando bd

def obtemConexao(servidor, usuario, senha, bd): #conectando bd
    if obtemConexao.conexao==None:
        obtemConexao.conexao=mysql.connector.connect(host=f"{BD-ACD}",\
                                                     user=f"{BD240225249}",\
                                                     password=f"{Jjzly3}",\
                                                     database=f"{BD240225249}")
        return obtemConexao.conexao
    obtemConexao.conexao=None

def insercao_registro(nome,data_formatada,L_de_agua,kwh,kg_de_residuos,porcentagem_de_residuos,transporte): #inserção de dados
    comando=f"insert into registros (nome,data,litros_agua,kwh_energia,kg_residuos,porcentagem_reciclada,transporte) values ('{nome}',{data_formatada},{L_de_agua},{kwh},{kg_de_residuos},{porcentagem_de_residuos},'{transporte}')"
    conexao=obtemConexao("BD-ACD","BD240225249","Jjzly3","BD240225249")
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()

def selecao_de_aluno(ra): # consulta específica
    comando=f"select * from registros where nome=(nome)"
    conexao=obtemConexao("BD-ACD","BD240225249","Jjzly3","BD240225249")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    if linhas==[]: return None
    return linhas [0]

def selecao_de_alunos( ): #consulta geral
    comando=("select * from registros")
    conexao=obtemConexao("BD-ACD","BD240225249","Jjzly3","BD240225249")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    return linhas

def fechaConexao(): #encerrar conexão
    conexao=obtemConexao("BD-ACD","BD240225249","Jjzly3","BD240225249")
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()

fechaConexao()
