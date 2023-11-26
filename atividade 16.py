class Pessoa:
    def __init__(self, nome, cpf, endereço, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereço
    
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_endereco(self):
        return self.__endereco

    def quemSou(self):
        return print(f"Eu sou uma pessoa.")


class Aluno(Pessoa):
    #matricula em no máximo 2 cursos
    def __init__(self, matricula, nome, cpf, endereço, telefone):
        super().__init__(nome, cpf, endereço, telefone)
        self.__matricula = matricula
        self.__cursos = []

    #getters e setters
    def get_matricula(self):
        return self.__matricula
    def get_cursos(self):
        return self.__cursos

    def set_cursos(self, cursos):
        self.__cursos = cursos

    #metodo para adicionar curso ao aluno e logo após adiciona-lo no curso
    def adicionar_curso(self, cursos):
        if len(self.__cursos) < 2:
            self.__cursos.append(cursos)
            cursos.add_aluno(self)
        else:
            print(f"Limite atingido!! O aluno {self._Pessoa__nome} não pode se matricular em mais cursos :(")

    #metodo de escrita
    def quemSou(self):
        return print(f"Yo soy un alumno")


class Professor(Pessoa):
    #horaSem vai acumulando de acordo com os cursos cadastrados
    def __init__(self, salario, nome, cpf, endereço, telefone):
        #chmando construtuos da classe base
        Pessoa.__init__(self, nome, cpf, endereço, telefone)
        # super().__init__(nome, cpf, endereço, telefone)
        self.__uc = []
        self.__salario = salario
        self.__horaSem = 0

    #getters e setters
    def get_salario(self):
        return self.__salario
    def get_horaSem(self):
        return self.__horaSem
    def get_uc(self):
        return self.__uc
   
    def set_horaSem(self, horas):
        self.__horaSem = horas
    
    def adicionar_curso(self, uc):
        if len(self.__uc) < 1:
            self.__uc.append(uc)
            uc.add_aluno(self)
        else:
            print(f"Limite atingido!! O aluno {self._Pessoa__nome} não pode se matricular em mais cursos :(")
    
    def __str__(self):
        return f"Nome: {self._Pessoa__nome}\nSalário:{self.__salario}"

    def quemSou(self):
        return print(f"I'm professor...")
        
class Curso:
    #só é aberto com minimo 10 alunos
    def __init__(self, professor, horassem, nome, descricao):
        self.__prof = professor
        self.__alunos = []
        self.__horassem = horassem
        self.__nome = nome
        self.__desc = descricao
        self.__cursoValido = False
        
    #getters e setters
    def get_nome(self):
        return self.__nome
    def get_prof(self):
        return self.__prof
    def get_aluno(self):
        return self.__alunos
    def get_horassem(self):
        return self.__horas
    def get_descricao(self):
        return self.__desc
    def get_cursoValido(self):
        return self.__cursoValido

    def set_nome(self, nome):
        self.__nome = nome
    def set_prof(self, prof):
        self.__prof = prof
    def set_horassem(self, hrs):
        self.__horassem = hrs
    def set_alunos(self, alu):
        self.__alunos = alu
    def set_cursoValido(self, cursoVal):
        self.__cursoValido = cursoVal
    def set_desc(self, descricao):
        self.__desc = descricao
    
    #metodo para adicionar um aluno por vez
    def add_aluno(self, aluno):
        if aluno not in self.__alunos:
            if aluno != self.__prof:
                self.__alunos.append(aluno)
            
    
    #metodo para verificar se o curso pode ser aberto
    def aberturaCurso(self):
        cont = 0
        for a in self.__alunos:
            cont += 1
        if cont >= 10:
            return print(f"O curso está aberto para aulas!!")
        else:
            return print(f"O curso não atende os requisitos para abertura :(")

    #metodo para validar caso o professor tenha hora disponível na semana
    def validarHoraP(self):
        if self.__prof.get_horaSem() > 40:
           return print(f"O professor {self.__prof.get_nome()} já está em muitas aulas\nNão é possível matricula-lo a este curso de {self.__nome}")
        else:
           self.__prof.set_horaSem(self.__prof.get_horaSem() +self.__horassem)

    def toString(self):
        professor_str = self.__prof.get_nome()
        alunos_str = [aluno.get_nome() for aluno in self.__alunos]
        alunos_str = ', '.join(alunos_str)
        return print(f"Professor: {professor_str}\nAlunos: {alunos_str}\nCurso: {self.__nome}\nDescrição: {self.__desc}\nHoras semanais: {self.__horassem}")


# Instâncias de Alunos
aluno1 = Aluno("A123", "João", 8745215, "rua japibaí", 8495612)
aluno2 = Aluno("B456", "Maria", 9876543, "avenida XYZ", 9871234)
aluno3 = Aluno("C789", "Pedro", 1234567, "rua ABC", 4567890)
aluno4 = Aluno("D101", "Ana", 9876543, "avenida 123", 1239876)
aluno5 = Aluno("E202", "Lucas", 8745215, "rua 456", 4561238)
aluno6 = Aluno("F303", "Carla", 4567890, "avenida DEF", 9876543)
aluno7 = Aluno("G404", "Miguel", 1234567, "rua GHI", 4569870)
aluno8 = Aluno("H505", "Isabela", 9871234, "avenida 789", 7894561)
aluno9 = Aluno("I606", "Tiago", 4561238, "rua JKL", 1237894)
aluno10 = Aluno("J707", "Larissa", 4569870, "avenida MNO", 7891234)
aluno11 = Aluno("K987", "Maíssa", 1237894, "rua PQR", 9871230)

# Instâncias de Professores
professor1 = Professor(800, "Algum Doidin aí", 21456980, "rua dos cabloquinhos", 98787512)
professor2 = Professor(700, "Mary Sue", 9876543, "avenida ZYX", 4569871)
professor3 = Professor(900, "Carolina", 1234567, "rua LMN", 7894562)

# # instanciando cursos
curso1 = Curso(professor1, 15, "Web python", "desenvolvimento de aplicações web com frameworks em python")
curso2 = Curso(professor3, 20, "Introdução à Programação", "Noções básicas de programação")
curso3 = Curso(professor2, 20, "Design Gráfico", "Criação de gráficos e designs")

# # chamada dos métodos
curso2.aberturaCurso()
curso1.validarHoraP()
curso2.validarHoraP()
curso3.validarHoraP()

aluno3.adicionar_curso(curso1)
aluno3.adicionar_curso(curso2)
aluno3.adicionar_curso(curso3)
professor1.adicionar_curso(curso3)


curso1.toString()
print("////")
curso2.toString()
print("////")
curso3.toString()