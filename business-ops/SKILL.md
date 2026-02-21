---
name: Operaciones de Negocio & Escalamiento
description: CRO (Conversion Rate Optimization), analytics, pricing strategy, dashboards de reportes, SOPs, y estrategias para escalar la agencia Valtyk Solutions.
---

# 💼 Operaciones de Negocio — Skill Guide

## Cuándo usar esta skill
- Al definir precios y paquetes de servicio
- Al crear reportes y dashboards para clientes
- Al optimizar tasas de conversión en landing pages
- Al documentar procesos (SOPs) para escalar
- Al planificar el crecimiento de la agencia

---

## 1. Pricing Strategy (Estrategia de Precios)

### Modelo de Pricing por Valor
```
REGLA FUNDAMENTAL:
"No cobres por horas, cobra por el valor que generas"

Si tu landing page le consigue al doctor 5 pacientes nuevos al mes,
y cada paciente genera ~$800 por consulta:
→ Valor mensual generado = $4,000 MXN
→ Tu servicio de $1,000/mes = 25% del valor
→ ROI del cliente = 4x

JUSTIFICACIÓN DE PRECIO:
"Por $1,000/mes, usted obtiene en promedio $4,000 en nuevos pacientes.
Eso es un retorno de 4 a 1 en su inversión."
```

### Estructura de Paquetes
```
📦 STARTER — $2,500 setup + $500/mes
   Ideal para: Quien empieza y quiere presencia básica
   ✓ Landing page (template personalizado)
   ✓ WhatsApp button flotante
   ✓ Google Business Profile (setup)
   ✓ SEO básico (meta tags, schema)
   ✓ Hosting incluido
   ✗ Sin sistema de citas
   ✗ Sin automatizaciones
   ✗ Sin reportes

📦 GROWTH — $5,000 setup + $1,200/mes
   Ideal para: Quien quiere automatizar su consultorio
   ✓ Todo de Starter
   ✓ Diseño premium con animaciones (GSAP + Lottie)
   ✓ Sistema de agendamiento Cal.com
   ✓ Google Calendar sync  
   ✓ Confirmaciones por email automáticas
   ✓ SEO local completo
   ✓ Google Analytics + Search Console
   ✓ Reporte mensual básico
   ★ PAQUETE RECOMENDADO

📦 SCALE — $8,000 setup + $2,500/mes
   Ideal para: Quien quiere máximo crecimiento
   ✓ Todo de Growth
   ✓ Confirmaciones por WhatsApp
   ✓ Recordatorios automáticos (-24h)
   ✓ Solicitud de reviews automática
   ✓ 4 posts/mes en Google Business
   ✓ Google Ads management (presupuesto aparte)
   ✓ Dashboard de métricas en tiempo real
   ✓ Reporte ejecutivo mensual
   ✓ Soporte prioritario (respuesta <4h)
   ✓ Llamada mensual de estrategia
```

### Descuentos y Ofertas
```
🎯 Descuento por pago anual:
   Mensual: $1,200/mes = $14,400/año
   Anual: $12,000/año (ahorra 2 meses) = $1,000/mes efectivo

🎯 Referidos:
   "Si refieres a un colega, ambos reciben 1 mes gratis"

🎯 Early adopter:
   "Primeros 10 clientes: setup al 50%"
```

---

## 2. CRO (Conversion Rate Optimization)

### Métricas de Conversión
```
Definiciones:
  Visita → Landing page = "Sesión"
  Clic en CTA = "Engagement"
  Agenda cita / envía WhatsApp = "Conversión"
  
  Tasa de conversión = Conversiones / Sesiones × 100

Benchmarks:
  Landing page general: 2-5%
  Landing page optimizada: 5-15%
  Landing page de salud/servicios locales: 8-20%
  
Meta: El landing page de cada cliente debe convertir >5%
```

