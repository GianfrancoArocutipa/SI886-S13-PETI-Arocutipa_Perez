# Anexo D · Casos de Negocio de los Tres Proyectos de Mayor Inversión

### 7.1.5 Casos de negocio de los proyectos de mayor inversión

Se desarrollan los casos de negocio completos de los tres proyectos de mayor TCO del portafolio (`PR-09`, `PR-03` y `PR-04`), evaluando en cada uno al menos tres alternativas (incluida la línea base **«A. No hacer nada»** con su costo de inacción cuantificado) y su impacto sobre las cinco dimensiones del desarrollo sostenible.

---

#### Caso de Negocio 1 · `PR-09` — Renovación y consolidación de la plataforma del ERP agroindustrial

1. **Problema u oportunidad:** En 2025 la organización ejecutó **S/ 260,819.96** en la *Implantación de módulo del ERP* (`Expediente 1 · INV01`, responsable Karla Cáceres Salazar) a partir de un pedido verbal del área usuaria, sin caso de negocio, sin acta de aceptación y sin medir beneficios. El núcleo del ERP opera sobre una versión próxima a fin de soporte, sin integración con recepción de cosecha ni cámaras de frío, ocasionando que la partida `PT02` (*Soporte y mantenimiento de sistemas*) sufriera una desviación de **+17.9 %** (S/ 92,315.88 ejecutados vs. S/ 78,280.00 planificados) y alimentando los **1,020 pagos por `Servicio informático` (S/ 1,475,059.22)** registrados en `pagos.csv`.
2. **Consecuencia de no actuar (Costo de la inacción):** **S/ 180,000 anuales (S/ 900,000 en 5 años)** compuestos por: (a) S/ 95,000/año en servicios informáticos correctivos, parches externos y soporte fuera de garantía; (b) S/ 55,000/año en horas-hombre de reproceso contable, liquidación manual de productores y cierres mensuales de 10 días; y (c) S/ 30,000/año de riesgo esperado por contingencias tributarias SUNAT (libros electrónicos y guías electrónicas) e indisponibilidad en plena campaña de exportación.
3. **Objetivo al que contribuye:** `OD-04` (Continuidad y eficiencia operativa de TI) y `OD-03` (Eficiencia y trazabilidad de operaciones agroindustriales).
4. **Alcance:**
   - *Incluye:* Migración a versión soportada del ERP actual, remediación formal y cierre del módulo `INV01`, unificación del costeo agrícola por lote/fundo sobre los maestros de `PR-01`, exposición de transacciones vía `PR-03`, capacitación certificada y acta de aceptación con línea base.
   - *No incluye:* Reemplazo por un ERP de otro fabricante desde cero ni desarrollo de portales externos (cubierto en `PR-04`).
5. **Alternativas evaluadas (`PF04_alternativas.csv`):**

| Concepto | A. No hacer nada (Línea base) | B. Consolidar y migrar a versión soportada del ERP actual (Recomendada) | C. Reemplazar por un nuevo ERP agroindustrial Tier-1 |
|---|---:|---:|---:|
| **Inversión inicial** | S/ 0 | S/ 145,000 | S/ 260,000 |
| **Otros costos únicos (Cap., Migr., Int.)** | S/ 0 | S/ 85,000 | S/ 110,000 |
| **Costo operativo anual** | S/ 0 (base) | S/ 110,100 | S/ 138,000 |
| **TCO a 5 años (`costo_5`)** | **S/ 0** | **S/ 780,500** | **S/ 1,060,000** |
| **Beneficio anual esperado** | -S/ 180,000 | S/ 235,000 | S/ 250,000 |
| **Beneficio acumulado a 5 años** | **-S/ 900,000** | **S/ 1,175,000** | **S/ 1,250,000** |
| **Beneficio Neto a 5 años (`neto_5`)** | **-S/ 900,000** | **+S/ 394,500** | **+S/ 190,000** |
| **Retorno sobre TCO a 5 años (`ROI`)** | N/A (Pérdida pura) | **+50.5 %** | **+17.9 %** |

