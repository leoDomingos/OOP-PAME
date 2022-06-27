from aluno import Aluno
from professor import Professor
from sala_de_aula import Sala_de_Aula
from disciplinas import Disciplinas

# TODO: implementar funcao para adicionar alunos às materias; impedir que adicionar horarios indenticos duplique as listas dos dicts


class Organizador():
	def __init__(self):
		self.alunos_totais = {}
		self.professores_totais = {}
		self.salas_totais = {}
		self.disciplinas_totais = {}

	def adicionar_elemento(self):
		"""
		Cria um elemento do tipo desejado, com identificaçao e , se nao for aluno, horas de funcionamento
		:return:
		"""
		elemento_a_adicionar = input("O que voce quer adicionar? (professor, aluno, disciplina, sala) ")

		if elemento_a_adicionar == "aluno":
			nome = input("nome do aluno: ")
			novo_aluno = Aluno()
			novo_aluno.identificacao = nome
			self.alunos_totais[nome] = novo_aluno

		elif elemento_a_adicionar == "professor":
			# Precisamos definir o nome e horas de trabalho dele
			nome = input("nome do professor: ")
			novo_professor = Professor()
			novo_professor.identificacao = nome
			while True:
				dia_novo = input("Adicione um dia no qual ele trabalha: (break para sair) ")
				if dia_novo == "break":
					break
				horas_novas = []
				while True:
					hora_nova = input("Nesse dia, digite uma hora de trabalho: (break para sair) ")
					if hora_nova == "break":
						break
					hora_nova = int(hora_nova)
					horas_novas.append(hora_nova)
				novo_professor.def_horarios_de_func(dia_novo, horas_novas)
			self.professores_totais[nome] = novo_professor

		elif elemento_a_adicionar == "sala":
			# essencialmente o mesmo que o de adicionar professor, mas com nomes mudados pra nao ficar estranho
			nome = input("nome da sala: ")
			nova_sala = Sala_de_Aula()
			nova_sala.identificacao = nome
			while True:
				dia_novo = input("Adicione um dia no qual ela funciona: (break para sair) ")
				if dia_novo == "break":
					break
				horas_novas = []
				while True:
					hora_nova = input("Nesse dia, digite uma hora de funcionamento: (break para sair) ")
					if hora_nova == "break":
						break
					hora_nova = int(hora_nova)
					horas_novas.append(hora_nova)
				nova_sala.def_horarios_de_func(dia_novo, horas_novas)
			self.salas_totais[nome] = nova_sala

		elif elemento_a_adicionar == "disciplina":
			# essencialmente o mesmo que o de adicionar professor, mas com nomes mudados pra nao ficar estranho
			nome = input("nome da materia: ")
			nova_materia = Disciplinas()
			nova_materia.identificacao = nome
			while True:
				dia_novo = input("Adicione um dia no qual ela acontece: (break para sair) ")
				if dia_novo == "break":
					break
				horas_novas = []
				while True:
					hora_nova = input("Nesse dia, digite uma hora de aula: (break para sair) ")
					if hora_nova == "break":
						break
					hora_nova = int(hora_nova)
					horas_novas.append(hora_nova)
				nova_materia.def_horarios_de_func(dia_novo, horas_novas)
			self.disciplinas_totais[nome] = nova_materia

	def checar_elemento(self):
		elemento_a_checar = input("O que voce quer checar? (professor, aluno, disciplina, sala)")
		if elemento_a_checar == "professor":
			identificacao_a_checar = input("Qual o nome do professor? ")
			objeto_a_checar = self.professores_totais[identificacao_a_checar]

		elif elemento_a_checar == "aluno":
			identificacao_a_checar = input("Qual o nome do aluno? ")
			objeto_a_checar = self.alunos_totais[identificacao_a_checar]

		elif elemento_a_checar == "disciplina":
			identificacao_a_checar = input("Qual o nome da disciplina? ")
			objeto_a_checar = self.disciplinas_totais[identificacao_a_checar]

		elif elemento_a_checar == "sala":
			identificacao_a_checar = input("Qual o nome da sala? ")
			objeto_a_checar = self.salas_totais[identificacao_a_checar]

		objeto_a_checar.checar_elemento()

	def atualizar_elemento(self): # adicionar/tirar : sala, disciplina /// # mudar: identificacao, horas de funcionamento
		elemento_a_atualizar = input("O que voce deseja atualizar? professor, aluno, disciplina, sala (p/a/d/s) ")
		acao_a_realizar = input("Você deseja... (adicionar/tirar) disciplinas - (mudar) identificacao, hora de funcionamento? (d/i/h) ")
		# Primeiro devemos pegar o objeto e dicionario corretos para modificar
		if elemento_a_atualizar == "p":  # Caso seja professor
			identificacao_a_atualizar = input("Nome do professor: ")
			objeto_a_atualizar = self.professores_totais[identificacao_a_atualizar]
			dict_a_atualizar = self.professores_totais
		elif elemento_a_atualizar == "a":  # Caso seja aluno
			identificacao_a_atualizar = input("Nome do aluno: ")
			objeto_a_atualizar = self.alunos_totais[identificacao_a_atualizar]
			dict_a_atualizar = self.alunos_totais
		elif elemento_a_atualizar == "d":  # Caso seja disciplina
			identificacao_a_atualizar = input("Nome da disciplina: ")
			objeto_a_atualizar = self.disciplinas_totais[identificacao_a_atualizar]
			dict_a_atualizar = self.disciplinas_totais
		elif elemento_a_atualizar == "s":
			identificacao_a_atualizar = input("Nome da sala: ")
			objeto_a_atualizar = self.salas_totais[identificacao_a_atualizar]
			dict_a_atualizar = self.salas_totais

		if acao_a_realizar == "i":  # Mudando a identificacao do elemento
			# Mudamos o nome do elemento
			antigo_nome = objeto_a_atualizar.identificacao
			novo_nome = input(f"Nome atual: {antigo_nome}. Nome novo: ")
			dados_do_elemento = self.dict_a_atualizar[antigo_nome].pop()
			dict_a_atualizar[novo_nome] = dados_do_elemento

		elif acao_a_realizar == "d":  # Adicionando disciplina ao elemento
			informacao_adicional = input("Deseja adicionar ou tirar? (a/t) ")
			identificacao_da_disciplina = input("Qual o nome da disciplina? ")
			disciplina_alvo = self.disciplinas_totais[identificacao_da_disciplina]
			if informacao_adicional == "a":  # Adicionando disciplina ao objeto
				if not objeto_a_atualizar.adicionar_disciplina(disciplina_alvo):
					print("Algo deu errado. Verifique se tem espaço disponivel no elemento.")
			if elemento_a_atualizar == "a":  # Adicionando aluno à disciplina, caso seja um aluno que estamos adicionando
				disciplina_alvo.alunos.append(objeto_a_atualizar)

			elif informacao_adicional == "t":  # Retirando todas as disciplinas e horarios ocupados do objeto
				print("Removendo todas as disciplinas do elemento...")
				objeto_a_atualizar.disciplinas.remove(identificacao_da_disciplina)
				objeto_a_atualizar.horarios_ocupados = {}

		elif acao_a_realizar == "h":  # Mudando horários de funcionamento
			informacao_adicional = input("Deseja adicionar ou tirar? (a/t) ")
			if informacao_adicional == "a":  # Adicionando horario de funcionamento ao objeto
				dia_novo = input("Adicione um novo dia no qual ele trabalha: ")
				horas_novas = []
				while True:
					hora_nova = input("Nesse dia, digite uma hora de trabalho: (break para sair) ")
					if hora_nova == "break":
						break
					hora_nova = int(hora_nova)
					horas_novas.append(hora_nova)
				objeto_a_atualizar.def_horarios_de_func(dia_novo, horas_novas)

			elif informacao_adicional == "t":  # Retirando todas as disciplinas e horarios de funcionamento do objeto
				print("Removendo todas as disciplinas e horarios de funcionamento do elemento...")
				objeto_a_atualizar.horarios_de_func = {}
				objeto_a_atualizar.disciplinas = []

	def remover_elemento(self):
		elemento_a_remover = input("O que voce deseja remover? professor, aluno, disciplina, sala (p/a/d/s) ")
		identificacao_a_remover = input("Qual o nome desse elemento? ")

		if elemento_a_remover == "p":
			self.professores_totais.pop(identificacao_a_remover)

		elif elemento_a_remover == "a":
			self.alunos_totais.pop(identificacao_a_remover)

		elif elemento_a_remover == "d":
			self.disciplinas_totais.pop(identificacao_a_remover)

		elif elemento_a_remover == "s":
			self.disciplinas_totais.pop(identificacao_a_remover)

		print("Elemento deletado.")


	def checar_dicionario(self, dicionario):
		print("Elementos desse tipo:")
		for identificacao, objeto in dicionario.items():
			print(identificacao)

	def checar_tudo(self):
		"""
		Printa todos de um determinado tipo.
		:return:
		"""
		categoria_a_checar = input("Qual categoria? (p/d/a/s) ")
		if categoria_a_checar == "p":
			self.checar_dicionario(self.professores_totais)
		elif categoria_a_checar == "d":
			self.checar_dicionario(self.disciplinas_totais)
		elif categoria_a_checar == "a":
			self.checar_dicionario(self.alunos_totais)
		elif categoria_a_checar == "s":
			self.checar_dicionario(self.salas_totais)

