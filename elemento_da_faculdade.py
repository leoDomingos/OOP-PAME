# TODO: adicionar formas diferentes de verificar lotaçao maxima para cada elemento


class Elemento_da_Faculdade():
	def __init__(self) -> None:
		self.horarios_de_func = {}  # Horários de funcionamento do elemento
		self.horarios_ocupados = {}  # Horários ocupados do elemento
		self.capacidade_max = 0  # Capacidade máxima do elemento
		self.disciplinas = []  # Disciplinas que o elemento tem
		self.identificacao = ""

	def def_horarios_de_func(self, dia, horas):
		"""
		Define os horários de funcionamento do elemento.
		"""
		# list, str
		if dia in list(self.horarios_de_func.keys()):
			self.horarios_de_func[dia].append(horas)
		else:
			self.horarios_de_func[dia] = horas

	def def_capacidade_max(self, capacidade_max):
		"""
		Define a capacidade máxima do elemento.
		:param capacidade_max:
		:return:
		"""
		self.capacidade_max = capacidade_max

	def is_horario_disponivel(self, disciplina_a_adicionar):
		"""
		Aceita uma disciplina; retorna False se os horários já estão ocupados pelo Elemento.
		"""
		horarios_a_adicionar = disciplina_a_adicionar.horarios

		for dia in list(self.horarios_ocupados.keys()):
			if dia in list(horarios_a_adicionar.keys()):  # Só precisamos checar o resto se a sala já tem aula nesse dia
				horarios_ocupados_do_dia = self.horarios_ocupados[dia]
				for hora_indisponivel in horarios_ocupados_do_dia:
					if hora_indisponivel in horarios_a_adicionar[dia]:
						# print("horario conflitante.")
						return False
		return True

	def is_elemento_funcionando(self, disciplina_a_adicionar):
		"""
		Aceita uma disciplina e verifica se o elemento trabalha ou não nos horários dela.
		:param disciplina_a_adicionar:
		:return:
		"""
		horarios_a_adicionar = disciplina_a_adicionar.horarios

		for dia, horas in horarios_a_adicionar.items():
			if dia in list(
					self.horarios_de_func.keys()):  # Só precisamos checar o resto se o dia está na agenda da sala
				for hora_exigida in horas:
					if hora_exigida not in self.horarios_de_func[dia]:
						# print("horario nao disponivel.")
						return False
			else:  # Se o dia não está na agenda da sala, já podemos parar
				# print("horario nao disponivel.")
				return False
		# print("sala funciona nos horários dessa disciplina.")
		return True  # Se chegamos aqui, os horarios batem

	def adicionar_disciplina(self, disciplina_a_adicionar):
		"""
		Adiciona a disciplina nos horários do elemento, se der.
		"""
		if not self.is_elemento_funcionando(disciplina_a_adicionar) or not self.is_horario_disponivel(disciplina_a_adicionar) or not(len(self.disciplinas) < self.capacidade_max):
			return False
		horarios_a_adicionar = disciplina_a_adicionar.horarios
		self.disciplinas.append(disciplina_a_adicionar)
		for dia in list(disciplina_a_adicionar.horarios.keys()):  # Pegamos o dia da disciplina a adicionar
			if dia in list(self.horarios_ocupados.keys()):  # Se o dict horarios_do_prof ja tem esse dia
				self.horarios_ocupados[dia].append(horarios_a_adicionar[dia])  # Damos append
			else:
				self.horarios_ocupados[dia] = horarios_a_adicionar[dia]  # Se nao criamos uma nova key
		else:
			return True




	def checar_elemento(self):
		"""
		Mostra as disciplinas associadas ao elemento.
		:return:
		"""
		for dia_trabalho, horas_trabalho in self.horarios_de_func.items():
			print(f"\nEsse elemento pode trabalhar na {dia_trabalho}, nos horários {horas_trabalho}")
		for dia_ocupado, horas_ocupado in self.horarios_de_func.items():
			print(f"Esse elemento atualmente trabalha na {dia_ocupado}, nos horários {horas_ocupado}")
		print("\nDisciplinas desse elemento:")
		for disciplina in self.disciplinas:
			print(disciplina.identificacao)

		print(f"\nCapacidade max desse elemento: {self.capacidade_max}")


	def mostrar_funcionamento(self):
		"""
		Mostra os horários de funcionamento do elemento.
		:return:
		"""
		for dias_ocupados, horas_ocupadas in self.horarios_de_func.items():
			print(f"Esse elemento funciona na {dias_ocupados}, nos horários{horas_ocupadas}.")