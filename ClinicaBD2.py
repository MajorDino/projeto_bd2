from datetime import date

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
        
    def updateNomePaciente(self, nome):
        self.nomePaciente = nome
        #Update no BD
    def updateDddTelefonePaciente(self, ddd, telefone ):
        self.dddPaciente = ddd
        self.telefonePaciente = telefone
        #Update no BD
    def addPlano(self,codPlano: int):
        self.codPlano = codPlano
        #Update no BD
    def deletePaciente(self):
        #Delete no BD
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
        #Insert no BD na tabela Consulta
        