6. **Solución recomendada:** **Alternativa B (Consolidar y migrar a la versión soportada del ERP actual)**, ejecutada en 2 fases. Entrega el mayor beneficio neto a 5 años (**+S/ 394,500**, ROI de **50.5 %**), rescata los **S/ 260,819.96** ya invertidos en `INV01` y evita el riesgo de parálisis operativa de 18 meses que implicaría cambiar de fabricante (Alternativa C) en plena campaña agroexportadora.
7. **Beneficios esperados y su medición:** Ahorro verificable de **S/ 235,000/año** medido en: (i) reducción >= 35 % en pagos a proveedores de soporte correctivo de sistemas respecto a la línea base de `pagos.csv`, y (ii) reducción del ciclo de cierre contable y costeo de lotes de 10 a 3 días hábiles.
8. **Costo total de propiedad (TCO):** **S/ 780,500** a 5 años (rango ±50 %: S/ 390,250 – S/ 1,170,750), más un costo de salida estimado de S/ 18,000.
9. **Recursos y dependencias:** 28 persona-mes durante 12 meses. **Depende obligatoriamente de `PR-01` (Gobierno del dato maestro) y `PR-03` (Capa de integración API)**.
10. **Riesgos principales:** Rechazo de usuarios clave por fallas previas en `INV01` -> *Tratamiento:* pruebas de aceptación de usuario (UAT) obligatorias y firma de acta de conformidad auditada por el Comité de TI (`PR-11`).
11. **Criterio de éxito:** 100 % de lotes exportados costeados automáticamente en el ERP con cierre mensual <= 3 días hábiles al mes 12.

##### Impacto en el desarrollo sostenible · `PR-09`

| Dimensión | A quién afecta | Efecto esperado, con su cifra o su indicador | ¿Norma o derecho aplicable? |
|---|---|---|---|
| **Sociedad** | 380 pequeños y medianos productores agrícolas proveedores de Valle Viejo | Reduce de 14 a 4 días hábiles la liquidación y pago de cosechas acopiadas gracias al cierre automático de lotes en el ERP. | Ley N.º 31110 (Ley del Régimen Laboral Agrario y de Incentivos) |
| **Economía** | Accionistas, Gerencia y área de Administración y Finanzas | Genera un beneficio neto de **S/ 394,500** en 5 años y evita **S/ 900,000** de pérdida por inacción y soporte reactivo disperso. | Marco COBIT 2019 `EDM02` / `APO05` y NIC / NIIF de información financiera |
| **Salud y seguridad** | 24 analistas contables, de logística y de planillas | Elimina ~1,200 horas/año de sobretiempos nocturnos en cierres de campaña, reduciendo riesgos psicosociales y fatiga laboral. | Ley N.º 29783 (Ley de Seguridad y Salud en el Trabajo) |
| **Marco legal** | Administración Tributaria (SUNAT) y Ministerio de Trabajo | Asegura el 100 % de emisión oportuna de Libros Electrónicos (SIRE), Guías de Remisión Electrónicas y Planilla Electrónica PLAME sin multas. | Resoluciones de Superintendencia SUNAT sobre SIRE y GRE; D.S. 018-2007-TR |
| **Medio ambiente** | Entorno operativo de oficinas administrativas y planta | Suprime la impresión de ~48,000 hojas/año de reportes de conciliación manual y vouchers físicos entre almacén, planta y contabilidad. | Ley N.º 30884 y políticas de ecoeficiencia y cero papel |

---

#### Caso de Negocio 2 · `PR-03` — Capa de integración de servicios API (ERP - Planta - Campo - Aduanas)

