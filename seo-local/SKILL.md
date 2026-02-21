---
name: SEO Local & Posicionamiento
description: Guía completa de SEO local para profesionistas independientes — Google Business Profile, Schema Markup, Search Console, Analytics, y técnicas de posicionamiento para negocios locales.
---

# 🔍 SEO Local & Posicionamiento — Skill Guide

## Cuándo usar esta skill
- Al configurar una nueva landing page de cliente
- Al crear el perfil de Google Business del cliente
- Al optimizar una página existente para búsquedas locales
- Al generar reportes de posicionamiento para clientes

---

## 1. SEO On-Page para Landing Pages

### Meta Tags Esenciales
```html
<!-- TITLE TAG: 50-60 caracteres, incluir ciudad + servicio -->
<title>Psiquiatra en Guadalajara | Dra. Tabatha Barron — Consultas</title>

<!-- META DESCRIPTION: 150-160 caracteres, incluir CTA -->
<meta name="description" content="Psiquiatra en Guadalajara con 15+ años de experiencia. Consultas presenciales y en línea. Depresión, ansiedad, insomnio. Agenda tu cita hoy.">

<!-- CANONICAL URL -->
<link rel="canonical" href="https://tabatha-barron.valtyk.com/">

<!-- OPEN GRAPH -->
<meta property="og:title" content="Dra. Tabatha Barron — Psiquiatra en Guadalajara">
<meta property="og:description" content="Consultas psiquiátricas presenciales y en línea. Agenda tu cita.">
<meta property="og:image" content="https://tabatha-barron.valtyk.com/assets/og-image.jpg">
<meta property="og:url" content="https://tabatha-barron.valtyk.com/">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">

<!-- TWITTER CARD -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Dra. Tabatha Barron — Psiquiatra en Guadalajara">
<meta name="twitter:description" content="Consultas psiquiátricas presenciales y en línea.">
<meta name="twitter:image" content="https://tabatha-barron.valtyk.com/assets/og-image.jpg">

<!-- GEO TAGS (para SEO local) -->
<meta name="geo.region" content="MX-JAL">
<meta name="geo.placename" content="Guadalajara">
<meta name="geo.position" content="20.6597;-103.3496">
<meta name="ICBM" content="20.6597, -103.3496">
```

### Estructura de Headings
```html
<!-- REGLA: Solo 1 H1 por página -->
<h1>Psiquiatra en Guadalajara — Dra. Tabatha Barron</h1>

<!-- H2 para secciones principales -->
<h2>Servicios de Psiquiatría</h2>
<h2>Condiciones que Tratamos</h2>
<h2>Sobre la Dra. Tabatha</h2>
<h2>Proceso de Consulta</h2>
<h2>Preguntas Frecuentes</h2>
<h2>Ubicación y Contacto</h2>

<!-- H3 para sub-secciones -->
<h3>Consulta Psiquiátrica Inicial</h3>
<h3>Seguimiento y Control</h3>
```

### Optimización de Imágenes
```html
<!-- Usar WebP, incluir alt descriptivo con keywords -->
<img
  src="dra-tabatha-barron-psiquiatra-guadalajara.webp"
  alt="Dra. Tabatha Barron, psiquiatra en Guadalajara, en su consultorio"
  width="600"
  height="400"
  loading="lazy"
>

<!-- Nombres de archivo descriptivos (NO: img001.jpg) -->
<!-- SÍ: consultorio-psiquiatrico-guadalajara.webp -->
<!-- SÍ: dra-tabatha-barron-psiquiatra.webp -->
```

---

## 2. Schema Markup (Datos Estructurados)

### Schema para Profesionista de Salud
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://tabatha-barron.valtyk.com/#business",
  "name": "Dra. Tabatha Barron — Psiquiatra",
  "description": "Consulta psiquiátrica en Guadalajara. Especialista en depresión, ansiedad, insomnio y TDAH.",
  "url": "https://tabatha-barron.valtyk.com",
  "telephone": "+52-33-XXXX-XXXX",
  "email": "contacto@ejemplo.com",
  "image": "https://tabatha-barron.valtyk.com/assets/dra-tabatha.webp",
  "priceRange": "$$",
  "currenciesAccepted": "MXN",
  "paymentAccepted": "Efectivo, Tarjeta, Transferencia",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Av. Ejemplo 123, Col. Centro",
    "addressLocality": "Guadalajara",
    "addressRegion": "Jalisco",
    "postalCode": "44100",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 20.6597,
    "longitude": -103.3496
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "47"
  },
  "medicalSpecialty": "Psychiatric",
  "availableService": [
    {
      "@type": "MedicalProcedure",
      "name": "Consulta Psiquiátrica Inicial",
      "description": "Evaluación completa con diagnóstico y plan de tratamiento",
      "howPerformed": "Presencial o en línea",
      "offers": {
        "@type": "Offer",
        "price": "800",
        "priceCurrency": "MXN"
      }
    },
    {
      "@type": "MedicalProcedure",
      "name": "Consulta de Seguimiento",
      "description": "Revisión de avance y ajuste de tratamiento"
    }
  ]
}
</script>
```

### Schema FAQ
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cuánto cuesta una consulta psiquiátrica?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La consulta inicial tiene un costo de $800 MXN y dura aproximadamente 40 minutos."
      }
    },
    {
      "@type": "Question",
      "name": "¿Ofrecen consultas en línea?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sí, ofrecemos consultas por videollamada con la misma calidad de atención."
      }
    }
  ]
}
</script>
```

