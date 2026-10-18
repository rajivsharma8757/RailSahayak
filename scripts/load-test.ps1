# RailSahayak Local Performance and Load Testing Script
# Measures latency (min, max, mean, p50, p95, p99), throughput, and error rates across all core endpoints
param (
    [string]$BaseUrl = "http://localhost:8081",
    [int]$RequestsPerEndpoint = 30
)

$ErrorActionPreference = "Continue"

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host " RailSahayak Local Performance & Load Test Suite" -ForegroundColor Cyan
Write-Host " Target URL: $BaseUrl" -ForegroundColor Cyan
Write-Host " Requests per Endpoint: $RequestsPerEndpoint" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

$passengerAuth = "Basic " + [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("passenger:PassengerDemo123!"))
$adminAuth     = "Basic " + [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:AdminDemo123!"))

function Measure-Endpoint {
    param (
        [string]$Name,
        [string]$Method,
        [string]$Url,
        [hashtable]$Headers,
        [string]$Body = $null,
        [int]$Count = 30
    )

    Write-Host "`nTesting: $Name ($Method $Url) x $Count requests..." -ForegroundColor Yellow
    $durations = [System.Collections.Generic.List[double]]::new()
    $successCount = 0
    $failCount = 0
    $stopwatchTotal = [System.Diagnostics.Stopwatch]::StartNew()

    for ($i = 1; $i -le $Count; $i++) {
        $sw = [System.Diagnostics.Stopwatch]::StartNew()
        try {
            $reqHeaders = @{}
            foreach ($k in $Headers.Keys) { $reqHeaders[$k] = $Headers[$k] }
            # Rotate X-Forwarded-For per iteration to simulate multi-client traffic within rate limits
            $reqHeaders["X-Forwarded-For"] = "192.168.1.$($i % 50 + 1)"
            $reqHeaders["X-Correlation-ID"] = "load-test-$i"

            if ($Method -eq "GET") {
                $response = Invoke-RestMethod -Uri $Url -Method Get -Headers $reqHeaders -TimeoutSec 10 -ErrorAction Stop
            } else {
                $response = Invoke-RestMethod -Uri $Url -Method $Method -Headers $reqHeaders -Body $Body -ContentType "application/json" -TimeoutSec 10 -ErrorAction Stop
            }
            $sw.Stop()
            $durations.Add($sw.Elapsed.TotalMilliseconds)
            $successCount++
        } catch {
            $sw.Stop()
            $durations.Add($sw.Elapsed.TotalMilliseconds)
            $failCount++
        }
    }
    $stopwatchTotal.Stop()
    $totalElapsedSec = $stopwatchTotal.Elapsed.TotalSeconds
    if ($totalElapsedSec -eq 0) { $totalElapsedSec = 0.001 }

    $sorted = $durations | Sort-Object
    $min = [math]::Round($sorted[0], 2)
    $max = [math]::Round($sorted[-1], 2)
    $sum = 0
    foreach ($d in $sorted) { $sum += $d }
    $mean = [math]::Round(($sum / $sorted.Count), 2)

    $p50Index = [math]::Floor($sorted.Count * 0.50)
    $p95Index = [math]::Min([math]::Floor($sorted.Count * 0.95), $sorted.Count - 1)
    $p99Index = [math]::Min([math]::Floor($sorted.Count * 0.99), $sorted.Count - 1)

    $p50 = [math]::Round($sorted[$p50Index], 2)
    $p95 = [math]::Round($sorted[$p95Index], 2)
    $p99 = [math]::Round($sorted[$p99Index], 2)
    $throughput = [math]::Round(($Count / $totalElapsedSec), 2)
    $errorRate = [math]::Round((($failCount / $Count) * 100), 2)

    [PSCustomObject]@{
        Endpoint   = $Name
        Requests   = $Count
        Success    = $successCount
        Failed     = $failCount
        MinMs      = $min
        MeanMs     = $mean
        P50Ms      = $p50
        P95Ms      = $p95
        P99Ms      = $p99
        MaxMs      = $max
        RPS        = $throughput
        ErrorRate  = "$errorRate%"
    }
}

$results = [System.Collections.Generic.List[PSCustomObject]]::new()

# 1. Health Probe
$results.Add((Measure-Endpoint -Name "Health Check" -Method "GET" -Url "$BaseUrl/api/v1/health" -Headers @{} -Count $RequestsPerEndpoint))

# 2. Auth / Me (Passenger)
$results.Add((Measure-Endpoint -Name "Auth Me (Passenger)" -Method "GET" -Url "$BaseUrl/api/v1/auth/me" -Headers @{ "Authorization" = $passengerAuth } -Count $RequestsPerEndpoint))

# 3. Train Search
$trainBody = '{"from":"New Delhi","to":"Patna Junction","date":"2026-10-25","travelClass":"3A"}'
$results.Add((Measure-Endpoint -Name "Smart Train Search" -Method "POST" -Url "$BaseUrl/api/v1/train-search" -Headers @{ "Authorization" = $passengerAuth } -Body $trainBody -Count $RequestsPerEndpoint))

# 4. Payment Help Diagnose
$paymentBody = '{"issue":"deducted","method":"UPI","purpose":"TICKET_BOOKING","reference":"UPI123456789012"}'
$results.Add((Measure-Endpoint -Name "Payment Help Diagnose" -Method "POST" -Url "$BaseUrl/api/v1/payment-help/diagnose" -Headers @{ "Authorization" = $passengerAuth } -Body $paymentBody -Count $RequestsPerEndpoint))

# 5. PNR Guide Explain
$pnrBody = '{"pnr":"2345678901","statusCode":"RAC"}'
$results.Add((Measure-Endpoint -Name "PNR Guide Explain" -Method "POST" -Url "$BaseUrl/api/v1/pnr-guide/explain" -Headers @{ "Authorization" = $passengerAuth } -Body $pnrBody -Count $RequestsPerEndpoint))

# 6. Passenger Cases List (Database Query)
$results.Add((Measure-Endpoint -Name "List My Cases (DB)" -Method "GET" -Url "$BaseUrl/api/v1/cases" -Headers @{ "Authorization" = $passengerAuth } -Count $RequestsPerEndpoint))

# 7. Admin Cases List (Database Query)
$results.Add((Measure-Endpoint -Name "Admin List All Cases (DB)" -Method "GET" -Url "$BaseUrl/api/v1/admin/cases" -Headers @{ "Authorization" = $adminAuth } -Count $RequestsPerEndpoint))

# 8. Admin Audit Logs (Database Query with Index)
$results.Add((Measure-Endpoint -Name "Admin Audit Logs (DB)" -Method "GET" -Url "$BaseUrl/api/v1/admin/audit-logs" -Headers @{ "Authorization" = $adminAuth } -Count $RequestsPerEndpoint))

Write-Host "`n=================================================================" -ForegroundColor Green
Write-Host " RailSahayak Performance & Load Test Results Summary" -ForegroundColor Green
Write-Host "=================================================================" -ForegroundColor Green

$results | Format-Table -AutoSize -Property Endpoint, Requests, Success, Failed, MinMs, P50Ms, P95Ms, P99Ms, RPS, ErrorRate

# Export JSON report
$reportPath = Join-Path $PSScriptRoot "..\target\performance-benchmark.json"
$results | ConvertTo-Json -Depth 3 | Out-File -FilePath $reportPath -Encoding utf8
Write-Host "`nBenchmark report saved to: $reportPath" -ForegroundColor Cyan
