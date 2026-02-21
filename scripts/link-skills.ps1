param(
    [string]$ProjectPath,
    [switch]$All,
    [switch]$Status
)

$SkillsRepo = "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent\skills"
$CentralAgent = "C:\Users\admor\.gemini\antigravity\playground\fractal-supernova\.agent"
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
    
    # Create .agent/ if needed
    if (-not (Test-Path $agentDir)) {
        New-Item -ItemType Directory -Path $agentDir -Force | Out-Null
    }
    
    # Handle skills junction
    $needsLink = $true
    if (Test-Path $skillsDir) {
        $item = Get-Item $skillsDir -Force
        if ($item.Attributes -match "ReparsePoint") {
            Write-Host "  OK   $projectName - Ya conectado (junction)" -ForegroundColor Green
            $needsLink = $false
        }
        else {
            $ts = Get-Date -Format "yyyyMMdd-HHmmss"
            $backupDir = "${skillsDir}.bak.${ts}"
            Write-Host "  BAK  $projectName - Respaldando skills existentes..." -ForegroundColor Yellow
            Rename-Item $skillsDir $backupDir
        }
    }
    
    if ($needsLink) {
        try {
            cmd /c mklink /J "$skillsDir" "$SkillsRepo" 2>&1 | Out-Null
            Write-Host "  LINK $projectName - Skills conectadas!" -ForegroundColor Green
        }
        catch {
            Write-Host "  ERR  $projectName - Error: $_" -ForegroundColor Red
        }
    }
    
    # Always copy rules.md
    $rulesSource = Join-Path $CentralAgent "rules.md"
    $rulesDest = Join-Path $agentDir "rules.md"
    if (Test-Path $rulesSource) {
        Copy-Item $rulesSource $rulesDest -Force
    }
    
    # Copy workflows if they don't exist yet
    $wfSource = Join-Path $CentralAgent "workflows"
    $wfDest = Join-Path $agentDir "workflows"
    if ((Test-Path $wfSource) -and -not (Test-Path $wfDest)) {
        Copy-Item $wfSource $wfDest -Recurse -Force
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
