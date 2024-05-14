# Resolução da Ponderada de Mat - Vitto Mazeto
- Modelagem de planilha e análise de decisão: uma introdução prática a business analytics", Cliff T. Ragsdale, capítulo 6, página 249, faça o exercício 19.

## Enunciado

Um criador de jogos de videogame tem sete propostas para novos jogos. Infelizmente, a empresa não pode desenvolver todas as propostas porque o orçamento para novos projetos está limitado a $ 950.000 e existem apenas 20 programadores para desenvolver os novos projetos. As exigências financeiras, os retornos e o número de programadores necessários para cada projeto estão resumidos na tabela a seguir. Os projetos 2 e 6 requerem conhecimento de programação espe- cializado que apenas um dos programadores tem. Esses dois projetos não podem ser selecionados simultaneamente porque o programador com os conhecimentos necessários consegue desenvolver apenas um dos projetos. (Observação: Todos os valores monetários representam milhares de dólares.)

| Projeto | Programadores necessários | Capital necessário | VPL estimado |
|---------|---------------------------|--------------------|--------------|
| 1       | 7                         | $250               | $650         |
| 2       | 6                         | $175               | $550         |
| 3       | 9                         | $300               | $600         |
| 4       | 5                         | $150               | $450         |
| 5       | 6                         | $145               | $375         |
| 6       | 4                         | $160               | $525         |
| 7       | 8                         | $325               | $750         |


a) Formule um Modelo PLI para esse Problema

b) Crie um Modelo de Planilha e resolva-o

c) Qual é a Solução Ótima

## Resolução

1. Carregamento dos dados: Os dados são carregados a partir do CSV projetos.csv.
2. Criação do solver: Um solver SCIP é criado para resolver o problema de otimização.
3. Variáveis de decisão: Criadas para cada projeto, indicando se o projeto é selecionado ou não.
Restrições:
4. O orçamento total não pode exceder $950.000.
5. O número total de programadores não pode exceder 20.
6. Os projetos 2 e 6 não podem ser selecionados simultaneamente.

**Função objetivo:** Maximizar o VPL estimado dos projetos selecionados.
Resolução e saída: O problema é resolvido e os resultados são exibidos, incluindo os projetos selecionados e os totais de VPL, orçamento e programadores.

## Modelagem Matemática

### Definições
Seja:
- $n$ o número total de projetos, onde $n = 7$.
- $x_i$ uma variável binária que indica se o projeto $i$ é selecionado (1) ou não (0), para $i = 1, 2, \ldots, 7$.

### Parâmetros
- $P_i$ o número de programadores necessários para o projeto $i$.
- $C_i$ o capital necessário para o projeto $i$ (em milhares de dólares).
- $V_i$ o VPL estimado para o projeto $i$ (em milhares de dólares).

### Conjuntos
- $i \in \{1, 2, 3, 4, 5, 6, 7\}$

### Função Objetivo
Maximizar o VPL total dos projetos selecionados:
$$
\text{Maximizar} \quad Z = \sum_{i=1}^{n} V_i \cdot x_i
$$

### Restrições
1. **Limitação do orçamento**:
$$
\sum_{i=1}^{n} C_i \cdot x_i \leq 950
$$

2. **Limitação do número de programadores**:
$$
\sum_{i=1}^{n} P_i \cdot x_i \leq 20
$$

3. **Exclusividade dos projetos 2 e 6**:
$$
x_2 + x_6 \leq 1
$$

## Resolução do Solver
- O solver foi criado usando OR-Tools. Está no solver.py, nesse mesmo repositório. E segue abaixo o print do resultado.

```
Solução ótima encontrada:
Projeto 1 selecionado.
Projeto 6 selecionado.
Projeto 7 selecionado.
VLP Total: 1925.0
Budget Total: 735.0
Programadores: 19
```