1. **Problema u oportunidad:** Los sistemas de recepción en planta de empaque, control de cámaras de frío, el portal de autoservicio (`INV03`) y el ERP (`INV01`) carecen de una capa de integración; se comunican mediante consultas directas a tablas de base de datos o carga manual de archivos planos, provocando caídas recurrentes, errores de transcripción en certificados de exportación y contrataciones fragmentadas de programación a medida dentro de los S/ 1,475,059.22 de `pagos.csv`.
2. **Consecuencia de no actuar (Costo de la inacción):** **S/ 112,000 anuales (S/ 560,000 en 5 años)** por: (a) 2,100 horas/año de doble digitación de pesajes, calibres y despachos entre planta y ERP (S/ 52,000/año); (b) sobrecostos por parches de integración rotos en cada actualización del ERP (S/ 35,000/año); y (c) rectificaciones documentales ante SENASA/Aduanas y **bloqueo técnico de 5 proyectos del portafolio (`PR-04`, `PR-05`, `PR-06`, `PR-09` y `PR-13`)** (S/ 25,000/año).
3. **Objetivo al que contribuye:** `OD-01` (Digitalización de canales de atención) y `OD-03` (Trazabilidad e integración operativa).
4. **Alcance:**
   - *Incluye:* Pasarela API Gateway en alta disponibilidad, 12 servicios REST/eventos documentados bajo OpenAPI 3.0, autenticación OAuth2/JWT, límite de tasa (rate limiting) y monitoreo de transacciones.
   - *No incluye:* Modificación de pantallas de usuario final ni migración de servidores de base de datos.
5. **Alternativas evaluadas (`PF04_alternativas.csv`):**

| Concepto | A. No hacer nada (Línea base) | B. Capa de integración API Gateway gestionada y conectores estándar (Recomendada) | C. Suite iPaaS empresarial propietaria |
|---|---:|---:|---:|
| **Inversión inicial** | S/ 0 | S/ 78,000 | S/ 155,000 |
| **Otros costos únicos (Cap., Int.)** | S/ 0 | S/ 23,000 | S/ 35,000 |
| **Costo operativo anual** | S/ 0 (base) | S/ 71,640 | S/ 104,000 |
| **TCO a 5 años (`costo_5`)** | **S/ 0** | **S/ 459,200** | **S/ 710,000** |
| **Beneficio anual esperado** | -S/ 112,000 | S/ 138,000 | S/ 148,000 |
| **Beneficio acumulado a 5 años** | **-S/ 560,000** | **S/ 690,000** | **S/ 740,000** |
| **Beneficio Neto a 5 años (`neto_5`)** | **-S/ 560,000** | **+S/ 230,800** | **+S/ 30,000** |
| **Retorno sobre TCO a 5 años (`ROI`)** | N/A (Pérdida pura) | **+50.3 %** | **+4.2 %** |

6. **Solución recomendada:** **Alternativa B (Capa de integración API Gateway gestionada con conectores estándar OpenAPI)**. Genera un beneficio neto de **+S/ 230,800** (ROI **50.3 %**), cuesta S/ 250,800 menos en TCO a 5 años que la suite iPaaS propietaria (Alternativa C) y evita el atamiento a licencias en dólares (*vendor lock-in*), manteniendo un costo de salida bajo (S/ 6,500).
7. **Beneficios esperados y su medición:** **S/ 138,000/año** por eliminación de integraciones ad-hoc, supresión de 2,100 horas/año de redigitación planta-ERP y habilitación directa del 62 % del TCO del portafolio.
8. **Costo total de propiedad (TCO):** **S/ 459,200** a 5 años (rango ±40 %: S/ 275,520 – S/ 642,880), más S/ 6,500 de costo de salida.
9. **Recursos y dependencias:** 18 persona-mes en 8 meses. Sin dependencias previas (inicia en Ola 1); **habilita 5 proyectos (`PR-04`, `PR-05`, `PR-06`, `PR-09`, `PR-13`)**.
10. **Riesgos principales:** Latencia en sincronización de pesajes de balanza de planta -> *Tratamiento:* colas asíncronas de mensajes con reintento automático local.
11. **Criterio de éxito:** 12 APIs en producción con disponibilidad >= 99.5 % y 0 conexiones directas de portales externos a la base de datos del ERP al mes 8.

##### Impacto en el desarrollo sostenible · `PR-03`

