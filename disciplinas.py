from elemento_da_faculdade import Elemento_da_Faculdade

class Disciplinas(Elemento_da_Faculdade):
    def __init__(self) -> None:
        super().__init__()
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
        if len(self.alunos) < self.max_alunos:
            self.alunos.append(aluno)
        else:
            print("Sala lotada.")

    def definir_sala_de_aula(self, sala):
        # Sala_de_Aula
        self.sala = sala

    def checar_elemento(self):
        """
		Mostra as disciplinas associadas ao elemento.
		:return:
		"""
        for dia_ocupado, horas_ocupado in self.horarios_de_func.items():
            print(f"Esse elemento atualmente trabalha na {dia_ocupado}, nos horários {horas_ocupado}")

        print(f"\nCapacidade max desse elemento: {self.capacidade_max}")
