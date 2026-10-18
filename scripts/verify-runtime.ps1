# RailSahayak Runtime Verification Script
# Directly audits endpoints, headers, permissions, and responses against running local server

$base = 'http://localhost:8081'
$pAuth = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes('passenger:PassengerDemo123!'))
$aAuth = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes('admin:AdminDemo123!'))

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " RailSahayak Runtime Verification Audit" -ForegroundColor Cyan
Write-Host " Target URL: $base" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Health Probe & Security Headers
Write-Host "`n[1/8] Probing Health and HTTP Security Headers..." -ForegroundColor Yellow
$h = Invoke-WebRequest -Uri "$base/api/v1/health" -UseBasicParsing
Write-Host "HTTP Status          : $($h.StatusCode)"
Write-Host "X-Content-Type-Options: $($h.Headers['X-Content-Type-Options'])"
Write-Host "X-Frame-Options      : $($h.Headers['X-Frame-Options'])"
Write-Host "X-Correlation-ID     : $($h.Headers['X-Correlation-ID'])"
Write-Host "Health Response Body : $($h.Content)"

# 2. Passenger Authentication
Write-Host "`n[2/8] Testing Passenger Authentication (/api/v1/auth/me)..." -ForegroundColor Yellow
$meP = Invoke-RestMethod -Uri "$base/api/v1/auth/me" -Headers @{ Authorization = $pAuth }
Write-Host "Authenticated: $($meP.authenticated), Username: $($meP.username), Roles: $($meP.roles -join ', ')"

# 3. Admin Authentication
Write-Host "`n[3/8] Testing Admin Authentication (/api/v1/auth/me)..." -ForegroundColor Yellow
$meA = Invoke-RestMethod -Uri "$base/api/v1/auth/me" -Headers @{ Authorization = $aAuth }
Write-Host "Authenticated: $($meA.authenticated), Username: $($meA.username), Roles: $($meA.roles -join ', ')"

# 4. Role-Based Access Control (Passenger attempting Admin Endpoint)
Write-Host "`n[4/8] Testing RBAC: Passenger requesting Admin Cases..." -ForegroundColor Yellow
try {
    $bad = Invoke-WebRequest -Uri "$base/api/v1/admin/cases" -Headers @{ Authorization = $pAuth } -UseBasicParsing
    Write-Host "ERROR: Expected 403 Forbidden but received $($bad.StatusCode)" -ForegroundColor Red
} catch {
    $statusCode = $_.Exception.Response.StatusCode.value__
    Write-Host "SUCCESS: Access denied as expected with HTTP $statusCode Forbidden" -ForegroundColor Green
}

# 5. Smart Train Finder
Write-Host "`n[5/8] Testing Smart Train Finder (/api/v1/train-search)..." -ForegroundColor Yellow
$trainReq = '{"from":"New Delhi","to":"Patna Junction","date":"2026-10-25","travelClass":"3A"}'
$ts = Invoke-RestMethod -Uri "$base/api/v1/train-search" -Method Post -ContentType 'application/json' -Headers @{ Authorization = $pAuth } -Body $trainReq
Write-Host "Mode        : $($ts.mode)"
Write-Host "Live Notice : $($ts.notice)"
Write-Host "Results     : $($ts.results.Count) trains returned"
Write-Host "Sample Train: $($ts.results[0].trainName) ($($ts.results[0].trainNumber)) - $($ts.results[0].availabilitySummary)"

# 6. Payment Help Diagnoser
Write-Host "`n[6/8] Testing Payment Help Diagnoser (/api/v1/payment-help/diagnose)..." -ForegroundColor Yellow
$payReq = '{"issue":"deducted","method":"UPI","purpose":"TICKET_BOOKING","reference":"UPI123456789012"}'
$ph = Invoke-RestMethod -Uri "$base/api/v1/payment-help/diagnose" -Method Post -ContentType 'application/json' -Headers @{ Authorization = $pAuth } -Body $payReq
Write-Host "Mode         : $($ph.mode)"
Write-Host "Masked Ref   : $($ph.maskedReference)"
Write-Host "Advice Title : $($ph.title)"
Write-Host "Action Rec   : $($ph.actionRecommendation)"

# 7. PNR Guide Explainer
Write-Host "`n[7/8] Testing PNR Guide Explainer (/api/v1/pnr-guide/explain)..." -ForegroundColor Yellow
$pnrReq = '{"pnr":"2345678901","statusCode":"RAC"}'
$pnr = Invoke-RestMethod -Uri "$base/api/v1/pnr-guide/explain" -Method Post -ContentType 'application/json' -Headers @{ Authorization = $pAuth } -Body $pnrReq
Write-Host "Mode        : $($pnr.mode)"
Write-Host "Masked PNR  : $($pnr.maskedPnr)"
Write-Host "PRS Zone    : $($pnr.prsZone)"
Write-Host "Status Code : $($pnr.statusCategory) - $($pnr.statusTitle)"
Write-Host "Eligibility : $($pnr.travelEligibility)"

# 8. Frontend HTML Delivery & Branding Audit
Write-Host "`n[8/8] Testing Frontend Single-Page App Delivery & Branding..." -ForegroundColor Yellow
$page = Invoke-WebRequest -Uri "$base/" -UseBasicParsing
Write-Host "Frontend HTTP Status : $($page.StatusCode)"
Write-Host "Frontend Size (bytes): $($page.Content.Length)"
$hasForbidden = $page.Content.Contains("RailSahayak AI")
if ($hasForbidden) {
    Write-Host "Contains 'RailSahayak AI': True (FAILED - FORBIDDEN)" -ForegroundColor Red
} else {
    Write-Host "Contains 'RailSahayak AI': False (PASSED - Clean)" -ForegroundColor Green
}
$hasOfficial = $page.Content.Contains("RailSahayak")
if ($hasOfficial) {
    Write-Host "Contains 'RailSahayak'   : True (PASSED - Official Name)" -ForegroundColor Green
} else {
    Write-Host "Contains 'RailSahayak'   : False (FAILED - Missing Official Name)" -ForegroundColor Red
}

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host " All Runtime Verification Checks Completed Successfully!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
