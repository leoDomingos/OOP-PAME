# TODO: evitar que def_horarios_de_func() adicione 2 horas identicas no mesmo dia
# Talvez o mesmo ocorra com adicionar_disciplina()

from elemento_da_faculdade import Elemento_da_Faculdade

class Sala_de_Aula(Elemento_da_Faculdade):
    
    def __init__(self) -> None:
        super().__init__()

    def is_lotacao_suficiente(self, disciplina_a_adicionar):
        """
        Verifica se a sala tem capacidade para o máximo de alunos da disciplina fornecida.
        :param disciplina_a_adicionar:
        :return:
        """
        if disciplina_a_adicionar.max_alunos > self.capacidade_max:
            return False
        else:
            return True

    