import pandas as pd
import matplotlib.pyplot as plt

# Leggi i dati dal CSV
# Assicurati che il nome del file sia lo stesso che hai generato (nqueens_experiments.csv)
df = pd.read_csv('nqueens_experiments.csv')

# --- GRAFICO 1: Confronto Tempi (Time vs N) ---
plt.figure(figsize=(10, 6))

# Filtra i dati per A* e CSP
astar_data = df[df['Algorithm'] == 'A*']
csp_data = df[df['Algorithm'] == 'CSP']

# Disegna le linee
plt.plot(astar_data['N'], astar_data['Time(s)'], marker='o', label='A* Search', color='blue')
plt.plot(csp_data['N'], csp_data['Time(s)'], marker='s', label='CSP Solver', color='green')

plt.title('Execution Time Comparison: A* vs CSP')
plt.xlabel('N (Board Size)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)

# Salva il grafico come immagine
plt.savefig('time_plot.png')
print("Grafico 1 salvato come 'time_plot.png'")
plt.show() # Mostra a video


# --- GRAFICO 2: Nodi Espansi (Solo A*) ---
plt.figure(figsize=(10, 6))

# Prendiamo solo A* (CSP non espande nodi nello stesso modo)
plt.plot(astar_data['N'], astar_data['Nodes Expanded'], marker='o', color='red', linestyle='--')

plt.title('A* Search: Nodes Expanded vs Problem Size')
plt.xlabel('N (Board Size)')
plt.ylabel('Nodes Expanded')
plt.grid(True)

# Annotazione dei valori sui punti per chiarezza
for x, y in zip(astar_data['N'], astar_data['Nodes Expanded']):
    plt.text(x, y, str(y), ha='right', va='bottom')

# Salva il grafico
plt.savefig('nodes_plot.png')
print("Grafico 2 salvato come 'nodes_plot.png'")
plt.show()