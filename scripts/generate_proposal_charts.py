"""
Generate High-Resolution Charts and Diagrams for RailSahayak Comprehensive Proposal
Using Matplotlib and Pillow with Corporate Railway Design Identity:
- Navy: #0A2540
- Steel Blue: #1E5591
- Accent Cyan: #0070BA
- Slate / Border: #CBD5E1
- Light BG: #F8FAFC
- Warning / Amber: #B45309
- Success / Green: #15803D
- Danger / Red: #A31D1D
"""

import os
import sys
import tempfile

os.environ['MPLCONFIGDIR'] = os.path.join(tempfile.gettempdir(), 'mpl_cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "proposal_assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color Palette Constants
HEX_NAVY = "#0A2540"
HEX_STEEL = "#1E5591"
HEX_CYAN = "#0070BA"
HEX_LIGHT_BLUE = "#EEF4FB"
HEX_BORDER = "#CBD5E1"
HEX_DARK = "#1E293B"
HEX_MUTED = "#64748B"
HEX_AMBER = "#B45309"
HEX_GREEN = "#15803D"
HEX_RED = "#A31D1D"
HEX_BG = "#F8FAFC"
HEX_WHITE = "#FFFFFF"

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']


def generate_chart_a_readiness():
    """Chart A: Feature Readiness Breakdown"""
    fig, ax = plt.subplots(figsize=(7.5, 3.0), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)

    categories = [
        "Implemented & Verified\n(Production-Grade)",
        "Functional Prototype\n(Sample / Local Engine)",
        "Advisory Explainer\n(Guidance / Zero-Trust)",
        "External Integration\n(Requires Authorization)"
    ]
    counts = [11, 3, 2, 5]
    colors_list = [HEX_NAVY, HEX_STEEL, HEX_CYAN, HEX_AMBER]

    bars = ax.barh(categories, counts, color=colors_list, height=0.52, edgecolor=HEX_BORDER, linewidth=1)
    
    for bar, count in zip(bars, counts):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, f"{count} Features", 
                va='center', ha='left', fontsize=9, fontweight='bold', color=HEX_DARK)

    ax.set_xlim(0, 14)
    ax.set_xlabel("Number of Evaluated Technical Capabilities / Modules", fontsize=8.5, fontweight='bold', color=HEX_NAVY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(HEX_BORDER)
    ax.spines['bottom'].set_color(HEX_BORDER)
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color=HEX_BORDER)
    ax.set_axisbelow(True)
    ax.tick_params(colors=HEX_DARK, labelsize=8.5)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "chart_a_readiness.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_chart_b_testing():
    """Chart B: Automated Verification & Testing Suite"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 2.8), dpi=300, gridspec_kw={'width_ratios': [1.2, 1]})
    fig.patch.set_facecolor(HEX_WHITE)
    ax1.set_facecolor(HEX_WHITE)
    ax2.set_facecolor(HEX_WHITE)

    # Bar breakdown
    modules = ["Security & RBAC", "Data Persistence", "Advisory Engines", "Rate Limit & Proxy"]
    tests = [8, 6, 10, 5]
    colors_b = [HEX_NAVY, HEX_STEEL, HEX_CYAN, "#2563EB"]

    bars = ax1.bar(modules, tests, color=colors_b, width=0.55, edgecolor=HEX_BORDER, linewidth=1)
    for bar, val in zip(bars, tests):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(val), 
                 ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=HEX_NAVY)

    ax1.set_ylim(0, 12)
    ax1.set_ylabel("Automated Integration Tests", fontsize=8, fontweight='bold', color=HEX_NAVY)
    ax1.set_title("Test Distribution by Component (29 Tests)", fontsize=8.5, fontweight='bold', color=HEX_NAVY)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color(HEX_BORDER)
    ax1.spines['bottom'].set_color(HEX_BORDER)
    ax1.yaxis.grid(True, linestyle='--', alpha=0.5, color=HEX_BORDER)
    ax1.set_axisbelow(True)
    ax1.tick_params(colors=HEX_DARK, labelsize=7.5)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=12, ha='right')

    # Donut Chart for Pass Rate
    wedges, texts = ax2.pie([29, 0], colors=[HEX_GREEN, HEX_RED], startangle=90,
                            wedgeprops=dict(width=0.4, edgecolor=HEX_WHITE, linewidth=2))
    ax2.text(0, 0, "100%\nPASS", ha='center', va='center', fontsize=11, fontweight='bold', color=HEX_GREEN)
    ax2.set_title("Integration Test Pass Rate\n(29 Passed, 0 Failed, 0 Errors)", fontsize=8.5, fontweight='bold', color=HEX_NAVY)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "chart_b_testing.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_chart_c_kpis():
    """Chart C: Proposed Pilot Evaluation KPIs"""
    fig, ax = plt.subplots(figsize=(7.5, 2.9), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)

    kpis = [
        "First-Contact Triage Accuracy",
        "Self-Service Guidance Comprehension",
        "Official Channel Identification",
        "Zero-Trust Credential Defense",
        "Advisory Query Response (<250ms)"
    ]
    targets = [95, 90, 88, 100, 96]
    y_pos = np.arange(len(kpis))

    ax.barh(y_pos, [100]*len(kpis), color=HEX_LIGHT_BLUE, height=0.48, edgecolor=HEX_BORDER, label="Scale (100%)")
    bars = ax.barh(y_pos, targets, color=HEX_STEEL, height=0.48, edgecolor=HEX_NAVY, label="Target Benchmark")

    for i, target in enumerate(targets):
        ax.text(target - 3, y_pos[i], f"{target}%", va='center', ha='right', fontsize=8, fontweight='bold', color=HEX_WHITE)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(kpis, fontsize=8, color=HEX_DARK, fontweight='bold')
    ax.set_xlim(0, 105)
    ax.set_xlabel("Proposed Target Success Threshold (%)", fontsize=8, fontweight='bold', color=HEX_NAVY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(HEX_BORDER)
    ax.spines['bottom'].set_color(HEX_BORDER)
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color=HEX_BORDER)
    ax.set_axisbelow(True)
    ax.tick_params(colors=HEX_DARK, labelsize=7.5)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "chart_c_kpis.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_chart_d_costs():
    """Chart D: Multi-Tier Infrastructure & Operating Cost Scenarios"""
    fig, ax = plt.subplots(figsize=(7.5, 3.0), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)

    scenarios = ["Tier 1: Dev / Sandbox\n(Single-Node Prototype)", "Tier 2: Controlled Pilot\n(100k Queries / Month)", "Tier 3: Multi-Zone Scale\n(1M Queries / Month)"]
    compute = [4500, 16000, 48000]
    db_storage = [3500, 12000, 32000]
    redis_cache = [0, 6000, 18000]
    security_mon = [2000, 8000, 22000]
    gateway_buf = [1000, 3000, 5000]

    width = 0.42
    x = np.arange(len(scenarios))

    b1 = ax.bar(x, compute, width, label="Compute (App Services)", color=HEX_NAVY, edgecolor=HEX_BORDER)
    b2 = ax.bar(x, db_storage, width, bottom=compute, label="Managed PostgreSQL", color=HEX_STEEL, edgecolor=HEX_BORDER)
    b3 = ax.bar(x, redis_cache, width, bottom=np.array(compute)+np.array(db_storage), label="Distributed Redis", color=HEX_CYAN, edgecolor=HEX_BORDER)
    b4 = ax.bar(x, security_mon, width, bottom=np.array(compute)+np.array(db_storage)+np.array(redis_cache), label="Security & Logging", color="#2563EB", edgecolor=HEX_BORDER)
    b5 = ax.bar(x, gateway_buf, width, bottom=np.array(compute)+np.array(db_storage)+np.array(redis_cache)+np.array(security_mon), label="TLS & Network Buffer", color="#60A5FA", edgecolor=HEX_BORDER)

    totals = [c + d + r + s + g for c, d, r, s, g in zip(compute, db_storage, redis_cache, security_mon, gateway_buf)]
    for i, total in enumerate(totals):
        ax.text(x[i], total + 2000, f"Rs. {total:,}\n/ mo", ha='center', va='bottom', fontsize=7.5, fontweight='bold', color=HEX_NAVY)

    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=7.5, color=HEX_DARK, fontweight='bold')
    ax.set_ylabel("Estimated Monthly Cloud Spend (INR)", fontsize=8, fontweight='bold', color=HEX_NAVY)
    ax.set_ylim(0, 150000)
    ax.legend(loc='upper left', fontsize=7, frameon=True, facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_BORDER)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(HEX_BORDER)
    ax.spines['bottom'].set_color(HEX_BORDER)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5, color=HEX_BORDER)
    ax.set_axisbelow(True)
    ax.tick_params(colors=HEX_DARK, labelsize=7.5)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "chart_d_costs.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_chart_e_risk_matrix():
    """Chart E: Qualitative Risk Prioritization Matrix"""
    fig, ax = plt.subplots(figsize=(7.5, 3.0), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)

    # 3x3 background grid
    grid_colors = [
        ["#F0FDF4", "#FEFCE8", "#FEF2F2"],
        ["#FEFCE8", "#FFFBEB", "#FEE2E2"],
        ["#FEF2F2", "#FEE2E2", "#FCA5A5"]
    ]

    for ix in range(3):
        for iy in range(3):
            rect = patches.Rectangle((ix + 0.5, iy + 0.5), 1, 1, facecolor=grid_colors[iy][ix], edgecolor=HEX_BORDER, alpha=0.8)
            ax.add_patch(rect)

    risks = [
        ("R1: Misinterpreted as Official", 1.95, 2.75, HEX_RED, (0.0, 0.13), 'center'),
        ("R2: Outdated Tariff Rules", 1.15, 2.75, HEX_AMBER, (0.0, 0.13), 'center'),
        ("R3: Tatkal Surge Concurrency", 2.15, 2.05, HEX_AMBER, (0.08, 0.0), 'left'),
        ("R4: Live API MoU Absence", 2.85, 2.85, HEX_RED, (0.0, -0.13), 'center'),
        ("R5: Sensitive Financial Data Input", 1.15, 1.85, HEX_GREEN, (0.0, -0.13), 'center'),
        ("R6: Distributed Rate Limit Drift", 1.15, 1.15, HEX_GREEN, (0.08, 0.0), 'left')
    ]

    for r in risks:
        label = r[0]
        x_val = r[1]
        y_val = r[2]
        col = r[3]
        offset = r[4]
        align = r[5]
        ax.scatter(x_val, y_val, color=col, s=80, edgecolors=HEX_NAVY, zorder=5)
        ax.text(x_val + offset[0], y_val + offset[1], label, fontsize=6.8, fontweight='bold', color=HEX_NAVY, va='center', ha=align, zorder=6)

    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0.5, 3.5)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["Low Likelihood", "Medium Likelihood", "High Likelihood"], fontsize=8, fontweight='bold', color=HEX_DARK)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["Low Impact", "Medium Impact", "High Impact"], fontsize=8, fontweight='bold', color=HEX_DARK)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(HEX_BORDER)
    ax.spines['bottom'].set_color(HEX_BORDER)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "chart_e_risk_matrix.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_system_architecture():
    """Diagram 1: System Architecture Diagram"""
    fig, ax = plt.subplots(figsize=(7.5, 3.6), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    def draw_box(x, y, w, h, title, subtitle, bg_c=HEX_LIGHT_BLUE, border_c=HEX_NAVY, text_c=HEX_NAVY, dashed=False):
        ls = '--' if dashed else '-'
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.05",
                                      facecolor=bg_c, edgecolor=border_c, linestyle=ls, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h*0.65, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color=text_c)
        if subtitle:
            ax.text(x + w/2, y + h*0.32, subtitle, ha='center', va='center', fontsize=6.5, color=HEX_DARK)

    # 1. Client Tier
    draw_box(0.04, 0.72, 0.25, 0.22, "CLIENT TIER", "Passenger Browser / Web UI\nHTML5, JS, Responsive CSS", HEX_LIGHT_BLUE, HEX_NAVY)

    # 2. Security & Gateway Tier
    draw_box(0.34, 0.72, 0.28, 0.22, "SECURITY & GATEWAY", "Reverse Proxy (Trusted IP)\nRateLimitingFilter (300 rpm)\nCorrelationIdFilter (MDC)", HEX_LIGHT_BLUE, HEX_STEEL)

    # 3. Application Services Tier
    draw_box(0.04, 0.36, 0.58, 0.28, "SPRING BOOT 3.4.5 BACKEND REST SERVICES", 
             "CaseController • AdminCaseController • PaymentHelpController\nPnrGuideController • TrainSearchController • GlobalExceptionHandler\nSpring Security RBAC (ROLE_PASSENGER, ROLE_ADMIN)", HEX_BG, HEX_NAVY)

    # 4. Persistence Tier
    draw_box(0.04, 0.04, 0.58, 0.24, "PERSISTENCE TIER (POSTGRESQL 16)", 
             "support_cases (Tickets) • case_events (Timeline Audit)\naudit_logs (Admin Actions) • Flyway Schema Migrations V1-V2", HEX_LIGHT_BLUE, HEX_STEEL)

    # 5. External Official Railway Infrastructure
    rect_ext = patches.FancyBboxPatch((0.67, 0.04), 0.30, 0.90, boxstyle="round,pad=0.02,rounding_size=0.05",
                                      facecolor="#FFFBEB", edgecolor=HEX_AMBER, linestyle='--', linewidth=1.5)
    ax.add_patch(rect_ext)
    ax.text(0.82, 0.90, "OFFICIAL RAILWAY SYSTEMS", ha='center', va='center', fontsize=7.5, fontweight='bold', color=HEX_AMBER)
    ax.text(0.82, 0.85, "(Proposed Authorization / Future)", ha='center', va='center', fontsize=6.2, color=HEX_MUTED)

    draw_box(0.69, 0.65, 0.26, 0.15, "CRIS PRS & NTES", "Seat Inventory & Train Running\n(Read-Only Staging Gateway)", HEX_WHITE, HEX_AMBER, HEX_AMBER, dashed=True)
    draw_box(0.69, 0.45, 0.26, 0.15, "IRCTC E-TICKETING", "Official Passenger Booking &\nCancellation Engine", HEX_WHITE, HEX_AMBER, HEX_AMBER, dashed=True)
    draw_box(0.69, 0.25, 0.26, 0.15, "RAILMADAD CRM", "Ministry of Railways 139\nOfficial Grievance Redressal", HEX_WHITE, HEX_AMBER, HEX_AMBER, dashed=True)
    draw_box(0.69, 0.06, 0.26, 0.15, "NPCI / PAYMENT GATEWAYS", "Banking Settlement Verification\n& Reversal Reconciliations", HEX_WHITE, HEX_AMBER, HEX_AMBER, dashed=True)

    # Connectors
    ax.annotate("", xy=(0.34, 0.83), xytext=(0.29, 0.83), arrowprops=dict(arrowstyle="->", color=HEX_NAVY, lw=1.2))
    ax.annotate("", xy=(0.33, 0.64), xytext=(0.48, 0.72), arrowprops=dict(arrowstyle="->", color=HEX_NAVY, lw=1.2))
    ax.annotate("", xy=(0.33, 0.28), xytext=(0.33, 0.36), arrowprops=dict(arrowstyle="<->", color=HEX_NAVY, lw=1.2))
    ax.annotate("", xy=(0.67, 0.50), xytext=(0.62, 0.50), arrowprops=dict(arrowstyle="->", color=HEX_AMBER, lw=1.2, linestyle='--'))

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "diagram_system_architecture.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_data_flow():
    """Diagram 2: End-to-End Request & Data Flow"""
    fig, ax = plt.subplots(figsize=(7.5, 2.2), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    steps = [
        ("Step 1:\nIngress", "HTTP Request\nClient IP & Headers"),
        ("Step 2:\nProxy Check", "Trusted Proxy Filter\n& Rate Limiter"),
        ("Step 3:\nObservability", "Correlation ID\nMDC SLF4J Injected"),
        ("Step 4:\nSecurity", "Spring Security\nRBAC & Secret Regex"),
        ("Step 5:\nExecution", "Advisory Engine or\nPostgreSQL DB"),
        ("Step 6:\nEgress", "Sanitized Response\nOfficial Link")
    ]

    for i, (title, desc) in enumerate(steps):
        x = 0.015 + i * 0.165
        rect = patches.FancyBboxPatch((x, 0.08), 0.135, 0.84, boxstyle="round,pad=0.005,rounding_size=0.03",
                                      facecolor=HEX_LIGHT_BLUE if i < 5 else "#F0FDF4",
                                      edgecolor=HEX_NAVY if i < 5 else HEX_GREEN, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x + 0.0675, 0.72, title, ha='center', va='center', fontsize=6.2, fontweight='bold', color=HEX_NAVY if i < 5 else HEX_GREEN)
        ax.text(x + 0.0675, 0.32, desc, ha='center', va='center', fontsize=5.6, color=HEX_DARK)

        if i < 5:
            ax.annotate("", xy=(x + 0.165, 0.50), xytext=(x + 0.138, 0.50),
                        arrowprops=dict(arrowstyle="->", color=HEX_CYAN, lw=1.2))

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "diagram_data_flow.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_ecosystem_boundary():
    """Diagram 3: Ecosystem Boundary Diagram"""
    fig, ax = plt.subplots(figsize=(7.5, 3.0), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    rect_left = patches.FancyBboxPatch((0.04, 0.06), 0.42, 0.86, boxstyle="round,pad=0.02,rounding_size=0.05",
                                       facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_NAVY, linewidth=1.5)
    ax.add_patch(rect_left)
    ax.text(0.25, 0.84, "RAILSAHAYAK ADVISORY LAYER", ha='center', va='center', fontsize=8, fontweight='bold', color=HEX_NAVY)
    ax.text(0.25, 0.78, "(Independent Pre-Triage Prototype)", ha='center', va='center', fontsize=6.8, color=HEX_MUTED)

    adv_items = [
        "• Plain-language procedural guidance",
        "• Heuristic PNR routing taxonomy explainer",
        "• Zero-trust payment help & RBI TAT advisory",
        "• Structured passenger issue intake & case ID",
        "• Referral to verified authoritative channels",
        "• Does NOT issue tickets or modify bookings",
        "• Does NOT hold funds or execute reversals"
    ]
    for i, item in enumerate(adv_items):
        ax.text(0.07, 0.67 - i*0.078, item, fontsize=6.8, color=HEX_DARK)

    rect_right = patches.FancyBboxPatch((0.54, 0.06), 0.42, 0.86, boxstyle="round,pad=0.02,rounding_size=0.05",
                                        facecolor="#FFFBEB", edgecolor=HEX_AMBER, linewidth=1.5)
    ax.add_patch(rect_right)
    ax.text(0.75, 0.84, "AUTHORITATIVE RAILWAY SYSTEMS", ha='center', va='center', fontsize=8, fontweight='bold', color=HEX_AMBER)
    ax.text(0.75, 0.78, "(Indian Railways • CRIS • IRCTC • RailMadad)", ha='center', va='center', fontsize=6.8, color=HEX_MUTED)

    auth_items = [
        "• IRCTC: Official e-ticketing & commercial bookings",
        "• CRIS PRS: Authoritative seat inventory & charts",
        "• CRIS NTES: Live train tracking & delay feeds",
        "• RailMadad & 139: Official grievance investigation",
        "• RBI / Bank Gateways: Financial settlement & reversals",
        "• Station TTE / Staff: On-train accommodation rights",
        "• Statutory Authority: Sole official legal records"
    ]
    for i, item in enumerate(auth_items):
        ax.text(0.57, 0.67 - i*0.078, item, fontsize=6.8, color=HEX_DARK)

    # Middle Bridge
    ax.annotate("Directs Passengers to\nOfficial Channels\n(Zero Override)", xy=(0.53, 0.45), xytext=(0.47, 0.45),
                ha='center', va='center', fontsize=6.5, fontweight='bold', color=HEX_NAVY,
                arrowprops=dict(arrowstyle="->", color=HEX_CYAN, lw=1.5))

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "diagram_ecosystem_boundary.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_payment_workflow():
    """Diagram 4: Payment Diagnostic Decision Tree"""
    fig, ax = plt.subplots(figsize=(7.5, 2.8), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    def draw_node(x, y, w, h, text, bg_c=HEX_LIGHT_BLUE, border_c=HEX_NAVY, text_c=HEX_NAVY):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                                      facecolor=bg_c, edgecolor=border_c, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=6.8, fontweight='bold', color=text_c)

    # Tree Nodes
    draw_node(0.04, 0.38, 0.22, 0.24, "Passenger Input:\nMoney Debited,\nNo Ticket Generated")
    draw_node(0.32, 0.65, 0.28, 0.24, "Secret Pattern Detection:\nPAN / CVV / PIN / OTP?\n-> HTTP 400 Bad Request", "#FEF2F2", HEX_RED, HEX_RED)
    draw_node(0.32, 0.12, 0.28, 0.24, "Valid Reference Provided:\nMask Ref (UPI****098)\nEvaluate Payment Mode", HEX_LIGHT_BLUE, HEX_STEEL)
    draw_node(0.68, 0.38, 0.28, 0.28, "Advisory Action Checklist:\n1. RBI TAT Framework\n   (UPI: T+1, Cards: T+5)\n2. Prevent Duplicate Debits\n3. Escalate if TAT Exceeded", "#F0FDF4", HEX_GREEN, HEX_GREEN)

    # Connections
    ax.annotate("Regex Match", xy=(0.32, 0.77), xytext=(0.26, 0.55),
                arrowprops=dict(arrowstyle="->", color=HEX_RED, lw=1.2), fontsize=6.5, color=HEX_RED)
    ax.annotate("Sanitized", xy=(0.32, 0.25), xytext=(0.26, 0.45),
                arrowprops=dict(arrowstyle="->", color=HEX_STEEL, lw=1.2), fontsize=6.5, color=HEX_STEEL)
    ax.annotate("Generate Advice", xy=(0.68, 0.50), xytext=(0.60, 0.25),
                arrowprops=dict(arrowstyle="->", color=HEX_GREEN, lw=1.2), fontsize=6.5, color=HEX_GREEN)

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "diagram_payment_workflow.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_case_lifecycle():
    """Diagram 5: Support Case & Audit Lifecycle"""
    fig, ax = plt.subplots(figsize=(7.5, 2.3), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)
    ax.axis('off')

    stages = [
        ("STAGE 1: CREATION", "Passenger Submits Issue\nMandatory Category & Desc\nGenerates RS-XXXXXX ID\nStatus: OPEN", HEX_LIGHT_BLUE, HEX_NAVY),
        ("STAGE 2: TRIAGE", "Admin Investigates Case\nReviews Issue Context\nStatus: IN_PROGRESS\nMandatory Staff Note", HEX_LIGHT_BLUE, HEX_STEEL),
        ("STAGE 3: RESOLUTION", "Advisory Resolution or\nOfficial Channel Referral\nStatus: RESOLVED\nFinal Note Recorded", "#F0FDF4", HEX_GREEN),
        ("AUDIT & TIMELINE", "Atomic Dual Persistence:\n1. case_events (User View)\n2. audit_logs (Security View)\nImmutable DB Records", HEX_BG, HEX_NAVY)
    ]

    for i, (title, desc, bg_c, border_c) in enumerate(stages):
        x = 0.03 + i * 0.245
        rect = patches.FancyBboxPatch((x, 0.10), 0.22, 0.78, boxstyle="round,pad=0.02,rounding_size=0.04",
                                      facecolor=bg_c, edgecolor=border_c, linewidth=1.2)
        ax.add_patch(rect)
        ax.text(x + 0.11, 0.72, title, ha='center', va='center', fontsize=7.2, fontweight='bold', color=border_c)
        ax.text(x + 0.11, 0.38, desc, ha='center', va='center', fontsize=6.2, color=HEX_DARK)

        if i < 3:
            ax.annotate("", xy=(x + 0.245, 0.50), xytext=(x + 0.22, 0.50),
                        arrowprops=dict(arrowstyle="->", color=HEX_CYAN, lw=1.5))

    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 1.0)
    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, "diagram_case_lifecycle.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def generate_diagram_roadmap():
    """Diagram 6: Implementation Roadmap Gantt / Flow"""
    fig, ax = plt.subplots(figsize=(7.5, 2.7), dpi=300)
    fig.patch.set_facecolor(HEX_WHITE)
    ax.set_facecolor(HEX_WHITE)

    stages = [
        "Stage 7: Scale / Transfer Decision",
        "Stage 6: Bounded Passenger Pilot",
        "Stage 5: Multi-User Sandbox Testing",
        "Stage 4: Staging API Access MoU",
        "Stage 3: Security & DPDP VAPT Audit",
        "Stage 2: Regulatory Rule Validation",
        "Stage 1: Codebase & Tech Review"
    ]
    starts = [10, 7, 5, 3, 2, 1, 0]
    durations = [2, 3, 2, 2, 1, 1, 1]
    colors_r = [HEX_NAVY, HEX_STEEL, HEX_CYAN, HEX_AMBER, "#2563EB", HEX_STEEL, HEX_NAVY]

    y_pos = np.arange(len(stages))
    ax.barh(y_pos, durations, left=starts, height=0.45, color=colors_r, edgecolor=HEX_BORDER, linewidth=1)

    for i in range(len(stages)):
        ax.text(starts[i] + durations[i] + 0.2, y_pos[i], f"Month {starts[i]+1}-{starts[i]+durations[i]}",
                va='center', fontsize=7.2, fontweight='bold', color=HEX_NAVY)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(stages, fontsize=7.5, fontweight='bold', color=HEX_DARK)
    ax.set_xlabel("Indicative Phased Timeline (Months from Formal Institutional Authorization)", fontsize=7.5, fontweight='bold', color=HEX_NAVY)
    ax.set_xlim(0, 14)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(HEX_BORDER)
    ax.spines['bottom'].set_color(HEX_BORDER)
    ax.xaxis.grid(True, linestyle='--', alpha=0.5, color=HEX_BORDER)
    ax.set_axisbelow(True)
    ax.tick_params(colors=HEX_DARK, labelsize=7.2)

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "diagram_roadmap.png")
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated: {out_path}")


def main():
    print("Regenerating Refined Proposal Assets...")
    generate_chart_a_readiness()
    generate_chart_b_testing()
    generate_chart_c_kpis()
    generate_chart_d_costs()
    generate_chart_e_risk_matrix()
    generate_diagram_system_architecture()
    generate_diagram_data_flow()
    generate_diagram_ecosystem_boundary()
    generate_diagram_payment_workflow()
    generate_diagram_case_lifecycle()
    generate_diagram_roadmap()
    print("All Refined Proposal Assets Generated Successfully!")


if __name__ == "__main__":
    main()
