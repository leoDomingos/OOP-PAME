class Professor():
    def __init__(self) -> None:
        self.disciplinas = []
        self.horarios_do_professor = {}
    def adicionar_disciplina(self, disciplina_a_adicionar):
        # Disciplina
        """
        Aceita uma disciplina; retorna False se os horários são conflitantes.
        """
        horarios_a_adicionar = disciplina_a_adicionar.horarios

        for dia in list(self.horarios_do_professor.keys()):
            if dia in list(horarios_a_adicionar.keys()):  # Só precisamos checar o resto se o professor já trabalha nesse dia
                horarios_ocupados_do_dia = self.horarios_do_professor[dia]
                for hora_indisponivel in horarios_ocupados_do_dia:
                    if hora_indisponivel in horarios_a_adicionar[dia]:
                        print("horario conflitante.")
                        return False

        self.disciplinas.append(disciplina_a_adicionar)
        for dia in list(disciplina_a_adicionar.horarios.keys()):  # Pegamos o dia da disciplina a adicionar
            if dia in list(self.horarios_do_professor.keys()):  # Se o dict horarios_do_prof ja tem esse dia
                self.horarios_do_professor[dia].append(horarios_a_adicionar[dia])  # Damos append
            else:
                self.horarios_do_professor[dia] = horarios_a_adicionar[dia]  # Se nao criamos uma nova key

    def mostrar_disciplinas(self):
        for disciplina in self.disciplinas:
            tabela_de_horarios = disciplina.horarios
            for dia, horarios in tabela_de_horarios.items():
                print(f"Esse professor tem na {dia} os horarios {horarios} ocupados.")
