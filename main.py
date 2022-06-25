from aluno import Aluno
from professor import Professor
from sala_de_aula import Sala_de_Aula
from disciplinas import Disciplinas

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

dia1 = "seg"
dia2 = "ter"
horarios1 = [5, 13, 4]
horarios2 = [6, 5, 8]

matematica = Disciplinas()
matematica.def_horarios(dia1, horarios1)

historia = Disciplinas()
historia.def_horarios(dia2, horarios2)

geografia = Disciplinas()
geografia.def_horarios(dia2, horarios2)

alberto = Professor()
alberto.adicionar_disciplina(matematica)
alberto.adicionar_disciplina(historia)
alberto.adicionar_disciplina(geografia)

alberto.mostrar_disciplinas()