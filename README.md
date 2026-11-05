# Semana 13 · Construcción del Portafolio de Proyectos (Sección 7.1 del PETI)

**Curso:** SI-886 · Planeamiento Estratégico de TI — Universidad Privada de Tacna (UPT)  
**Organización analizada:** **Agroexportadora Valle Viejo S.A.C.** (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Integrantes:**  
- **PEREZ PERALTA, FABRIZIO SALVADOR ELIAS** · `2023077476`  
- **AROCUTIPA AROCUTIPA, GIANFRANCO** · `2023076790`  

**Docente:** Dr. Oscar Juan Jimenez Flores  
**Informe final:** [`SI886-S13-TALLER-Arocutipa_Perez.docx`](SI886-S13-TALLER-Arocutipa_Perez.docx)  
**Etiquetas de versión:** `v0.13` · `taller-13`  

---

## 1. ¿Qué encontramos en la empresa? (Diagnóstico simple)

Al revisar los 4 archivos entregados por **Agroexportadora Valle Viejo S.A.C.**, encontramos tres problemas principales que este portafolio resuelve:

1. **Inversiones pasadas sin sustento ni medición (`expedientes-de-inversion.md` e `inversiones_cerradas.csv`):**  
   Entre 2024 y 2025 la empresa gastó **S/ 561,557.38** en 3 proyectos (`INV01` Módulo ERP por S/ 260,820; `INV02` Enlace redundante por S/ 75,773 con **+20.6 %** de sobrecosto; e `INV03` Portal de autoservicio por S/ 224,964 con **+24.5 %** de sobrecosto). Los tres se hicieron solo por pedidos verbales, sin comparar alternativas, sin acta de conformidad y **nunca se midió si dieron resultado**.
2. **Presupuesto estancado en mantenimiento (`presupuesto_ti.csv`):**  
   De los **S/ 414,893.28** ejecutados en el presupuesto de TI de 2025, el **93.2 %** se fue en mantener lo que ya existe (**Operar**), solo el **6.8 %** en proyectos nuevos (**Crecer**) y **0 %** en innovar (**Transformar**).
3. **Gasto informático oculto en pagos sueltos (`pagos.csv`):**  
   Aunque el presupuesto oficial de TI es de S/ 412,000, en la contabilidad (`pagos.csv`) aparecen **1,020 pagos por `Servicio informático` a 71 proveedores que suman S/ 1,475,059.22** (incluyendo 18 pagos por S/ 48,144 donde la misma persona registró y aprobó el pago). Es decir, se gasta casi 4 veces más por fuera del presupuesto en parches y servicios sin control.

---

## 2. Resumen de lo realizado en el Taller (Pasos A – G)

| Paso | Qué se hizo | Resultado principal | Archivos en el repositorio |
|---|---|---|---|
| **Paso A** | Se evaluaron 17 propuestas iniciales, se eliminaron 2 sin sustento (`C-16` por ser pedido verbal y `C-17` por no tener objetivo) y se unieron 2 duplicadas (`C-05` en `C-04` y `C-11` en `C-02`). | **13 proyectos aprobados (`PR-01` a `PR-13`)** que cubren los 6 objetivos (`OD-01` a `OD-06`). | [`PF01_consolidacion.py`](07_portafolio/PF01_consolidacion.py) · [`PF01_portafolio_candidatos.csv`](07_portafolio/PF01_portafolio_candidatos.csv) |
| **Paso B** | Se crearon las **13 fichas de 20 campos** y se calculó el costo real a 5 años (**TCO**), sumando compra inicial, licencias, soporte, personal, migración, integración y costo de salida. | Inversión inicial: **S/ 580,000** · **TCO a 5 años: S/ 2,964,050** (**`5.11x`** veces la inversión inicial). Operar los 13 proyectos cuesta **S/ 427,810/año**. | [`PF02_tco.py`](07_portafolio/PF02_tco.py) · [`PF02_tco.csv`](07_portafolio/PF02_tco.csv) · [`07_portafolio/PF03_fichas/`](07_portafolio/PF03_fichas) |
| **Paso C** | Se elaboraron los **3 casos de negocio** de mayor inversión (`PR-09`, `PR-03` y `PR-04`) con 3 opciones cada uno, calculando cuánto pierde la empresa si **«no hace nada»** y su impacto sostenible en 5 dimensiones. | Costo de no hacer nada a 5 años: **S/ 900,000** en `PR-09`, **S/ 560,000** en `PR-03` y **S/ 475,000** en `PR-04`. En los 3 gana la **Alternativa B**. | [`PF04_alternativas.py`](07_portafolio/PF04_alternativas.py) · [`PF04_alternativas.csv`](07_portafolio/PF04_alternativas.csv) · [`anexo_D_casos_negocio.md`](anexos/anexo_D_casos_negocio.md) |
| **Paso D** | Se midió el balance **Operar / Crecer / Transformar** y se armó el **mapa de dependencias** para saber qué proyectos van primero. | Balance equilibrado: **60.0 % Operar**, **24.1 % Crecer** y **15.8 % Transformar**. Proyectos base que van primero: **`PR-03`** (habilita 5 proyectos) y **`PR-01`** (habilita 4). | [`PF05_balance.py`](07_portafolio/PF05_balance.py) · [`PF06_dependencias.py`](07_portafolio/PF06_dependencias.py) · [`PF_balance.png`](graficos/PF_balance.png) · [`PF_dependencias.png`](graficos/PF_dependencias.png) |
| **Paso E** | Se redactó la **Sección 7.1 completa del PETI** (subsecciones `7.1.1` a `7.1.8`). | Documento unificado listo para el plan estratégico. | [`7.1_portafolio_proyectos.md`](07_portafolio/7.1_portafolio_proyectos.md) |
| **Paso F** | Se validaron automáticamente las 3 reglas de calidad (objetivos, fusiones sin pérdida de alcance y TCO con operación). | **100 % CONFORME** en las 3 comprobaciones. | [`PF07_validacion.py`](07_portafolio/PF07_validacion.py) · [`PF07_salida.txt`](evidencias/S13/salidas/PF07_salida.txt) |

---

## 3. Los 13 Proyectos del Portafolio (`PR-01` a `PR-13`)

| Código | Nombre del proyecto | Categoría | Objetivo(s) | Inv. Inicial | TCO a 5 años |
|:---:|---|---|:---:|---:|---:|
| **`PR-01`** | Gobierno del dato maestro (lotes agrícolas, productores y clientes) | Transformar | `OD-02, OD-03` | S/ 55,000 | S/ 290,250 |
| **`PR-02`** | Programa de cumplimiento de datos personales y RAT (Ley N.º 29733) | Operar | `OD-05` | S/ 18,000 | S/ 75,000 |
| **`PR-03`** | Capa de integración de servicios API (ERP - Planta - Campo - Aduanas) | Operar | `OD-01, OD-03` | S/ 78,000 | S/ 459,200 |
| **`PR-04`** | Rediseño del portal B2B de agroexportación y consulta de embarques | Crecer | `OD-01` | S/ 92,000 | S/ 425,000 |
| **`PR-05`** | Planificación inteligente de rutas de acopio, cadena de frío y despacho | Transformar | `OD-03` | S/ 34,000 | S/ 179,500 |
| **`PR-06`** | Tablero de gestión comercial, costos por lote y rentabilidad | Crecer | `OD-02` | S/ 28,000 | S/ 154,000 |
| **`PR-07`** | Mesa de servicio de TI y control centralizado de proveedores | Operar | `OD-04` | S/ 15,000 | S/ 66,500 |
| **`PR-08`** | Continuidad de infraestructura, enlace redundante y respaldo inmutable | Operar | `OD-04` | S/ 42,000 | S/ 161,200 |
| **`PR-09`** | Renovación y consolidación de la plataforma del ERP agroindustrial | Operar | `OD-04, OD-03` | S/ 145,000 | S/ 780,500 |
| **`PR-10`** | Gestión del conocimiento y base de datos de configuración (CMDB) | Operar | `OD-06` | S/ 22,000 | S/ 129,000 |
| **`PR-11`** | Comité de gobierno e inversiones de TI (casos de negocio y actas) | Operar | `OD-02, OD-04` | S/ 6,000 | S/ 23,000 |
| **`PR-12`** | Instrumentación de monitoreo y disponibilidad (frío, enlace y ERP) | Operar | `OD-04` | S/ 19,000 | S/ 85,400 |
| **`PR-13`** | Autoservicio digital de trabajadores de campo y planta (boletas y destajo) | Crecer | `OD-01, OD-05` | S/ 26,000 | S/ 135,500 |
| **TOTAL** | **13 Proyectos en el Portafolio** | **60% / 24.1% / 15.8%** | **100% cubiertos** | **S/ 580,000** | **S/ 2,964,050** |

---

## 4. Estructura de Carpetas del Repositorio

* [`07_portafolio/`](07_portafolio/): Scripts Python (`PF01` a `PF07`), archivos CSV generados, carpeta [`PF03_fichas/`](07_portafolio/PF03_fichas/) con las 13 fichas y el documento completo [`7.1_portafolio_proyectos.md`](07_portafolio/7.1_portafolio_proyectos.md).
* [`graficos/`](graficos/): Gráficos generados [`PF_balance.png`](graficos/PF_balance.png) y [`PF_dependencias.png`](graficos/PF_dependencias.png).
* [`evidencias/S13/`](evidencias/S13/): Gráficos y carpeta [`salidas/`](evidencias/S13/salidas/) con los resultados en texto de todos los scripts (`PF01_salida.txt` a `PF07_salida.txt`).
* [`anexos/`](anexos/): Los 6 anexos del informe (`anexo_A` a `anexo_F`).
