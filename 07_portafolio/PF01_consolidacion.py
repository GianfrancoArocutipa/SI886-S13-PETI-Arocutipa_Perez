# 07_portafolio/PF01_consolidacion.py
# Organización: AGROEXPORTADORA VALLE VIEJO S.A.C. (EMPRESA-01)
import pandas as pd

# 1. Candidatos brutos recolectados desde las secciones previas del PETI y solicitudes de áreas
CANDIDATOS_BRUTOS = pd.DataFrame([
 # codigo, nombre, fuente, seccion_origen, objetivo, categoria
 ("C-01", "Gobierno del dato maestro (lotes agrícolas, productores y clientes)",
  "Brecha de arquitectura", "Sección 5.4.2 PT-01", "OD-02, OD-03", "Transformar"),
 ("C-02", "Registro de actividades de tratamiento de datos (Ley N.º 29733)",
  "Obligación normativa", "Sección 4.1.5", "OD-05", "Operar"),
 ("C-03", "Capa de integración de servicios API (ERP - Planta - Campo - Aduanas)",
  "Brecha de arquitectura", "Sección 5.4.2 PT-02", "OD-01, OD-03", "Operar"),
 ("C-04", "Rediseño y adopción del portal B2B de agroexportación",
  "Brecha de servicio digital", "Sección 6.1.7 S-01", "OD-01", "Crecer"),
 ("C-05", "Consulta de estado de embarque y lotes fitosanitarios en autoservicio",
  "Brecha de servicio digital", "Sección 6.1.7 S-02", "OD-01", "Crecer"),
 ("C-06", "Planificación inteligente de rutas de acopio, cadena de frío y trazabilidad de despacho",
  "Estrategia FODA", "Sección 3.5 E-02", "OD-03", "Transformar"),
 ("C-07", "Tablero de gestión comercial, costos por lote y rentabilidad de exportación",
  "Brecha de arquitectura", "Sección 5.4.2 PT-05", "OD-02", "Crecer"),
 ("C-08", "Mesa de servicio de TI y control centralizado de proveedores informáticos",
  "Brecha de capacidad", "Sección 4.3.5 DSS02", "OD-04", "Operar"),
 ("C-09", "Continuidad de infraestructura, conmutación de enlace redundante y respaldo inmutable",
  "Brecha de capacidad", "Sección 4.3.5 DSS04", "OD-04", "Operar"),
 ("C-10", "Renovación y consolidación de la plataforma del ERP agroindustrial",
  "Estrategia FODA", "Sección 3.5 E-04", "OD-04, OD-03", "Operar"),
 ("C-11", "Programa integral de cumplimiento de datos personales (jornaleros y clientes)",
  "Obligación normativa", "Sección 4.1.5", "OD-05", "Operar"),
 ("C-12", "Gestión del conocimiento y base de datos de configuración (CMDB)",
  "Estrategia FODA", "Sección 3.5 E-07", "OD-06", "Operar"),
 ("C-13", "Comité de gobierno e inversiones de TI (casos de negocio y actas de beneficio)",
  "Brecha de capacidad", "Sección 4.3.5 EDM01, APO05, EDM02", "OD-02, OD-04", "Operar"),
 ("C-14", "Instrumentación de monitoreo y disponibilidad (cámaras de frío, enlace y ERP)",
  "Brecha de capacidad", "Sección 4.3.5 DSS01", "OD-04", "Operar"),
 ("C-15", "Autoservicio digital de trabajadores de campo y planta (boletas, destajo y vacaciones)",
  "Brecha de servicio digital", "Sección 6.1.7 S-06, S-07", "OD-01, OD-05", "Crecer"),
 ("C-16", "Adquisición de software departamental aislado por pedido verbal de área usuaria",
  "Solicitud verbal de área usuaria", "Sin sección (vicio detectado en INV01/INV03)", "OD-04", "Operar"),
 ("C-17", "Remodelación visual de boletín interno sin indicador asociado",
  "Brecha de servicio digital", "Sección 6.1.7", "", "Operar"),
], columns=["codigo", "nombre", "fuente", "seccion_origen", "objetivo", "categoria"])

# Las cinco fuentes admisibles según Sección 1 de la Teoría y Sección 1.2 del Taller
FUENTES_VALIDAS = {
    "Obligación normativa",
    "Brecha de arquitectura",
    "Brecha de capacidad",
    "Estrategia FODA",
    "Brecha de servicio digital",
}

print("=== 1. CONTROL DE ADMISIÓN (AGROEXPORTADORA VALLE VIEJO S.A.C.) ===")
print(f"Candidatos brutos recibidos: {len(CANDIDATOS_BRUTOS)}")

