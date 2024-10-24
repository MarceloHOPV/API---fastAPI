from fastapi import FastAPI, HTTPException
import uvicorn
from typing import List
from Models import Funcionario, FuncionarioUpdateRequest, Horario, Genero, HorarioTrabalho, Cargo
from uuid import uuid4,UUID

app = FastAPI()

db: List[Funcionario] = [
    Funcionario(
        id= UUID("b7a9e9d4-b47e-4072-a933-242ca5841861"),
        nome="João",
        idade=25,
        salario=5000.00,
        genero=Genero.masculino,
        email="joao@gmail.com",
        senha="123456",
        cargo=Cargo.gerente,
        telefone="999999999",
        horario_de_trabalho=[
            HorarioTrabalho(horarioInicio=Horario(hora=8, minuto=0), horarioFim=Horario(hora=11, minuto=30)),
            HorarioTrabalho(horarioInicio=Horario(hora=18, minuto=0), horarioFim=Horario(hora=22, minuto=30))
        ],
        tabela_de_ponto=[
            Horario(hora=11, minuto=30),
            Horario(hora=22, minuto=0)
        ],
        banco_de_horas=Horario(hora=8, minuto=52)
    ),
    Funcionario(
        id= UUID("2d4bf2ef-78e8-45dc-b016-064213a7e279"),
        nome="Maria",
        idade=30,
        cargo=Cargo.funcionario,
        salario=6000.00,
        genero=Genero.feminino,
        email="maria@gmail.com",
        senha="123456",
        telefone="999999991",
        horario_de_trabalho=[
            HorarioTrabalho(horarioInicio=Horario(hora=8, minuto=0), horarioFim=Horario(hora=11, minuto=30)),
            HorarioTrabalho(horarioInicio=Horario(hora=13, minuto=30), horarioFim=Horario(hora=18, minuto=0))
        ],
        tabela_de_ponto=[
            Horario(hora=11, minuto=23),
            Horario(hora=18, minuto=0)
        ],
        banco_de_horas=Horario(hora=10, minuto=13)
    )
]

# Minha primeira API ;)
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/api/v1/usuarios")
async def get_funcionarios():
    return db

@app.post("/api/v1/usuarios")
async  def register_funcionario(funcionario: Funcionario):
    db.append(funcionario)
    return{"funcionarioID": funcionario.id}

@app.delete("/api/v1/usuarios/{funcionario_id}")
async def delete_funcionario(funcionario_id: UUID):
    for funcionario in db:
        if funcionario.id == funcionario_id:
            db.remove(funcionario)
            return{"message": "Funcionario removido com sucesso"}
    raise HTTPException(status_code=404, detail=f"Usuario com o id {funcionario_id} não encontrado")

@app.put("/api/v1/usuarios/{funcionario_id}")
async def update_funcionario(funcionario_update: FuncionarioUpdateRequest, funcionario_id: UUID):
    for f in db:
        if f.id == funcionario_id:
            if funcionario_update.nome is not None:
                f.nome = funcionario_update.nome
            if funcionario_update.idade is not None:
                f.idade = funcionario_update.idade
            if funcionario_update.salario is not None:
                f.salario = funcionario_update.salario
            if funcionario_update.genero is not None:
                f.genero = funcionario_update.genero
            if funcionario_update.email is not None:
                f.email = funcionario_update.email
            if funcionario_update.senha is not None:
                f.senha = funcionario_update.senha
            if funcionario_update.cargo is not None:
                f.cargo = funcionario_update.cargo
            if funcionario_update.telefone is not None:
                f.telefone = funcionario_update.telefone
            if funcionario_update.horario_de_trabalho is not None:
                f.horario_de_trabalho = funcionario_update.horario_de_trabalho
            if funcionario_update.tabela_de_ponto is not None:
                f.tabela_de_ponto = funcionario_update.tabela_de_ponto
            if funcionario_update.banco_de_horas is not None:
                f.banco_de_horas = funcionario_update.banco_de_horas
            return{"message": "Funcionario atualizado com sucesso"}
    raise HTTPException(status_code=404, detail=f"Usuario com o id {funcionario_id} não encontrado")



# uvicorn PrimeiraAPI:app --reload

# /my-project
# │
# ├── /frontend
# │   ├── /public         # Arquivos estáticos (como imagens e ícones)
# │   ├── /src            # Código-fonte React
# │   │   ├── /components # Componentes reutilizáveis de UI
# │   │   ├── /pages      # Páginas da aplicação
# │   │   ├── /services   # Lógica de integração com APIs
# │   │   └── /hooks      # Hooks personalizados
# │   ├── package.json    # Dependências do frontend
# │   └── README.md       # Documentação do frontend
# │
# ├── /backend
# │   ├── /app            # Código principal do FastAPI
# │   │   ├── /api        # Endpoints da API
# │   │   ├── /models     # Definição dos modelos de dados (Pydantic, SQLAlchemy)
# │   │   ├── /schemas    # Schemas Pydantic
# │   │   ├── /services   # Lógica de negócios
# │   │   ├── /db         # Conexão e operações com o banco de dados (PostgreSQL ou SQLite)
# │   │   └── /utils      # Funções utilitárias
# │   ├── /tests          # Testes unitários e de integração
# │   ├── main.py         # Arquivo principal do FastAPI
# │   ├── requirements.txt # Dependências do FastAPI
# │   └── README.md       # Documentação do backend
# │
# ├── /database            # Arquivos relacionados ao banco de dados
# │   ├── migrations       # Scripts de migração do banco de dados
# │   └── db_setup.sql     # Script de inicialização do banco de dados
# │
# ├── /docker              # Arquivos para containers Docker (se for usar)
# │   ├── Dockerfile       # Dockerfile para o backend
# │   └── docker-compose.yml # Arquivo de configuração Docker Compose
# │
# ├── /docs                # Documentação geral do projeto
# │
# ├── .gitignore           # Arquivos que o Git deve ignorar
# ├── README.md            # Documentação geral do projeto
# └── .env                 # Variáveis de ambiente (não commitadas no Git)
