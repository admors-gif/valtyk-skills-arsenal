---
name: Analytics & A/B Testing
description: Guía de analytics avanzado, heatmaps, A/B testing, y optimización basada en datos para landing pages de clientes.
---

# 🧪 Analytics & A/B Testing — Skill Guide

## Cuándo usar esta skill
- Al implementar tracking en una landing page
- Al analizar el comportamiento de usuarios
- Al optimizar tasas de conversión con datos
- Al crear reportes basados en datos reales

---

## 1. Stack de Analytics Gratuito

### Herramientas
```
OBLIGATORIO (en cada landing):
  ✓ Google Analytics 4 → Tráfico, fuentes, conversiones
  ✓ Google Search Console → SEO, keywords, indexación

RECOMENDADO:
  ✓ Microsoft Clarity → Heatmaps, recordings (100% gratis)
  ✓ Hotjar → Heatmaps, surveys (gratis hasta 35 sessions/día)

AVANZADO:
  ○ Looker Studio → Dashboards automáticos
  ○ Google Tag Manager → Gestión de tags centralizada
```

---

## 2. Microsoft Clarity (Heatmaps Gratis)

### Setup
```html
<!-- Agregar en <head> de cada landing page -->
<script type="text/javascript">
  (function(c,l,a,r,i,t,y){
    c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  })(window, document, "clarity", "script", "PROJECT_ID");
</script>
```

### Qué Analizar
```
HEATMAPS:
  → ¿Dónde hacen clic más?
  → ¿Hasta dónde scrollean?
  → ¿Qué secciones ignoran?
  → ¿Hacen clic en elementos no clickeables?

RECORDINGS:
  → Ver sesiones reales de usuarios
  → Identificar puntos de confusión
  → Ver dónde abandonan
  → Ver si encuentran el CTA

INSIGHTS:
  → Dead clicks (clic sin resultado)
  → Rage clicks (frustración)
  → Excessive scrolling
  → Quick backs (vuelven rápido)
```

---

## 3. Google Tag Manager (GTM)

### Setup
```html
<!-- Agregar inmediatamente después de <head> -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>

<!-- Agregar inmediatamente después de <body> -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Tags Comunes
```
Tags a configurar en GTM:
  1. Google Analytics 4 → Config tag
  2. Conversión de cita → Event tag (click en CTA)
  3. Conversión WhatsApp → Event tag
  4. Scroll tracking → Trigger al 25%, 50%, 75%, 100%
  5. Microsoft Clarity → Custom HTML tag
  6. Facebook Pixel → Custom HTML tag (si corren ads)
  7. Google Ads remarketing → Ads conversion tag
```

---

## 4. A/B Testing

### Qué Testear (por orden de impacto)
```
ALTO IMPACTO:
  1. Headline del hero
  2. Texto del CTA principal
  3. Imagen del hero (con doctor vs sin doctor)
  4. Mostrar precios vs ocultarlos
  
MEDIO IMPACTO:
  5. Color del botón CTA
  6. Orden de secciones
  7. Número de testimonios
  8. Layout de servicios (cards vs lista)

BAJO IMPACTO:
  9. Tipografía
  10. Colores de fondo
  11. Tamaño de padding
```

### A/B Test con JavaScript (sin herramientas)
```javascript
// A/B test simple con JavaScript puro
function getVariant() {
  // Verificar si ya tiene variante asignada
  let variant = localStorage.getItem('ab_hero_test');
  if (!variant) {
    variant = Math.random() < 0.5 ? 'A' : 'B';
    localStorage.setItem('ab_hero_test', variant);
  }
  return variant;
}

const variant = getVariant();

if (variant === 'A') {
  // Control: Headline original
  document.querySelector('.hero-title').textContent = 
    'Psiquiatra en Guadalajara';
} else {
  // Variante B: Headline con beneficio
  document.querySelector('.hero-title').textContent = 
    'Recupera tu bienestar mental con ayuda profesional';
}

// Trackear qué variante vio
gtag('event', 'ab_test_view', {
  test_name: 'hero_headline',
  variant: variant
});

// Trackear conversión con variante
document.querySelector('.cta-btn').addEventListener('click', () => {
  gtag('event', 'ab_test_conversion', {
    test_name: 'hero_headline',
    variant: variant
  });
});
```

### Cuánto Tiempo Correr un Test
```
Regla general:
  Mínimo: 2 semanas
  Ideal: 4 semanas
  Mínimo de visitantes: 100 por variante
  Mínimo de conversiones: 20 por variante

Herramienta para calcular:
  https://www.evanmiller.org/ab-testing/sample-size.html

No tomar decisiones con menos de 95% de confianza estadística
```

---

## 5. KPIs por Tipo de Landing Page

```
Landing de Profesionista de Salud:
  → Tasa de conversión (visita → cita): meta >8%
  → Tasa de scroll al CTA: meta >60%
  → Bounce rate: meta <45%
  → Tiempo en página: meta >90 seg
  → Clics en WhatsApp: tracking obligatorio

Landing de Abogado:
  → Tasa de conversión (visita → contacto): meta >5%
  → Formulario completado: tracking obligatorio
  → Llamadas desde landing: call tracking

Landing de Coach/Bienestar:
  → Tasa de conversión: meta >10% (nicho motivado)
  → Leads de email: tracking obligatorio
```
