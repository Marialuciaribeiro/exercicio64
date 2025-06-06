import os
import datetime #modulo usado para trabalhar com datas e horas

class Quarto: #classe de quartos do hotel
    def __init__(self, numero, tipo, preco, status):
        self.numero = numero
        self.tipo = tipo #quarto solo, duplo ou triplo
        self.preco = preco
        self.status = status #disponivel, ocupado ou reservado
        self.reservas = [] #lista de reservas associadas ao quarto

    def __str__(self):
        tipo_cama = getattr(self, 'tipo_cama', '') #getattr usada para acessar dinamicamente atributos de um objeto
        cama_info = f" - {tipo_cama}" if tipo_cama else '' #usado para verificar se o atributo tipo_cama existe
        return f"Quarto {self.numero} ({self.tipo}{cama_info}) - R${self.preco:.2f} - Status: {self.status}"
    #como na subclasse solo não existe atributo tipo_cama isso faz com que nesse caso retorne vazio

class Duplo(Quarto): #subclasse, tipo de quarto
    def __init__(self, numero, preco, status, tipo_cama):
        super().__init__(numero, 'Duplo', preco, status) #super funçao que retorna uma referencia a classe pai
        #serve para evitar repetição de codigo, facilita a manutenção e é muito util em herença multipla
        self.tipo_cama = tipo_cama #solteiro ou casal

class Triplo(Quarto): #subclasse, tipo de quarto
    def __init__(self, numero, preco, status, tipo_cama):
        super().__init__(numero, 'Triplo', preco, status)
        self.tipo_cama = tipo_cama #solteiro ou casal

class Solo(Quarto): #subclasse, tipo de quarto
    def __init__(self, numero, preco, status):
        super().__init__(numero, 'Solo', preco, status)

class Hospede: #classe dos hospedes
    def __init__(self, nome, cpf, contato, data_nasc):
        self.nome= nome
        self.cpf = cpf
        self.contato = contato
        self.data_nasc = data_nasc

class Reserva: #classe das reservas
    def __init__(self, hospede, quarto, data_inicio, data_fim):
        self.hospede = hospede
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        

class Hotel: #classe geral do hotel
    def __init__(self):
        self.quartos = []
        self.reservas = []
    
    def add_quarto(self, quarto): #funçao para adicionar quartos
        self.quartos.append(quarto)
    
    def listar_quartos(self): #funçao para listar quartos adicionados
        if not self.quartos:
            print("Nenhum quarto cadastrado.")
        else:
            for quarto in self.quartos:
                print(quarto)

    def buscar_quarto_por_numero(self, numero): #função para buscar quarto por numero
        for quarto in self.quartos:
            if quarto.numero == numero:
                return quarto
            print(f"Quarto número {numero} não encontrado.")
            return None

    def listar_reservas(self): #função para listar reservas
        if not self.reservas:
            print("Nenhuma reserva registrada.")
        else:
            for reserva in self.reservas:
                print(f"Hóspede: {reserva.hospede.nome} | Quarto: {reserva.quarto.numero} | "
                      f"De: {reserva.data_inicio.strftime('%d/%m/%Y')} até {reserva.data_fim.strftime('%d/%m/%Y')}")
        #strftime é um metodo usado para formatar objetos de data e hora
    
    @staticmethod #Mantém funções relacionadas agrupadas dentro da classe, 
    #mesmo que não precisem acessar atributos da instância
    def disponibilidade(quartos, data_inicio, data_fim):
        disponiveis = []
        for quarto in quartos:
            if quarto.status == 'Disponível':
                disponiveis.append(quarto)
            elif quarto.status == 'Reservado':
                for reserva in quarto.reservas:
                    if not (data_fim < reserva.data_inicio or data_inicio > reserva.data_fim):
                        break
                    else: 
                        disponiveis.append(quarto)
        return disponiveis
    
    @staticmethod #Indica claramente que o método não depende do estado da instância, 
    #tornando o código mais fácil de entender.
    def fazer_reserva(hospede, quarto, data_inicio, data_fim):
        if quarto.status == 'Disponível':
            reserva = Reserva(hospede, quarto, data_inicio, data_fim)
            quarto.status = 'Reservado'
            quarto.reservas.append(reserva)
            return reserva
        else:
            return None
    
    @staticmethod
    def check_in(reserva):
        reserva.quarto.status = 'Ocupado'
        return None
    
    @staticmethod
    def check_out(reserva):
        reserva.quarto.status = 'Disponível'
        reserva.quarto.reservas.remove(reserva)


def limpar(): #função de limpar o sistema dependendo do sistema operacional
        os.system('cls' if os.name == 'nt' else 'clear')

def coletar_dados_hospede(): #função para validar, nome, cpf e contato dos hospedes
    while True:
        nome = input("Nome do hóspede: ").strip().lower()
        if not all(palavra.isalpha() for palavra in nome.split()):
            print("Nome deve conter apenas letras!")
            continue

        cpf = input("CPF do hóspede (somente números): ")
        if not (len(cpf) == 11 and cpf.isdigit()):
            print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
            continue

        contato = input("Contato do hóspede: ")
        if not contato.isdigit():
            print("Número de contato inválido! Use apenas números.")
            continue

        return nome, cpf, contato


