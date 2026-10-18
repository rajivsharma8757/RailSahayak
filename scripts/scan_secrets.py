import os
import re

PATTERNS = [
    (re.compile(r"ghp_[a-zA-Z0-9]{36}"), "GitHub Personal Access Token"),
    (re.compile(r"gho_[a-zA-Z0-9]{36}"), "GitHub OAuth Token"),
    (re.compile(r"github_pat_[a-zA-Z0-9_]{82}"), "GitHub Fine-Grained Token"),
    (re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----"), "Private Key"),
    (re.compile(r"AIza[0-9A-Za-z-_]{35}"), "Google API Key"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS Access Key"),
]

EXCLUDE_DIRS = {".git", "target", ".idea", ".vscode", "backups", "comprehensive_proposal_qa_images"}
EXCLUDE_EXTS = {".png", ".jpg", ".jpeg", ".pdf", ".jar", ".class", ".exe", ".pyc"}

findings = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in EXCLUDE_EXTS:
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                for line_idx, line in enumerate(f, 1):
                    for pat, name in PATTERNS:
                        if pat.search(line):
                            findings.append((filepath, line_idx, name, line.strip()[:80]))
        except Exception:
            pass

print(f"Total findings: {len(findings)}")
for item in findings:
    print(item)
