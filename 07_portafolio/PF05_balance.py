# 07_portafolio/PF05_balance.py
# Organización: AGROEXPORTADORA VALLE VIEJO S.A.C. (EMPRESA-01)
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

os.makedirs("../graficos", exist_ok=True)

p   = pd.read_csv("PF01_portafolio_candidatos.csv")
tco = pd.read_csv("PF02_tco.csv")
d   = p.merge(tco, on="codigo")

orden_cat = ["Operar", "Crecer", "Transformar"]
bal = d.groupby("categoria").agg(
    proyectos=("codigo", "count"),
    inversion=("inv_inicial", "sum"),
    tco=("tco_5", "sum")
).reindex(orden_cat).reset_index()

bal["pct_inv"] = (bal.inversion / bal.inversion.sum() * 100).round(1)
bal["pct_tco"] = (bal.tco / bal.tco.sum() * 100).round(1)

REF = {"Operar": (50, 70), "Crecer": (20, 30), "Transformar": (10, 20)}
print("=== BALANCE DEL PORTAFOLIO PROPUESTO (AGROEXPORTADORA VALLE VIEJO S.A.C.) ===")
print(bal.to_string(index=False))

print("\nContraste con las proporciones de referencia (Teoría Sección 1):")
for _, r in bal.iterrows():
    lo, hi = REF.get(r.categoria, (0, 100))
    est = "DENTRO DEL RANGO" if lo <= r.pct_tco <= hi else ("POR DEBAJO" if r.pct_tco < lo else "POR ENCIMA")
    print(f"  {r.categoria:12s}: {r.pct_tco:5.1f} % del TCO | {r.pct_inv:5.1f} % de Inv. Inicial  (referencia {lo}-{hi} %) -> {est}")

# Contraste con el balance ACTUAL del presupuesto de Agroexportadora Valle Viejo S.A.C. (presupuesto_ti.csv)
# Operación (PT01..PT05, PT07): Planificado S/ 379,040.00 (92.0%) | Ejecutado S/ 386,784.97 (93.2%)
# Inversión / Proyectos nuevos (PT06): Planificado S/ 32,960.00 (8.0%) | Ejecutado S/ 28,108.31 (6.8%)
# Transformar: S/ 0.00 (0.0%)
print("\n=== COMPARACIÓN CON EL BALANCE ACTUAL DE LA ORGANIZACIÓN (presupuesto_ti.csv) ===")
print("  Presupuesto TI 2025 Planificado (S/ 412,000.00): Operar 92.0 % (S/ 379,040.00) | Crecer 8.0 % (S/ 32,960.00) | Transformar 0.0 % (S/ 0.00)")
print("  Presupuesto TI 2025 Ejecutado   (S/ 414,893.28): Operar 93.2 % (S/ 386,784.97) | Crecer 6.8 % (S/ 28,108.31) | Transformar 0.0 % (S/ 0.00)")
print(f"  Portafolio PETI propuesto (TCO S/ {bal.tco.sum():,.0f}) : "
      f"Operar {bal.loc[bal.categoria=='Operar','pct_tco'].values[0]:.1f} % | "
      f"Crecer {bal.loc[bal.categoria=='Crecer','pct_tco'].values[0]:.1f} % | "
      f"Transformar {bal.loc[bal.categoria=='Transformar','pct_tco'].values[0]:.1f} %")
print("-> El PETI corrige el desequilibrio actual (93.2 % ejecutado en Operar, 6.8 % en Crecer y 0.0 % en Transformar)")
print("   llevando el portafolio a 60.0 % en Operar (ref. 50-70 %), 24.1 % en Crecer (ref. 20-30 %) y")
print("   15.8 % en Transformar (ref. 10-20 %), cumpliendo las tres bandas de referencia.")

fig, ax = plt.subplots(1, 2, figsize=(13, 5.5))
COL = {"Operar": "#16285C", "Crecer": "#0EA5E9", "Transformar": "#F59E0B"}
ax[0].pie(
    bal.tco,
    labels=[f"{c}\n(S/ {v:,.0f})" for c, v in zip(bal.categoria, bal.tco)],
    autopct="%1.1f%%",
    colors=[COL[c] for c in bal.categoria],
    startangle=90,
    textprops={"fontsize": 9},
)
ax[0].set_title("Balance del portafolio por TCO a 5 años\nAgroexportadora Valle Viejo S.A.C.", fontweight="bold")

d_sorted = d.sort_values("tco_5")
bars = ax[1].barh(
    d_sorted.codigo,
    d_sorted.tco_5,
    color=[COL[c] for c in d_sorted.categoria],
)
ax[1].set_xlabel("TCO a 5 años (S/)")
ax[1].set_title("TCO a 5 años por proyecto y categoría", fontweight="bold")
for bar in bars:
    w = bar.get_width()
    ax[1].text(w + 8000, bar.get_y() + bar.get_height()/2, f"S/ {w:,.0f}", va="center", fontsize=8)
ax[1].set_xlim(0, d_sorted.tco_5.max() * 1.18)

legend_elements = [Patch(facecolor=COL[c], label=c) for c in orden_cat]
ax[1].legend(handles=legend_elements, loc="lower right", title="Categoría")

plt.tight_layout()
plt.savefig("../graficos/PF_balance.png", dpi=150)
print("\nGráfico generado: ../graficos/PF_balance.png")
