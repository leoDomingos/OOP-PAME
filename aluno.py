from elemento_da_faculdade import Elemento_da_Faculdade

class Aluno(Elemento_da_Faculdade):
    def __init__(self) -> None:
        super().__init__()
        self.capacidade_max = 1000  # Alunos nao tem limite de quantas disciplinas puxar

    def checar_elemento(self):  # Diferente da classe Elemento da Faculdade, pois aluno nao trabalha
        """
        Checa o aluno.
        :param self:
        :return:
        """
        for dia_ocupado, horas_ocupado in self.horarios_de_func.items():
            print(f"\nEsse elemento atualmente está ocupado na {dia_ocupado}, nos horários {horas_ocupado}")
        print("\nDisciplinas desse elemento:")
        for disciplina in self.disciplinas:
            print(disciplina.identificacao)