### Schema para Profesional (Breadcrumb, Person)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Dra. Tabatha Barron",
  "jobTitle": "Psiquiatra",
  "worksFor": {
    "@type": "MedicalBusiness",
    "name": "Consultorio Psiquiátrico Dra. Tabatha Barron"
  },
  "alumniOf": "Universidad de Guadalajara",
  "knowsAbout": ["Psiquiatría", "Depresión", "Ansiedad", "TDAH", "Insomnio"]
}
</script>
```

---

## 3. Google Business Profile — Setup

### Checklist de Optimización
- [ ] **NAP Consistente:** Nombre, Dirección y Teléfono IDÉNTICOS en todos lados
- [ ] **Categoría Principal:** Elegir la más específica (ej: "Psiquiatra" no "Médico")
- [ ] **Categorías Secundarias:** Agregar 2-3 relevantes
- [ ] **Descripción:** 750 caracteres con keywords naturales
- [ ] **Horarios:** Correctos y actualizados
- [ ] **Fotos:** Mínimo 10 (fachada, interior, equipo, servicios)
- [ ] **Posts:** Publicar 1-2 por semana (ofertas, tips, novedades)
- [ ] **Reviews:** Pedir reviews activamente (link directo)
- [ ] **Q&A:** Responder todas las preguntas
- [ ] **Servicios:** Listar cada servicio con precio y descripción
- [ ] **Atributos:** Marcar todos los relevantes (WiFi, accesibilidad, etc.)
- [ ] **Reservas:** Conectar con Cal.com si es posible
- [ ] **Sitio Web:** Apuntar a la landing page

### Cómo Obtener el Link Directo de Reviews
```
https://search.google.com/local/writereview?placeid=PLACE_ID_AQUI
```
Encontrar el Place ID en: https://developers.google.com/maps/documentation/places/web-service/place-id

---

## 4. Keywords para Profesionistas Locales

### Fórmula de Keywords
```
[Especialidad] + en + [Ciudad]
[Especialidad] + [Colonia/Zona]
[Especialidad] + cerca de mí
mejor + [especialidad] + en + [ciudad]
[especialidad] + consulta en línea
[especialidad] + costo consulta + [ciudad]
```

### Ejemplo para Psiquiatra en Guadalajara
```
Primarias (volumen alto):
- psiquiatra en guadalajara
- psiquiatra guadalajara
- consulta psiquiátrica guadalajara

Secundarias (volumen medio):
- mejor psiquiatra en guadalajara
- psiquiatra cerca de mí
- psiquiatra en línea guadalajara
- consulta psiquiátrica precio guadalajara

Long-tail (baja competencia):
- psiquiatra especialista en depresión guadalajara
- psiquiatra para ansiedad en guadalajara
- consulta psiquiátrica en línea jalisco
- psiquiatra mujer en guadalajara
- tratamiento para insomnio guadalajara
```

---

## 5. Google Search Console — Setup

### Verificación del sitio
1. Ir a https://search.google.com/search-console
2. Agregar propiedad → Prefijo de URL → `https://tabatha-barron.valtyk.com`
3. Verificar con meta tag HTML:
```html
<meta name="google-site-verification" content="CODIGO_VERIFICACION">
```

### Enviar Sitemap
Crear `sitemap.xml` en la raíz:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://tabatha-barron.valtyk.com/</loc>
    <lastmod>2026-02-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

### Métricas Clave a Monitorear
- **Impresiones:** Cuántas veces aparece en búsquedas
- **Clics:** Cuántas veces hacen clic
- **CTR:** Click-through rate (meta: >5%)
- **Posición promedio:** Meta: primeras 5 posiciones
- **Queries:** Qué buscan para encontrarte

---

## 6. Performance & Core Web Vitals

### Métricas Objetivo
```
LCP (Largest Contentful Paint): < 2.5s
FID (First Input Delay): < 100ms
CLS (Cumulative Layout Shift): < 0.1
```

### Optimizaciones Clave
```html
<!-- Preload de fuentes críticas -->
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>

<!-- Preconnect a CDNs -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Imágenes responsive -->
<img
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1024px) 800px, 1200px"
  src="hero-800.webp"
  alt="..."
  width="1200"
  height="600"
  loading="eager"
>
```

### Herramientas de Testing
- [PageSpeed Insights](https://pagespeed.web.dev/) — Core Web Vitals
- [GTmetrix](https://gtmetrix.com/) — Performance detallado
- [Rich Results Test](https://search.google.com/test/rich-results) — Schema markup
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

---

## 7. Checklist SEO para Cada Landing Page

### Antes de publicar
- [ ] Title tag con keyword + ciudad (50-60 chars)
- [ ] Meta description con CTA (150-160 chars)
- [ ] URL limpia y descriptiva
- [ ] Solo 1 H1 con keyword principal
- [ ] H2s con keywords secundarias
- [ ] Alt text en todas las imágenes
- [ ] Schema LocalBusiness implementado
- [ ] Schema FAQ implementado
- [ ] Canonical URL definida
- [ ] Open Graph tags completos
- [ ] Sitemap.xml creado
- [ ] robots.txt configurado
- [ ] Google Search Console verificado
- [ ] Google Analytics instalado
- [ ] Google Business Profile optimizado
- [ ] NAP consistente en toda la web
- [ ] Mobile-responsive perfecto
- [ ] Core Web Vitals en verde
- [ ] SSL/HTTPS activo

### Después de publicar (mensual)
- [ ] Revisar Search Console (errores, queries)
- [ ] Publicar posts en Google Business Profile
- [ ] Solicitar 2-3 reviews nuevas
- [ ] Verificar que las fotos están actualizadas
- [ ] Revisar posiciones para keywords target
- [ ] Crear reporte para el cliente
