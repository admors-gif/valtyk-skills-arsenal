param(
    [string]$ProjectPath,
    [switch]$All,
    [switch]$Status
)

$SkillsRepo = "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent\skills"
$PlaygroundDir = "C:\Users\admor\.gemini\antigravity\playground"

function Show-Banner {
    Write-Host ""
    Write-Host "  ============================================" -ForegroundColor Cyan
    Write-Host "  Valtyk Skills Arsenal - Link Manager" -ForegroundColor Cyan
    Write-Host "  ============================================" -ForegroundColor Cyan
    Write-Host ""
}

function Link-Skills {
    param([string]$Target)
    
    $projectName = Split-Path $Target -Leaf
    $skillsDir = Join-Path $Target ".agent\skills"
    $agentDir = Join-Path $Target ".agent"
    
    if ($skillsDir -eq $SkillsRepo) {
        Write-Host "  SKIP $projectName - ES el repo central" -ForegroundColor DarkGray
        return
    }
    
    if (Test-Path $skillsDir) {
        $item = Get-Item $skillsDir -Force
        if ($item.Attributes -match "ReparsePoint") {
            Write-Host "  OK   $projectName - Ya conectado (junction)" -ForegroundColor Green
            return
        }
        
        $ts = Get-Date -Format "yyyyMMdd-HHmmss"
        $backupDir = "${skillsDir}.bak.${ts}"
        Write-Host "  BAK  $projectName - Respaldando skills existentes..." -ForegroundColor Yellow
        Rename-Item $skillsDir $backupDir
    }
    
    if (-not (Test-Path $agentDir)) {
        New-Item -ItemType Directory -Path $agentDir -Force | Out-Null
    }
    
    try {
        cmd /c mklink /J "$skillsDir" "$SkillsRepo" 2>&1 | Out-Null
        Write-Host "  LINK $projectName - Skills conectadas!" -ForegroundColor Green
    }
    catch {
        Write-Host "  ERR  $projectName - Error: $_" -ForegroundColor Red
    }
}

function Show-Status {
    Show-Banner
    Write-Host "  Estado de Skills por Workspace:" -ForegroundColor White
    Write-Host ""
    
    $dirs = Get-ChildItem $PlaygroundDir -Directory
    foreach ($dir in $dirs) {
        $skillsDir = Join-Path $dir.FullName ".agent\skills"
        $name = $dir.Name
        
        if (Test-Path $skillsDir) {
            $item = Get-Item $skillsDir -Force
            if ($item.Attributes -match "ReparsePoint") {
                $count = @(Get-ChildItem $skillsDir -Directory | Where-Object { $_.Name -ne ".git" }).Count
                Write-Host "  LINK $name - JUNCTION ($count skills)" -ForegroundColor Green
            }
            else {
                $count = @(Get-ChildItem $skillsDir -Directory | Where-Object { $_.Name -ne ".git" }).Count
                Write-Host "  LOCAL $name - FOLDER ($count skills)" -ForegroundColor Yellow
            }
        }
        else {
            Write-Host "  NONE $name - Sin skills" -ForegroundColor DarkGray
        }
    }
    Write-Host ""
}

# Main
Show-Banner

if ($Status) {
    Show-Status
    exit
}

if ($All) {
    Write-Host "  Conectando TODOS los workspaces..." -ForegroundColor White
    Write-Host ""
    
    $dirs = Get-ChildItem $PlaygroundDir -Directory
    foreach ($dir in $dirs) {
        if ($dir.Name -eq "calcom") { continue }
        Link-Skills -Target $dir.FullName
    }
    
    Write-Host ""
    Write-Host "  Listo! Todas las skills conectadas." -ForegroundColor Green
    Write-Host ""
}
elseif ($ProjectPath) {
    if (-not (Test-Path $ProjectPath)) {
        Write-Host "  No existe: $ProjectPath" -ForegroundColor Red
        exit 1
    }
    Link-Skills -Target $ProjectPath
}
else {
    Write-Host "  Uso:" -ForegroundColor White
    Write-Host "    .\link-skills.ps1 -ProjectPath PATH" -ForegroundColor Gray
    Write-Host "    .\link-skills.ps1 -All" -ForegroundColor Gray
    Write-Host "    .\link-skills.ps1 -Status" -ForegroundColor Gray
    Write-Host ""
}
