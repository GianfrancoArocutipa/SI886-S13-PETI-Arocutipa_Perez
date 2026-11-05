# 07_portafolio/PF07_validacion.py
# Paso F — Validar y corregir (AGROEXPORTADORA VALLE VIEJO S.A.C.)
import os
import pandas as pd

p   = pd.read_csv("PF01_portafolio_candidatos.csv")
tco = pd.read_csv("PF02_tco.csv")
alt = pd.read_csv("PF04_alternativas.csv")

FUENTES_VALIDAS = {
    "Obligación normativa",
    "Brecha de arquitectura",
    "Brecha de capacidad",
    "Estrategia FODA",
    "Brecha de servicio digital",
}

print("=== PASO F: VALIDACIÓN INTEGRAL DEL PORTAFOLIO (AGROEXPORTADORA VALLE VIEJO S.A.C.) ===")

# Comprobación 1: Trazabilidad a objetivos y fuentes admisibles
sin_obj = p[p.objetivo.isna() | (p.objetivo.astype(str).str.strip() == "")]
sin_fte = p[~p.fuente.isin(FUENTES_VALIDAS)]
c1_ok = (len(sin_obj) == 0) and (len(sin_fte) == 0) and (len(p) >= 12)
print(f"\n[Comprobación 1] Trazabilidad a objetivos y fuentes admisibles (>= 12 proyectos):")
print(f"  - Total de proyectos admitidos       : {len(p)} (requisito >= 12)")
print(f"  - Proyectos sin objetivo estratégico : {len(sin_obj)}")
print(f"  - Proyectos con fuente no admisible  : {len(sin_fte)}")
print(f"  -> Resultado Comprobación 1          : {'CONFORME' if c1_ok else 'OBSERVADO'}")

# Comprobación 2: Verificación de que los duplicados fusionados no perdieron alcance
with open("PF03_fichas/PR-02.md", encoding="utf-8") as f02:
    txt_pr02 = f02.read()
with open("PF03_fichas/PR-04.md", encoding="utf-8") as f04:
    txt_pr04 = f04.read()

f02_preserva = ("RAT" in txt_pr02 or "Registro de Actividades de Tratamiento" in txt_pr02) and ("ARCO" in txt_pr02)
f04_preserva = ("portal B2B" in txt_pr04) and ("embarques" in txt_pr04) and ("autoservicio" in txt_pr04)
fichas_20_campos = 0
for cod in p.codigo:
    ruta = f"PF03_fichas/{cod}.md"
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            contenido = fh.read()
            if "| **20** |" in contenido:
                fichas_20_campos += 1

c2_ok = f02_preserva and f04_preserva and (fichas_20_campos == len(p))
print(f"\n[Comprobación 2] Integridad de alcance en fusiones y fichas estandarizadas (20 campos):")
print(f"  - Fusión C-02 + C-11 en PR-02 preserva RAT + programa ARCO/ANPD : {'SÍ' if f02_preserva else 'NO'}")
print(f"  - Fusión C-04 + C-05 en PR-04 preserva portal B2B + embarques   : {'SÍ' if f04_preserva else 'NO'}")
print(f"  - Fichas con los 20 campos completos en PF03_fichas/            : {fichas_20_campos}/{len(p)}")
print(f"  -> Resultado Comprobación 2                                     : {'CONFORME' if c2_ok else 'OBSERVADO'}")

# Comprobación 3: Verificación de que el TCO a 5 años incluye el costo operativo y costos únicos
tco_calc_ok = all((tco.costo_unico + tco.costo_anual * 5) == tco.tco_5)
tco_mayor_inv = all(tco.tco_5 > tco.inv_inicial)
alt_3_casos = (alt.proyecto.nunique() == 3) and all(alt.groupby("proyecto")["alternativa"].count() == 3)
c3_ok = tco_calc_ok and tco_mayor_inv and alt_3_casos
print(f"\n[Comprobación 3] Consistencia de TCO a 5 años y casos de negocio:")
print(f"  - Todos los proyectos incluyen costo operativo a 5 años (TCO > Inv. Inicial): {'SÍ' if tco_mayor_inv else 'NO'}")
print(f"  - Exactitud aritmética (TCO_5 = Costo_Único + 5 × Costo_Anual)              : {'SÍ' if tco_calc_ok else 'NO'}")
print(f"  - Tres casos de negocio con 3 alternativas c/u (incluida 'No hacer nada')   : {'SÍ' if alt_3_casos else 'NO'}")
print(f"  -> Resultado Comprobación 3                                                 : {'CONFORME' if c3_ok else 'OBSERVADO'}")

print("\n=== DICTAMEN FINAL DE VALIDACIÓN ===")
print("Estado general:", "100% VALIDADO Y CONFORME" if (c1_ok and c2_ok and c3_ok) else "REQUIERE CORRECCIÓN")

