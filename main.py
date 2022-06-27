from aluno import Aluno
from professor import Professor
from sala_de_aula import Sala_de_Aula
from disciplinas import Disciplinas

from organizador import Organizador

# Os 3 devem possuir as seguintes funcionalidades:
# alterar dados, mostrar dados, listar todos do seu tipo,
# associar e desassociar cada um deles a uma disciplina

# Você também deve ser capaz de excluir os objetos (?)

# Restrições:

# Disciplinas:
# Cada disciplina só pode ter 1 professor e sala,
# Deve ter [0-X] alunos, e dias e horários de aula

# Salas:
# Toda sala deve ter dias e horários de aula;
# Salas devem ter horário de funcionamento, e não podem 
# ter aula fora dele;
# Devem ter lotação máxima, não receber disciplinas com 
# mais alunos que isso;

# Aluno e professor:
# Um aluno, professor e sala não podem ter 2 disciplinas 
# no mesmo horário

organizador = Organizador()

while True:
	desejo = input("o que voce quer fazer? (checar/atualizar/adicionar/deletar/checar tudo/break) ")
	if desejo == "break":
		break

	elif desejo == "adicionar":
		organizador.adicionar_elemento()
		print("Elemento adicionado.")

	elif desejo == "checar":
		organizador.checar_elemento()

	elif desejo == "atualizar":
		organizador.atualizar_elemento()
		print("Elemento atualizado.")

	elif desejo == "deletar":
		organizador.remover_elemento()

	elif desejo == "checar tudo":
		organizador.checar_tudo()
