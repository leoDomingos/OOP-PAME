from elemento_da_faculdade import Elemento_da_Faculdade

class Professor(Elemento_da_Faculdade):
    def __init__(self) -> None:
        super().__init__()
        self.capacidade_max = 1  # Um professor só pode ter uma disciplina
