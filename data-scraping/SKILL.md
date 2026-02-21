---
name: Data Scraping & Lead Generation
description: Guía de web scraping con Apify, generación de leads, y automatización de prospección para alimentar el pipeline de ventas.
---

# 🕷️ Data Scraping & Lead Generation — Skill Guide

## Cuándo usar esta skill
- Al buscar prospectos de forma masiva
- Al extraer datos de Google Maps, Doctoralia, directorios
- Al crear listas de leads para outreach
- Al automatizar la prospección

---

## 1. Apify — Scraping de Google Maps

### Actor Recomendado
```
Actor: compass/crawler-google-places
URL: https://apify.com/compass/crawler-google-places

Input ejemplo:
{
  "searchStringsArray": [
    "psiquiatra en guadalajara",
    "dentista en guadalajara",
    "abogado en guadalajara"
  ],
  "maxCrawledPlacesPerSearch": 50,
  "language": "es",
  "countryCode": "mx"
}

Output incluye:
  - Nombre del negocio
  - Dirección
  - Teléfono
  - Website
  - Rating
  - Número de reviews
  - Horarios
  - Categoría
  - Coordenadas GPS
```

### Flujo de Prospección con Apify
```
1. Ejecutar scraper de Google Maps
   → Query: "[profesión] en [ciudad]"
   
2. Filtrar resultados en n8n:
   → Sin website = PROSPECTO HOT 🔥
   → Con website básico = PROSPECTO WARM 🟡
   → Con website profesional = SKIP ❌
   
3. Enriquecer datos:
   → Buscar email con Hunter.io API
   → Buscar Instagram/LinkedIn
   
4. Guardar en Google Sheets (CRM)
   
5. Iniciar secuencia de cold outreach
```

### Rotador de API Keys
```
Si excedes el límite de una API key:
  → Tener 3-5 keys de Apify (cuentas gratuitas)
  → Rotar automáticamente con n8n
  → Cada cuenta gratis = $5 USD/mes de crédito
```

---

## 2. Scraping de Directorios Médicos

### Fuentes de Datos
```
Para doctores:
  - Google Maps (principal)
  - Sección Amarilla
  - Páginas del hospital/clínica
  - Colegios médicos estatales

Para abogados:
  - Google Maps
  - Directorio del Colegio de Abogados
  - Páginas amarillas

Para otros profesionistas:
  - Google Maps (siempre funciona)
  - LinkedIn
  - Directorios sectoriales
```

---

## 3. Limpieza y Calificación de Leads

### Pipeline de Calificación
```
LEAD SCORE (1-10):
  +3 → No tiene website
  +2 → Tiene website pero es básico/viejo
  +2 → Tiene 4+ stars en Google
  +1 → Tiene 20+ reviews
  +1 → Está en zona con alta competencia
  +1 → Tiene redes sociales activas
  
  8-10 = HOT 🔥 → Contactar primero
  5-7  = WARM 🟡 → Contactar después
  1-4  = COLD 🔵 → Lista de espera
```

### Automatización con n8n
```
Workflow: Lead Scoring Automático

Trigger: Nuevo lead en Google Sheets
  ↓
Verificar si tiene website (HTTP Request)
  ↓
Si no tiene → Score +3
Si tiene → Analizar con Lighthouse API → Score basado en performance
  ↓
Verificar reviews en Google Maps
  ↓
Calcular score total
  ↓
Actualizar Google Sheets con score
  ↓
Si score > 7 → Iniciar secuencia de cold email
```

---

## 4. Google Sheets como CRM de Leads

### Estructura del Sheet
```
HEADERS:
| ID | Nombre | Profesión | Ciudad | Teléfono | Email | Website |
| Rating | Reviews | Score | Estado | Fecha Contacto | Notas | Fuente |

ESTADOS:
  🔵 Nuevo
  📧 Email 1 enviado
  📧 Email 2 enviado
  📧 Email 3 enviado
  📱 DM enviado
  🟢 Respondió
  📞 Llamada agendada
  ✅ Cliente
  ❌ No interesado
  ⏸️ Seguimiento en 60 días
```

---

## 5. Automatización Completa

### Workflow: Pipeline de Leads to Client
```
FASE 1: GENERACIÓN (automática)
  Apify scraper (semanal)
  → Filtrar prospectos sin web
  → Enriquecer con email
  → Guardar en Google Sheets
  → Calcular lead score

FASE 2: OUTREACH (semi-automática)
  Para leads con score > 7:
  → Enviar email frío (Día 0)
  → Follow-up (Día 3)
  → Último intento (Día 7)
  → DM en Instagram (Día 14)

FASE 3: CONVERSIÓN (manual)
  Lead responde:
  → Agendar llamada
  → Enviar propuesta
  → Seguimiento
  → Cerrar venta

TODO el pipeline puede correr en n8n
con intervención manual solo en Fase 3
```

---

## 6. Límites y Ética

```
IMPORTANTE:
  ✓ Respetar rate limits de las APIs
  ✓ No scrapear datos privados
  ✓ Solo usar datos públicos (Google Maps, directorios)
  ✓ Cumplir con leyes de email (incluir unsubscribe)
  ✓ No enviar spam masivo (máx 25 emails personalizados/día)
  ✓ Personalizar cada mensaje
  ✓ Respetar cuando alguien dice "no"
```