def valid_data_nasc(): #função para validar data de nascimento
    while True:
        data_str = input("Data de nascimento do hóspede (dd/mm/yyyy): ")
        try:
            data_nasc = datetime.datetime.strptime(data_str, '%d/%m/%Y')
            hoje = datetime.datetime.today()
            idade = (hoje - data_nasc).days // 365

            if data_nasc > hoje:
                print("A data de nascimento não pode ser no futuro.")
            elif idade > 120:
                print("Idade inválida. Verifique a data digitada.")
            else:
                return data_nasc
        except ValueError:
            print("Formato inválido. Use o formato dd/mm/yyyy.")

def valid_datas_reserva():
    while True:
        try: #gera uma exceçao, se caso ocorra, a execuçao do cod
            #dentro do try é interrompida e é passado para o except
            data_inicio_str = input("Data de início da reserva (dd/mm/yyyy): ")
            data_fim_str = input("Data de fim da reserva (dd/mm/yyyy): ")
            #strptime é usado para converter uma string que representa uma data em um objeto datetime
            data_inicio = datetime.datetime.strptime(data_inicio_str, '%d/%m/%Y')
            data_fim = datetime.datetime.strptime(data_fim_str, '%d/%m/%Y')

            if data_fim < data_inicio:
                print("A data de fim não pode ser anterior à data de início. Tente novamente.")
            else:
                return data_inicio, data_fim
        except ValueError:#valueError valida se números digitados são positivos
            #O ValueError é uma exceção em Python que é levantada quando uma função 
            #recebe um argumento com o tipo correto, mas com um valor inadequado.
            print("Formato de data inválido. Use o formato dd/mm/yyyy.")

def processar_check(hotel, tipo):
    numero = int(input('Número do Quarto: '))
    quarto = hotel.buscar_quarto_por_numero(numero)
    if quarto:
        for reserva in quarto.reservas:
            if reserva.quarto.numero == numero:
                if tipo == 'in':
                    Hotel.check_in(reserva)
                    print(f'Check-in realizado para o quarto {numero} com sucesso!')
                elif tipo == 'out':
                    Hotel.check_out(reserva)
                    print(f'Check-out realizado para o quarto {numero} com sucesso!')
                return
        print(f'Nenhuma reserva encontrada para o quarto {numero}')
    else:
        print(f'Quarto número {numero} não encontrado.')



def exibirMenu(): #função para exibir Menu
    hotel = Hotel()

    while True:
        print('''\n### Menu do Hotel ###
1. Adicionar Quarto
2. Listar Quartos
3. Buscar Quarto por número
4. Fazer Reserva
5. Listar Reservas
6. Check-in
7. Check-out
0. Sair
              ''')
        opcao = int(input('Escolha uma opção: \n'))

        if opcao == 1:
            limpar()
            print('\n### Adicionar Quarto ###')
            tipo = input('Tipo de Quarto (Solo, Duplo, Triplo): ').lower()
            numero = int(input('Número do Quarto: '))
            preco = float(input('Preço do Quarto: '))
            status = 'Disponível'

            if tipo == 'duplo' or tipo == 'triplo':
                tipo_cama = input('Tipo de cama (Solteiro, Casal): ')
                if tipo == 'duplo':
                    quarto = Duplo(numero, preco, status, tipo_cama)
                else:
                    quarto = Triplo(numero, preco, status, tipo_cama)
            elif tipo == 'solo': 
                quarto = Solo(numero, preco, status)
            else:
                print('Tipo de quarto inválido!')
                continue

            #add quarto a lista de quartos do hotel
            hotel.add_quarto(quarto) #hotel é uma instancia da classe hotel
            #add_quarto é um metodo da classe hotel
            #quarto é um objeto de uma das subclasses de Quarto
            print(f"Quarto {numero} adicionado com sucesso.")
        
        elif opcao == 2:
            limpar()
            print('\n### Lista de Quartos ###')
            hotel.listar_quartos()
        
        elif opcao == 3:
            limpar()
            print('\n### Busca por número de Quarto ###')
            numero = int(input('Número do Quarto: '))
            quarto = hotel.buscar_quarto_por_numero(numero)
            if quarto:
                print(quarto)
        
        elif opcao == 4:
            limpar()
            print('\n### Fazer Reverva ###')
            nome, cpf, contato = coletar_dados_hospede()
            data_nasc = valid_data_nasc()
            hospede = Hospede(nome, cpf, contato, data_nasc)
            numero = int(input('Número do quarto: '))
            quarto = hotel.buscar_quarto_por_numero(numero)
            if quarto:
                data_inicio, data_fim = valid_datas_reserva()
                reserva = hotel.fazer_reserva(hospede, quarto, data_inicio, data_fim)
                if reserva:
                    print(f"Reserva feita para o quarto {reserva.quarto.numero}.")            
            
        elif opcao == 5:
            limpar()
            print('\n### Listar Reservas ###')
            hotel.listar_reservas()
        
        elif opcao == 6:
            limpar()
            print('\n### Check-in ###')
            processar_check(hotel, 'in')
        
        elif opcao == 7:
            limpar()
            print('\n### Check-out ###')
            processar_check(hotel, 'out')
        
        elif opcao == 0:
            limpar()
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Digite novamente!')

#executando menu do hotel
exibirMenu()
    
    
