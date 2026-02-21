---
name: Google Ads & PPC
description: Guía de campañas de Google Ads — búsqueda, display, remarketing, presupuestos, y optimización para profesionistas locales.
---

# 📱 Google Ads & PPC — Skill Guide

## Cuándo usar esta skill
- Al activar publicidad pagada para un cliente
- Al crear campañas de búsqueda local
- Al optimizar el presupuesto de ads
- Al configurar remarketing

---

## 1. Estructura de Cuenta

### Jerarquía
```
Cuenta de Google Ads (Valtyk — MCC Manager)
  └── Cuenta de Cliente (Dra. Tabatha)
       └── Campaña: "Psiquiatra Guadalajara — Búsqueda"
            ├── Ad Group: "Consulta Psiquiátrica"
            │    ├── Keywords: psiquiatra guadalajara, consulta psiquiátrica
            │    └── Anuncios: 3 variaciones
            ├── Ad Group: "Depresión y Ansiedad"
            │    ├── Keywords: tratamiento depresión, doctor ansiedad
            │    └── Anuncios: 3 variaciones
            └── Ad Group: "Consulta en Línea"
                 ├── Keywords: psiquiatra en línea, consulta online
                 └── Anuncios: 3 variaciones
```

### Cuenta MCC (Manager)
```
Crear cuenta MCC en: https://ads.google.com/intl/es/home/tools/manager-accounts/
Beneficios:
  ✓ Manejar múltiples clientes desde una cuenta
  ✓ Facturación centralizada
  ✓ Reportes comparativos
  ✓ Acceso sin compartir credenciales
```

---

## 2. Campaña de Búsqueda Local

### Keywords para Profesionistas
```
Tipo: [Exact Match]
  [psiquiatra en guadalajara]
  [consulta psiquiatrica guadalajara]
  [mejor psiquiatra guadalajara]

Tipo: "Phrase Match"
  "psiquiatra guadalajara"
  "consulta psiquiatrica"
  "doctor para ansiedad"

Negativos (excluir):
  -gratis
  -gratuito
  -pdf
  -trabajo
  -empleo
  -universidad
  -que es (búsquedas informativas)
```

### Estructura del Anuncio
```
Headline 1 (30 chars): Psiquiatra en Guadalajara
Headline 2 (30 chars): Agenda tu Cita Hoy
Headline 3 (30 chars): 15+ Años de Experiencia

Description 1 (90 chars): 
Consultas presenciales y en línea. Depresión, ansiedad, insomnio. Agenda en 30 seg.

Description 2 (90 chars):
Dra. Tabatha Barron. Horario L-V 9am-6pm. Primera consulta $800 MXN. Sin lista de espera.

Sitelinks:
  - Agendar Cita → /agendar
  - Servicios → /#servicios
  - Sobre la Dra. → /#bio
  - Ubicación → /#contacto

Callout Extensions:
  - ✓ Consulta en Línea
  - ✓ Sin lista de espera
  - ✓ 500+ pacientes
  - ✓ Ambiente cálido

Call Extension: +52 33 XXXX XXXX
Location Extension: Dirección del consultorio
```

---

## 3. Presupuestos Recomendados

### Para Profesionistas Locales (México)
```
MÍNIMO VIABLE:
  Presupuesto diario: $100 MXN (~$5 USD)
  Mensual: ~$3,000 MXN
  Clics esperados: 100-200/mes
  CPC promedio: $15-30 MXN
  Conversiones estimadas: 5-15 citas/mes

RECOMENDADO:
  Presupuesto diario: $200-300 MXN
  Mensual: ~$6,000-9,000 MXN
  Clics esperados: 200-500/mes
  Conversiones estimadas: 15-40 citas/mes

PREMIUM:
  Presupuesto diario: $500+ MXN
  Mensual: $15,000+ MXN
  Para mercados muy competitivos
```

### ROI Esperado
```
Costo por clic (CPC): $20 MXN promedio
Tasa de conversión landing: 10%
Costo por conversión: $200 MXN
Valor de un paciente: $800 MXN (primera consulta)
ROI: 4x (por cada $200 invertidos, ganas $800)

Si el paciente regresa (4 seguimientos):
  Valor lifetime: $800 + (4 × $500) = $2,800 MXN
  ROI lifetime: 14x
```

---

## 4. Remarketing

### Configuración
```
1. Instalar Google Ads tag en landing page:

<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXX');
</script>

2. Crear audiencia: "Visitantes que NO agendaron"
   → Personas que visitaron la landing pero no convirtieron
   → Mostrar anuncios de display recordándoles

3. Crear campaña de Display con remarketing
   → Presupuesto: $50/día
   → Banners con: foto del doctor + CTA "¿Aún buscas psiquiatra?"
```

---

## 5. Conversiones

### Tracking de Conversiones
```javascript
// Cuando el usuario agenda cita exitosamente:
gtag('event', 'conversion', {
  'send_to': 'AW-XXXXXXXX/AbCdEfGh',
  'value': 800,
  'currency': 'MXN'
});

// Cuando hace clic en WhatsApp:
gtag('event', 'conversion', {
  'send_to': 'AW-XXXXXXXX/IjKlMnOp',
  'value': 400,
  'currency': 'MXN'
});
```

---

## 6. Fee de Valtyk por Google Ads Management

```
Modelo sugerido:
  Setup inicial: $1,500 MXN (una vez)
  Management mensual: 15-20% del presupuesto de ads
    Ejemplo: Si el cliente gasta $5,000/mes en ads
    Fee de Valtyk: $750-1,000/mes

Mínimo mensual: $500 MXN de fee
Incluye: Setup, optimización semanal, reporte mensual
```

---

## 7. Certificación
- [Google Ads Search](https://skillshop.withgoogle.com/) — Gratis, ~4h
- [Google Ads Display](https://skillshop.withgoogle.com/) — Gratis, ~3h
- [Google Ads Measurement](https://skillshop.withgoogle.com/) — Gratis, ~3h
