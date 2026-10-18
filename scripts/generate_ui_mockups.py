"""
Generate High-Resolution UI Mockup Cards for Section 13 of RailSahayak Proposal.
Generates 4 authentic architectural screen specification cards matching static/index.html.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"C:\Railshahayak\railsahayak-backend-starter\railsahayak-backend-starter\docs\proposal_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEX_NAVY = "#0A2540"
HEX_STEEL = "#1E5591"
HEX_CYAN = "#0070BA"
HEX_LIGHT_BLUE = "#EEF4FB"
HEX_BORDER = "#CBD5E1"
HEX_DARK = "#1E293B"
HEX_MUTED = "#64748B"
HEX_WHITE = "#FFFFFF"
HEX_GREEN = "#15803D"
HEX_LIGHT_GREEN = "#F0FDF4"
HEX_AMBER = "#B45309"
HEX_LIGHT_AMBER = "#FFFBEB"
HEX_RED = "#A31D1D"
HEX_LIGHT_RED = "#FEF2F2"


def generate_mockup_train_finder():
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    # Main Card
    main_rect = patches.FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="round,pad=0.015,rounding_size=0.03",
                                       facecolor=HEX_WHITE, edgecolor=HEX_BORDER, linewidth=1.2)
    ax.add_patch(main_rect)

    # Title Bar
    title_rect = patches.Rectangle((0.02, 0.86), 0.96, 0.11, facecolor=HEX_LIGHT_BLUE)
    ax.add_patch(title_rect)
    ax.text(0.05, 0.915, "MODULE 1: SMART TRAIN FINDER — ROUTE DISCOVERY & CLASS FILTER",
            fontsize=8.5, fontweight='bold', color=HEX_NAVY, va='center')

    # Search Form Box
    form_rect = patches.FancyBboxPatch((0.04, 0.52), 0.92, 0.31, boxstyle="round,pad=0.01,rounding_size=0.02",
                                       facecolor="#F8FAFC", edgecolor=HEX_BORDER, linewidth=0.8)
    ax.add_patch(form_rect)
    ax.text(0.06, 0.77, "Journey Input Parameters (Prototype Form)", fontsize=7.2, fontweight='bold', color=HEX_STEEL)

    fields = [
        ("From Station:", "NDLS — New Delhi"),
        ("To Station:", "PNBE — Patna Junction"),
        ("Travel Date:", "2026-10-20 (Confirmed)"),
        ("Class Filter:", "3A — AC 3 Tier")
    ]
    for i, (label, val) in enumerate(fields):
        col = i % 2
        row = i // 2
        x_pos = 0.06 + col * 0.46
        y_pos = 0.69 - row * 0.09
        ax.text(x_pos, y_pos, label, fontsize=6.8, color=HEX_MUTED)
        ax.text(x_pos + 0.16, y_pos, val, fontsize=6.8, fontweight='bold', color=HEX_DARK)

    # Result Card Box
    res_rect = patches.FancyBboxPatch((0.04, 0.15), 0.92, 0.34, boxstyle="round,pad=0.01,rounding_size=0.02",
                                      facecolor=HEX_LIGHT_GREEN, edgecolor=HEX_GREEN, linewidth=1.0)
    ax.add_patch(res_rect)
    ax.text(0.06, 0.42, "12310 — New Delhi Rajdhani Express", fontsize=8.0, fontweight='bold', color=HEX_GREEN)
    ax.text(0.68, 0.42, "SAMPLE SCHEDULE", fontsize=6.5, fontweight='bold', color=HEX_GREEN,
            bbox=dict(boxstyle="round,pad=0.2", facecolor=HEX_WHITE, edgecolor=HEX_GREEN, lw=0.8))

    ax.text(0.06, 0.33, "Departure: 17:10 (NDLS)  --->  Arrival: 05:15 (+1 day, PNBE)  |  Duration: 12h 05m", fontsize=6.8, color=HEX_DARK)
    ax.text(0.06, 0.25, "Available Sample Classes: 1A (AC First), 2A (AC 2 Tier), 3A (AC 3 Tier)  |  Pantry Car: Yes", fontsize=6.5, color=HEX_MUTED)
    ax.text(0.06, 0.18, "Handoff Button: [Book on Official IRCTC Portal — irctc.co.in]  (External Browser Direct)", fontsize=6.8, fontweight='bold', color=HEX_CYAN)

    # Bottom Notice
    ax.text(0.04, 0.07, "[Operational Boundary] Prototype displays deterministic sample schedules; no live PRS seat inventory is queried.",
            fontsize=6.2, color=HEX_MUTED, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "ui_spec_train_finder.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_mockup_payment_help():
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    # Main Card
    main_rect = patches.FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="round,pad=0.015,rounding_size=0.03",
                                       facecolor=HEX_WHITE, edgecolor=HEX_BORDER, linewidth=1.2)
    ax.add_patch(main_rect)

    # Title Bar
    title_rect = patches.Rectangle((0.02, 0.86), 0.96, 0.11, facecolor=HEX_LIGHT_BLUE)
    ax.add_patch(title_rect)
    ax.text(0.05, 0.915, "MODULE 2: PAYMENT HELP DIAGNOSER — ADVISORY TRIAGE",
            fontsize=7.8, fontweight='bold', color=HEX_NAVY, va='center')

    # Ingress Filter Badge
    ax.text(0.76, 0.915, "[ZERO-TRUST ACTIVE]", fontsize=6.0, fontweight='bold', color=HEX_GREEN,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#F0FDF4", edgecolor=HEX_GREEN, lw=0.8), va='center')

    # Query Input Display
    q_rect = patches.FancyBboxPatch((0.04, 0.58), 0.92, 0.25, boxstyle="round,pad=0.01,rounding_size=0.02",
                                    facecolor="#F8FAFC", edgecolor=HEX_BORDER, linewidth=0.8)
    ax.add_patch(q_rect)
    ax.text(0.06, 0.77, "Reported Transaction Parameters", fontsize=7.2, fontweight='bold', color=HEX_STEEL)
    ax.text(0.06, 0.69, "Issue: Money Deducted, Ticket Not Generated  |  Payment Method: UPI  |  Masked Ref: UPI****098", fontsize=6.8, color=HEX_DARK)
    ax.text(0.06, 0.62, "Secret Cleansing Result: PASSED (Regex filter confirmed zero 16-digit card/secret patterns in reference string)", fontsize=6.4, color=HEX_GREEN, fontweight='bold')

    # Diagnostic Output Box
    diag_rect = patches.FancyBboxPatch((0.04, 0.13), 0.92, 0.42, boxstyle="round,pad=0.01,rounding_size=0.02",
                                       facecolor="#FFFBEB", edgecolor=HEX_AMBER, linewidth=1.0)
    ax.add_patch(diag_rect)
    ax.text(0.06, 0.49, "Structured Advisory Assessment & Action Plan (RBI TAT Framework)", fontsize=7.5, fontweight='bold', color=HEX_AMBER)

    advice_steps = [
        "1. Interbank Settlement Window: Bank debit without PNR indicates unconfirmed session. Allow T+1 business day.",
        "2. Avoid Duplicate Booking Attempts: Prevent immediate retry on same payment handle to avoid multiple debits.",
        "3. Official RBI Auto-Reversal TAT: UPI debits auto-reverse in T+1 business day; Cards in T+5 calendar days.",
        "4. Formal Dispute Escalation: If uncredited after official TAT, lodge formal chargeback with issuing bank."
    ]
    for i, step in enumerate(advice_steps):
        ax.text(0.06, 0.41 - i * 0.08, step, fontsize=5.8, color=HEX_DARK)

    # Bottom Notice
    ax.text(0.04, 0.06, "[Financial Authority Boundary] RailSahayak provides advisory guidance only; it does not process, refund, or reverse bank transactions.",
            fontsize=6.2, color=HEX_MUTED, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "ui_spec_payment_help.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_mockup_pnr_guide():
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    # Main Card
    main_rect = patches.FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="round,pad=0.015,rounding_size=0.03",
                                       facecolor=HEX_WHITE, edgecolor=HEX_BORDER, linewidth=1.2)
    ax.add_patch(main_rect)

    # Title Bar
    title_rect = patches.Rectangle((0.02, 0.86), 0.96, 0.11, facecolor=HEX_LIGHT_BLUE)
    ax.add_patch(title_rect)
    ax.text(0.05, 0.915, "MODULE 3: PNR STATUS GUIDE — PROCEDURAL ADVISORY & STATUTORY NOTICE",
            fontsize=8.5, fontweight='bold', color=HEX_NAVY, va='center')

    # Input PNR Box
    p_rect = patches.FancyBboxPatch((0.04, 0.60), 0.92, 0.23, boxstyle="round,pad=0.01,rounding_size=0.02",
                                    facecolor="#F8FAFC", edgecolor=HEX_BORDER, linewidth=0.8)
    ax.add_patch(p_rect)
    ax.text(0.06, 0.77, "Evaluated PNR: 2418901234 (10 Digits Validated)", fontsize=7.5, fontweight='bold', color=HEX_STEEL)
    ax.text(0.06, 0.69, "Derived PRS Cluster: Northern Railway / Delhi PRS Zone [Offline First-Digit Heuristic Routing Convention]", fontsize=6.8, color=HEX_DARK)
    ax.text(0.06, 0.63, "Database Lookup Disclosure: Not a live query against CRIS Passenger Reservation System (PRS)", fontsize=6.5, color=HEX_AMBER, style='italic')

    # Advisory Box
    adv_rect = patches.FancyBboxPatch((0.04, 0.13), 0.92, 0.44, boxstyle="round,pad=0.01,rounding_size=0.02",
                                      facecolor=HEX_LIGHT_RED, edgecolor=HEX_RED, linewidth=1.0)
    ax.add_patch(adv_rect)
    ax.text(0.06, 0.51, "Procedural Charting Rules & Section 138 Statutory Notice", fontsize=7.5, fontweight='bold', color=HEX_RED)

    guidance_lines = [
        "- 1st Charting Timeline: Prepared at least 4 hours prior to train departure (20:00 hrs for morning trains).",
        "- 2nd Charting Timeline: Prepared 30 to 50 minutes prior to departure, accommodating last-minute cancellations.",
        "- RAC Accommodation: RAC ticket holders are legally entitled to board the train and share a side-lower berth.",
        "- STATUTORY SECTION 138 WARNING: Fully waitlisted e-tickets (WL on charting) cancel automatically via IRCTC.",
        "  Under Section 138 of The Railways Act 1989, boarding a train with a cancelled e-ticket is deemed travelling without ticket,",
        "  attracting excess charges (penalty fare) and immediate detraining by Ticket Checking Staff (TTE)."
    ]
    for i, line in enumerate(guidance_lines):
        ax.text(0.06, 0.44 - i * 0.062, line, fontsize=5.8, color=HEX_DARK if i < 3 else HEX_RED)

    # Bottom Notice
    ax.text(0.04, 0.06, "[Verification Mandatory] Live PNR confirmation status must always be checked on indianrail.gov.in or irctc.co.in.",
            fontsize=6.2, color=HEX_MUTED, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "ui_spec_pnr_guide.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_mockup_case_admin():
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    # Main Card
    main_rect = patches.FancyBboxPatch((0.02, 0.03), 0.96, 0.94, boxstyle="round,pad=0.015,rounding_size=0.03",
                                       facecolor=HEX_WHITE, edgecolor=HEX_BORDER, linewidth=1.2)
    ax.add_patch(main_rect)

    # Title Bar
    title_rect = patches.Rectangle((0.02, 0.86), 0.96, 0.11, facecolor=HEX_LIGHT_BLUE)
    ax.add_patch(title_rect)
    ax.text(0.05, 0.915, "MODULE 4: SUPPORT CASE CAPTURE & ADMIN TRIAGE CONSOLE",
            fontsize=8.5, fontweight='bold', color=HEX_NAVY, va='center')

    # Left Box: Passenger Case Submission
    c_rect = patches.FancyBboxPatch((0.04, 0.14), 0.44, 0.69, boxstyle="round,pad=0.01,rounding_size=0.02",
                                    facecolor="#F8FAFC", edgecolor=HEX_BORDER, linewidth=0.8)
    ax.add_patch(c_rect)
    ax.text(0.06, 0.77, "Passenger Case Submission (REST API)", fontsize=7.2, fontweight='bold', color=HEX_STEEL)
    ax.text(0.06, 0.71, "Endpoint: POST /api/v1/cases", fontsize=6.2, color=HEX_MUTED)
    ax.text(0.06, 0.64, "Generated Public ID: RS-D8A75608", fontsize=6.8, fontweight='bold', color=HEX_NAVY)
    ax.text(0.06, 0.58, "Category: Accessibility assistance", fontsize=6.5, color=HEX_DARK)
    ax.text(0.06, 0.51, "Description: Wheelchair requested for\nsenior citizen at Patna Jn, Platform 1.", fontsize=6.3, color=HEX_DARK)
    ax.text(0.06, 0.38, "Status: OPEN (Local PostgreSQL)", fontsize=6.5, fontweight='bold', color=HEX_AMBER)
    ax.text(0.06, 0.32, "Correlation ID: rs-4a9f821c", fontsize=6.0, color=HEX_MUTED)
    ax.text(0.06, 0.22, "Security: Passenger role isolated;\nother passengers receive HTTP 404.", fontsize=6.0, color=HEX_GREEN)

    # Right Box: Admin Triage Console
    adm_rect = patches.FancyBboxPatch((0.52, 0.14), 0.44, 0.69, boxstyle="round,pad=0.01,rounding_size=0.02",
                                      facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_STEEL, linewidth=0.8)
    ax.add_patch(adm_rect)
    ax.text(0.54, 0.77, "Staff Triage Console (ROLE_ADMIN)", fontsize=7.2, fontweight='bold', color=HEX_NAVY)
    ax.text(0.54, 0.71, "Endpoint: PATCH /api/v1/admin/cases/{id}/status", fontsize=6.2, color=HEX_MUTED)
    ax.text(0.54, 0.64, "State Transition: OPEN ---> IN_PROGRESS", fontsize=6.8, fontweight='bold', color=HEX_GREEN)
    ax.text(0.54, 0.57, "Staff Actor: admin (Commercial Desk)", fontsize=6.5, color=HEX_DARK)
    ax.text(0.54, 0.50, "Investigation Note: 'Station Master notified;\nwheelchair attendant deployed to Coach B4.'", fontsize=6.2, color=HEX_DARK)
    ax.text(0.54, 0.36, "Dual Audit Persistence:", fontsize=6.5, fontweight='bold', color=HEX_STEEL)
    ax.text(0.54, 0.30, "- case_events: Appended timeline event", fontsize=6.0, color=HEX_DARK)
    ax.text(0.54, 0.24, "- audit_logs: Recorded actor, note, and delta", fontsize=6.0, color=HEX_DARK)
    ax.text(0.54, 0.18, "Integrity: B-Tree indexed on created_at DESC", fontsize=6.0, color=HEX_GREEN)

    # Bottom Notice
    ax.text(0.04, 0.06, "[Redressal Scope] Prototype manages local pre-triage cases; emergency grievances must be submitted directly to RailMadad 139.",
            fontsize=6.2, color=HEX_MUTED, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "ui_spec_case_admin.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def main():
    print("Generating High-Resolution UI Mockup Cards...")
    generate_mockup_train_finder()
    generate_mockup_payment_help()
    generate_mockup_pnr_guide()
    generate_mockup_case_admin()
    print("All UI Specification Assets Generated Successfully!")


if __name__ == "__main__":
    main()