| Dimensión | A quién afecta | Efecto esperado, con su cifra o su indicador | ¿Norma o derecho aplicable? |
|---|---|---|---|
| **Sociedad** | 1,200 trabajadores agrarios y 85 clientes importadores | Habilita técnicamente el autoservicio de boletas laborales (`PR-13`) y el seguimiento en línea de embarques (`PR-04`), beneficiando a 1,285 usuarios directos. | D.S. N.º 009-2011-TR (boletas laborales) y estándares de comercio exterior |
| **Economía** | Agroexportadora Valle Viejo S.A.C. | Aporta un valor neto de **S/ 230,800** a 5 años, evita **S/ 560,000** de pérdida por inacción y desbloquea 5 proyectos cuyo TCO suma S/ 1,973,500. | COBIT 2019 `BAI02` / `APO05` |
| **Salud y seguridad** | 18 digitadores y asistentes de planta de empaque y despacho | No aplica impacto físico directo en riesgos mecánicos de planta; en el ámbito ergonómico reduce 2,100 horas/año de digitación repetitiva nocturna. | Ley N.º 29783 y RM 375-2008-TR (Norma Básica de Ergonomía) |
| **Marco legal** | Protección de datos personales y seguridad de la información | Elimina el acceso directo del portal web a las tablas internas del ERP mediante tokens OAuth2/JWT y cifrado TLS 1.3, evitando exposición de datos personales y comerciales. | Ley N.º 29733 (Directiva de Seguridad de la Información de la ANPD) e ISO/IEC 27001 |
| **Medio ambiente** | Infraestructura de servidores de la organización | La consolidación en una pasarela ligera evita desplegar servidores intermedios redundantes por cada proveedor externo, reduciendo el consumo eléctrico del cuarto de servidores en ~1,800 kWh/año. | Estándares de eficiencia energética en centros de datos |

---

#### Caso de Negocio 3 · `PR-04` — Rediseño del portal B2B de agroexportación y consulta de embarques en autoservicio

1. **Problema u oportunidad:** En 2024 Agroexportadora Valle Viejo S.A.C. ejecutó **S/ 224,964.21** en el *Portal de autoservicio* (`Expediente 3 · INV03`, responsable Luis Copaja Mamani) frente a un presupuesto aprobado de S/ 180,696.04 (**+24.5 % de desviación sin aprobación específica**), pidiendo solo tres cotizaciones del mismo producto, sin caso de negocio, sin acta de aceptación y sin medir beneficios. Hoy el portal sufre caídas por consultar directamente la base del ERP y carece de seguimiento de contenedores y certificados fitosanitarios (`C-05`), obligando al equipo comercial a responder consultas manualmente.
2. **Consecuencia de no actuar (Costo de la inacción):** **S/ 95,000 anuales (S/ 475,000 en 5 años)** integrados por: (a) 1,850 horas/año del equipo comercial y de exportaciones atendiendo por correo/teléfono el estado de embarques y reenviando packing lists, BL y certificados SENASA (S/ 58,000/año); (b) penalidades comerciales y costos de sobreestadía (*demurrage*) por demoras documentales en destino (S/ 25,000/año); y (c) deterioro y pérdida efectiva del capital invertido en `INV03` (S/ 12,000/año en mantenimiento correctivo improductivo).
3. **Objetivo al que contribuye:** `OD-01` (Incrementar la adopción y satisfacción en canales digitales de clientes e importadores).
4. **Alcance:**
   - *Incluye:* Refactorización del portal B2B existente (`C-04`) para consumir servicios seguros de `PR-03` y maestros de `PR-01`, incorporación del módulo de consulta de estado de embarques, trazabilidad de termógrafos y descarga de documentos fitosanitarios en autoservicio (`C-05`), ejecutado en 2 etapas.
   - *No incluye:* Ventas minoristas B2C ni pasarela de pagos con tarjetas de crédito.
5. **Alternativas evaluadas (`PF04_alternativas.csv`):**

| Concepto | A. No hacer nada (Línea base) | B. Rediseño del portal existente sobre API (`PR-03`) + trazabilidad de embarques (Recomendada) | C. Nueva plataforma SaaS B2B de comercio exterior desde cero |
|---|---:|---:|---:|
| **Inversión inicial** | S/ 0 | S/ 92,000 | S/ 210,000 |
| **Otros costos únicos (Cap., Migr., Int.)** | S/ 0 | S/ 36,000 | S/ 45,000 |
| **Costo operativo anual** | S/ 0 (base) | S/ 59,400 | S/ 84,000 |
| **TCO a 5 años (`costo_5`)** | **S/ 0** | **S/ 425,000** | **S/ 675,000** |
| **Beneficio anual esperado** | -S/ 95,000 | S/ 145,000 | S/ 165,000 |
| **Beneficio acumulado a 5 años** | **-S/ 475,000** | **S/ 725,000** | **S/ 825,000** |
| **Beneficio Neto a 5 años (`neto_5`)** | **-S/ 475,000** | **+S/ 300,000** | **+S/ 150,000** |
| **Retorno sobre TCO a 5 años (`ROI`)** | N/A (Pérdida pura) | **+70.6 %** | **+22.2 %** |

