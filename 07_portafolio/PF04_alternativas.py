# 07_portafolio/PF04_alternativas.py
# Organización: AGROEXPORTADORA VALLE VIEJO S.A.C. (EMPRESA-01)
import pandas as pd

AÑOS = 5

# Tres proyectos de mayor TCO en Agroexportadora Valle Viejo S.A.C.:
# 1. PR-09 (Renovación y consolidación del ERP agroindustrial) -> TCO 5 años: S/ 780,500
# 2. PR-03 (Capa de integración de servicios API Gateway)      -> TCO 5 años: S/ 459,200
# 3. PR-04 (Rediseño del portal B2B y consulta de embarques)   -> TCO 5 años: S/ 425,000

ALT = pd.DataFrame([
 # proyecto, alternativa, inv_inicial, otros_unicos, costo_anual, beneficio_anual, descripcion
 ("PR-09", "A. No hacer nada", 0, 0, 0, -180000,
  "Se mantiene el ERP fragmentado tras INV01 (S/ 260,819.96 sin acta ni medición): "
  "pérdida de soporte, sobrecosto en soporte reactivo (PT02 +17.9%) y pagos dispersos "
  "a proveedores (pagos.csv: S/ 1,475,059.22/año). Costo anual de inacción: S/ 180,000."),
 ("PR-09", "B. Consolidar y migrar a versión soportada del ERP actual (Recomendada)", 145000, 85000, 110100, 235000,
  "Aprovecha la base de INV01 corrigiendo brechas de costeo agrícola por lote, "
  "capacitación, migración e integración vía API (PR-03); reduce gasto externo disperso."),
 ("PR-09", "C. Reemplazar por un nuevo ERP agroindustrial Tier-1", 260000, 110000, 138000, 250000,
  "Elimina dependencia del proveedor actual, pero exige alta inversión inicial, "
  "18 meses de despliegue y alto riesgo operativo en plena campaña de exportación."),

 ("PR-03", "A. No hacer nada", 0, 0, 0, -112000,
  "Sistemas de campo, planta de empaque, cámaras de frío y ERP siguen aislados; "
  "doble digitación de guías y lotes, errores en documentación SENASA/Aduanas y "
  "bloqueo estructural de 5 proyectos dependientes (PR-04, PR-05, PR-06, PR-09, PR-13)."),
 ("PR-03", "B. Capa de integración API Gateway gestionada y conectores estándar (Recomendada)", 78000, 23000, 71640, 138000,
  "Arquitectura desacoplada basada en estándares REST/eventos; habilita 5 proyectos "
  "del portafolio y elimina integraciones ad-hoc contratadas a terceros."),
 ("PR-03", "C. Suite iPaaS empresarial propietaria", 155000, 35000, 104000, 148000,
  "Menor esfuerzo de configuración inicial pero alto costo recurrente en suscripciones "
  "en dólares y elevado costo de salida (vendor lock-in)."),

 ("PR-04", "A. No hacer nada", 0, 0, 0, -95000,
  "El portal de autoservicio INV03 (S/ 224,964.21 ejecutados en 2024 con +24.5% de "
  "desviación) continúa con fallas recurrentes, baja adopción y atención manual por "
  "correo/teléfono del estado de contenedores y certificados de exportación."),
 ("PR-04", "B. Rediseño del portal existente sobre API (PR-03) + trazabilidad de embarques (Recomendada)", 92000, 36000, 59400, 145000,
  "Rescata la inversión previa INV03 desacoplándola de la base del ERP mediante PR-03 "
  "e incorpora consulta de estado de embarques y lotes (fusión C-04 + C-05) en 2 etapas."),
 ("PR-04", "C. Nueva plataforma SaaS B2B de comercio exterior desde cero", 210000, 45000, 84000, 165000,
  "Desecha por completo el activo INV03 (S/ 224,964.21); duplica el costo inicial "
  "y eleva la carga de licencias anuales."),
], columns=["proyecto", "alternativa", "inv_inicial", "otros_unicos", "costo_anual", "beneficio_anual", "descripcion"])

ALT["costo_unico"] = ALT.inv_inicial + ALT.otros_unicos
ALT["costo_5"]     = ALT.costo_unico + ALT.costo_anual * AÑOS
ALT["beneficio_5"] = ALT.beneficio_anual * AÑOS
ALT["neto_5"]      = ALT.beneficio_5 - ALT.costo_5
ALT["retorno"]     = (ALT.neto_5 / ALT.costo_5.replace(0, float("nan")) * 100).round(1)

for p, g in ALT.groupby("proyecto", sort=False):
    print(f"\n{'='*100}\nCASO DE NEGOCIO: {p} (AGROEXPORTADORA VALLE VIEJO S.A.C.)")
    print(g[["alternativa", "inv_inicial", "costo_unico", "costo_anual", "costo_5", "beneficio_5", "neto_5", "retorno"]].to_string(index=False))
    mejor = g.loc[g.neto_5.idxmax()]
    print(f"-> Mayor beneficio neto a 5 años: {mejor.alternativa} (Neto: S/ {mejor.neto_5:,.0f} | ROI 5a: {mejor.retorno}%)")
    base = g[g.alternativa.str.startswith("A.")].iloc[0]
    print(f"-> Costo de la inacción a 5 años: S/ {abs(base.beneficio_5):,.0f} (S/ {abs(base.beneficio_anual):,.0f}/año)")

ALT.to_csv("PF04_alternativas.csv", index=False)
