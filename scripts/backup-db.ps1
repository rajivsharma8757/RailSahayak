# RailSahayak PostgreSQL Database Backup Script
# Creates a timestamped plain SQL dump of the railsahayak database
param (
    [string]$ContainerName = "railsahayak-backend-starter-postgres-1",
    [string]$DbUser = "railsahayak",
    [string]$DbName = "railsahayak",
    [string]$BackupDir = "$PSScriptRoot\..\backups"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $BackupDir)) {
    New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
}

$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$BackupFile = Join-Path $BackupDir "railsahayak_backup_$Timestamp.sql"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "RailSahayak Database Backup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Target Container: $ContainerName"
Write-Host "Target Database : $DbName"
Write-Host "Output File     : $BackupFile"

try {
    $running = docker inspect -f '{{.State.Running}}' $ContainerName 2>$null
    if ($running -ne "true") {
        Write-Error "Container $ContainerName is not running. Please start it before taking a backup."
        exit 1
    }

    # Execute pg_dump
    docker exec $ContainerName pg_dump -U $DbUser --clean --if-exists $DbName | Out-File -FilePath $BackupFile -Encoding utf8

    if ((Test-Path $BackupFile) -and ((Get-Item $BackupFile).Length -gt 0)) {
        $fileSizeKb = [math]::Round(((Get-Item $BackupFile).Length / 1KB), 2)
        Write-Host "Backup completed successfully! ($fileSizeKb KB)" -ForegroundColor Green
        Write-Host "Backup saved at: $BackupFile" -ForegroundColor Green
    } else {
        Write-Error "Backup file was created but appears to be empty."
        exit 1
    }
} catch {
    Write-Error "Database backup failed: $_"
    exit 1
}
