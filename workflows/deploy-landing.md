---
description: Deploy a new client landing page to Firebase Hosting
---

# 🚀 Deploy Landing Page to Firebase

This workflow deploys a new client landing page to Firebase Hosting under the `valtyk-landings` project.

## Prerequisites

- Firebase CLI installed (`firebase --version`)
- Logged into Firebase (`firebase login`)
- Firebase project: `valtyk-landings`
- Source repo: `C:\Users\admor\.gemini\antigravity\playground\void-oort`
- Deploy workspace: `C:\Users\admor\.gemini\antigravity\playground\fractal-supernova`

## Architecture

```
void-oort/                          ← Source repository (PRIVATE on GitHub)
├── shared/                         ← Shared assets across ALL clients
│   ├── styles/
│   │   ├── design-system.css       ← Core design tokens & utilities
│   │   └── animations.css          ← Shared animations
│   └── js/
│       ├── scroll-reveal.js        ← Scroll reveal effects
│       ├── whatsapp-button.js      ← Floating WhatsApp CTA button
│       └── counter.js              ← Animated number counters
├── clients/
│   ├── tabatha-psiquiatra/         ← Client: Dra. Tabatha Barron
│   │   ├── index.html
│   │   ├── content.json
│   │   ├── styles/
│   │   │   ├── custom.css          ← Client-specific color overrides
│   │   │   └── page.css            ← Client-specific page styles
│   │   └── assets/                 ← Client images, logos, etc.
│   └── [new-client]/               ← Future clients follow same structure
│       ├── index.html
│       ├── content.json
│       ├── styles/
│       └── assets/

fractal-supernova/                  ← Firebase deploy workspace
├── firebase.json                   ← Hosting config (update per deploy)
├── .firebaserc                     ← Project & target mappings
└── public/                         ← Built files for deployment
    ├── index.html                  ← Client HTML (paths corrected)
    ├── shared/                     ← Copied from void-oort/shared/
    ├── styles/                     ← Client-specific styles
    └── assets/                     ← Client-specific assets
```

## Deployed Sites

| Site ID          | URL                                | Client                  | Status  |
|------------------|------------------------------------|-------------------------|---------|
| tabatha-barron   | https://tabatha-barron.web.app     | Dra. Tabatha Barron     | ✅ Live |

## Steps to Deploy a NEW Client

### 1. Create the client folder in source repo

Create the client's landing page files under `void-oort/clients/[client-slug]/` following the existing structure. The HTML should reference shared assets with `../../shared/` relative paths.

### 2. Create Firebase Hosting site

// turbo
```powershell
firebase hosting:sites:create [client-slug] --project valtyk-landings
```

Replace `[client-slug]` with the client's URL-friendly name (lowercase, hyphens only).
Example: `maria-dentista`, `carlos-abogado`, `ana-nutriologa`

### 3. Update `.firebaserc` targets

Add the new site to the targets section in `fractal-supernova/.firebaserc`:

```json
{
  "projects": {
    "default": "valtyk-landings"
  },
  "targets": {
    "valtyk-landings": {
      "hosting": {
        "tabatha-barron": ["tabatha-barron"],
        "[client-slug]": ["[client-slug]"]
      }
    }
  }
}
```

### 4. Update `firebase.json`

Change the site target in `fractal-supernova/firebase.json`:

```json
{
  "hosting": {
    "site": "[client-slug]",
    "public": "public",
    ...
  }
}
```

### 5. Clean and prepare the public folder

// turbo
```powershell
Remove-Item "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\public\*" -Recurse -Force
```

### 6. Copy files to public folder

// turbo
```powershell
$src = "C:\Users\admor\.gemini\antigravity\playground\void-oort"
$client = "[client-folder-name]"   # e.g., "tabatha-psiquiatra"
$pub = "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\public"

# Create directories
New-Item -ItemType Directory -Force -Path "$pub\shared\styles","$pub\shared\js","$pub\styles","$pub\assets" | Out-Null

# Copy shared assets
Copy-Item "$src\shared\styles\*" "$pub\shared\styles\" -Force
Copy-Item "$src\shared\js\*" "$pub\shared\js\" -Force

# Copy client-specific files
Copy-Item "$src\clients\$client\styles\*" "$pub\styles\" -Force
if (Test-Path "$src\clients\$client\assets") {
    Copy-Item "$src\clients\$client\assets\*" "$pub\assets\" -Force -Recurse
}

# Copy and fix paths in index.html
$content = Get-Content "$src\clients\$client\index.html" -Raw
$content = $content -replace '../../shared/', '/shared/'
Set-Content "$pub\index.html" -Value $content -NoNewline

Write-Host "✅ Files ready for deploy"
```

### 7. Deploy to Firebase

// turbo
```powershell
firebase deploy --only hosting:[client-slug] --project valtyk-landings
```

### 8. Verify deployment

Open the URL in the browser: `https://[client-slug].web.app`

### 9. Update the Deployed Sites table

Update the table in this workflow file with the new site details.

## Steps to UPDATE an Existing Client

### 1. Make changes in source repo

Edit files in `void-oort/clients/[client-folder]/`

### 2. Re-copy and redeploy

Follow steps 4-8 above with the existing client's slug.

### 3. Commit changes to source repo

```powershell
cd C:\Users\admor\.gemini\antigravity\playground\void-oort
git add .
git commit -m "Update [client-name] landing page"
git push origin main
```

## Adding a Custom Domain (Optional)

If a client wants their own domain (e.g., `www.dratabathabarron.com`):

1. Go to Firebase Console > Hosting > tabatha-barron site
2. Click "Add custom domain"
3. Follow the DNS verification steps
4. Add the provided A records and/or CNAME to the domain registrar
5. Wait for SSL provisioning (usually 24-48 hours)

The `.web.app` URL will continue working alongside the custom domain.

## Adding Firestore Database (for forms, leads, etc.)

The `valtyk-landings` Firebase project supports Firestore. To collect data from client landing pages:

1. Enable Firestore in Firebase Console
2. Structure: `clients/{client-slug}/leads/{auto-id}`
3. Add Firebase SDK to the landing page HTML
4. Create a form submission handler in JavaScript

## Notes

- **GitHub repo is PRIVATE**: `admors-gif/Valtyk-Solutions-Web-Services`
- **Firebase project**: `valtyk-landings`
- **All sites share** the same Firebase project but are independently deployed
- **Free tier limits**: 10 GB storage, 360 MB/day bandwidth (plenty for landing pages)
- **Max sites per project**: 36 hosting sites
