class Disciplinas():
    def __init__(self) -> None:
        # str, list, str, list, list
        self.alunos = []
        self.max_alunos = 0
        self.sala = ""
        self.professor = ""
        self.horarios = {}

    def adicionar_professor(self, professor):
        # Professor
        self.professor = professor

    def adicionar_aluno(self, aluno):
        # Aluno
        self.alunos.append(aluno)

    def definir_sala_de_aula(self, sala):
        # Sala_de_Aula
        self.sala = sala

    def def_horarios(self, dia, horas):
        """
        Adiciona um dia com seus horários.
        """
        # list, str
        self.horarios[dia] = horas

    def def_max_alunos(self, quantidade):
        # int
        self.max_alunos = quantidade
