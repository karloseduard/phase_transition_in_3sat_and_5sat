from pysat.solvers import Glucose4
import random
import numpy as np
import matplotlib.pyplot as plt

k = 3
n_valores = [50,100,150,200]
instancia_numero = 30
a_valores = np.arange(1.0, 10.1, 0.1)

plt.figure(figsize=(10, 6))
ax1 = plt.gca()
ax2 = ax1.twinx()

for n in n_valores:
    prob = []
    media_de_tempo = []

    for a in a_valores:
        total_tempo = 0.0
        total_sat = 0

        for _ in range(instancia_numero):
            solver = Glucose4(use_timer=True)
            m = int(a * n)
            clauses = [[random.choice([-1, 1]) * var for var in random.sample(range(1, n + 1), k)] for _ in range(m)]

            for clause in clauses:
                solver.add_clause(clause)

            if solver.solve():
                total_sat += 1
            total_tempo += solver.time()

        probabilidade = total_sat / instancia_numero
        media_tempo = total_tempo / instancia_numero

        prob.append(probabilidade)
        media_de_tempo.append(media_tempo)


    ax1.plot(a_valores, prob, label=f"n = {n}")


    ax2.plot(a_valores, media_de_tempo, linestyle="dashed", alpha=0.7, label=f"Tempo médio (n = {n})")


    max_tempo = max(media_de_tempo)
    max_tempo_index = media_de_tempo.index(max_tempo)
    max_a = a_valores[max_tempo_index]

ax2.axvline(x=max_a, color='black', linestyle=':', linewidth=1.5, label=f'Pico tempo (n={n}, α={max_a:.2f})')


ax1.set_xlabel("Alpha (a)")
ax1.set_ylabel("Probabilidade de Satisfatibilidade")
ax2.set_ylabel("Tempo Médio (s)")

ax1.set_xlim(0, 10)
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.title("Probabilidade de Satisfatibilidade do 3-SAT e Tempo Médio")
plt.grid(True)
plt.show()
