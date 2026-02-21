---
name: Video Marketing & Reels
description: Guía de video marketing para profesionistas — Reels, YouTube, videos para landing pages, edición con herramientas gratuitas.
---

# 🎥 Video Marketing & Reels — Skill Guide

## Cuándo usar esta skill
- Al crear contenido de video para clientes
- Al implementar video en landing pages
- Al planificar estrategia de Reels/TikTok
- Al grabar/editar testimonios de clientes

---

## 1. Video en Landing Pages

### Hero Video Background
```html
<section class="hero-video">
  <video autoplay muted loop playsinline class="hero-bg-video">
    <source src="/assets/hero-video.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <h1>Tu bienestar mental es prioridad</h1>
    <p>Consulta psiquiátrica profesional en Guadalajara</p>
    <a href="#agendar" class="cta-btn">Agenda tu Cita</a>
  </div>
</section>

<style>
.hero-video {
  position: relative;
  height: 100vh;
  overflow: hidden;
}
.hero-bg-video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  transform: translate(-50%, -50%);
  object-fit: cover;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(10,11,26,0.7) 0%,
    rgba(10,11,26,0.9) 100%
  );
}
.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  padding-top: 30vh;
  color: white;
}
</style>
```

### Video Testimonial Embebido
```html
<div class="testimonial-video">
  <div class="video-wrapper" style="aspect-ratio: 16/9; border-radius: 16px; overflow: hidden;">
    <!-- YouTube Lite Embed (mejor performance) -->
    <lite-youtube videoid="VIDEO_ID" style="background-image: url('/assets/thumb-testimonial.webp');">
      <a href="https://youtube.com/watch?v=VIDEO_ID" class="lty-playbtn" title="Ver testimonio">
        <span class="lyt-visually-hidden">Ver testimonio</span>
      </a>
    </lite-youtube>
  </div>
</div>

<!-- Lite YouTube Embed (solo carga YouTube cuando dan play) -->
<script src="https://cdn.jsdelivr.net/npm/lite-youtube-embed@0.3.2/src/lite-yt-embed.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lite-youtube-embed@0.3.2/src/lite-yt-embed.min.css">
```

---

## 2. Estrategia de Reels/TikTok

### Tipos de Videos para Profesionistas
```
📚 EDUCATIVO (40% del contenido):
  - "3 señales de que necesitas ver a un psiquiatra"
  - "Mito vs Realidad: la medicación psiquiátrica"
  - "¿Cuál es la diferencia entre psicólogo y psiquiatra?"
  Duración: 30-60 seg
  Hook: Pregunta provocadora en los primeros 3 seg

🎬 BEHIND THE SCENES (30%):
  - Tour del consultorio
  - "Un día conmigo como psiquiatra"
  - Preparando el consultorio
  Duración: 15-30 seg
  Hook: "Te muestro algo que nunca has visto..."

💬 TESTIMONIOS (20%):
  - Pacientes compartiendo su experiencia (con permiso)
  - Antes/después emocional
  - Screenshots de reviews leídos en voz alta
  Duración: 15-45 seg

🎯 PROMOCIONAL (10%):
  - "Estoy aceptando nuevos pacientes"
  - "Nueva modalidad: consulta en línea"
  - "Horario especial este mes"
  Duración: 15-20 seg
```

### Calendario de Publicación
```
Frecuencia mínima: 3 Reels/semana

Lunes: Educativo (tip de la semana)
Miércoles: Behind the scenes
Viernes: Testimonial o Q&A

Mejor horario México:
  Instagram: 12pm-2pm y 7pm-9pm
  TikTok: 11am-1pm y 6pm-8pm
```

### Hooks que Funcionan (primeros 3 segundos)
```
"Esto nadie te dice sobre..."
"Si sientes esto, necesitas ver esto"
"Error #1 que cometen las personas con ansiedad"
"POV: Llegas a tu primera consulta psiquiátrica"
"¿Sabías que...?"
"Deja de hacer esto si tienes insomnio"
"La verdad sobre la medicación psiquiátrica"
```

---

## 3. Herramientas de Edición Gratuitas

```
📱 Mobile:
  - CapCut (gratis, muy completo)
  - InShot (gratis con marca de agua)
  - Canva Video (gratis)

💻 Desktop:
  - DaVinci Resolve (gratis, profesional)
  - CapCut Desktop (gratis)
  - Clipchamp (gratis, incluido en Windows)

🎵 Música sin copyright:
  - Biblioteca de Audio de YouTube Studio
  - Pixabay Music
  - Uppbeat (gratis con atribución)

📸 Stock video:
  - Pexels Videos
  - Pixabay Videos
  - Coverr.co
```

---

## 4. Optimización de Video para Web

```
Formato: MP4 (H.264)
Resolución: 1080p máximo para web
Bitrate: 4-8 Mbps
Tamaño máximo: 5-10 MB para hero video
Codec: H.264 para compatibilidad

Comprimir con FFmpeg:
  ffmpeg -i input.mp4 -vcodec h264 -acodec aac -b:v 4M -maxrate 6M output.mp4

Comprimir online (gratis):
  - https://handbrake.fr/
  - https://www.veed.io/tools/video-compressor
```