inv = CANDIDATOS_BRUTOS[~CANDIDATOS_BRUTOS.fuente.isin(FUENTES_VALIDAS)]
print(f"Candidatos sin fuente admisible: {len(inv)} -> se retiran: {list(inv.codigo)}")
for _, r in inv.iterrows():
    print(f"  - Retirado {r.codigo} ({r.nombre}): fuente '{r.fuente}' no pertenece a las 5 fuentes admisibles.")

sin_obj = CANDIDATOS_BRUTOS[
    CANDIDATOS_BRUTOS.fuente.isin(FUENTES_VALIDAS)
    & (CANDIDATOS_BRUTOS.objetivo.isna() | (CANDIDATOS_BRUTOS.objetivo.astype(str).str.strip() == ""))
]
print(f"Candidatos sin objetivo asociado: {len(sin_obj)} -> se retiran: {list(sin_obj.codigo)}")
for _, r in sin_obj.iterrows():
    print(f"  - Retirado {r.codigo} ({r.nombre}): carece de objetivo estratégico en la Sección 6.2.")

admitidos = CANDIDATOS_BRUTOS[
    CANDIDATOS_BRUTOS.fuente.isin(FUENTES_VALIDAS)
    & CANDIDATOS_BRUTOS.objetivo.notna()
    & (CANDIDATOS_BRUTOS.objetivo.astype(str).str.strip() != "")
].copy()

print("\n=== 2. DEPURACIÓN Y FUSIÓN DE DUPLICADOS ===")
FUSIONES = [
    ("C-05", "C-04",
     "C-05 (Consulta de estado de embarque y lotes fitosanitarios) se incorpora como entregable "
     "del portal B2B en C-04 (Sección 6.1.7 S-01, S-02), corrigiendo de forma unificada el Portal "
     "de autoservicio INV03 (S/ 224,964.21 ejecutados en 2024 sin medición de beneficios)."),
    ("C-11", "C-02",
     "C-11 (Programa de cumplimiento de datos personales) y C-02 (Registro de actividades de "
     "tratamiento) responden a la misma obligación legal (Ley N.º 29733 y D.S. 016-2024-JUS, "
     "Sección 4.1.5, OD-05); se fusionan en un solo proyecto normativo integral."),
]
for orig, dest, razon in FUSIONES:
    print(f"  - Fusión {orig} -> {dest}: {razon}")

# Aplicamos las fusiones preservando todo el alcance en el candidato destino
admitidos.loc[admitidos.codigo == "C-02", "nombre"] = (
    "Programa de cumplimiento de datos personales y Registro de Actividades de Tratamiento (RAT)"
)
admitidos.loc[admitidos.codigo == "C-04", "nombre"] = (
    "Rediseño del portal B2B de agroexportación y consulta de embarques en autoservicio"
)
admitidos.loc[admitidos.codigo == "C-04", "seccion_origen"] = "Sección 6.1.7 S-01, S-02"

p = admitidos[~admitidos.codigo.isin(["C-05", "C-11"])].copy().reset_index(drop=True)
p["candidato_origen"] = p["codigo"].replace({"C-02": "C-02 + C-11", "C-04": "C-04 + C-05"})
p["codigo"] = [f"PR-{i+1:02d}" for i in range(len(p))]

p.to_csv("PF01_portafolio_candidatos.csv", index=False)

print(f"\nProyectos admitidos y depurados en el portafolio final: {len(p)}")
print("\n=== TABLA DEL PORTAFOLIO DEPURADO ===")
print(p[["codigo", "candidato_origen", "nombre", "fuente", "seccion_origen", "objetivo", "categoria"]].to_string(index=False))

print("\nPor fuente admisible:\n", p.fuente.value_counts().to_string())
print("\nPor categoría:\n", p.categoria.value_counts().to_string())

print("\n=== 3. COBERTURA DE OBJETIVOS ESTRATÉGICOS (SECCIÓN 6.2) ===")
obj = p.objetivo.str.split(", ").explode().value_counts().sort_index()
print(obj.to_string())
OBJETIVOS_SECCION_6_2 = {"OD-01", "OD-02", "OD-03", "OD-04", "OD-05", "OD-06"}
ausentes = OBJETIVOS_SECCION_6_2 - set(obj.index)
print(f"-> Objetivos de la Sección 6.2 sin proyecto asociado: {len(ausentes)} ({'Ninguno, 100% cubiertos' if not ausentes else ausentes})")
