# 🧠 Valtyk Skills Arsenal

Kit portable de skills para agencias digitales. Estas skills son archivos de referencia que un asistente IA (como Antigravity/Claude/GPT) consulta automáticamente al recibir tareas relevantes.

## 📦 Skills Activas

| # | Skill | Archivo | Descripción |
|---|-------|---------|-------------|
| 1 | 🎨 Web Design Premium | `web-design-premium/SKILL.md` | GSAP, Lottie, CSS avanzado, Awwwards patterns |
| 2 | 🔍 SEO Local | `seo-local/SKILL.md` | Schema, GBP, Search Console, Keywords |
| 3 | 📣 Marketing & Ventas | `marketing-sales/SKILL.md` | Copywriting, Email, Ventas, Pricing |
| 4 | 📊 Presentaciones | `presentations/SKILL.md` | Pitch decks, Propuestas, Contratos |
| 5 | 🤖 Automatización | `automation/SKILL.md` | n8n, Cal.com, WhatsApp, SMTP |
| 6 | 💼 Business Ops | `business-ops/SKILL.md` | CRO, Analytics, SOPs, Escalamiento |

## 🚀 Cómo Usar

### En un proyecto nuevo:
1. Copia la carpeta `skills/` a tu proyecto en `.agent/skills/`
2. El asistente IA las detectará automáticamente
3. Al pedir una tarea, el asistente lee la skill relevante y aplica las técnicas

### Ejemplo:
```
TÚ: "Crea una landing page para un dentista"
IA: Lee web-design-premium + seo-local + marketing-sales → Entrega landing completa
```

## 📊 Dashboard Visual
Abre `dashboard.html` en el navegador para ver el estado de todas las skills.

## 🔧 Agregar Nueva Skill
Crea un directorio nuevo con un `SKILL.md` siguiendo el formato:

```markdown
---
name: Nombre de la Skill
description: Descripción breve
---
# Contenido de la skill...
```

## 📝 Changelog
- **2026-02-20** — v1.0 — 6 skills iniciales creadas
