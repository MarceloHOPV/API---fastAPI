from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID, uuid4
from enum import Enum

class Genero(str, Enum):
    masculino = 'masculino'
    feminino = 'feminino'

class Cargo(str, Enum):
    desenvolvedor = 'desenvolvedor'
    gerente = 'gerente'
    funcionario = 'funcionario'

class Horario(BaseModel):
    hora: int
    minuto: int

class HorarioTrabalho(BaseModel):
    horarioInicio: Horario
    horarioFim: Horario


class Funcionario(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str
    idade: int
    salario: float
    genero: Genero
    email: str
    senha: str
    cargo: Cargo
    telefone: str
    horario_de_trabalho: List[HorarioTrabalho]
    tabela_de_ponto: List[Horario]
    banco_de_horas: Horario

class FuncionarioUpdateRequest(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    cargo: Optional[str] = None
    salario: Optional[float] = None
    genero: Optional[Genero] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    cargo: Optional[Cargo] = None
    telefone: Optional[str] = None
    horario_de_trabalho: Optional[List[HorarioTrabalho]] = None
    tabela_de_ponto: Optional[List[Horario]] = None
    banco_de_horas: Optional[Horario] = None
    