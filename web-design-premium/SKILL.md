---
name: Web Design Premium (Nivel Awwwards)
description: Técnicas de diseño web premium — GSAP animations, Lottie, CSS avanzado, micro-interacciones, y patrones de diseño de sitios ganadores de Awwwards y CSS Design Awards.
---

# 🎨 Web Design Premium — Skill Guide

## Cuándo usar esta skill
- Al crear una nueva landing page para un cliente
- Al mejorar animaciones y micro-interacciones
- Al diseñar un sistema de diseño (design system)
- Al querer elevar la calidad visual de cualquier página

---

## 1. GSAP (GreenSock Animation Platform)

### Instalación
```html
<!-- CDN (recomendado para landing pages estáticas) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```

### Animaciones de Entrada (Scroll-Triggered)
```javascript
// Registrar ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Fade in desde abajo (el más usado)
gsap.utils.toArray('.reveal-up').forEach(el => {
  gsap.from(el, {
    y: 60,
    opacity: 0,
    duration: 1,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%',
      toggleActions: 'play none none none'
    }
  });
});

// Fade in desde la izquierda
gsap.utils.toArray('.reveal-left').forEach(el => {
  gsap.from(el, {
    x: -80,
    opacity: 0,
    duration: 1,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: el,
      start: 'top 85%'
    }
  });
});

// Stagger (elementos que aparecen uno tras otro)
gsap.from('.service-card', {
  y: 40,
  opacity: 0,
  duration: 0.8,
  stagger: 0.15,
  ease: 'power2.out',
  scrollTrigger: {
    trigger: '.services-grid',
    start: 'top 80%'
  }
});
```

### Animación del Hero (Primera Impresión)
```javascript
// Timeline para el hero section
const heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });

heroTl
  .from('.hero-badge', { y: -30, opacity: 0, duration: 0.6 })
  .from('.hero-title', { y: 50, opacity: 0, duration: 0.8 }, '-=0.3')
  .from('.hero-subtitle', { y: 30, opacity: 0, duration: 0.6 }, '-=0.4')
  .from('.hero-cta', { y: 20, opacity: 0, scale: 0.9, duration: 0.5 }, '-=0.3')
  .from('.hero-image', { x: 60, opacity: 0, duration: 1 }, '-=0.6');
```

### Parallax Suave
```javascript
gsap.to('.parallax-bg', {
  yPercent: -20,
  ease: 'none',
  scrollTrigger: {
    trigger: '.parallax-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  }
});
```

### Contador Animado (Números que suben)
```javascript
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  gsap.to(el, {
    innerHTML: target,
    duration: 2,
    ease: 'power2.out',
    snap: { innerHTML: 1 },
    scrollTrigger: {
      trigger: el,
      start: 'top 80%'
    }
  });
}
document.querySelectorAll('.counter').forEach(animateCounter);
```

---

## 2. Lottie Animations

### Instalación
```html
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
```

### Uso Básico
```html
<!-- Player embebido -->
<lottie-player
  src="https://lottie.host/xxx/animation.json"
  background="transparent"
  speed="1"
  style="width: 200px; height: 200px"
  loop
  autoplay>
</lottie-player>
```

### Lottie con Interactividad
```html
<!-- Se anima al hacer hover -->
<lottie-player
  src="/assets/lottie/check-animation.json"
  background="transparent"
  speed="1"
  style="width: 80px; height: 80px"
  hover>
</lottie-player>
```

### Dónde encontrar animaciones Lottie GRATIS
- https://lottiefiles.com/free-animations
- Buscar: "medical", "calendar", "checkmark", "loading", "success"
- Las animaciones más útiles para landing pages de profesionistas:
  - ✅ Checkmarks (para listas de beneficios)
  - 📅 Calendarios (para sección de agendamiento)
  - 💬 Chat bubbles (para testimonios)
  - 🏥 Medical icons (para doctoras como la Dra. Tabatha)
  - ⭐ Stars/ratings (para reviews)

---

## 3. CSS Avanzado — Técnicas Premium

### Glassmorphism
```css
.glass-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

### Gradientes Premium
```css
/* Gradiente sutil para fondos */
.premium-bg {
  background: linear-gradient(135deg, #0a0a1a 0%, #1a1a3e 50%, #0d0d2b 100%);
}

/* Gradiente para texto */
.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Gradiente con mesh (efecto moderno) */
.mesh-gradient {
  background-color: #0a0a1a;
  background-image:
    radial-gradient(at 20% 80%, hsla(212, 80%, 42%, 0.3) 0px, transparent 50%),
    radial-gradient(at 80% 20%, hsla(280, 80%, 42%, 0.2) 0px, transparent 50%),
    radial-gradient(at 50% 50%, hsla(340, 80%, 42%, 0.15) 0px, transparent 50%);
}
```

### Hover Effects Premium
```css
/* Lift on hover */
.card-hover {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card-hover:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

/* Shine effect */
.shine-effect {
  position: relative;
  overflow: hidden;
}
.shine-effect::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    45deg,
    transparent 40%,
    rgba(255, 255, 255, 0.05) 50%,
    transparent 60%
  );
  transform: translateX(-100%);
  transition: transform 0.6s ease;
}
.shine-effect:hover::before {
  transform: translateX(100%);
}