6. **Solución recomendada:** **Alternativa B (Rediseño del portal existente acoplado a `PR-03` + módulo de trazabilidad de embarques `C-05`), ejecutada en dos etapas.** Alcanza el mayor beneficio neto (**+S/ 300,000**, ROI **70.6 %**), rescata la inversión previa de **S/ 224,964.21 (`INV03`)** en lugar de desecharla como hace la Alternativa C, y aplica gestión de riesgos por etapas: la Etapa 1 (meses 1–5) desacopla el portal mediante `PR-03` y habilita la descarga documental; una vez verificado un umbral de adopción > 25 %, la Etapa 2 (meses 6–9) despliega el tracking completo de contenedores y lotes.
7. **Beneficios esperados y su medición:** **S/ 145,000/año** (1,850 horas/año comerciales liberadas para prospección de nuevos mercados y reducción del 80 % en reclamos por demora de documentos de embarque).
8. **Costo total de propiedad (TCO):** **S/ 425,000** a 5 años (rango ±35 %: S/ 276,250 – S/ 573,750), más S/ 7,500 de costo de salida.
9. **Recursos y dependencias:** 20 persona-mes en 9 meses. **Depende de `PR-01` y `PR-03`**.
10. **Riesgos principales:** Desalineación entre datos de embarque y registros de aduana -> *Tratamiento:* validación automática contra el maestro de lotes (`PR-01`) antes de publicar el dossier en el portal.
11. **Criterio de éxito:** >= 65 % de clientes importadores activos descargando documentos y consultando estatus de contenedores en autoservicio al noveno mes, con acta de aceptación y medición trimestral auditada.

##### Impacto en el desarrollo sostenible · `PR-04`

| Dimensión | A quién afecta | Efecto esperado, con su cifra o su indicador | ¿Norma o derecho aplicable? |
|---|---|---|---|
| **Sociedad** | 85 empresas importadoras/brokers internacionales y 14 ejecutivos de exportación de Valle Viejo | Reduce el tiempo de obtención del dossier de embarque de 36 horas (vía correo manual) a < 2 minutos en autoservicio 24x7 sin diferencia horaria. | Facilitación del comercio exterior y atención al cliente B2B |
| **Economía** | Agroexportadora Valle Viejo S.A.C. | Genera un beneficio neto de **S/ 300,000** en 5 años (ROI 70.6 %), evita **S/ 475,000** por inacción y recupera el valor del activo `INV03` (S/ 224,964.21). | COBIT 2019 `EDM02` (Asegurar la entrega de beneficios) y Val IT |
| **Salud y seguridad** | Consumidores finales en mercados de destino y personal de calidad | Garantiza la trazabilidad fitosanitaria y de cadena de frío de cada lote exportado en línea, previniendo alertas sanitarias o rechazos en puerto. | Reglamentos fitosanitarios SENASA, GlobalG.A.P., FSMA (FDA) y Codex Alimentarius |
| **Marco legal** | Aduanas (SUNAT), SENASA y protección de datos de contactos B2B | Cumple con la trazabilidad obligatoria de lotes de agroexportación y protege las credenciales de clientes conforme a la Ley N.º 29733. | Ley General de Aduanas (D.L. 1053), normativas SENASA y Ley N.º 29733 |
| **Medio ambiente** | Cadena logística documental de comercio exterior | Sustituye el envío físico por courier internacional y la impresión de ~1,400 juegos anuales de carpetas de exportación (packing list, certificados internos y copias de BL) por dossiers digitales firmados. | Políticas de desmaterialización documental en comercio exterior |

---

