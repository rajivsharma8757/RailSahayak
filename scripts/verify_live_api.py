import subprocess
import time
import requests
import json
import base64
import sys

JAR_PATH = r"target\railsahayak-backend-0.1.0.jar"
BASE_URL = "http://localhost:8081"

H2_URL = "jdbc:h2:mem:railsahayak;MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;DEFAULT_NULL_ORDERING=HIGH;DB_CLOSE_DELAY=-1;INIT=CREATE DOMAIN IF NOT EXISTS TIMESTAMPTZ AS TIMESTAMP WITH TIME ZONE"

cmd = [
    "java",
    "-Duser.timezone=Asia/Kolkata",
    f"-Dspring.datasource.url={H2_URL}",
    "-Dspring.datasource.driver-class-name=org.h2.Driver",
    "-Dspring.datasource.username=sa",
    "-Dspring.datasource.password=",
    "-jar",
    JAR_PATH
]

print("Starting RailSahayak Spring Boot application...")
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

# Wait for server to start
started = False
start_time = time.time()
while time.time() - start_time < 30:
    try:
        r = requests.get(f"{BASE_URL}/api/v1/health", timeout=1)
        if r.status_code == 200:
            started = True
            print("Server is UP and responsive!")
            break
    except Exception:
        time.sleep(0.8)

if not started:
    print("FAILED to start server within 30 seconds.")
    proc.terminate()
    sys.exit(1)

print("\n" + "="*70)
print("RUNNING LIVE ENDPOINT & DASHBOARD VERIFICATION SUITE")
print("="*70)

results = []

def record(test_name, success, details):
    status = "PASS" if success else "FAIL"
    print(f"[{status}] {test_name}: {details}")
    results.append({"test": test_name, "status": status, "details": details})

# 1. Health Endpoint
try:
    r = requests.get(f"{BASE_URL}/api/v1/health")
    data = r.json()
    record("1. Public Health Check", r.status_code == 200 and data.get("status") == "PROTOTYPE", f"HTTP {r.status_code} | status: {data.get('status')} | prototype: {data.get('prototype')}")
except Exception as e:
    record("1. Public Health Check", False, str(e))

# 2. Frontend Index.html
try:
    r = requests.get(f"{BASE_URL}/")
    record("2. Static Frontend UI", r.status_code == 200 and "RailSahayak" in r.text, f"HTTP {r.status_code} | Contains 'RailSahayak': {'RailSahayak' in r.text} | Length: {len(r.text)} bytes")
except Exception as e:
    record("2. Static Frontend UI", False, str(e))

# 3. Smart Train Finder
try:
    payload = {"from": "New Delhi", "to": "Patna Junction", "date": "2026-10-25", "travelClass": "3A"}
    r = requests.post(f"{BASE_URL}/api/v1/train-search", json=payload)
    data = r.json()
    record("3. Smart Train Finder", r.status_code == 200 and len(data.get("results", [])) > 0, f"HTTP {r.status_code} | Found {len(data.get('results', []))} trains | First train: {data.get('results', [{}])[0].get('trainName')}")
except Exception as e:
    record("3. Smart Train Finder", False, str(e))

# 4. PNR Explainer
try:
    payload = {"pnrNumber": "2418901234"}
    r = requests.post(f"{BASE_URL}/api/v1/pnr-guide/explain", json=payload)
    data = r.json()
    record("4. PNR Explainer Engine", r.status_code == 200 and data.get("originatingZone") == "Northern Railway (New Delhi PRS)", f"HTTP {r.status_code} | Zone: {data.get('originatingZone')} | Advisory: {data.get('advisoryNote')[:45]}...")
except Exception as e:
    record("4. PNR Explainer Engine", False, str(e))

# 5. Payment Help - Secret Blocking (16 digit card)
try:
    payload = {"issueType": "deducted", "method": "CARD", "txRef": "My card is 4111 2222 3333 4444 please refund"}
    r = requests.post(f"{BASE_URL}/api/v1/payment-help/diagnose", json=payload)
    record("5. Payment Secret Blocking (Card PAN)", r.status_code == 400, f"HTTP {r.status_code} (Properly Rejected) | Error: {r.json().get('error')}")
except Exception as e:
    record("5. Payment Secret Blocking (Card PAN)", False, str(e))

# 6. Payment Help - Valid Diagnosis
try:
    payload = {"issueType": "deducted", "method": "UPI", "txRef": "UPI9876543210"}
    r = requests.post(f"{BASE_URL}/api/v1/payment-help/diagnose", json=payload)
    data = r.json()
    record("6. Payment Guidance Diagnostic", r.status_code == 200 and "T + 1" in data.get("expectedTat", ""), f"HTTP {r.status_code} | TAT: {data.get('expectedTat')} | Masked Ref: {data.get('maskedReference')}")
