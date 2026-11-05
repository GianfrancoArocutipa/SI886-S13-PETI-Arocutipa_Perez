# 07_portafolio/PF06_dependencias.py
# Organización: AGROEXPORTADORA VALLE VIEJO S.A.C. (EMPRESA-01)
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyArrowPatch

try:
    import networkx as nx
except ImportError:
    # Implementación compatible de respaldo cuando networkx no está preinstalado en el entorno local
    class _SimpleDiGraph:
        def __init__(self):
            self.nodes = []
            self._succ = {}
            self._pred = {}
        def add_nodes_from(self, nodes):
            for n in nodes:
                if n not in self._succ:
                    self.nodes.append(n)
                    self._succ[n] = []
                    self._pred[n] = []
        def add_edges_from(self, edges):
            for u, v in edges:
                self.add_nodes_from([u, v])
                if v not in self._succ[u]:
                    self._succ[u].append(v)
                if u not in self._pred[v]:
                    self._pred[v].append(u)
        def out_degree(self):
            return [(n, len(self._succ[n])) for n in self.nodes]
        def in_degree(self, n=None):
            if n is not None:
                return len(self._pred[n])
            return [(k, len(self._pred[k])) for k in self.nodes]
        def successors(self, n):
            return self._succ[n]
        def predecessors(self, n):
            return self._pred[n]
        def edges(self):
            res = []
            for u in self.nodes:
                for v in self._succ[u]:
                    res.append((u, v))
            return res

    class _NXFallback:
        DiGraph = _SimpleDiGraph
        class NetworkXUnfeasible(Exception):
            pass
        @staticmethod
        def topological_generations(G):
            in_deg = {n: G.in_degree(n) for n in G.nodes}
            actual = [n for n in G.nodes if in_deg[n] == 0]
            visitados = 0
            while actual:
                yield actual
                visitados += len(actual)
                sig = []
                for u in actual:
                    for v in G.successors(u):
                        in_deg[v] -= 1
                        if in_deg[v] == 0:
                            sig.append(v)
                actual = sig
            if visitados != len(G.nodes):
                raise _NXFallback.NetworkXUnfeasible("Ciclo detectado")
        @staticmethod
        def topological_sort(G):
            for gen in _NXFallback.topological_generations(G):
                for n in gen:
                    yield n
        @staticmethod
        def draw(G, pos, with_labels=True, node_color="#16285C", font_color="white",
                 font_weight="bold", node_size=2100, font_size=9.5, arrows=True,
                 arrowsize=20, edge_color="#64748B", width=1.8, connectionstyle="arc3,rad=0.08"):
            ax = plt.gca()
            for u, v in G.edges():
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                arr = FancyArrowPatch(
                    (x1, y1), (x2, y2),
                    connectionstyle=connectionstyle,
                    arrowstyle="-|>",
                    mutation_scale=arrowsize,
                    color=edge_color,
                    linewidth=width,
                    shrinkA=22,
                    shrinkB=22,
                    zorder=1,
                )
                ax.add_patch(arr)
            xs = [pos[n][0] for n in G.nodes]
            ys = [pos[n][1] for n in G.nodes]
            ax.scatter(xs, ys, s=node_size, c=node_color, zorder=3, edgecolors="white", linewidths=1.5)
            if with_labels:
                for n in G.nodes:
                    x, y = pos[n]
                    ax.text(x, y, n, color=font_color, fontweight=font_weight,
                            fontsize=font_size, ha="center", va="center", zorder=4)
            ax.margins(0.18)
            ax.axis("off")
    nx = _NXFallback()

os.makedirs("../graficos", exist_ok=True)

# Tuplas (proyecto_dependiente, depende_de_habilitador)
DEP = [
 ("PR-04", "PR-03"), ("PR-04", "PR-01"),
 ("PR-05", "PR-03"), ("PR-05", "PR-01"),
 ("PR-06", "PR-01"), ("PR-06", "PR-03"),
 ("PR-09", "PR-01"), ("PR-09", "PR-03"),
 ("PR-10", "PR-07"),
 ("PR-12", "PR-08"),
 ("PR-13", "PR-03"),
]

