---
description: Conectar el Valtyk Skills Arsenal a nuevos workspaces de Antigravity
---

# Conectar Skills Arsenal a Workspaces

## Cuándo usar
- Cuando se crea un nuevo workspace de Antigravity
- Cuando un workspace no tiene skills disponibles
- Para verificar que todos los workspaces están conectados

## Comando para conectar TODOS los workspaces de una vez

// turbo
1. Ejecutar el script de link:
```
powershell -ExecutionPolicy Bypass -File "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent\skills\scripts\link-skills.ps1" -All
```

## Comando para ver el estado actual

// turbo
2. Ver qué workspaces están conectados:
```
powershell -ExecutionPolicy Bypass -File "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent\skills\scripts\link-skills.ps1" -Status
```

## Comando para conectar UN workspace específico

3. Conectar un solo workspace:
```
powershell -ExecutionPolicy Bypass -File "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent\skills\scripts\link-skills.ps1" -ProjectPath "C:\ruta\al\workspace"
```

## Notas
- El repo central está en: `fractal-supernova/.agent/skills/`
- GitHub repo: `admors-gif/valtyk-skills-arsenal`
- Los junctions son transparentes — cualquier cambio en el repo central se refleja en todos los workspaces automáticamente
- Para agregar una nueva skill, crearla en el repo central y hacer push a GitHub
