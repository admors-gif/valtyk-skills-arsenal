---
name: UI Design & Figma
description: Diseño de interfaces con Figma, wireframing, prototipado, design tokens, y workflow de diseño antes de codificar.
---

# 🎨 UI Design & Figma — Skill Guide

## Cuándo usar esta skill
- Al diseñar una landing page antes de codificarla
- Al crear mockups para mostrar al cliente
- Al definir un design system
- Al prototipar interacciones

---

## 1. Figma — Setup Gratuito

### Cuenta y Acceso
```
Figma (gratis):
  → https://figma.com
  → Plan gratis: 3 proyectos, sin límite de archivos
  → Suficiente para agencias pequeñas

Alternativas:
  → Penpot (open source, gratis): https://penpot.app
  → Lunacy (gratis para Windows): https://icons8.com/lunacy
```

---

## 2. Workflow de Diseño

### Paso a Paso
```
1. INVESTIGACIÓN (30 min)
   → Ver sitios de la competencia
   → Buscar inspiración en Dribbble/Awwwards
   → Anotar gustos del cliente (colores, estilo)

2. WIREFRAME — Lo-Fi (1h)
   → Usar rectángulos grises
   → Definir estructura y jerarquía
   → Sin colores, sin imágenes
   → Validar con el cliente: "¿Esta estructura te funciona?"

3. DISEÑO — Hi-Fi (2-3h)
   → Aplicar colores y tipografía
   → Agregar imágenes reales o placeholders
   → Diseñar mobile Y desktop
   → Definir hover states

4. PROTOTIPO (30 min)
   → Conectar pantallas
   → Agregar transiciones
   → Compartir link de prototipo con cliente

5. HANDOFF → CÓDIGO (después de aprobación)
   → Exportar assets
   → Usar CSS de Figma como referencia
   → Crear componentes HTML/CSS
```

---

## 3. Design Tokens

### Sistema de Variables
```css
/* Equivalente en CSS de lo que defines en Figma */
:root {
  /* Colores */
  --color-primary: #2E86AB;
  --color-primary-light: #4DA3C4;
  --color-primary-dark: #1A5276;
  --color-accent: #A23B72;
  --color-bg: #0F1729;
  --color-surface: #1A1F3A;
  --color-text: #E8E8F0;
  --color-text-muted: #8888AA;

  /* Tipografía */
  --font-sans: 'Inter', sans-serif;
  --font-display: 'Outfit', sans-serif;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  --font-size-5xl: 3rem;
  --font-size-hero: 3.5rem;

  /* Espaciado */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 50%;

  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.15);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.2);
  --shadow-xl: 0 16px 48px rgba(0,0,0,0.3);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 400ms ease;
}
```

---

## 4. Componentes Reutilizables

### Template de Landing Page (Secciones)
```
Componente: hero-section
  → Variantes: con imagen, con video, con Lottie
  
Componente: service-card
  → Variantes: vertical, horizontal
  → States: default, hover, active

Componente: testimonial-card
  → Variantes: con foto, sin foto, con rating

Componente: cta-button
  → Variantes: primary, secondary, outline, ghost
  → States: default, hover, active, disabled
  → Sizes: small, medium, large

Componente: nav-bar
  → Variantes: transparent, solid, dark

Componente: faq-accordion
  → States: closed, open, animating

Componente: footer
  → Variantes: simple, with newsletter, with map
```

---

## 5. Recursos de Diseño Gratuitos

```
🎨 UI Kits:
  - Figma Community (miles de kits gratis)
  - Untitled UI (design system completo)
  - Shadcn/UI (para devs)

📸 Fotos:
  - Unsplash (gratis, sin atribución)
  - Pexels (gratis, sin atribución)

🖼️ Mockups:
  - Mockup World (gratis)
  - Smartmockups (gratis básico)
  - Shots.so (gratis para screenshots)

🎭 Íconos:
  - Lucide (ya los usas)
  - Heroicons
  - Phosphor Icons
  - Tabler Icons

🌈 Colores:
  - Coolors.co (generador de paletas)
  - Realtime Colors (preview paletas en UI)
  - Color Hunt (paletas curadas)

✏️ Fonts:
  - Google Fonts
  - Font Pair (combinaciones que funcionan)
```