/* Magnetic button (con JS) */
.magnetic-btn {
  transition: transform 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

### Tipografía Premium
```css
/* Importar Google Fonts premium */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap');

/* Sistema tipográfico */
:root {
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-display: 'Outfit', sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;

  /* Escala tipográfica (Major Third - 1.25) */
  --text-xs: 0.64rem;
  --text-sm: 0.8rem;
  --text-base: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.563rem;
  --text-2xl: 1.953rem;
  --text-3xl: 2.441rem;
  --text-4xl: 3.052rem;
  --text-5xl: 3.815rem;
}
```

### Smooth Scroll
```css
html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px; /* altura del navbar */
}

/* Scrollbar personalizada */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: #0a0a1a;
}
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #667eea, #764ba2);
  border-radius: 4px;
}
```

---

## 4. Patrones de Diseño Awwwards

### Estructura de Landing Page Premium
```
1. Hero Section
   - Badge/tag ("Consulta en línea disponible")
   - Título impactante (max 8 palabras)
   - Subtítulo (1-2 líneas)
   - CTA principal + CTA secundario
   - Imagen/Video/3D del servicio

2. Social Proof Bar
   - Logos de certificaciones
   - "500+ pacientes atendidos"
   - Rating stars

3. Servicios (cards con hover effects)
   - Ícono animado (Lottie)
   - Título del servicio
   - Descripción corta
   - Precio (si aplica)
   - CTA

4. Sobre Mí / Bio
   - Foto profesional
   - Historia emocional
   - Credenciales
   - Estadísticas (años exp, pacientes, etc.)

5. Proceso (3-4 pasos visuales)
   - Línea conectora animada
   - Números grandes
   - Íconos Lottie por paso

6. Testimonios / Reviews
   - Cards con foto + nombre
   - Rating stars
   - Texto del review
   - Slider o grid

7. FAQ (accordion animado)
   - 5-8 preguntas
   - Smooth expand/collapse

8. CTA Final (full-width)
   - Gradiente de fondo
   - "¿Lista para tu consulta?"
   - Botón grande

9. Footer
   - Links de navegación
   - Redes sociales
   - "Powered by Valtyk"
```

### Paletas de Colores por Industria
```
🏥 Salud/Médico:
   Primary: #2E86AB (azul confianza)
   Accent: #A23B72 (magenta cálido)
   Dark: #0F1729
   Light: #F0F4F8

⚖️ Legal/Abogados:
   Primary: #1B3A4B (azul oscuro)
   Accent: #C5933F (oro)
   Dark: #0D1117
   Light: #F5F0E8

🦷 Dental:
   Primary: #00B4D8 (turquesa)
   Accent: #48CAE4 (azul claro)
   Dark: #0B1622
   Light: #F0FEFF

💼 Negocios/Coaching:
   Primary: #7209B7 (púrpura)
   Accent: #F72585 (rosa vibrante)
   Dark: #10002B
   Light: #FAF0FF

🧘 Bienestar/Spa:
   Primary: #606C38 (verde olivo)
   Accent: #DDA15E (dorado)
   Dark: #1A1A1A
   Light: #FEFAE0
```

---

## 5. Checklist de Calidad Premium

Antes de entregar cualquier landing page, verificar:

### Diseño
- [ ] Tipografía: máximo 2-3 fuentes, con jerarquía clara
- [ ] Colores: paleta de 3-5 colores coherentes
- [ ] Espaciado: padding/margin consistente (usar múltiplos de 8px)
- [ ] Imágenes: alta calidad, optimizadas (WebP)
- [ ] Íconos: consistentes en estilo y tamaño
- [ ] Dark mode friendly (si aplica)

### Animaciones
- [ ] Hero: timeline de entrada (GSAP)
- [ ] Scroll reveals: al menos en títulos y cards
- [ ] Hover effects: en botones, cards y links
- [ ] Loading: transición suave al cargar
- [ ] Lottie: al menos 1-2 animaciones como acentos

### Responsivo
- [ ] Mobile first: funciona perfecto en 375px
- [ ] Tablet: layout ajustado para 768px
- [ ] Desktop: aprovecha el espacio en 1440px
- [ ] Navegación: hamburger menu funcional en mobile

### Performance
- [ ] Lighthouse score > 90
- [ ] Imágenes lazy-loaded
- [ ] CSS/JS minificado
- [ ] Fuentes optimizadas (font-display: swap)
- [ ] GSAP: animaciones usando transform/opacity (GPU)

---

## 6. Recursos

### Inspiración
- [Awwwards](https://awwwards.com) — Sitios del día
- [CSS Design Awards](https://cssdesignawards.com)
- [Codepen](https://codepen.io/trending) — Snippets
- [Dribbble](https://dribbble.com) — Diseños UI
- [Land-book](https://land-book.com) — Landing pages

### Assets Gratuitos
- [LottieFiles](https://lottiefiles.com) — Animaciones
- [Unsplash](https://unsplash.com) — Fotos HD
- [Pexels](https://pexels.com) — Fotos y videos
- [Google Fonts](https://fonts.google.com) — Tipografías
- [Coolors](https://coolors.co) — Generador de paletas
- [Heroicons](https://heroicons.com) — Íconos SVG
- [Lucide](https://lucide.dev) — Íconos (ya los usas)
- [Haikei](https://haikei.app) — Generador de backgrounds SVG

### Aprendizaje
- [GSAP Docs](https://gsap.com/docs/v3/)
- [Codrops](https://tympanus.net/codrops/)
- [CSS-Tricks](https://css-tricks.com)
- [Awwwards Academy](https://awwwards.com/academy)
