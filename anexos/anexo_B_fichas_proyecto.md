# Anexo B · Fichas Estandarizadas de Proyecto (PR-01 a PR-13)

# Ficha Estandarizada de Proyecto · PR-01

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-01` |
| **2** | **Nombre del proyecto** | Gobierno del dato maestro (lotes agrícolas, productores y clientes) |
| **3** | **Fuente y sección de origen** | Brecha de arquitectura · Sección 5.4.2 PT-01 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-02, OD-03` |
| **5** | **Categoría del portafolio** | **Transformar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Inconsistencia de códigos de lotes agrícolas, fundos proveedores y clientes importadores entre planta de empaque, campo y el módulo ERP implantado en INV01 (S/ 260,819.96 ejecutados sin acta ni diccionario de datos), ocasionando reprocesos manuales de conciliación en cada campaña de exportación. |
| **7** | **Alcance incluido** | Catálogo único y diccionario de datos maestros (productores, lotes fitosanitarios SENASA, variedades de cultivo, clientes B2B y proveedores); reglas de calidad de datos; comité de custodia de datos; migración y depuración de maestros actuales. |
| **8** | **Alcance excluido** | Desarrollo de tableros BI comerciales (cubierto en PR-06) y construcción de pasarelas API (cubierto en PR-03). |
| **9** | **Entregables concretos** | 1) Diccionario y modelo canónico de datos maestros; 2) Repositorio centralizado MDM validado; 3) Matriz RACI de propietarios de datos (Data Stewards); 4) Base maestra depurada y migrada sin duplicados. |
| **10** | **Duración estimada (meses)** | 6 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 12 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 55,000 (rango ±30 %: S/ 38,500 – S/ 71,500) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 41,850 / año (Licencias: S/ 6,000 + Infraestructura: S/ 3,600 + Soporte 15 %: S/ 8,250 + Personal dedicado: S/ 24,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 26,000 (Capacitación: S/ 6,000 + Migración: S/ 12,000 + Integración: S/ 8,000) · Costo de salida estimado: S/ 4,500 (exportación abierta en estándar SQL/CSV). |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 290,250 (rango ±30 %: S/ 203,175 – S/ 377,325; S/ 294,750 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Ahorro de S/ 92,000/año por eliminación de 1,450 horas/año de reproceso en conciliación de lotes de acopio y facturación de exportación; reducción de errores de codificación fitosanitaria de 8.4 % a < 0.5 %. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | No depende de ningún proyecto previo (inicia en Ola 1). Habilita estructuralmente a 4 proyectos: PR-04, PR-05, PR-06 y PR-09. |
| **18** | **Riesgos principales y su tratamiento** | Resistencia de las áreas de Acopio, Planta y Administración a ceder el alta libre de códigos en el ERP -> Mitigación: bloqueo técnico de altas sin validación MDM y patrocinio de Gerencia General. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Jefe de TI / Arquitecto de Datos (en coordinación con Karla Cáceres Salazar) · **Área usuaria:** Operaciones Agrícolas, Planta de Empaque, Comercial y Administración y Finanzas |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de lotes de exportación, productores y clientes registrados bajo código único validado, con < 0.5 % de duplicidad al sexto mes. |


---

# Ficha Estandarizada de Proyecto · PR-02

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-02` |
| **2** | **Nombre del proyecto** | Programa de cumplimiento de datos personales y Registro de Actividades de Tratamiento (RAT) |
| **3** | **Fuente y sección de origen** | Obligación normativa · Sección 4.1.5 (Fusión de C-02 + C-11) |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-05` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Agroexportadora Valle Viejo S.A.C. administra datos sensibles y biométricos/planillas de más de 1,200 trabajadores de campo y planta, productores y contactos comerciales sin inscripción de bancos de datos ni RAT actualizado ante la ANPD (Ley N.º 29733 y D.S. 016-2024-JUS), exponiéndose a multas graves de 5 a 50 UIT. |
| **7** | **Alcance incluido** | Elaboración del Registro de Actividades de Tratamiento (RAT, de C-02); inscripción de bancos de datos personales (trabajadores, productores, clientes, videovigilancia) ante la ANPD; cláusulas de consentimiento informado y políticas de privacidad; procedimiento de atención de derechos ARCO y notificación de incidentes (de C-11). |
| **8** | **Alcance excluido** | Implementación de portal web de boletas de pago (cubierto en PR-13) y despliegue de respaldos inmutables de servidores (cubierto en PR-08). |
| **9** | **Entregables concretos** | 1) Registro de Actividades de Tratamiento (RAT) aprobado; 2) Resoluciones de inscripción de 4 bancos de datos ante la ANPD; 3) Formatos legales de consentimiento de jornaleros, proveedores y clientes; 4) Protocolo ARCO y actas de capacitación al personal administrativo. |
| **10** | **Duración estimada (meses)** | 3 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 5 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 18,000 (rango ±20 %: S/ 14,400 – S/ 21,600) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 10,800 / año (Licencias: S/ 0 + Infraestructura: S/ 0 + Soporte/Auditoría legal 10 %: S/ 1,800 + Personal dedicado: S/ 9,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 3,000 (Capacitación inicial: S/ 3,000) · Costo de salida estimado: S/ 1,500 (archivo documental normativo propio). |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 75,000 (rango ±20 %: S/ 60,000 – S/ 90,000; S/ 76,500 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Riesgo legal evitado cuantificado en S/ 128,750/año (probabilidad de fiscalización 50 % × multa media de 50 UIT = S/ 257,500 ante la ANPD / SUNAFIL). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Sin dependencias previas (inicia en Ola 1). No bloquea técnicamente a otros proyectos, pero resguarda legalmente a PR-04 y PR-13. |
| **18** | **Riesgos principales y su tratamiento** | Demora en la firma de consentimientos físicos de trabajadores temporales de campaña -> Mitigación: incorporación obligatoria en el kit de contratación de RR.HH. antes del ingreso a fundo. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Oficial de Datos Personales / Asesoría Legal y Jefatura de TI · **Área usuaria:** Recursos Humanos, Administración y Finanzas, Comercial |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de bancos de datos inscritos ante la ANPD, RAT vigente y 100 % de contratos y portales con cláusulas de protección de datos al mes 3. |


---

# Ficha Estandarizada de Proyecto · PR-03

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-03` |
| **2** | **Nombre del proyecto** | Capa de integración de servicios API (ERP - Planta - Campo - Aduanas) |
| **3** | **Fuente y sección de origen** | Brecha de arquitectura · Sección 5.4.2 PT-02 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-01, OD-03` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | El portal de autoservicio (INV03: S/ 224,964.21 ejecutados con +24.5 % de sobrecosto) y las balanzas/sistemas de planta consultan o cargan datos directamente o mediante archivos Excel al ERP (INV01: S/ 260,819.96), generando acoplamiento frágil, doble digitación y pagos reactivos dispersos en 71 proveedores informáticos (S/ 1,475,059.22 en pagos.csv). |
| **7** | **Alcance incluido** | Despliegue de pasarela API Gateway empresarial; diseño y publicación de servicios REST/eventos para lotes agrícolas, recepción en planta, stock de cámaras de frío, pedidos de exportación y boletas RR.HH.; seguridad OAuth2/JWT, control de tráfico y logs de auditoría. |
| **8** | **Alcance excluido** | Rediseño de la interfaz de usuario del portal B2B (cubierto en PR-04) y migración del motor de base de datos del ERP (cubierto en PR-09). |
| **9** | **Entregables concretos** | 1) Pasarela API Gateway en alta disponibilidad; 2) Catálogo OpenAPI/Swagger con 12 servicios expuestos y documentados; 3) Conectores desacoplados ERP–Planta–Portal; 4) Tablero de telemetría y seguridad de APIs. |
| **10** | **Duración estimada (meses)** | 8 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 18 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 78,000 (rango ±40 %: S/ 46,800 – S/ 109,200) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 71,640 / año (Licencias: S/ 12,000 + Infraestructura: S/ 9,600 + Soporte 18 %: S/ 14,040 + Personal dedicado: S/ 36,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 23,000 (Capacitación: S/ 8,000 + Integración inicial: S/ 15,000) · Costo de salida estimado: S/ 6,500 (especificaciones OpenAPI estándar portables). |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 459,200 (rango ±40 %: S/ 275,520 – S/ 642,880; S/ 465,700 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Ahorro y riesgo evitado de S/ 138,000/año (eliminación de integraciones ad-hoc contratadas en pagos.csv, reducción de 2,100 horas/año de digitación duplicada entre planta y ERP, y habilitación de 5 proyectos del portafolio). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | No depende de ningún proyecto previo (inicia en Ola 1). Es el principal habilitador estructural del portafolio: habilita 5 proyectos (PR-04, PR-05, PR-06, PR-09 y PR-13). |
| **18** | **Riesgos principales y su tratamiento** | Falta de documentación técnica de las tablas del ERP implantado en INV01 -> Mitigación: ingeniería inversa controlada sobre entorno de pruebas con participación del proveedor del ERP. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Arquitecto de Integración / Jefe de TI · **Área usuaria:** Todas las áreas operativas (Planta de Empaque, Acopio, Comercial, RR.HH. y Finanzas) |
| **20** | **Criterio de éxito (con umbral verificable)** | 0 accesos directos de aplicaciones externas a la base de datos del ERP y >= 99.5 % de disponibilidad en las 12 APIs publicadas al octavo mes. |


---

# Ficha Estandarizada de Proyecto · PR-04

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-04` |
| **2** | **Nombre del proyecto** | Rediseño del portal B2B de agroexportación y consulta de embarques en autoservicio |
| **3** | **Fuente y sección de origen** | Brecha de servicio digital · Sección 6.1.7 S-01, S-02 (Fusión de C-04 + C-05) |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-01` |
| **5** | **Categoría del portafolio** | **Crecer** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | En 2024 Agroexportadora Valle Viejo ejecutó S/ 224,964.21 en el 'Portal de autoservicio' (Expediente 3 - INV03, responsable Luis Copaja Mamani, desviación +24.5 %) sin caso de negocio, sin acta de aceptación y sin medir beneficios. El portal presenta problemas recurrentes, no muestra trazabilidad de embarques ni certificados fitosanitarios y obliga a atender consultas de clientes e importadores por correo y teléfono. |
| **7** | **Alcance incluido** | Rediseño funcional y técnico del portal B2B (C-04) desacoplado del ERP mediante PR-03; módulo de consulta en tiempo real de estado de pedidos, contenedores refrigerados, packing list y certificados SENASA en autoservicio (C-05); despliegue en 2 etapas con validación de adopción al mes 5. |
| **8** | **Alcance excluido** | Sistema de gestión de rutas internas de camiones de campo (cubierto en PR-05) y pasarela de cobro minorista B2C (la empresa opera en modelo B2B agroexportador). |
| **9** | **Entregables concretos** | 1) Portal web B2B responsivo integrado vía API Gateway (PR-03); 2) Módulo de seguimiento de embarques, lotes y descarga de dossier de exportación (packing list, BL, certificado fitosanitario); 3) Panel de métricas de adopción por cliente importador; 4) Acta de aceptación formal y medición de línea base. |
| **10** | **Duración estimada (meses)** | 9 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 20 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 92,000 (rango ±35 %: S/ 59,800 – S/ 124,200) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 59,400 / año (Licencias: S/ 8,400 + Infraestructura: S/ 7,200 + Soporte 15 %: S/ 13,800 + Personal dedicado: S/ 30,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 36,000 (Capacitación: S/ 12,000 + Migración: S/ 6,000 + Integración: S/ 18,000) · Costo de salida estimado: S/ 7,500. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 425,000 (rango ±35 %: S/ 276,250 – S/ 573,750; S/ 432,500 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Beneficio cuantificado de S/ 145,000/año (liberación de 1,850 horas/año del equipo comercial y de exportaciones en envío manual de documentos de embarque, reducción de penalidades por demora documental y rescate del activo INV03). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-01 (Gobierno del dato maestro) y PR-03 (Capa de integración de servicios API). No habilita a otros proyectos. |
| **18** | **Riesgos principales y su tratamiento** | Baja adopción de clientes e importadores acostumbrados a pedir estatus por WhatsApp/correo -> Mitigación: ejecución en 2 etapas (Etapa 1 valida umbral > 25 % de adopción antes de liberar Etapa 2) y envío automático de enlace de tracking. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Jefe de Aplicaciones / Líder Comercial de Exportaciones (en coordinación con Luis Copaja Mamani) · **Área usuaria:** Comercial, Comercio Exterior / Exportaciones y Aseguramiento de la Calidad |
| **20** | **Criterio de éxito (con umbral verificable)** | >= 65 % de clientes importadores/brokers consultando embarques y descargando documentación fitosanitaria en autoservicio sin intervención telefónica al mes 9. |


---

# Ficha Estandarizada de Proyecto · PR-05

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-05` |
| **2** | **Nombre del proyecto** | Planificación inteligente de rutas de acopio, cadena de frío y trazabilidad de despacho |
| **3** | **Fuente y sección de origen** | Estrategia FODA · Sección 3.5 E-02 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-03` |
| **5** | **Categoría del portafolio** | **Transformar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | La programación de recojo de cosecha en fundos del Valle Viejo y el control de temperatura desde el acopio hasta el despacho de contenedores refrigerados se gestiona en hojas de cálculo aisladas, generando mermas por ruptura de cadena de frío, tiempos muertos de transporte (S/ 1,509,984.67 en Servicio de transporte y S/ 1,650,557.88 en Combustible en pagos.csv) y demoras en el cierre de lotes. |
| **7** | **Alcance incluido** | Módulo de planificación de rutas de acopio agrícola; registro móvil de recepción de jabas/pallets por lote en campo y planta; integración de sensores de temperatura de cadena de frío y trazabilidad de despacho de contenedores. |
| **8** | **Alcance excluido** | Compra de flota propia de camiones refrigerados (el transporte se contrata como servicio) y renovación del ERP contable (PR-09). |
| **9** | **Entregables concretos** | 1) Aplicación web/móvil de ruteo de acopio y trazabilidad de lotes; 2) Integración de lecturas de cadena de frío por pallet/contenedor; 3) Conector API con ERP y portal B2B; 4) Reporte auditable de trazabilidad campo-a-puerto para SENASA y certificaciones GlobalG.A.P. |
| **10** | **Duración estimada (meses)** | 5 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 10 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 34,000 (rango ±30 %: S/ 23,800 – S/ 44,200) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 25,500 / año (Licencias: S/ 4,800 + Infraestructura: S/ 3,600 + Soporte 15 %: S/ 5,100 + Personal dedicado: S/ 12,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 18,000 (Capacitación: S/ 4,000 + Migración: S/ 5,000 + Integración: S/ 9,000) · Costo de salida estimado: S/ 3,000. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 179,500 (rango ±30 %: S/ 125,650 – S/ 233,350; S/ 182,500 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Ahorro de S/ 96,000/año (reducción del 3.5 % en gasto de fletes y combustible de acopio sobre la base de pagos.csv y disminución de 1.2 % en merma por deshidratación/cadena de frío). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-01 (Gobierno del dato maestro de lotes y fundos) y PR-03 (Capa de integración de servicios API). |
| **18** | **Riesgos principales y su tratamiento** | Zonas agrícolas del valle con cobertura celular intermitente -> Mitigación: modo offline con sincronización diferida automática al llegar a planta de empaque. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Coordinador de Sistemas Operativos / Jefe de Logística y Planta · **Área usuaria:** Acopio Agrícola, Planta de Empaque, Frío y Despacho |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de lotes de exportación con trazabilidad digital completa desde fundo hasta contenedor y reducción >= 20 % en el tiempo de despacho al quinto mes. |


---

# Ficha Estandarizada de Proyecto · PR-06

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-06` |
| **2** | **Nombre del proyecto** | Tablero de gestión comercial, costos por lote y rentabilidad de exportación |
| **3** | **Fuente y sección de origen** | Brecha de arquitectura · Sección 5.4.2 PT-05 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-02` |
| **5** | **Categoría del portafolio** | **Crecer** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | La Gerencia General y Administración y Finanzas carecen de visibilidad oportuna de la rentabilidad por lote exportado, variedad, cliente y campaña; los reportes tardan hasta 12 días tras el cierre mensual porque se consolidan manualmente desde el ERP (INV01) y planillas contables. |
| **7** | **Alcance incluido** | Data mart comercial y de costos agroindustriales; tableros ejecutivos automatizados de margen por lote/contenedor, ejecución presupuestal de TI y seguimiento de beneficios de inversiones (cerrando la brecha de medición detectada en INV01, INV02 e INV03). |
| **8** | **Alcance excluido** | Modelos predictivos de precios internacionales de commodities con IA (fuera de horizonte actual) y modificación de asientos en el ERP. |
| **9** | **Entregables concretos** | 1) Modelo dimensional de rentabilidad por lote, calibre y destino; 2) 5 tableros gerenciales (Comercial, Costos de Planta/Campo, Logística, Presupuesto y Beneficios TI); 3) Automatización de ingesta diaria vía PR-03. |
| **10** | **Duración estimada (meses)** | 4 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 8 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 28,000 (rango ±25 %: S/ 21,000 – S/ 35,000) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 22,200 / año (Licencias: S/ 3,600 + Infraestructura: S/ 2,400 + Soporte 15 %: S/ 4,200 + Personal dedicado: S/ 12,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 15,000 (Capacitación: S/ 5,000 + Migración: S/ 3,000 + Integración: S/ 7,000) · Costo de salida estimado: S/ 2,500. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 154,000 (rango ±25 %: S/ 115,500 – S/ 192,500; S/ 156,500 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Reducción del tiempo de generación de reportes gerenciales de 12 días a actualización diaria (< 24 h) y ahorro de S/ 54,000/año en horas de analistas financieros y comerciales. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-01 (Gobierno del dato maestro) y PR-03 (Capa de integración de servicios API). |
| **18** | **Riesgos principales y su tratamiento** | Discrepancia en criterios de prorrateo de costos indirectos de planta de empaque -> Mitigación: definición y firma previa de reglas de costeo con Administración y Finanzas. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Analista de Inteligencia de Negocios / Jefe de Administración y Finanzas · **Área usuaria:** Gerencia General, Comercial, Administración y Finanzas |
| **20** | **Criterio de éxito (con umbral verificable)** | Cierre de rentabilidad por lote disponible en <= 24 horas tras el embarque con 0 diferencias frente al balance contable del ERP. |


---

# Ficha Estandarizada de Proyecto · PR-07

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-07` |
| **2** | **Nombre del proyecto** | Mesa de servicio de TI y control centralizado de proveedores informáticos |
| **3** | **Fuente y sección de origen** | Brecha de capacidad · Sección 4.3.5 DSS02 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-04` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Las incidencias de usuarios y los requerimientos a proveedores de TI se gestionan de manera informal, lo que ha derivado en 1,020 pagos por 'Servicio informático' (S/ 1,475,059.22 en pagos.csv) repartidos en 71 proveedores y aprobados por 13 empleados distintos (incluyendo 18 pagos auto-aprobados por S/ 48,144.00), además de un sobrecosto de +17.9 % en la partida PT02 de soporte. |
| **7** | **Alcance incluido** | Implantación de plataforma ITSM de Mesa de Servicio (incidentes, requerimientos y niveles de servicio SLA); catálogo de servicios de TI; flujo obligatorio de validación técnica previa a toda orden de compra de 'Servicio informático' y homologación de proveedores. |
| **8** | **Alcance excluido** | Inventario automatizado de configuración y activos (cubierto en PR-10). |
| **9** | **Entregables concretos** | 1) Herramienta de Mesa de Servicio configurada con colas, prioridades y SLA; 2) Procedimiento DSS02 y bloqueo de órdenes de compra informáticas sin ticket de conformidad técnica; 3) Padrón depurado y homologado de proveedores de TI (reducción de 71 a <= 12 proveedores autorizados). |
| **10** | **Duración estimada (meses)** | 3 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 5 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 15,000 (rango ±20 %: S/ 12,000 – S/ 18,000) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 9,300 / año (Licencias: S/ 0 [Open Source] + Infraestructura: S/ 1,800 + Soporte 10 %: S/ 1,500 + Personal dedicado: S/ 6,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 5,000 (Capacitación: S/ 3,000 + Integración correo/AD: S/ 2,000) · Costo de salida estimado: S/ 1,200. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 66,500 (rango ±20 %: S/ 53,200 – S/ 79,800; S/ 67,700 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Ahorro directo estimado de S/ 185,000/año al eliminar servicios informáticos duplicados, fraccionados o sin conformidad técnica sobre la bolsa de S/ 1,475,059.22 detectada en pagos.csv. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | No depende de ningún proyecto previo (inicia en Ola 1). Habilita a PR-10 (Gestión del conocimiento y CMDB). |
| **18** | **Riesgos principales y su tratamiento** | Compras directas de áreas usuarias eludiendo la Mesa de Servicio -> Mitigación: regla en Administración y Finanzas que impide pagar comprobantes de 'Servicio informático' sin número de ticket y acta en PR-07. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Coordinador de Soporte y Operaciones de TI · **Área usuaria:** Toda la organización y Administración y Finanzas (Compras/Tesorería) |
| **20** | **Criterio de éxito (con umbral verificable)** | >= 95 % de incidentes y 100 % de órdenes de servicio informático registradas y aprobadas a través de la Mesa de Servicio con cumplimiento de SLA >= 90 %. |


---

# Ficha Estandarizada de Proyecto · PR-08

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-08` |
| **2** | **Nombre del proyecto** | Continuidad de infraestructura, conmutación de enlace redundante y respaldo inmutable |
| **3** | **Fuente y sección de origen** | Brecha de capacidad · Sección 4.3.5 DSS04 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-04` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | En 2025 se ejecutaron S/ 75,773.21 (+20.6 % de desviación) en el 'Enlace de datos redundante' (Expediente 2 - INV02, responsable Carlos Apaza Ancco) sin acta de aceptación ni pruebas de conmutación automática (failover), y la organización carece de copias de respaldo inmutables fuera de sede para proteger el ERP y los registros de exportación ante ransomware o siniestros en planta. |
| **7** | **Alcance incluido** | Configuración de balanceo y failover automático SD-WAN sobre el enlace redundante existente (INV02); implementación de respaldos 3-2-1 con repositorio inmutable en nube/off-site; Plan de Continuidad Tecnológica (DRP) y pruebas semestrales de restauración. |
| **8** | **Alcance excluido** | Instrumentación de monitoreo de aplicaciones y sensores de cámaras de frío (cubierto en PR-12). |
| **9** | **Entregables concretos** | 1) Failover automático operativo y certificado sobre los enlaces de planta y sede administrativa; 2) Sistema de respaldo automático 3-2-1 con inmutabilidad activada; 3) Plan de Recuperación ante Desastres (DRP) con RPO <= 4 h y RTO <= 2 h; 4) Acta de prueba exitosa de restauración y conmutación. |
| **10** | **Duración estimada (meses)** | 4 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 6 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 42,000 (rango ±25 %: S/ 31,500 – S/ 52,500) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 23,040 / año (Licencias: S/ 0 + Infraestructura cloud/almacenamiento inmutable: S/ 6,000 + Soporte 12 %: S/ 5,040 + Personal dedicado: S/ 12,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 4,000 (Capacitación inicial: S/ 4,000) · Costo de salida estimado: S/ 3,500. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 161,200 (rango ±25 %: S/ 120,900 – S/ 201,500; S/ 164,700 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Riesgo evitado de S/ 160,000/año por parálisis de despacho de contenedores y facturación electrónica durante campaña agrícola, rentabilizando además la inversión previa INV02 de S/ 75,773.21. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | No depende de ningún proyecto previo (inicia en Ola 1). Habilita a PR-12 (Instrumentación de monitoreo y disponibilidad). |
| **18** | **Riesgos principales y su tratamiento** | Ancho de banda insuficiente en horarios pico de copia hacia repositorio externo -> Mitigación: ventanas de replicación incremental nocturna con deduplicación. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Administrador de Redes e Infraestructura (en coordinación con Carlos Apaza Ancco) · **Área usuaria:** Planta de Empaque, Despacho, Facturación y TI |
| **20** | **Criterio de éxito (con umbral verificable)** | Tiempo de conmutación de enlace < 30 segundos, RPO <= 4 horas y RTO <= 2 horas verificados mediante simulacro documentado al cuarto mes. |


---

# Ficha Estandarizada de Proyecto · PR-09

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-09` |
| **2** | **Nombre del proyecto** | Renovación y consolidación de la plataforma del ERP agroindustrial |
| **3** | **Fuente y sección de origen** | Estrategia FODA · Sección 3.5 E-04 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-04, OD-03` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | En 2025 se gastaron S/ 260,819.96 en la 'Implantación de módulo del ERP' (Expediente 1 - INV01, responsable Karla Cáceres Salazar) por pedido verbal del área usuaria, sin caso de negocio, sin acta de aceptación y sin medir beneficios. El núcleo del ERP sigue en versión próxima a fin de soporte, con módulos desconectados de planta y campo, provocando que la partida PT02 (Soporte y mantenimiento) se desvíe +17.9 % (S/ 92,315.88) y que proliferen gastos externos en pagos.csv. |
| **7** | **Alcance incluido** | Actualización a la versión soportada del ERP agroindustrial; remediación y cierre formal del módulo implantado en INV01; integración nativa vía PR-03 con datos maestros gobernados por PR-01; parametrización de costeo agrícola por fundo/lote y régimen agrario; capacitación certificada y acta de aceptación con línea base de beneficios. |
| **8** | **Alcance excluido** | Reemplazo por un ERP de otro fabricante desde cero (descartado en el caso de negocio por su mayor TCO de S/ 1,060,000 y riesgo en campaña). |
| **9** | **Entregables concretos** | 1) Plataforma ERP en versión vigente con soporte oficial garantizado por 5 años; 2) Módulos de Costos Agrícolas, Almacenes/Empaque, Contabilidad y Exportaciones unificados; 3) Migración auditada sobre maestros de PR-01 e integración vía PR-03; 4) Acta de aceptación y medición trimestral de beneficios. |
| **10** | **Duración estimada (meses)** | 12 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 28 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 145,000 (rango ±50 %: S/ 72,500 – S/ 217,500) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 110,100 / año (Licencias: S/ 24,000 + Infraestructura: S/ 12,000 + Soporte 18 %: S/ 26,100 + Personal dedicado: S/ 48,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 85,000 (Capacitación: S/ 20,000 + Migración: S/ 35,000 + Integración: S/ 30,000) · Costo de salida estimado: S/ 18,000 (extracción estructurada y desencriptación de históricos). |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 780,500 (rango ±50 %: S/ 390,250 – S/ 1,170,750; S/ 798,500 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Beneficio cuantificado de S/ 235,000/año (S/ 1,175,000 en 5 años): reducción de S/ 145,000/año en servicios informáticos correctivos dispersos (pagos.csv) y S/ 90,000/año por eliminación de reprocesos contables, tributarios y de liquidación de campañas. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-01 (Gobierno del dato maestro) y PR-03 (Capa de integración de servicios API). No puede iniciar su migración productiva sin ambos habilitadores. |
| **18** | **Riesgos principales y su tratamiento** | Interrupción de facturación y guías de remisión durante ventana de cosecha pico -> Mitigación: despliegue por fases fuera de campaña alta y marcha blanca en paralelo durante 30 días. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Jefe de Proyecto ERP / Jefatura de TI (en coordinación con Karla Cáceres Salazar) · **Área usuaria:** Administración y Finanzas, Contabilidad, Operaciones Agrícolas, Planta y Logística |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de procesos contables, logísticos y de costeo por lote operando en la versión soportada del ERP, con cierre contable mensual reducido de 10 a 3 días hábiles y 0 hallazgos de soporte sin cobertura. |


---

# Ficha Estandarizada de Proyecto · PR-10

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-10` |
| **2** | **Nombre del proyecto** | Gestión del conocimiento y base de datos de configuración (CMDB) |
| **3** | **Fuente y sección de origen** | Estrategia FODA · Sección 3.5 E-07 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-06` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | La partida PT05 (Personal de TI) tuvo una sub-ejecución de -30.8 % en 2025 (S/ 56,994.53 ejecutados de S/ 82,400.00 planificados) por rotación y vacantes no cubiertas, mientras que la configuración de servidores, enlaces y módulos implantados (INV01, INV02, INV03) no queda documentada, generando dependencia crítica de personas y proveedores externos. |
| **7** | **Alcance incluido** | Base de datos de gestión de la configuración (CMDB) integrada a la Mesa de Servicio (PR-07); inventario de activos de hardware, licencias (PT01), contratos de soporte (PT02) y enlaces (PT04); repositorio de manuales técnicos, runbooks operativos y actas de proyectos. |
| **8** | **Alcance excluido** | Auditoría financiera contable de bienes muebles no tecnológicos. |
| **9** | **Entregables concretos** | 1) CMDB poblada con el 100 % de servidores, equipos de planta, licencias y contratos TI; 2) Wiki técnica con arquitectura, diagramas y procedimientos operativos estándar (SOP); 3) Matriz de vencimientos de licencias y garantías. |
| **10** | **Duración estimada (meses)** | 5 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 8 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 22,000 (rango ±25 %: S/ 16,500 – S/ 27,500) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 20,200 / año (Licencias: S/ 0 + Infraestructura: S/ 0 + Soporte 10 %: S/ 2,200 + Personal dedicado: S/ 18,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 6,000 (Capacitación inicial: S/ 6,000) · Costo de salida estimado: S/ 1,800. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 129,000 (rango ±25 %: S/ 96,750 – S/ 161,250; S/ 130,800 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Reducción del 60 % en el tiempo de inducción de nuevo personal de TI y ahorro de S/ 38,000/año al evitar sobrecostos por renovaciones tardías de licencias (PT01 +12.8 %) e infraestructura (PT03 +15.8 %). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-07 (Mesa de servicio de TI), sobre cuya plataforma se vinculan los activos (CI) a los tickets de incidentes y cambios. |
| **18** | **Riesgos principales y su tratamiento** | Desactualización progresiva de la CMDB tras su carga inicial -> Mitigación: actualización obligatoria del CI como paso de cierre de todo ticket de cambio en PR-07. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Analista de Gestión de Activos y Configuración de TI · **Área usuaria:** Área de TI y Administración y Finanzas (Control Patrimonial) |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de activos críticos, licencias y contratos registrados en la CMDB y >= 90 % de procedimientos críticos documentados y verificados al quinto mes. |


---

# Ficha Estandarizada de Proyecto · PR-11

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-11` |
| **2** | **Nombre del proyecto** | Comité de gobierno e inversiones de TI (casos de negocio y actas de beneficio) |
| **3** | **Fuente y sección de origen** | Brecha de capacidad · Sección 4.3.5 EDM01, APO05, EDM02 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-02, OD-04` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Los tres expedientes de inversión cerrados en 2024–2025 (INV01: S/ 260,819.96; INV02: S/ 75,773.21 con +20.6 % de desviación; INV03: S/ 224,964.21 con +24.5 % de desviación) evidencian que Agroexportadora Valle Viejo aprueba inversiones por pedidos verbales, sin caso de negocio, sin evaluar alternativas reales, sin control formal de desviaciones, sin actas de aceptación y sin medir jamás si el beneficio declarado se cumplió. Además, en pagos.csv existen 18 pagos informáticos auto-aprobados (registrado_por == aprobado_por) por S/ 48,144.00. |
| **7** | **Alcance incluido** | Constitución formal del Comité de Gobierno e Inversiones de TI; reglamento de admisión y priorización de proyectos (COBIT EDM01, APO05, EDM02 y Val IT); plantillas obligatorias de Caso de Negocio con 3 alternativas y TCO a 5 años, Acta de Aceptación y Auditoría Post-Implementación de Beneficios a los 6 y 12 meses; regla de segregación de funciones en aprobaciones de TI. |
| **8** | **Alcance excluido** | Adquisición de software comercial de gestión de portafolio (se implementa sobre herramientas colaborativas y tableros de PR-06). |
| **9** | **Entregables concretos** | 1) Reglamento y Acta de instalación del Comité de TI; 2) Procedimiento obligatorio de Caso de Negocio, Control de Cambios Presupuestales (umbral > 5 %) y Acta de Aceptación; 3) Matriz de segregación de funciones para órdenes de compra de TI (bloqueo de auto-aprobación); 4) Primer informe trimestral de seguimiento de beneficios. |
| **10** | **Duración estimada (meses)** | 2 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 3 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 6,000 (rango ±15 %: S/ 5,100 – S/ 6,900) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 3,000 / año (Licencias: S/ 0 + Infraestructura: S/ 0 + Soporte: S/ 0 + Personal dedicado a secretaría técnica: S/ 3,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 2,000 (Capacitación a comité y jefaturas: S/ 2,000) · Costo de salida: S/ 0. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 23,000 (rango ±15 %: S/ 19,550 – S/ 26,450)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Eliminación de sobrecostos no autorizados como los S/ 57,213.20 de desviación acumulada en INV02 (+20.6 %) e INV03 (+24.5 %) y erradicación del 100 % de pagos auto-aprobados (S/ 48,144.00/año). |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | No depende de ningún proyecto previo (inicia en el mes 1 de la Ola 1 para gobernar la ejecución de todo el portafolio). |
| **18** | **Riesgos principales y su tratamiento** | Inasistencia de gerentes de área a las sesiones del comité -> Mitigación: sesiones ejecutivas mensuales de 45 minutos vinculadas a la liberación de presupuesto de inversión PT06. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Gerente General / Jefe de TI (Secretario Técnico del Comité) · **Área usuaria:** Gerencia General, Administración y Finanzas, Jefatura de TI y Jefaturas de Área |
| **20** | **Criterio de éxito (con umbral verificable)** | 100 % de inversiones de TI > S/ 10,000 aprobadas con caso de negocio de 3 alternativas, TCO a 5 años, acta de aceptación firmada y medición post-implementación, y 0 pagos de TI auto-aprobados. |


---

# Ficha Estandarizada de Proyecto · PR-12

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-12` |
| **2** | **Nombre del proyecto** | Instrumentación de monitoreo y disponibilidad (cámaras de frío, enlace y ERP) |
| **3** | **Fuente y sección de origen** | Brecha de capacidad · Sección 4.3.5 DSS01 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-04` |
| **5** | **Categoría del portafolio** | **Operar** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Las caídas del enlace de planta (pese a la inversión INV02 de S/ 75,773.21), la saturación del servidor ERP o las alertas de conectividad en cámaras de frío son detectadas recién cuando los usuarios llaman por teléfono, impidiendo medir el tiempo real de actividad (uptime) ni actuar preventivamente. |
| **7** | **Alcance incluido** | Despliegue de plataforma centralizada de monitoreo de infraestructura, enlaces de comunicaciones (PT04), servicios de base de datos/ERP y nodos de telemetría de planta; alertas tempranas multicanal y tableros de disponibilidad SLA. |
| **8** | **Alcance excluido** | Renovación de equipos de refrigeración industrial (alcance de mantenimiento de planta). |
| **9** | **Entregables concretos** | 1) Servidor de monitoreo activo 24x7 sobre infraestructura resiliente (PR-08); 2) Sensores lógicos y agentes en servidores ERP, API Gateway, enlaces WAN y red de planta; 3) Sistema de alertas tempranas y reportes mensuales de disponibilidad. |
| **10** | **Duración estimada (meses)** | 3 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 5 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 19,000 (rango ±25 %: S/ 14,250 – S/ 23,750) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 11,880 / año (Licencias: S/ 2,400 + Infraestructura: S/ 1,200 + Soporte 12 %: S/ 2,280 + Personal dedicado: S/ 6,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 7,000 (Capacitación: S/ 3,000 + Integración con Mesa de Servicio: S/ 4,000) · Costo de salida estimado: S/ 1,500. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 85,400 (rango ±25 %: S/ 64,050 – S/ 106,750; S/ 86,900 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Reducción del tiempo medio de detección (MTTD) de incidentes críticos de 45 minutos a < 2 minutos, evitando paradas no planificadas en línea de empaque y despacho valorizadas en S/ 52,000/año. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-08 (Continuidad de infraestructura, enlace redundante y respaldo inmutable). |
| **18** | **Riesgos principales y su tratamiento** | Exceso de falsos positivos (fatiga de alertas) en el equipo técnico -> Mitigación: calibración de umbrales escalonados (warning/critical) durante las primeras 4 semanas. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Administrador de Redes e Infraestructura · **Área usuaria:** TI, Planta de Empaque y Operaciones |
| **20** | **Criterio de éxito (con umbral verificable)** | Disponibilidad medida >= 99.5 % en servicios críticos (ERP, API Gateway y enlace de planta) y generación automática de ticket en PR-07 ante cualquier caída. |


---

# Ficha Estandarizada de Proyecto · PR-13

**Organización:** Agroexportadora Valle Viejo S.A.C. (`EMPRESA-01-agroexportadora-valle-viejo`)  
**Sección del PETI:** 7.1.3 Fichas de proyecto  
**Clasificación:** Confidencial  

| N.º | Campo estandarizado | Detalle del proyecto |
|:---:|---|---|
| **1** | **Código del proyecto** | `PR-13` |
| **2** | **Nombre del proyecto** | Autoservicio digital de trabajadores de campo y planta (boletas, destajo y vacaciones) |
| **3** | **Fuente y sección de origen** | Brecha de servicio digital · Sección 6.1.7 S-06, S-07 |
| **4** | **Objetivo(s) al que contribuye (Sección 6.2)** | `OD-01, OD-05` |
| **5** | **Categoría del portafolio** | **Crecer** |
| **6** | **Problema u oportunidad que resuelve (con cifra del diagnóstico)** | Más de 1,200 trabajadores agrarios (jornaleros de cosecha a destajo y operarios de planta de empaque) deben acudir presencialmente a las oficinas de RR.HH. para recabar boletas de pago impresas, consultar liquidaciones de destajo o solicitar vacaciones, generando colas en días de pago, alto consumo de papel/útiles (S/ 1,559,086.42 en 'Útiles de oficina' en pagos.csv) y riesgo de incumplimiento en la entrega oportuna de boletas ante SUNAFIL (D.S. N.º 009-2011-TR). |
| **7** | **Alcance incluido** | Portal móvil ligero y kioscos digitales en planta/fundo para consulta y descarga de boletas de pago firmadas digitalmente, detalle de avance de destajo semanal, solicitud de vacaciones y constancias laborales, consumiendo servicios de planilla vía PR-03. |
| **8** | **Alcance excluido** | Cálculo contable de planilla agraria (reside en el ERP y se consolida en PR-09). |
| **9** | **Entregables concretos** | 1) Aplicación web/móvil de autoservicio del trabajador y 2 tótems de consulta en planta de empaque; 2) Motor de firma digital y constancia de recepción electrónica de boletas con validez ante SUNAFIL; 3) Integración con módulo de planillas vía PR-03. |
| **10** | **Duración estimada (meses)** | 4 meses |
| **11** | **Esfuerzo estimado (persona-mes)** | 7 persona-mes |
| **12** | **Inversión inicial (S/ y rango)** | S/ 26,000 (rango ±30 %: S/ 18,200 – S/ 33,800) |
| **13** | **Costo operativo anual (S/ desglosado)** | S/ 18,900 / año (Licencias firma/notificación: S/ 3,600 + Infraestructura: S/ 2,400 + Soporte 15 %: S/ 3,900 + Personal dedicado: S/ 9,000) |
| **14** | **Costos únicos complementarios y costo de salida** | Costos únicos adicionales: S/ 15,000 (Capacitación: S/ 5,000 + Migración de históricos: S/ 4,000 + Integración: S/ 6,000) · Costo de salida estimado: S/ 2,200. |
| **15** | **Costo Total de Propiedad — TCO a 5 años (S/ y rango)** | **S/ 135,500 (rango ±30 %: S/ 94,850 – S/ 176,150; S/ 137,700 incluyendo costo de salida)** |
| **16** | **Beneficio cuantificado (S/ o métrica del indicador)** | Ahorro de S/ 64,000/año en impresión, distribución física y horas administrativas de RR.HH. (14,400 boletas anuales), evitando además multas laborales de SUNAFIL y eliminando traslados presenciales de trabajadores desde los fundos. |
| **17** | **Dependencias (proyectos de los que depende y proyectos que habilita)** | Depende de PR-03 (Capa de integración de servicios API) para consultar planillas del ERP de forma segura. |
| **18** | **Riesgos principales y su tratamiento** | Trabajadores de campo sin smartphone o sin plan de datos -> Mitigación: habilitación de 2 kioscos táctiles en comedor de planta/fundo y envío gratuito por SMS/WhatsApp ligero. |
| **19** | **Responsable propuesto (cargo) y Área usuaria** | **Responsable:** Jefe de Aplicaciones / Jefe de Recursos Humanos · **Área usuaria:** Recursos Humanos y Trabajadores de Campo y Planta de Empaque |
| **20** | **Criterio de éxito (con umbral verificable)** | >= 85 % de boletas de pago entregadas con constancia electrónica dentro del tercer día hábil posterior al pago y reducción del 80 % en atención presencial en ventanilla de RR.HH. al cuarto mes. |
