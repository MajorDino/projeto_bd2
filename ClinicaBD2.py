from datetime import date
import psycopg

connection = psycopg.connect(dbname="projectBD2", user="", password="postgres")
#alterar dbname (que é o nome do BD no pgAdmin 3), user e password de acordo com o database que for criar no pgAdmin 3 pra rodar esse código
#colocar os parametros port="", host="" se necessário, caso não utilize os padrões (que são localhost)
cursor = connection.cursor()

class Endereco():
    def __init__(self,uf: str, num: int, rua: str, cidade: str, bairro: str) -> None:
        self.uf = uf
        self.num = num
        self.rua = rua
        self.cidade = cidade
        self.bairro = bairro

class Paciente():
    def __init__(self,nomePaciente: str,cpfPaciente: int, dataNascPaciente: date,telefonePaciente: int,dddPaciente: int, enderecoPaciente: Endereco) -> None:
        self.nomePaciente = nomePaciente
        self.cpfPaciente = cpfPaciente
        self.dataNascPaciente = dataNascPaciente
        self.telefonePaciente = telefonePaciente
        self.dddPaciente = dddPaciente
        self.enderecoPaciente = enderecoPaciente
        #Insert no BD
        try:
            postgres_insert_query = """ INSERT INTO paciente (nomePaciente, cpfPaciente, dataNascPaciente, telefonePaciente, dddPaciente, enderecoPaciente) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (self.nomePaciente, self.cpfPaciente, self.dataNascPaciente, self.telefonePaciente, self.dddPaciente, self.enderecoPaciente)
            cursor.execute(postgres_insert_query, record_to_insert) #realiza o insert. Não sei o que esse record_to_insert retorna e nem porq o cara que eu vi fez assim
            #eu preferia ter feito um comando de 1 linha só, mas ok
            
            connection.commit()
            count = cursor.rowcount
            print(count, "Insercao no banco de dados realizada com sucesso!")
        except:
            print("Falha ao realizas insercao no banco de dados!", error)
        
    def updateNomePaciente(self, nome):
        #Update no BD
        sql_update_query = """Update paciente set nomePaciente = %s where nomePaciente = %s"""
        cursor.execute(sql_update_query, (nome, self.nomePaciente))
        connection.commit()
        count = cursor.rowcount
        print(count, "Nome do paciente atualizado com sucesso! ")
        
        self.nomePaciente = nome #resolvi alterar o self.nomePaciente somente no final pq a linha 41 precisa de 2 parametros: o nome novo e o antigo
        #o antigo serve pra ele procurar no banco qual dos pacientes vai sofrer o update e receber o nome novo no lugar
        #se preferir, em vez de usar nomePaciente pra buscar o paciente que deve ser atualizado, pode-se usar cpfPaciente que parece mais certo!
        #usei a mesma lógica desse update aqui nos de baixo...
    def updateDddTelefonePaciente(self, ddd, telefone ):
        #Update no BD
        sql_update_query = """Update paciente set dddPaciente = %s where dddPaciente = %s"""
        cursor.execute(sql_update_query, (ddd, self.dddPaciente))
        connection.commit()
        count = cursor.rowcount
        print(count, "DDD do paciente atualizado com sucesso! ")
        sql_update_query = """Update paciente set telefonePaciente = %s where telefonePaciente = %s"""
        cursor.execute(sql_update_query, (telefone, self.telefonePaciente))
        connection.commit()
        count = cursor.rowcount
        print(count, "Telefone do paciente atualizado com sucesso! ")
        
        self.dddPaciente = ddd
        self.telefonePaciente = telefone
    def addPlano(self,codPlano: int):
        #Update no BD
        #FIQUE EM DUVIDA DE COMO FAZER!!!!!
        #tem que se atualizar a variavel fk_codPlano da tabela paciente ou a variável pk_codPlano da tabela plano?
        #acho que seguindo os exemplos acima, vc desenrola como fazer...
        
        self.codPlano = codPlano
    def deletePaciente(self):
        #Delete no BD
        try:
            sql_delete_query = """Delete from paciente where nomePaciente = %s"""
            cursor.execute(sql_delete_query, (self.nomePaciente,))
            connection.commit()
            count = cursor.rowcount
            print(count, "Paciente deletado com sucesso (morreu)...")

        except (Exception, psycopg2.Error) as error:
            print("Erro ao deletar paciente (tá vivo).", error)
        del self
           

class Atendente():
    def __init__(self, nomeAtendente: str, cpfAtendente: int, telefoneAtendente: int, dddAtendente: int, enderecoAtendente: Endereco ) -> None:
        self.nomeAtendente = nomeAtendente
        self.cpfAtendente = cpfAtendente
        self.telefoneAtendente = telefoneAtendente
        self.dddAtendente = dddAtendente
        self.enderecoAtendente = enderecoAtendente
        #Insert no BD

class Medico():
    def __init__(self, nomeMedico: str, codMedico: int, telefoneMedico: int, dddMedico: int, enderecoMedico: Endereco) -> None:
        self.nomeMedico = nomeMedico
        self.codMedico = codMedico
        self.telefoneMedico = telefoneMedico
        self.dddMedico = dddMedico
        self.enderecoMedico = enderecoMedico
        #Insert no BD

class Plano():
    def __init__(self, codPlano: int, nomePlano: str, participacaoPlano: float) -> None:
        self.codPlano = codPlano
        self.nomePlano = nomePlano
        self.participacaoPlano = participacaoPlano
        #Insert no BD

    def deletePlano(self):
        #Delete no BD
        del self

class Consulta():
    def __init__(self, codMedico: int, cpfPaciente: int, codConsulta: int) -> None:
        self.codMedico = codMedico
        self.cpfPaciente = cpfPaciente
        self.codConsulta = codConsulta
         #Insert no BD

class Agendamento():
    def __init__(self, cpfAtendente: int, cpfPaciente: int, dataConsulta: date, codMedico: str) -> None:
        self.cpfAtendente = cpfAtendente
        self.cpfPaciente = cpfPaciente
        self.dataConsulta = dataConsulta
        self.dataAgendamento = date.today()
        self.codMedico = codMedico
        #self.codConsulta =  ( puxar do banco de dados a ultima consulta gerada e incrementar )
        cur.execute("select * from agendamento")
        resultado = cursor.fetchall() #coloca os resultados do último execute em um resultset
        for dados in resultado:
            print(dados) #percorre o resultset e a tabela linha por linha com seus respectivos dados
            #basta pegar a última linha de acordo com o comprimento de 'resultado' e formatar o seu print pra ficar bonitinho
        #Insert no BD na tabela Consulta
        
