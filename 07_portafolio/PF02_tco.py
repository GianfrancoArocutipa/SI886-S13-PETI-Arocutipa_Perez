# 07_portafolio/PF02_tco.py
# Organización: AGROEXPORTADORA VALLE VIEJO S.A.C. (EMPRESA-01)
import pandas as pd

# Estimaciones referenciales calibradas con la línea base de Agroexportadora Valle Viejo S.A.C.:
# - INV01 (Módulo ERP 2025): S/ 260,819.96 ejecutados
# - INV02 (Enlace redundante 2025): S/ 75,773.21 ejecutados (+20.6%)
# - INV03 (Portal autoservicio 2024): S/ 224,964.21 ejecutados (+24.5%)
# - Presupuesto TI 2025: S/ 412,000.00 planificado / S/ 414,893.28 ejecutado
# - Pagos reales en 'Servicio informático' (pagos.csv, 2025): S/ 1,475,059.22 en 1,020 pagos a 71 proveedores

PROYECTOS = pd.DataFrame([
 # codigo, inv_inicial, licencias, infra, soporte_pct, personal,
 # capacitacion, migracion, integracion, costo_salida, meses, incertidumbre, pct_inc
 ("PR-01",  55000,  6000,  3600, .15, 24000,  6000, 12000,  8000,  4500,  6, "±30 %", 0.30),
 ("PR-02",  18000,     0,     0, .10,  9000,  3000,     0,     0,  1500,  3, "±20 %", 0.20),
 ("PR-03",  78000, 12000,  9600, .18, 36000,  8000,     0, 15000,  6500,  8, "±40 %", 0.40),
 ("PR-04",  92000,  8400,  7200, .15, 30000, 12000,  6000, 18000,  7500,  9, "±35 %", 0.35),
 ("PR-05",  34000,  4800,  3600, .15, 12000,  4000,  5000,  9000,  3000,  5, "±30 %", 0.30),
 ("PR-06",  28000,  3600,  2400, .15, 12000,  5000,  3000,  7000,  2500,  4, "±25 %", 0.25),
 ("PR-07",  15000,     0,  1800, .10,  6000,  3000,     0,  2000,  1200,  3, "±20 %", 0.20),
 ("PR-08",  42000,     0,  6000, .12, 12000,  4000,     0,     0,  3500,  4, "±25 %", 0.25),
 ("PR-09", 145000, 24000, 12000, .18, 48000, 20000, 35000, 30000, 18000, 12, "±50 %", 0.50),
 ("PR-10",  22000,     0,     0, .10, 18000,  6000,     0,     0,  1800,  5, "±25 %", 0.25),
 ("PR-11",   6000,     0,     0, .00,  3000,  2000,     0,     0,     0,  2, "±15 %", 0.15),
 ("PR-12",  19000,  2400,  1200, .12,  6000,  3000,     0,  4000,  1500,  3, "±25 %", 0.25),
 ("PR-13",  26000,  3600,  2400, .15,  9000,  5000,  4000,  6000,  2200,  4, "±30 %", 0.30),
], columns=["codigo", "inv_inicial", "licencias", "infra", "soporte_pct", "personal",
            "capacitacion", "migracion", "integracion", "costo_salida", "meses",
            "incertidumbre", "pct_inc"])

AÑOS = 5
P = PROYECTOS.copy()
P["soporte_anual"]    = (P.inv_inicial * P.soporte_pct).round(0)
P["costo_anual"]      = P.licencias + P.infra + P.soporte_anual + P.personal
P["costo_unico"]      = P.inv_inicial + P.capacitacion + P.migracion + P.integracion
P["tco_5"]            = P.costo_unico + P.costo_anual * AÑOS
P["tco_5_con_salida"] = P.tco_5 + P.costo_salida
P["rango_tco_5"]      = P.apply(
    lambda r: f"S/ {r.tco_5*(1-r.pct_inc):,.0f} - S/ {r.tco_5*(1+r.pct_inc):,.0f}", axis=1
)
P["factor_tco"]       = (P.tco_5 / P.inv_inicial).round(2)
P["pct_operativo"]    = ((P.costo_anual * AÑOS) / P.tco_5 * 100).round(1)

P = P.sort_values("tco_5", ascending=False)
P.to_csv("PF02_tco.csv", index=False)

print("=== COSTO TOTAL DE PROPIEDAD A 5 AÑOS (AGROEXPORTADORA VALLE VIEJO S.A.C.) ===")
cols_vista = ["codigo", "inv_inicial", "costo_unico", "costo_anual", "costo_salida",
              "tco_5", "factor_tco", "pct_operativo", "incertidumbre", "rango_tco_5"]
print(P[cols_vista].to_string(index=False))

print(f"\nInversión inicial total        : S/ {P.inv_inicial.sum():,.0f}")
print(f"Costos únicos totales (CapEx+) : S/ {P.costo_unico.sum():,.0f}")
print(f"Costo operativo anual total    : S/ {P.costo_anual.sum():,.0f} / año")
print(f"TCO total a 5 años (base)      : S/ {P.tco_5.sum():,.0f}")
print(f"Costo de salida acumulado      : S/ {P.costo_salida.sum():,.0f}")
print(f"TCO total incluyendo salida    : S/ {P.tco_5_con_salida.sum():,.0f}")
print(f"Factor TCO/inversión inicial   : {P.tco_5.sum()/P.inv_inicial.sum():.2f}x")
print("\n-> El TCO es {:.1f} veces la inversión inicial. Presentar solo la inversión".format(
      P.tco_5.sum()/P.inv_inicial.sum()))
print("   inicial ante la gerencia subestima el compromiso en S/ {:,.0f}.".format(
      P.tco_5.sum()-P.inv_inicial.sum()))
print("-> Además, en Agroexportadora Valle Viejo S.A.C. el gasto real en 'Servicio informático'")
print("   (pagos.csv: S/ 1,475,059.22 en 2025) equivale a {:.1f} veces el costo operativo anual".format(
      1475059.22 / P.costo_anual.sum()))
print("   de todo el nuevo portafolio (S/ {:,.0f}/año), lo que demuestra que ordenar y consolidar".format(
      P.costo_anual.sum()))
print("   proveedores financia ampliamente la operación recurrente del portafolio.")

print("\n=== PROYECTOS CON MAYOR PROPORCIÓN DE COSTO OPERATIVO ===")
print(P.nlargest(4, "pct_operativo")[["codigo", "tco_5", "pct_operativo", "factor_tco"]].to_string(index=False))
print("-> Estos comprometen el presupuesto recurrente durante años: exigen mayor escrutinio.")
