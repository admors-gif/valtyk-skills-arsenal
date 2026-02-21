# 🧠 Valtyk Skills Arsenal

Kit portable de skills para agencias digitales. Estas skills son archivos de referencia que un asistente IA (como Antigravity/Claude/GPT) consulta automáticamente al recibir tareas relevantes.

## 📦 Skills Activas (16)

| # | Skill | Archivo | Descripción |
|---|-------|---------|-------------|
| 1 | 🎨 Web Design Premium | `web-design-premium/SKILL.md` | GSAP, Lottie, CSS avanzado, Awwwards patterns |
| 2 | 🔍 SEO Local | `seo-local/SKILL.md` | Schema, GBP, Search Console, Keywords |
| 3 | 📣 Marketing & Ventas | `marketing-sales/SKILL.md` | Copywriting, Email, Ventas, Pricing |
| 4 | 📊 Presentaciones | `presentations/SKILL.md` | Pitch decks, Propuestas, Contratos |
| 5 | 🤖 Automatización | `automation/SKILL.md` | n8n, Cal.com, WhatsApp, SMTP |
| 6 | 💼 Business Ops | `business-ops/SKILL.md` | CRO, Analytics, SOPs, Escalamiento |
| 7 | 🤖 AI Chatbots | `ai-chatbots/SKILL.md` | GPT widgets, WhatsApp bots, RAG/Embeddings |
| 8 | 📱 Google Ads & PPC | `google-ads/SKILL.md` | Búsqueda, Display, Remarketing, Presupuestos |
| 9 | 🎥 Video Marketing | `video-marketing/SKILL.md` | Hero videos, Reels, YouTube, Edición |
| 10 | 📧 Cold Outreach | `cold-outreach/SKILL.md` | Email frío, DMs, Follow-ups, Prospección |
| 11 | 🔒 Hosting & DevOps | `hosting-devops/SKILL.md` | Firebase, Docker, Nginx, SSL, VPS |
| 12 | 🕷️ Data Scraping | `data-scraping/SKILL.md` | Apify, Lead scoring, Pipelines de leads |
| 13 | 📋 Project Management | `project-management/SKILL.md` | Kanban, Templates, Comunicación, Tracking |
| 14 | 💬 WhatsApp Flows | `whatsapp-flows/SKILL.md` | Botones, Respuestas auto, Cloud API |
| 15 | 🎨 UI Design & Figma | `ui-design/SKILL.md` | Wireframes, Prototipos, Design tokens |
| 16 | 🧪 Analytics & A/B Testing | `analytics-testing/SKILL.md` | Clarity, GTM, Tests, KPIs |

## 📊 Dashboard Visual
Abre `dashboard.html` en el navegador para ver el estado de todas las skills.

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
- **2026-02-20** — v2.0 — Ampliado a 16 skills completas
