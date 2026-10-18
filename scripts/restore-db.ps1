# RailSahayak PostgreSQL Database Restore Script
# Restores a SQL dump file into the railsahayak database
param (
    [Parameter(Mandatory=$true)]
    [string]$BackupFile,
    [string]$ContainerName = "railsahayak-backend-starter-postgres-1",
    [string]$DbUser = "railsahayak",
    [string]$DbName = "railsahayak"
)

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "RailSahayak Database Restore" -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Yellow

if (-not (Test-Path $BackupFile)) {
    Write-Error "Specified backup file does not exist: $BackupFile"
    exit 1
}

Write-Host "Target Container: $ContainerName"
Write-Host "Target Database : $DbName"
Write-Host "Input File      : $BackupFile"
Write-Host ""

try {
    $running = docker inspect -f '{{.State.Running}}' $ContainerName 2>$null
    if ($running -ne "true") {
        Write-Error "Container $ContainerName is not running."
        exit 1
    }

    # Pipe backup file into docker exec psql
    Get-Content -Path $BackupFile -Raw | docker exec -i $ContainerName psql -U $DbUser -d $DbName

    Write-Host "Database restore completed successfully!" -ForegroundColor Green
} catch {
    Write-Error "Database restore failed: $_"
    exit 1
}