### Elementos que Mejoran Conversión
```
1. HERO SECTION (impacto inmediato)
   ✓ Headline claro y directo
   ✓ Subtítulo con beneficio principal
   ✓ CTA visible above-the-fold
   ✓ Imagen del profesionista (genera confianza)
   ✓ Badge de credibilidad ("15+ años de experiencia")

2. SOCIAL PROOF (confianza)
   ✓ Rating de Google (4.9 ★)
   ✓ Número de pacientes/clientes atendidos
   ✓ Testimonios con foto y nombre
   ✓ Logos de certificaciones
   ✓ "Featured in" badges

3. FRICCIÓN REDUCIDA (facilidad)
   ✓ Formulario de máximo 3-4 campos
   ✓ WhatsApp en 1 clic
   ✓ Calendario visible inline
   ✓ Precios transparentes
   ✓ FAQ que resuelve dudas comunes

4. URGENCIA (acción)
   ✓ "Lugares disponibles esta semana"
   ✓ "Consulta los [día] y [día]"
   ✓ Horarios visibles en el calendario
   ✓ "Respuesta en menos de 2 horas"

5. MÚLTIPLES CTAs
   ✓ CTA en hero (arriba)
   ✓ CTA después de servicios (medio)
   ✓ CTA flotante (sticky WhatsApp)
   ✓ CTA al final (bottom)
   ✓ CTA en el navbar
```

### A/B Testing Básico
```
Qué testear (en orden de impacto):
1. Headline principal
2. CTA text ("Agendar cita" vs "Hablar con la Dra.")
3. Imagen del hero
4. Precio visible vs. oculto
5. Color del botón CTA
6. Orden de secciones

Herramientas gratuitas:
- Google Optimize (descontinuado, usar alternativas)
- Hotjar (heatmaps, recordings, free tier)
- Microsoft Clarity (heatmaps, gratis 100%)
```

---

## 3. Analytics & Dashboards

### Google Analytics 4 — Events Clave
```javascript
// Tracking de eventos importantes en la landing page

// Clic en CTA de agendar cita
document.querySelector('.cta-booking').addEventListener('click', () => {
  gtag('event', 'clic_agendar_cita', {
    event_category: 'conversion',
    event_label: 'hero_cta'
  });
});

// Clic en WhatsApp
document.querySelector('.whatsapp-btn').addEventListener('click', () => {
  gtag('event', 'clic_whatsapp', {
    event_category: 'conversion',
    event_label: 'whatsapp_float'
  });
});

// Scroll depth (ver cuánto bajan)
let scrollThresholds = [25, 50, 75, 100];
let scrollFired = {};
window.addEventListener('scroll', () => {
  const scrollPercent = Math.round(
    (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
  );
  scrollThresholds.forEach(threshold => {
    if (scrollPercent >= threshold && !scrollFired[threshold]) {
      scrollFired[threshold] = true;
      gtag('event', 'scroll_depth', {
        event_category: 'engagement',
        event_label: `${threshold}%`
      });
    }
  });
});

// Tiempo en página
setTimeout(() => {
  gtag('event', 'tiempo_en_pagina', {
    event_category: 'engagement',
    event_label: '30_segundos'
  });
}, 30000);

setTimeout(() => {
  gtag('event', 'tiempo_en_pagina', {
    event_category: 'engagement',
    event_label: '60_segundos'
  });
}, 60000);
```

### Google Analytics 4 — Setup
```html
<!-- GA4 tag (agregar en <head>) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Looker Studio Dashboard
```
Crear dashboard en https://lookerstudio.google.com con:

Página 1: Resumen General
  - Scorecard: Usuarios totales (con comparación)
  - Scorecard: Sesiones
  - Scorecard: Tasa de conversión
  - Gráfica de líneas: Usuarios por día (30 días)
  - Tabla: Top 5 fuentes de tráfico
  - Gráfica de pastel: Dispositivos (mobile vs desktop)

