class Sala_de_Aula():
    
    def __init__(self) -> None:
        self.horarios_de_func = {}
        self.capacidade_max = 0
        self.disciplinas = []
        self.horarios_da_sala = {}

    def def_horarios(self, horas, dias):
        # list, list
        for dia in dias:
            self.horarios_de_func[dia] = horas

    def def_capacidade_max(self, capacidade_max):
        self.capacidade_max = capacidade_max

    def adicionar_disciplina(self, disciplina_a_adicionar):
        # Disciplina
        """
        Aceita uma disciplina; retorna False se os horários são conflitantes.
        """
        horarios_a_adicionar = disciplina_a_adicionar.horarios

        for dia in list(self.horarios_da_sala.keys()):
            if dia in list(
                    horarios_a_adicionar.keys()):  # Só precisamos checar o resto se o professor já trabalha nesse dia
                horarios_ocupados_do_dia = self.horarios_da_sala[dia]
                for hora_indisponivel in horarios_ocupados_do_dia:
                    if hora_indisponivel in horarios_a_adicionar[dia]:
                        print("horario conflitante.")
                        return False

        self.disciplinas.append(disciplina_a_adicionar)
        for dia in list(disciplina_a_adicionar.horarios.keys()):  # Pegamos o dia da disciplina a adicionar
            if dia in list(self.horarios_da_sala.keys()):  # Se o dict horarios_do_prof ja tem esse dia
                self.horarios_da_sala[dia].append(horarios_a_adicionar[dia])  # Damos append
            else:
                self.horarios_da_sala[dia] = horarios_a_adicionar[dia]  # Se nao criamos uma nova key

    def mostrar_disciplinas(self):
        for disciplina in self.disciplinas:
            tabela_de_horarios = disciplina.horarios
            for dia, horarios in tabela_de_horarios.items():
                print(f"Essa sala tem na {dia} os horarios {horarios} ocupados.")

    