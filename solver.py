import pandas as pd
from ortools.linear_solver import pywraplp

# Carregar os dados
df = pd.read_csv('projetos.csv')

df['Capital necessário'] = df['Capital necessário'].apply(lambda x: float(x))
df['VPL estimado'] = df['VPL estimado'].apply(lambda x: float(x))

# Criar o solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    print('Solver not created.')
    exit(1)

# Número de projetos
num_projects = df.shape[0]

# Criar variáveis de decisão (1 se o projeto for selecionado, 0 caso contrário)
x = []
for i in range(num_projects):
    x.append(solver.BoolVar(f'x[{i}]'))

# Restrição: Limitação do orçamento ($950.000)
budget_constraint = solver.Sum([x[i] * df['Capital necessário'][i] for i in range(num_projects)])
solver.Add(budget_constraint <= 950)

# Restrição: Limitação do número de programadores (20)
programmers_constraint = solver.Sum([x[i] * df['Programadores necessários'][i] for i in range(num_projects)])
solver.Add(programmers_constraint <= 20)

# Restrição: Os projetos 2 e 6 não podem ser selecionados simultaneamente
solver.Add(x[1] + x[5] <= 1)

# Função objetivo: Maximizar o VPL estimado
objective = solver.Objective()
for i in range(num_projects):
    coefficient = float(df['VPL estimado'][i])
    objective.SetCoefficient(x[i], coefficient)
objective.SetMaximization()

# Resolver o problema
status = solver.Solve()

# Verificar se foi encontrada uma solução ótima
if status == pywraplp.Solver.OPTIMAL:
    print('Solução ótima encontrada:')
    total_vpl = 0
    total_budget = 0
    total_programmers = 0
    selected_projects = []
    for i in range(num_projects):
        if x[i].solution_value() == 1:
            selected_projects.append(df['Projeto'][i])
            total_vpl += df['VPL estimado'][i]
            total_budget += df['Capital necessário'][i]
            total_programmers += df['Programadores necessários'][i]
            print(f'Projeto {df["Projeto"][i]} selecionado.')
    
    print(f'VLP Total: {total_vpl}')
    print(f'Budget Total: {total_budget}')
    print(f'Programadores: {total_programmers}')
else:
    print('Não foi encontrada uma solução ótima.')