Página 2: SEO Performance
  - Conectar Google Search Console
  - Scorecard: Impresiones, Clics, CTR, Posición promedio
  - Tabla: Top 20 queries con clics e impresiones
  - Gráfica de líneas: Impresiones por día

Página 3: Conversiones
  - Eventos de conversión (clics en CTA, WhatsApp)
  - Funnel: Visita → Scroll 50% → Clic CTA → Agendó cita
  - Tabla: Conversiones por fuente de tráfico
```

---

## 4. SOPs (Standard Operating Procedures)

### SOP: Crear Nueva Landing Page
```
TIEMPO ESTIMADO: 8-12 horas
RESPONSABLE: Valtyk (Admin)

PASO 1: Preparación (1h)
  □ Revisar formulario de onboarding completado
  □ Investigar industria/competencia del cliente
  □ Seleccionar paleta de colores apropiada
  □ Identificar keywords locales

PASO 2: Estructura (1h)
  □ Crear directorio del proyecto:
    - /clients/[nombre-cliente]/public/
  □ Copiar template base desde /templates/
  □ Personalizar firebase.json y .firebaserc
  □ Configurar target de Firebase Hosting

PASO 3: Contenido (2h)
  □ Reescribir todos los textos con info del cliente
  □ Aplicar fórmulas de copywriting (PAS, AIDA)
  □ Crear CTAs específicos
  □ Escribir FAQ (mínimo 5 preguntas)
  □ Escribir bio profesional

PASO 4: Diseño (2h)
  □ Aplicar colores del cliente en custom.css
  □ Subir fotos del cliente (optimizar a WebP)
  □ Ajustar responsive
  □ Agregar animaciones GSAP
  □ Agregar Lottie animations

PASO 5: SEO (1h)
  □ Title tag optimizado
  □ Meta description
  □ Schema markup (LocalBusiness, FAQ, Person)
  □ Alt text en imágenes
  □ Sitemap.xml
  □ Open Graph tags

PASO 6: Integraciones (1h)
  □ Cal.com embed
  □ WhatsApp button
  □ Google Analytics
  □ Google Search Console verification

PASO 7: Deploy (30min)
  □ firebase deploy --only hosting:nombre-cliente
  □ Verificar DNS/dominio
  □ Verificar SSL
  □ Test en mobile
  □ PageSpeed test (meta: >90)

PASO 8: Entrega (30min)
  □ Enviar URL al cliente
  □ Enviar credenciales de Cal.com
  □ Explicar cómo funciona todo
  □ Programar check-in en 1 semana
```

### SOP: Reporte Mensual de Cliente
```
TIEMPO ESTIMADO: 1 hora por cliente
FRECUENCIA: Primer lunes de cada mes
RESPONSABLE: Valtyk (Admin)

PASO 1: Recopilar Datos (20min)
  □ Google Analytics: usuarios, sesiones, fuentes
  □ Google Search Console: queries, impresiones, clics
  □ Cal.com: citas agendadas del mes
  □ Google Business: views, clicks, calls
  □ Reviews: nuevas reviews del mes

PASO 2: Analizar (15min)
  □ Comparar con mes anterior
  □ Identificar tendencias
  □ Identificar problemas
  □ Preparar recomendaciones

PASO 3: Crear Reporte (15min)
  □ Usar template de Gamma/Canva
  □ Incluir métricas clave con comparación
  □ Incluir gráficas (screenshots de GA4/SC)
  □ Incluir acciones realizadas
  □ Incluir plan para próximo mes

PASO 4: Enviar (10min)
  □ Exportar como PDF
  □ Enviar por email al cliente
  □ Si hay paquete Premium: programar llamada