p = pd.read_csv("PF01_portafolio_candidatos.csv")
G = nx.DiGraph()
G.add_nodes_from(p.codigo)
# Arista dirigida: habilitador -> dependiente
G.add_edges_from([(b, a) for a, b in DEP])

print("=== ORDEN TOPOLÓGICO (SECUENCIA OBLIGADA — AGROEXPORTADORA VALLE VIEJO S.A.C.) ===")
try:
    orden = list(nx.topological_sort(G))
    print(" -> ".join(orden))
except nx.NetworkXUnfeasible:
    print("ALERTA: Existe un ciclo de dependencias: revisar el modelo")

print("\n=== PROYECTOS HABILITADORES (MAYOR GRADO DE SALIDA) ===")
for n, g in sorted(G.out_degree(), key=lambda x: (-x[1], x[0])):
    if g > 0:
        dependientes = sorted(list(G.successors(n)))
        print(f"  {n}: habilita {g} proyecto(s) ({', '.join(dependientes)}) -> prioridad estructural")

print("\n=== PROYECTOS SIN DEPENDENCIAS PREVIAS (PUEDEN INICIAR EN OLA 1) ===")
sin_dep = [n for n in G.nodes if G.in_degree(n) == 0]
print("  " + ", ".join(sin_dep))

print("\n=== PROYECTOS DEPENDIENTES (REQUIEREN HABILITADORES PREVIOS) ===")
for n in G.nodes:
    if G.in_degree(n) > 0:
        reqs = sorted(list(G.predecessors(n)))
        print(f"  {n} requiere haber completado: {', '.join(reqs)}")

# Layout por capas (generaciones topológicas) para máxima claridad visual
capas = list(nx.topological_generations(G))
pos = {}
for idx_capa, nodos_capa in enumerate(capas):
    nodos_ord = sorted(nodos_capa)
    total = len(nodos_ord)
    for i, nodo in enumerate(nodos_ord):
        pos[nodo] = (idx_capa * 3.0, (total - 1) / 2.0 - i)

plt.figure(figsize=(11, 7.5))
colores_nodos = []
for n in G.nodes:
    out_d = dict(G.out_degree())[n]
    if out_d >= 3:
        colores_nodos.append("#F59E0B")  # Habilitador estructural clave
    elif out_d >= 1:
        colores_nodos.append("#0EA5E9")  # Habilitador secundario
    elif G.in_degree(n) == 0:
        colores_nodos.append("#10B981")  # Independiente (Ola 1)
    else:
        colores_nodos.append("#16285C")  # Proyecto dependiente (Ola 2)

nx.draw(
    G, pos, with_labels=True, node_color=colores_nodos, font_color="white",
    font_weight="bold", node_size=2100, font_size=9.5, arrows=True,
    arrowsize=20, edge_color="#64748B", width=1.8, connectionstyle="arc3,rad=0.08"
)

leyenda = [
    Patch(facecolor="#F59E0B", label="Habilitador estructural clave (PR-01, PR-03)"),
    Patch(facecolor="#0EA5E9", label="Habilitador operativo (PR-07, PR-08)"),
    Patch(facecolor="#10B981", label="Sin dependencias previas (PR-02, PR-11)"),
    Patch(facecolor="#16285C", label="Dependiente de habilitadores (Ola 2)"),
]
plt.legend(handles=leyenda, loc="lower center", bbox_to_anchor=(0.5, -0.10), ncol=2, fontsize=8.5)
plt.title("Mapa de dependencias del portafolio (Arista: Habilitador -> Dependiente)\nAgroexportadora Valle Viejo S.A.C.", fontweight="bold", pad=12)
plt.tight_layout()
plt.savefig("../graficos/PF_dependencias.png", dpi=150, bbox_inches="tight")
print("\nGráfico generado: ../graficos/PF_dependencias.png")
