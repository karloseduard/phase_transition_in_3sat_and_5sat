# Transição de Fase no Problema 3-SAT e 5-SAT

Este repositório investiga a transição de fase nos problemas de satisfação booleana (SAT), especificamente para as variantes 3-SAT e 5-SAT. O objetivo é analisar o comportamento do problema à medida que variamos a razão entre o número de cláusulas e o número de variáveis, identificando a região crítica onde a probabilidade de satisfazibilidade muda abruptamente.

## O Problema SAT
O problema SAT consiste em determinar se existe uma atribuição de valores verdadeiros e falsos para as variáveis de uma fórmula booleana de forma que todas as cláusulas sejam satisfeitas. No caso do k-SAT:

- No 3-SAT, cada cláusula contém exatamente três literais.
- No 5-SAT, cada cláusula contém exatamente cinco literais.

A transição de fase ocorre em um valor crítico da razão cláusulas/variáveis, onde a probabilidade de satisfazibilidade cai drasticamente de 1 para 0.

## Conteúdo do Repositório
- **`scripts/`**: Contém os códigos em Python para gerar instâncias aleatórias de 3-SAT e 5-SAT e analisar a satisfazibilidade.
- **`data/`**: Conjuntos de dados com exemplos de instâncias e resultados das simulações.
- **`notebooks/`**: Jupyter Notebooks com visualizações dos experimentos e análises estatísticas.
- **`README.md`**: Este arquivo, explicando o projeto.

## Como Rodar os Experimentos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute os scripts de geração e análise de instâncias:
   ```bash
   python scripts/experimento_3sat.py
   python scripts/experimento_5sat.py
   ```
4. Abra os notebooks para visualizar os resultados:
   ```bash
   jupyter notebook notebooks/analise_3sat_5sat.ipynb
   ```

## Contribuição
Sinta-se à vontade para contribuir com melhorias, novas análises ou otimizações de código. Para isso:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça commit das mudanças (`git commit -m "Adiciona nova análise"`).
4. Envie para o repositório remoto (`git push origin minha-feature`).
5. Abra um Pull Request!

## Referências
- [P versus NP e problemas SAT](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)
- [Transição de fase em problemas SAT](https://www.sciencedirect.com/topics/computer-science/phase-transition)