```

---

## 5. Business Model Canvas — Valtyk Solutions

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALTYK SOLUTIONS                              │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│ KEY PARTNERS │ KEY          │ VALUE        │ CUSTOMER           │
│              │ ACTIVITIES   │ PROPOSITION  │ RELATIONSHIPS      │
│ • Firebase   │ • Web design │ "Sistema     │ • Personal         │
│ • Cal.com    │ • SEO local  │  digital     │   (onboarding)     │
│ • n8n        │ • Automation │  completo    │ • Automated        │
│ • Google     │ • Client     │  para que    │   (emails, WA)     │
│ • Hostinger  │   management │  te          │ • Monthly          │
│              │ • Marketing  │  encuentren  │   reports          │
│              │              │  y agenden   │                    │
│              │              │  solos"      │                    │
├──────────────┤              ├──────────────┤                    │
│ KEY          │              │ CHANNELS     │ CUSTOMER           │
│ RESOURCES    │              │              │ SEGMENTS           │
│              │              │ • Referral   │                    │
│ • Technical  │              │ • Google     │ • Doctores         │
│   skills     │              │ • Instagram  │ • Abogados         │
│ • Templates  │              │ • WhatsApp   │ • Psicólogos       │
│ • Cal.com    │              │ • Cold email │ • Dentistas        │
│   license    │              │ • Networking │ • Nutriólogos      │
│ • VPS        │              │              │ • Coaches          │
│              │              │              │ • Arquitectos      │
├──────────────┴──────────────┴──────────────┴────────────────────┤
│ COST STRUCTURE                 │ REVENUE STREAMS                │
│                                │                                │
│ • Hostinger VPS: ~$200/mes     │ • Setup fee: $2,500-$8,000     │
│ • Cal.com license: $15/mes     │ • Monthly retainer: $500-$2,500│
│ • Domain: ~$200/año            │ • Add-ons: Google Ads mgmt     │
│ • Tools (Canva, etc): ~$0      │ • Referral bonus               │
│ • Tiempo personal: principal   │                                │
│   costo                        │ Meta: 10 clientes × $1,200/mes │
│                                │ = $12,000 MXN/mes recurrente   │
│ Total fijo: ~$300/mes          │                                │
└────────────────────────────────┴────────────────────────────────┘
```

---

## 6. Escalamiento: Roadmap de Ingresos

```
FASE 1: VALIDACIÓN (Mes 1-3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Meta: 3 clientes activos
Ingreso: ~$3,600/mes recurrente + setup
Enfoque: Perfeccionar el producto y proceso
KPI: Time to deliver < 14 días

FASE 2: CRECIMIENTO (Mes 4-6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Meta: 8 clientes activos
Ingreso: ~$9,600/mes recurrente
Enfoque: Referrals + marketing propio
KPI: Referral rate > 30%

FASE 3: ESCALA (Mes 7-12)
━━━━━━━━━━━━━━━━━━━━━━━━━
Meta: 15-20 clientes activos
Ingreso: ~$18,000-$24,000/mes recurrente
Enfoque: Contratar ayuda (diseñador/VA)
KPI: Churn rate < 5%

FASE 4: OPERACIÓN (Año 2)
━━━━━━━━━━━━━━━━━━━━━━━━━
Meta: 30+ clientes
Ingreso: $30,000+/mes
Enfoque: Sistematizar, delegar, nuevos servicios
KPI: Revenue per employee
```

---

## 7. Recursos de Aprendizaje

### Certificaciones Relevantes
- [HubSpot Agency Partner](https://academy.hubspot.com/) — Gratis
- [Google Analytics 4](https://skillshop.withgoogle.com/) — Gratis
- [Google Ads](https://skillshop.withgoogle.com/) — Gratis

### Herramientas de CRO
- [Hotjar](https://hotjar.com) — Heatmaps gratis
- [Microsoft Clarity](https://clarity.microsoft.com) — 100% gratis
- [PageSpeed Insights](https://pagespeed.web.dev/) — Performance

### Dashboards
- [Looker Studio](https://lookerstudio.google.com/) — Gratis
- [Google Sheets + Charts MCP] — Ya lo tienes integrado
