import requests
import json
import base64

BASE_URL = "http://localhost:8081"
print("Probing running RailSahayak server at:", BASE_URL)

results = []

def record(test_name, success, details):
    status = "PASS" if success else "FAIL"
    print(f"[{status}] {test_name}: {details}")
    results.append({"test": test_name, "status": status, "details": details})

def basic(u, p):
    t = f"{u}:{p}"
    return {"Authorization": "Basic " + base64.b64encode(t.encode()).decode()}

# 1. Health Endpoint
try:
    r = requests.get(f"{BASE_URL}/api/v1/health")
    data = r.json()
    record("1. Public Health Check", r.status_code == 200 and data.get("status") == "UP", f"HTTP {r.status_code} | status: {data.get('status')}")
except Exception as e:
    record("1. Public Health Check", False, str(e))

# 2. Static Frontend UI
try:
    r = requests.get(f"{BASE_URL}/")
    record("2. Static Frontend UI", r.status_code == 200 and "RailSahayak" in r.text, f"HTTP {r.status_code} | Title found | Length: {len(r.text)} bytes")
except Exception as e:
    record("2. Static Frontend UI", False, str(e))

# 3. Smart Train Finder (with Passenger Auth)
try:
    payload = {"from": "New Delhi", "to": "Patna Junction", "date": "2026-10-25", "travelClass": "3A"}
    r = requests.post(f"{BASE_URL}/api/v1/train-search", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("3. Smart Train Finder", r.status_code == 200 and len(data.get("results", [])) > 0, f"HTTP {r.status_code} | Found {len(data.get('results', []))} trains | Train: {data.get('results', [{}])[0].get('trainName')}")
except Exception as e:
    record("3. Smart Train Finder", False, str(e))

# 4. PNR Explainer (with Passenger Auth)
try:
    payload = {"pnr": "2418901234", "statusCode": "CNF"}
    r = requests.post(f"{BASE_URL}/api/v1/pnr-guide/explain", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("4. PNR Explainer Engine", r.status_code == 200 and "Northern" in data.get("prsZone", ""), f"HTTP {r.status_code} | Zone: {data.get('prsZone')[:50]}... | Title: {data.get('statusTitle')}")
except Exception as e:
    record("4. PNR Explainer Engine", False, str(e))

# 5. Payment Secret Blocking (Card PAN rejection)
try:
    payload = {"issue": "deducted", "method": "CARD", "reference": "My card is 4111 2222 3333 4444 please refund"}
    r = requests.post(f"{BASE_URL}/api/v1/payment-help/diagnose", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    record("5. Payment Secret Blocking (Card PAN)", r.status_code == 400, f"HTTP {r.status_code} (Properly Rejected) | Error: {r.json().get('error')}")
except Exception as e:
    record("5. Payment Secret Blocking (Card PAN)", False, str(e))

# 6. Payment Guidance Diagnostic
try:
    payload = {"issue": "deducted", "method": "UPI", "reference": "UPI9876543210"}
    r = requests.post(f"{BASE_URL}/api/v1/payment-help/diagnose", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("6. Payment Guidance Diagnostic", r.status_code == 200 and "UPI" in data.get("maskedReference", ""), f"HTTP {r.status_code} | Masked Ref: {data.get('maskedReference')} | Recommendation: {data.get('actionRecommendation')[:40]}...")
except Exception as e:
    record("6. Payment Guidance Diagnostic", False, str(e))

# 7. Unauthenticated Protection
try:
    r = requests.get(f"{BASE_URL}/api/v1/cases")
    record("7. Unauthenticated Ingress Protection", r.status_code == 401, f"HTTP {r.status_code} (Access Denied)")
except Exception as e:
    record("7. Unauthenticated Ingress Protection", False, str(e))

# 8. Passenger Authentication (/auth/me)
try:
    r = requests.get(f"{BASE_URL}/api/v1/auth/me", headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("8. Passenger Auth (/auth/me)", r.status_code == 200 and data.get("username") == "passenger", f"HTTP {r.status_code} | User: {data.get('username')} | Roles: {data.get('roles')}")
except Exception as e:
    record("8. Passenger Auth (/auth/me)", False, str(e))

# 9. Passenger Case Creation
created_case_id = None
try:
    payload = {"category": "Payment confirmation delay", "description": "Money deducted via UPI at 10:05 AM, but no PNR was generated."}
    r = requests.post(f"{BASE_URL}/api/v1/cases", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    created_case_id = data.get("id")
    record("9. Passenger Case Creation", r.status_code == 200 and created_case_id is not None, f"HTTP {r.status_code} | Created Case ID: {created_case_id} | Status: {data.get('status')}")
except Exception as e:
    record("9. Passenger Case Creation", False, str(e))

# 10. Passenger Case Listing
try:
    r = requests.get(f"{BASE_URL}/api/v1/cases", headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("10. Passenger Case Listing", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | Returned {len(data)} passenger cases")
except Exception as e:
    record("10. Passenger Case Listing", False, str(e))

# 11. RBAC Isolation: Passenger accessing Admin API (MUST BE 403 FORBIDDEN)
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/cases", headers=basic("passenger", "PassengerDemo123!"))
    record("11. RBAC Route Defense (Passenger -> Admin API)", r.status_code == 403, f"HTTP {r.status_code} (Strictly Forbidden for Passenger)")
except Exception as e:
    record("11. RBAC Route Defense (Passenger -> Admin API)", False, str(e))

# 12. Admin Authentication (/auth/me)
try:
    r = requests.get(f"{BASE_URL}/api/v1/auth/me", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("12. Admin Auth (/auth/me)", r.status_code == 200 and "ROLE_ADMIN" in data.get("roles", []), f"HTTP {r.status_code} | User: {data.get('username')} | Roles: {data.get('roles')}")
except Exception as e:
    record("12. Admin Auth (/auth/me)", False, str(e))

# 13. Admin Dashboard Case Retrieval
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/cases", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("13. Admin Dashboard Case Listing", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | Retrieved {len(data)} total cases")
except Exception as e:
    record("13. Admin Dashboard Case Listing", False, str(e))

# 14. Admin Case Status Update
try:
    if created_case_id:
        payload = {"status": "IN_PROGRESS", "note": "Investigating bank gateway transaction reference with acquiring switch."}
        r = requests.patch(f"{BASE_URL}/api/v1/admin/cases/{created_case_id}/status", json=payload, headers=basic("admin", "AdminDemo123!"))
        data = r.json()
        record("14. Admin Case Status Transition", r.status_code == 200 and data.get("status") == "IN_PROGRESS", f"HTTP {r.status_code} | Case {created_case_id} updated to {data.get('status')}")
    else:
        record("14. Admin Case Status Transition", False, "No case ID available")
except Exception as e:
    record("14. Admin Case Status Transition", False, str(e))

# 15. Admin View Audit Logs
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/audit-logs", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("15. Admin Audit Trail Retrieval", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | {len(data)} audit log events verified | Latest action: {data[0].get('action')}")
except Exception as e:
    record("15. Admin Audit Trail Retrieval", False, str(e))

print("\n" + "="*70)
passed = sum(1 for r in results if r["status"] == "PASS")
print(f"LIVE TEST REPORT: {passed}/{len(results)} PASSING")
print("="*70)