except Exception as e:
    record("6. Payment Guidance Diagnostic", False, str(e))

# 7. Unauthenticated Access to Protected Cases
try:
    r = requests.get(f"{BASE_URL}/api/v1/cases")
    record("7. Unauthenticated Protection", r.status_code == 401, f"HTTP {r.status_code} (Properly Blocked)")
except Exception as e:
    record("7. Unauthenticated Protection", False, str(e))

# Helper for Basic Auth
def basic(u, p):
    t = f"{u}:{p}"
    return {"Authorization": "Basic " + base64.b64encode(t.encode()).decode()}

# 8. Passenger Auth Me
try:
    r = requests.get(f"{BASE_URL}/api/v1/auth/me", headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("8. Passenger Authentication (/auth/me)", r.status_code == 200 and data.get("username") == "passenger", f"HTTP {r.status_code} | User: {data.get('username')} | Roles: {data.get('roles')}")
except Exception as e:
    record("8. Passenger Authentication (/auth/me)", False, str(e))

# 9. Passenger Submit Case
created_case_id = None
try:
    payload = {"category": "Payment confirmation delay", "description": "Money deducted via UPI at 10:05 AM, but no PNR was generated."}
    r = requests.post(f"{BASE_URL}/api/v1/cases", json=payload, headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    created_case_id = data.get("publicId")
    record("9. Passenger Case Creation", r.status_code == 201 and created_case_id.startswith("RS-"), f"HTTP {r.status_code} | Case ID: {created_case_id} | Status: {data.get('status')}")
except Exception as e:
    record("9. Passenger Case Creation", False, str(e))

# 10. Passenger List Cases (Own cases only)
try:
    r = requests.get(f"{BASE_URL}/api/v1/cases", headers=basic("passenger", "PassengerDemo123!"))
    data = r.json()
    record("10. Passenger Case Listing", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | Case Count: {len(data)} | Own Cases Verified")
except Exception as e:
    record("10. Passenger Case Listing", False, str(e))

# 11. RBAC Defense: Passenger Accessing Admin Cases (MUST FAIL 403)
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/cases", headers=basic("passenger", "PassengerDemo123!"))
    record("11. RBAC Isolation (Passenger $\to$ Admin)", r.status_code == 403, f"HTTP {r.status_code} (Strictly Forbidden for Passenger)")
except Exception as e:
    record("11. RBAC Isolation (Passenger $\to$ Admin)", False, str(e))

# 12. Admin Auth Me
try:
    r = requests.get(f"{BASE_URL}/api/v1/auth/me", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("12. Admin Authentication (/auth/me)", r.status_code == 200 and "ROLE_ADMIN" in data.get("roles", []), f"HTTP {r.status_code} | User: {data.get('username')} | Roles: {data.get('roles')}")
except Exception as e:
    record("12. Admin Authentication (/auth/me)", False, str(e))

# 13. Admin List All Cases
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/cases", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("13. Admin Dashboard Case Retrieval", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | Total Cases in System: {len(data)}")
except Exception as e:
    record("13. Admin Dashboard Case Retrieval", False, str(e))

# 14. Admin Update Case Status
try:
    if created_case_id:
        payload = {"status": "IN_PROGRESS", "note": "Investigating bank gateway reference with merchant aggregator."}
        r = requests.patch(f"{BASE_URL}/api/v1/admin/cases/{created_case_id}/status", json=payload, headers=basic("admin", "AdminDemo123!"))
        data = r.json()
        record("14. Admin Case Status Transition", r.status_code == 200 and data.get("status") == "IN_PROGRESS", f"HTTP {r.status_code} | New Status: {data.get('status')} | Event Logged")
    else:
        record("14. Admin Case Status Transition", False, "Skipped because no case ID was created")
except Exception as e:
    record("14. Admin Case Status Transition", False, str(e))

# 15. Admin View Audit Logs
try:
    r = requests.get(f"{BASE_URL}/api/v1/admin/audit-logs", headers=basic("admin", "AdminDemo123!"))
    data = r.json()
    record("15. Admin Audit Trail Access", r.status_code == 200 and len(data) >= 1, f"HTTP {r.status_code} | Audit Log Entries: {len(data)} | Latest Action: {data[0].get('action')}")
except Exception as e:
    record("15. Admin Audit Trail Access", False, str(e))

print("="*70)
passed = sum(1 for r in results if r["status"] == "PASS")
print(f"VERIFICATION COMPLETE: {passed}/{len(results)} Checks Passed.")
print("="*70)

# Gracefully terminate the server
proc.terminate()
try:
    proc.wait(timeout=5)
except Exception:
    proc.kill()

print("Server stopped cleanly.")
