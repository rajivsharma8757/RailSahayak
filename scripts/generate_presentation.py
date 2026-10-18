"""
RailSahayak Executive Stakeholder Presentation Generator
Page-by-page replication of the 11-page 'Blue and White Modern Business Proposal Presentation.pdf'

Deliverables:
- docs/RailSahayak_Stakeholder_Presentation.pptx (11 slides, widescreen 16:9)
- docs/RailSahayak_Stakeholder_Presentation.pdf (11 pages, matching layout and styling)

Strict boundaries & Content Corrections:
- Product name: RailSahayak only
- Zero live PRS scraping or live external railway system connections claimed
- Design boundary: Payment credentials and cardholder data outside intended prototype workflow
- Realistic scope: Use cases describe intended scope; individual workflows require verification against implementation and test evidence
- Unmeasured benefits clearly labelled as intended potential benefits; no claimed workload reduction or measured outcomes
- Project materials and technical evidence can be prepared for review (no unverified GitHub URL or contact details)
- Preserves 100% of the visual design, palette, images, fonts, and layouts
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

# Output paths
BASE_DIR = r"C:\Railshahayak\railsahayak-backend-starter\railsahayak-backend-starter"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
ASSETS_DIR = os.path.join(DOCS_DIR, "presentation_assets")
PPTX_PATH = os.path.join(DOCS_DIR, "RailSahayak_Stakeholder_Presentation.pptx")
PDF_PATH = os.path.join(DOCS_DIR, "RailSahayak_Stakeholder_Presentation.pdf")

# Photographic and Graphic Assets
IMG_COVER_TRAIN = os.path.join(ASSETS_DIR, "railway_cover_train.jpg")
IMG_PLATFORM = os.path.join(ASSETS_DIR, "railway_platform_vertical.jpg")
IMG_PIDS = os.path.join(ASSETS_DIR, "railway_pids_display.jpg")
IMG_PANORAMA = os.path.join(ASSETS_DIR, "railway_infrastructure_panorama.jpg")
IMG_LOGO = os.path.join(ASSETS_DIR, "railsahayak_logo.png")

# Corporate Railway Color Palette
COLOR_NAVY = RGBColor(15, 44, 89)          # #0F2C59 - Primary deep navy
COLOR_BLUE = RGBColor(29, 99, 148)         # #1D6394 - Secondary railway blue
COLOR_ACCENT = RGBColor(43, 120, 173)      # #2B78AD - Active accent blue
COLOR_LIGHT_BG = RGBColor(235, 245, 250)   # #EBF5FA - Pale ice blue fill
COLOR_CARD_BG = RGBColor(244, 249, 252)    # #F4F9FC - Subtle card fill
COLOR_BORDER = RGBColor(200, 220, 232)     # #C8DCE8 - Clean card borders
COLOR_DARK_TEXT = RGBColor(30, 41, 59)     # #1E293B - Primary charcoal text
COLOR_MUTED_TEXT = RGBColor(82, 96, 113)   # #526071 - Secondary muted text
COLOR_WHITE = RGBColor(255, 255, 255)      # #FFFFFF - Pure white
COLOR_CONTAINER = RGBColor(221, 240, 245)  # #DDF0F5 - Prominent container fill

HEX_NAVY = '#0F2C59'
HEX_BLUE = '#1D6394'
HEX_ACCENT = '#2B78AD'
HEX_LIGHT_BG = '#EBF5FA'
HEX_CARD_BG = '#F4F9FC'
HEX_BORDER = '#C8DCE8'
HEX_DARK_TEXT = '#1E293B'
HEX_MUTED_TEXT = '#526071'
HEX_WHITE = '#FFFFFF'
HEX_CONTAINER = '#DDF0F5'

TOTAL_SLIDES = 11


# =============================================================================
# PPTX BUILDER HELPERS
# =============================================================================

def add_bg(slide, color=COLOR_WHITE):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_header(slide, breadcrumb, pill_text, slide_num):
    if os.path.exists(IMG_LOGO):
        slide.shapes.add_picture(IMG_LOGO, Inches(0.80), Inches(0.35), Inches(0.40), Inches(0.40))
    
    tb_brand = slide.shapes.add_textbox(Inches(1.28), Inches(0.36), Inches(6.0), Inches(0.38))
    tf = tb_brand.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"RailSahayak  |  {breadcrumb}"
    p.font.name = "Arial"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE

    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.80), Inches(0.34), Inches(2.733), Inches(0.38))
    pill.fill.solid()
    pill.fill.fore_color.rgb = COLOR_LIGHT_BG
    pill.line.color.rgb = COLOR_BORDER
    pill.line.width = Pt(1)
    tf_pill = pill.text_frame
    p_pill = tf_pill.paragraphs[0]
    p_pill.text = pill_text.upper()
    p_pill.font.name = "Arial"
    p_pill.font.size = Pt(8.5)
    p_pill.font.bold = True
    p_pill.font.color.rgb = COLOR_NAVY
    p_pill.alignment = PP_ALIGN.CENTER

def add_footer(slide, slide_num):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.80), Inches(7.05), Inches(11.733), Pt(1))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.fill.background()

    tb_left = slide.shapes.add_textbox(Inches(0.80), Inches(7.10), Inches(7.5), Inches(0.30))
    p_l = tb_left.text_frame.paragraphs[0]
    p_l.text = "INDEPENDENT TECHNICAL PROPOSAL | NOT AN OFFICIAL IRCTC/CRIS/INDIAN RAILWAYS RELEASE"
    p_l.font.name = "Arial"
    p_l.font.size = Pt(8)
    p_l.font.color.rgb = COLOR_MUTED_TEXT

    tb_right = slide.shapes.add_textbox(Inches(9.533), Inches(7.10), Inches(3.0), Inches(0.30))
    p_r = tb_right.text_frame.paragraphs[0]
    p_r.text = f"Page {slide_num} of {TOTAL_SLIDES}"
    p_r.font.name = "Arial"
    p_r.font.size = Pt(8.5)
    p_r.font.bold = True
    p_r.font.color.rgb = COLOR_NAVY
    p_r.alignment = PP_ALIGN.RIGHT

def add_card(slide, left, top, width, height, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape


# =============================================================================
# BUILD PPTX PRESENTATION (11 SLIDES)
# =============================================================================

def build_pptx():
    print(f"Building PowerPoint presentation: {PPTX_PATH}...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------------------
    # SLIDE 1: COVER
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, RGBColor(248, 250, 252))

    if os.path.exists(IMG_LOGO):
        s1.shapes.add_picture(IMG_LOGO, Inches(0.80), Inches(0.60), Inches(0.55), Inches(0.55))
    tb_b = s1.shapes.add_textbox(Inches(1.45), Inches(0.65), Inches(4.5), Inches(0.40))
    p = tb_b.text_frame.paragraphs[0]
    p.text = "RailSahayak | Independent Technical Exploration"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY

    pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.80), Inches(1.35), Inches(4.6), Inches(0.38))
    pill1.fill.solid()
    pill1.fill.fore_color.rgb = COLOR_LIGHT_BG
    pill1.line.color.rgb = COLOR_BORDER
    p1 = pill1.text_frame.paragraphs[0]
    p1.text = "INDEPENDENT TECHNICAL PROPOSAL | OCTOBER 2026"
    p1.font.name = "Arial"
    p1.font.size = Pt(9)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_NAVY

    tb_title = s1.shapes.add_textbox(Inches(0.80), Inches(1.85), Inches(5.60), Inches(0.95))
    p_title = tb_title.text_frame.paragraphs[0]
    p_title.text = "RailSahayak"
    p_title.font.name = "Arial"
    p_title.font.size = Pt(46)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY

    tb_sec = s1.shapes.add_textbox(Inches(0.80), Inches(2.80), Inches(5.60), Inches(0.65))
    tf_sec = tb_sec.text_frame
    tf_sec.word_wrap = True
    p_sec = tf_sec.paragraphs[0]
    p_sec.text = "PASSENGER ASSISTANCE & RAILWAY SERVICE SUPPORT PROPOSAL"
    p_sec.font.name = "Arial"
    p_sec.font.size = Pt(14)
    p_sec.font.bold = True
    p_sec.font.color.rgb = COLOR_BLUE

    tb_sub = s1.shapes.add_textbox(Inches(0.80), Inches(3.45), Inches(5.60), Inches(0.65))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "An Independent Prototype for Clearer Passenger Guidance and Structured Service Support"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(12)
    p_sub.font.color.rgb = COLOR_DARK_TEXT

    div1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.80), Inches(4.15), Inches(5.60), Pt(2))
    div1.fill.solid()
    div1.fill.fore_color.rgb = COLOR_ACCENT
    div1.line.fill.background()

    tb_desc = s1.shapes.add_textbox(Inches(0.80), Inches(4.30), Inches(5.60), Inches(1.00))
    tf_desc = tb_desc.text_frame
    tf_desc.word_wrap = True
    p_desc = tf_desc.paragraphs[0]
    p_desc.text = "A technology concept designed to help passengers understand next steps for selected railway journey, payment, reservation-guidance, and complaint-tracking scenarios."
    p_desc.font.name = "Arial"
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = COLOR_MUTED_TEXT

    bound_box = add_card(s1, 0.80, 5.45, 5.60, 1.25, bg_color=COLOR_CONTAINER, border_color=COLOR_BORDER)
    tf_bb = bound_box.text_frame
    tf_bb.word_wrap = True
    p_bb0 = tf_bb.paragraphs[0]
    p_bb0.text = "INDEPENDENT TECHNICAL PROPOSAL"
    p_bb0.font.name = "Arial"
    p_bb0.font.size = Pt(9)
    p_bb0.font.bold = True
    p_bb0.font.color.rgb = COLOR_NAVY
    p_bb1 = tf_bb.add_paragraph()
    p_bb1.text = "Demonstrates local advisory capabilities only. Does not connect to live Indian Railways, IRCTC, or CRIS production systems. No transactional authority claimed."
    p_bb1.font.name = "Arial"
    p_bb1.font.size = Pt(8.5)
    p_bb1.font.color.rgb = COLOR_DARK_TEXT

    hero_card = add_card(s1, 6.70, 0.80, 5.833, 5.90, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
    if os.path.exists(IMG_COVER_TRAIN):
        s1.shapes.add_picture(IMG_COVER_TRAIN, Inches(6.90), Inches(1.00), Inches(5.433), Inches(5.10))
    
    tb_c = s1.shapes.add_textbox(Inches(6.90), Inches(6.15), Inches(5.433), Inches(0.40))
    p_c = tb_c.text_frame.paragraphs[0]
    p_c.text = "Modern Indian Passenger Train  |  Concept for Clearer Journey Guidance"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(8.5)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_NAVY
    p_c.alignment = PP_ALIGN.CENTER

    tb_f1 = s1.shapes.add_textbox(Inches(0.80), Inches(7.10), Inches(11.733), Inches(0.30))
    p_f1 = tb_f1.text_frame.paragraphs[0]
    p_f1.text = "Independent technical exploration prototype  |  October 2026  |  Repository: github.com/rajivsharma8757/RailSahayak"
    p_f1.font.name = "Arial"
    p_f1.font.size = Pt(8)
    p_f1.font.color.rgb = COLOR_MUTED_TEXT

    # -------------------------------------------------------------------------
    # SLIDE 2: PASSENGER NEEDS & OPPORTUNITY
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Context & Journey Touchpoints", "Opportunity Framework", 2)
    add_footer(s2, 2)

    tb_s2_h = s2.shapes.add_textbox(Inches(0.80), Inches(0.95), Inches(5.80), Inches(0.45))
    p_s2_h = tb_s2_h.text_frame.paragraphs[0]
    p_s2_h.text = "PASSENGER NEEDS & OPPORTUNITY"
    p_s2_h.font.name = "Arial"
    p_s2_h.font.size = Pt(22)
    p_s2_h.font.bold = True
    p_s2_h.font.color.rgb = COLOR_NAVY

    tb_s2_p = s2.shapes.add_textbox(Inches(0.80), Inches(1.40), Inches(5.80), Inches(0.60))
    tf_s2_p = tb_s2_p.text_frame
    tf_s2_p.word_wrap = True
    p_s2_p = tf_s2_p.paragraphs[0]
    p_s2_p.text = "Railway journeys involve multiple decisions before travel, during booking, and when unexpected issues occur. RailSahayak explores whether clearer, structured guidance can help passengers identify appropriate next steps."
    p_s2_p.font.name = "Arial"
    p_s2_p.font.size = Pt(10)
    p_s2_p.font.color.rgb = COLOR_DARK_TEXT

    needs = [
        ("01", "BEFORE TRAVEL", "Route and Reservation Guidance",
         "Passengers may need help understanding station codes, route options, quota terminology, reservation status, and official information sources."),
        ("02", "WHEN A PAYMENT FAILS", "Understand the Next Step",
         "A payment debit without a generated ticket can leave a passenger uncertain about transaction status, refund procedures, and whether to contact the bank or booking platform."),
        ("03", "RESERVATION & JOURNEY STATUS", "Understand the Applicable Rules",
         "Passengers may need clear explanations of waitlist status, charting, ticket category, and the limits of the information shown by an independent advisory tool."),
        ("04", "AFTER AN INCIDENT", "Find the Appropriate Support Channel",
         "Passengers may need assistance identifying the relevant official channel for a commercial, payment, operational, or safety-related concern.")
    ]

    card_y = 2.05
    for num, cat, title, desc in needs:
        card = add_card(s2, 0.80, card_y, 5.80, 0.85, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
        tf_c = card.text_frame
        tf_c.word_wrap = True
        p0 = tf_c.paragraphs[0]
        p0.text = f"{num}  {cat} — {title}"
        p0.font.name = "Arial"
        p0.font.size = Pt(9.5)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_c.add_paragraph()
        p1.text = desc
        p1.font.name = "Arial"
        p1.font.size = Pt(8.5)
        p1.font.color.rgb = COLOR_DARK_TEXT
        card_y += 0.95

    opp_box = add_card(s2, 0.80, 5.95, 5.80, 0.65, bg_color=COLOR_CONTAINER, border_color=COLOR_BORDER)
    tf_opp = opp_box.text_frame
    tf_opp.word_wrap = True
    p_opp = tf_opp.paragraphs[0]
    p_opp.text = "Opportunity: Make procedural guidance easier to understand without replacing official railway systems."
    p_opp.font.name = "Arial"
    p_opp.font.size = Pt(9.5)
    p_opp.font.bold = True
    p_opp.font.color.rgb = COLOR_NAVY
    p_opp.alignment = PP_ALIGN.CENTER

    right_card = add_card(s2, 6.90, 0.95, 5.633, 5.75, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER)
    if os.path.exists(IMG_PLATFORM):
        s2.shapes.add_picture(IMG_PLATFORM, Inches(7.10), Inches(1.15), Inches(5.233), Inches(5.00))
    tb_rc = s2.shapes.add_textbox(Inches(7.10), Inches(6.25), Inches(5.233), Inches(0.35))
    p_rc = tb_rc.text_frame.paragraphs[0]
    p_rc.text = "Indian Railways Platform  |  Point of passenger journey coordination"
    p_rc.font.name = "Arial"
    p_rc.font.size = Pt(8.5)
    p_rc.font.bold = True
    p_rc.font.color.rgb = COLOR_NAVY
    p_rc.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 3: PROBLEM STATEMENT (Corrected PASSENGER SUPPORT REALITY)
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Problem Context & Analysis", "Challenge Analysis", 3)
    add_footer(s3, 3)

    tb_s3_h = s3.shapes.add_textbox(Inches(0.80), Inches(1.05), Inches(5.40), Inches(0.50))
    p_s3_h = tb_s3_h.text_frame.paragraphs[0]
    p_s3_h.text = "THE PROBLEM STATEMENT"
    p_s3_h.font.name = "Arial"
    p_s3_h.font.size = Pt(24)
    p_s3_h.font.bold = True
    p_s3_h.font.color.rgb = COLOR_NAVY

    tb_s3_p = s3.shapes.add_textbox(Inches(0.80), Inches(1.65), Inches(5.40), Inches(1.20))
    tf_s3_p = tb_s3_p.text_frame
    tf_s3_p.word_wrap = True
    p_s3_p = tf_s3_p.paragraphs[0]
    p_s3_p.text = "Passengers can face uncertainty when the next step depends on the type of ticket, transaction state, railway rule, or responsible service channel. The proposed focus of RailSahayak is to organize these questions into clearer guidance and structured next steps."
    p_s3_p.font.name = "Arial"
    p_s3_p.font.size = Pt(11.5)
    p_s3_p.font.color.rgb = COLOR_DARK_TEXT

    # Qualified, evidence-based text without unsupported behavioral assertions
    box_s3 = add_card(s3, 0.80, 3.05, 5.40, 2.20, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
    tf_bs3 = box_s3.text_frame
    tf_bs3.word_wrap = True
    p_bs3_0 = tf_bs3.paragraphs[0]
    p_bs3_0.text = "PASSENGER SUPPORT REALITY"
    p_bs3_0.font.name = "Arial"
    p_bs3_0.font.size = Pt(10)
    p_bs3_0.font.bold = True
    p_bs3_0.font.color.rgb = COLOR_NAVY
    p_bs3_1 = tf_bs3.add_paragraph()
    p_bs3_1.text = "Payment issues, reservation questions, and operational disruptions can leave passengers uncertain about the appropriate next step. The frequency and impact of these situations should be established through reliable evidence or a future authorized evaluation."
    p_bs3_1.font.name = "Arial"
    p_bs3_1.font.size = Pt(9.5)
    p_bs3_1.font.color.rgb = COLOR_DARK_TEXT

    tb_s3_lim = s3.shapes.add_textbox(Inches(0.80), Inches(5.45), Inches(5.40), Inches(1.00))
    tf_s3_lim = tb_s3_lim.text_frame
    tf_s3_lim.word_wrap = True
    p_s3_lim = tf_s3_lim.paragraphs[0]
    p_s3_lim.text = "Boundary Note: This analysis is based on the proposed workflows and interface design; passenger impact remains to be validated. No claims are made regarding institutional workload reduction without authorized field data."
    p_s3_lim.font.name = "Arial"
    p_s3_lim.font.size = Pt(8.5)
    p_s3_lim.font.color.rgb = COLOR_MUTED_TEXT

    problems = [
        ("01", "TRANSACTION UNCERTAINTY", "Payment Debits & Settlement Lags",
         "A payment debit without ticket generation can create uncertainty about transaction reconciliation, refund procedures, and the appropriate support channel."),
        ("02", "RULE COMPLEXITY", "Reservation Categories & Charting",
         "Reservation status and ticket category can affect what a passenger should do next. Explanations must be accurate, current, and tied to the relevant rules."),
        ("03", "SUPPORT-CHANNEL CONFUSION", "Multi-Agency Support Boundaries",
         "Commercial, payment, operational, and safety issues may require different official channels. Clear routing guidance can help passengers understand where to seek authoritative assistance.")
    ]

    p_y = 1.05
    for num, title, subtitle, desc in problems:
        p_card = add_card(s3, 6.50, p_y, 6.00, 1.70, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER)
        
        circ = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.70), Inches(p_y + 0.20), Inches(0.40), Inches(0.40))
        circ.fill.solid()
        circ.fill.fore_color.rgb = COLOR_NAVY
        circ.line.fill.background()
        p_circ = circ.text_frame.paragraphs[0]
        p_circ.text = num
        p_circ.font.name = "Arial"
        p_circ.font.size = Pt(10)
        p_circ.font.bold = True
        p_circ.font.color.rgb = COLOR_WHITE
        p_circ.alignment = PP_ALIGN.CENTER

        tb_ct = s3.shapes.add_textbox(Inches(7.25), Inches(p_y + 0.12), Inches(5.10), Inches(1.45))
        tf_ct = tb_ct.text_frame
        tf_ct.word_wrap = True
        p0 = tf_ct.paragraphs[0]
        p0.text = title
        p0.font.name = "Arial"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_ct.add_paragraph()
        p1.text = subtitle
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_BLUE
        p2 = tf_ct.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(9)
        p2.font.color.rgb = COLOR_DARK_TEXT

        p_y += 1.85

    # -------------------------------------------------------------------------
    # SLIDE 4: OUR SOLUTION (Corrected Design Boundaries)
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "System Concept & Architecture", "Solution Architecture", 4)
    add_footer(s4, 4)

    sol_panel = add_card(s4, 0.80, 1.00, 11.733, 5.75, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)

    tb_s4_h = s4.shapes.add_textbox(Inches(1.20), Inches(1.30), Inches(5.00), Inches(0.50))
    p_s4_h = tb_s4_h.text_frame.paragraphs[0]
    p_s4_h.text = "OUR SOLUTION"
    p_s4_h.font.name = "Arial"
    p_s4_h.font.size = Pt(26)
    p_s4_h.font.bold = True
    p_s4_h.font.color.rgb = COLOR_NAVY

    tb_s4_p = s4.shapes.add_textbox(Inches(1.20), Inches(1.90), Inches(5.00), Inches(1.50))
    tf_s4_p = tb_s4_p.text_frame
    tf_s4_p.word_wrap = True
    p_s4_p = tf_s4_p.paragraphs[0]
    p_s4_p.text = "RailSahayak is an independent advisory prototype that brings selected passenger-support workflows into one interface. It aims to explain possible next steps and point users toward official channels when authoritative action or confirmation is required."
    p_s4_p.font.name = "Arial"
    p_s4_p.font.size = Pt(11)
    p_s4_p.font.color.rgb = COLOR_DARK_TEXT

    # Accurately framed design boundaries based on code verification
    bound_s4 = add_card(s4, 1.20, 3.60, 5.00, 2.60, bg_color=COLOR_WHITE, border_color=COLOR_BORDER)
    tf_bs4 = bound_s4.text_frame
    tf_bs4.word_wrap = True
    p_b4_0 = tf_bs4.paragraphs[0]
    p_b4_0.text = "IMPORTANT SYSTEM BOUNDARY"
    p_b4_0.font.name = "Arial"
    p_b4_0.font.size = Pt(10)
    p_b4_0.font.bold = True
    p_b4_0.font.color.rgb = COLOR_NAVY
    p_b4_1 = tf_bs4.add_paragraph()
    p_b4_1.text = "RailSahayak does not replace official booking systems. Live railway data and institutional integrations must not be represented as available unless verified and authorized."
    p_b4_1.font.name = "Arial"
    p_b4_1.font.size = Pt(9.5)
    p_b4_1.font.color.rgb = COLOR_DARK_TEXT
    p_b4_2 = tf_bs4.add_paragraph()
    p_b4_2.text = "• No live PRS integration is claimed.\n• Payment credentials and cardholder data are outside the intended prototype workflow; implementation should be verified.\n• Clear disclaimers directing passengers to official railway channels"
    p_b4_2.font.name = "Arial"
    p_b4_2.font.size = Pt(8.5)
    p_b4_2.font.color.rgb = COLOR_MUTED_TEXT

    v_line = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.85), Inches(1.50), Pt(2), Inches(4.50))
    v_line.fill.solid()
    v_line.fill.fore_color.rgb = COLOR_ACCENT
    v_line.line.fill.background()

    steps = [
        ("01", "CLARIFY", "Plain-Language Guidance",
         "Explain selected reservation, payment-help, and complaint procedures in clear language based on the functionality actually implemented."),
        ("02", "ORGANIZE", "Structured Issue Capture",
         "Help organize relevant incident details and complaint information without requesting unnecessary payment secrets or sensitive credentials."),
        ("03", "DIRECT", "Appropriate Next Steps",
         "Guide the passenger toward the relevant official service or support channel when an issue requires authoritative information or action.")
    ]

    step_y = 1.35
    for num, tag, title, desc in steps:
        circle = s4.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.65), Inches(step_y + 0.10), Inches(0.42), Inches(0.42))
        circle.fill.solid()
        circle.fill.fore_color.rgb = COLOR_NAVY
        circle.line.fill.background()
        tf_circ = circle.text_frame
        p_c = tf_circ.paragraphs[0]
        p_c.text = num
        p_c.font.name = "Arial"
        p_c.font.size = Pt(9.5)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_WHITE
        p_c.alignment = PP_ALIGN.CENTER

        step_card = add_card(s4, 7.25, step_y, 4.90, 1.45, bg_color=COLOR_WHITE, border_color=COLOR_BORDER)
        tf_sc = step_card.text_frame
        tf_sc.word_wrap = True
        p0 = tf_sc.paragraphs[0]
        p0.text = f"Step {num}  |  {tag} — {title}"
        p0.font.name = "Arial"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_sc.add_paragraph()
        p1.text = desc
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = COLOR_DARK_TEXT

        step_y += 1.65

    # -------------------------------------------------------------------------
    # SLIDE 5: VALUE PROPOSITION
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Proposed Impact & Principles", "Value Proposition", 5)
    add_footer(s5, 5)

    tb_s5_h = s5.shapes.add_textbox(Inches(0.80), Inches(0.95), Inches(11.733), Inches(0.50))
    p_s5_h = tb_s5_h.text_frame.paragraphs[0]
    p_s5_h.text = "THE VALUE PROPOSITION"
    p_s5_h.font.name = "Arial"
    p_s5_h.font.size = Pt(26)
    p_s5_h.font.bold = True
    p_s5_h.font.color.rgb = COLOR_NAVY
    p_s5_h.alignment = PP_ALIGN.CENTER

    tb_s5_sub = s5.shapes.add_textbox(Inches(0.80), Inches(1.45), Inches(11.733), Inches(0.40))
    p_s5_sub = tb_s5_sub.text_frame.paragraphs[0]
    p_s5_sub.text = "Four core principles shaping clearer guidance and disciplined institutional alignment."
    p_s5_sub.font.name = "Arial"
    p_s5_sub.font.size = Pt(11.5)
    p_s5_sub.font.color.rgb = COLOR_MUTED_TEXT
    p_s5_sub.alignment = PP_ALIGN.CENTER

    h_line = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.20), Inches(2.25), Inches(10.933), Pt(2))
    h_line.fill.solid()
    h_line.fill.fore_color.rgb = COLOR_ACCENT
    h_line.line.fill.background()

    values = [
        ("01", "CLARITY",
         "Organize complex procedural information into short, understandable guidance for everyday passengers."),
        ("02", "STRUCTURE",
         "Capture selected issue details in a consistent format to make the next step easier to understand."),
        ("03", "TRACEABILITY",
         "Where implemented, show complaint identifiers and recorded status changes to help users follow a case within the prototype."),
        ("04", "COMPLEMENTARY DESIGN",
         "Keep official booking, payment, and railway operations under their respective authorized systems.")
    ]

    col_x = 0.80
    col_w = 2.75
    col_gap = 0.24
    for num, title, desc in values:
        marker = s5.shapes.add_shape(MSO_SHAPE.OVAL, Inches(col_x + (col_w - 0.50)/2), Inches(2.00), Inches(0.50), Inches(0.50))
        marker.fill.solid()
        marker.fill.fore_color.rgb = COLOR_NAVY
        marker.line.fill.background()
        tf_m = marker.text_frame
        p_m = tf_m.paragraphs[0]
        p_m.text = num
        p_m.font.name = "Arial"
        p_m.font.size = Pt(10)
        p_m.font.bold = True
        p_m.font.color.rgb = COLOR_WHITE
        p_m.alignment = PP_ALIGN.CENTER

        v_card = add_card(s5, col_x, 2.70, col_w, 2.65, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
        tf_vc = v_card.text_frame
        tf_vc.word_wrap = True
        p0 = tf_vc.paragraphs[0]
        p0.text = title
        p0.font.name = "Arial"
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p0.alignment = PP_ALIGN.CENTER
        p1 = tf_vc.add_paragraph()
        p1.text = desc
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p1.alignment = PP_ALIGN.CENTER

        col_x += col_w + col_gap

    val_banner = add_card(s5, 0.80, 5.60, 11.733, 1.05, bg_color=COLOR_CONTAINER, border_color=COLOR_BORDER)
    tf_vb = val_banner.text_frame
    tf_vb.word_wrap = True
    p_vb0 = tf_vb.paragraphs[0]
    p_vb0.text = "CORE ARCHITECTURAL POSITION"
    p_vb0.font.name = "Arial"
    p_vb0.font.size = Pt(9.5)
    p_vb0.font.bold = True
    p_vb0.font.color.rgb = COLOR_NAVY
    p_vb0.alignment = PP_ALIGN.CENTER
    p_vb1 = tf_vb.add_paragraph()
    p_vb1.text = "The proposed value is clearer guidance and better-organized next steps — not a replacement for official railway services."
    p_vb1.font.name = "Arial"
    p_vb1.font.size = Pt(12)
    p_vb1.font.bold = True
    p_vb1.font.color.rgb = COLOR_NAVY
    p_vb1.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 6: TARGET AUDIENCE & USE CASES (Corrected Verification Wording)
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "User Touchpoints & Scenarios", "Use Cases", 6)
    add_footer(s6, 6)

    tb_s6_h = s6.shapes.add_textbox(Inches(0.80), Inches(1.05), Inches(4.60), Inches(0.90))
    tf_s6_h = tb_s6_h.text_frame
    tf_s6_h.word_wrap = True
    p_s6_h0 = tf_s6_h.paragraphs[0]
    p_s6_h0.text = "TARGET AUDIENCE &"
    p_s6_h0.font.name = "Arial"
    p_s6_h0.font.size = Pt(22)
    p_s6_h0.font.bold = True
    p_s6_h0.font.color.rgb = COLOR_NAVY
    p_s6_h1 = tf_s6_h.add_paragraph()
    p_s6_h1.text = "USE CASES"
    p_s6_h1.font.name = "Arial"
    p_s6_h1.font.size = Pt(22)
    p_s6_h1.font.bold = True
    p_s6_h1.font.color.rgb = COLOR_NAVY

    tb_s6_p = s6.shapes.add_textbox(Inches(0.80), Inches(2.05), Inches(4.60), Inches(1.10))
    tf_s6_p = tb_s6_p.text_frame
    tf_s6_p.word_wrap = True
    p_s6_p = tf_s6_p.paragraphs[0]
    p_s6_p.text = "The initial prototype is intended to explore passenger-facing guidance scenarios. Its usefulness and suitability for different groups must be assessed through stakeholder review and user evaluation."
    p_s6_p.font.name = "Arial"
    p_s6_p.font.size = Pt(10.5)
    p_s6_p.font.color.rgb = COLOR_DARK_TEXT

    # Precise scope wording replacing sweeping local testing claims
    box_s6_eval = add_card(s6, 0.80, 3.35, 4.60, 2.50, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
    tf_b6 = box_s6_eval.text_frame
    tf_b6.word_wrap = True
    p_b6_0 = tf_b6.paragraphs[0]
    p_b6_0.text = "EVALUATION SCOPE & SAFEGUARDS"
    p_b6_0.font.name = "Arial"
    p_b6_0.font.size = Pt(10)
    p_b6_0.font.bold = True
    p_b6_0.font.color.rgb = COLOR_NAVY
    p_b6_1 = tf_b6.add_paragraph()
    p_b6_1.text = "The use cases describe the intended scope of the prototype. Individual workflows require verification against the available implementation and test evidence. Claims of usefulness are presented as hypotheses to be evaluated in authorized technical discussions, not as pre-validated user demand."
    p_b6_1.font.name = "Arial"
    p_b6_1.font.size = Pt(9)
    p_b6_1.font.color.rgb = COLOR_DARK_TEXT
    p_b6_2 = tf_b6.add_paragraph()
    p_b6_2.text = "• No simulated booking confirmation\n• No fake live tracking data shown\n• Direct referral to official IRCTC / NTES portals"
    p_b6_2.font.name = "Arial"
    p_b6_2.font.size = Pt(8.5)
    p_b6_2.font.color.rgb = COLOR_MUTED_TEXT

    use_cases = [
        ("01", "PASSENGERS PLANNING A JOURNEY",
         "Potential use: understanding station codes, route guidance, reservation terminology, and where to find authoritative travel information."),
        ("02", "PASSENGERS WITH PAYMENT QUESTIONS",
         "Potential use: understanding what information to preserve and which official service to contact after a payment issue."),
        ("03", "RESERVATION & WAITLIST GUIDANCE",
         "Potential use: understanding the meaning and limitations of reservation and waitlist information."),
        ("04", "PASSENGERS TRACKING A COMPLAINT",
         "Potential use: recording an issue and following the status available within the RailSahayak prototype.")
    ]

    grid_w = 3.25
    grid_h = 2.65
    coords = [
        (5.70, 1.05),
        (9.25, 1.05),
        (5.70, 3.95),
        (9.25, 3.95)
    ]

    for (num, title, desc), (gx, gy) in zip(use_cases, coords):
        uc_card = add_card(s6, gx, gy, grid_w, grid_h, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER)
        tf_uc = uc_card.text_frame
        tf_uc.word_wrap = True
        p0 = tf_uc.paragraphs[0]
        p0.text = f"Case {num}  |  {title}"
        p0.font.name = "Arial"
        p0.font.size = Pt(11)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_uc.add_paragraph()
        p1.text = desc
        p1.font.name = "Arial"
        p1.font.size = Pt(9.5)
        p1.font.color.rgb = COLOR_DARK_TEXT

    # -------------------------------------------------------------------------
    # SLIDE 7: RAILSAHAYAK IN THE RAILWAY ECOSYSTEM (Unmeasured Benefits Qualified)
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Ecosystem Alignment & Positioning", "Ecosystem Architecture", 7)
    add_footer(s7, 7)

    t1 = add_card(s7, 0.80, 1.05, 5.40, 1.65, bg_color=COLOR_NAVY, border_color=None)
    tf_t1 = t1.text_frame
    tf_t1.word_wrap = True
    pt1_0 = tf_t1.paragraphs[0]
    pt1_0.text = "OFFICIAL RAILWAY & PAYMENT INFRASTRUCTURE"
    pt1_0.font.name = "Arial"
    pt1_0.font.size = Pt(10.5)
    pt1_0.font.bold = True
    pt1_0.font.color.rgb = COLOR_WHITE
    pt1_1 = tf_t1.add_paragraph()
    pt1_1.text = "IRCTC (Ticketing) | CRIS (PRS / NTES) | RailMadad | Bank Gateways"
    pt1_1.font.name = "Arial"
    pt1_1.font.size = Pt(9)
    pt1_1.font.bold = True
    pt1_1.font.color.rgb = RGBColor(185, 217, 235)
    pt1_2 = tf_t1.add_paragraph()
    pt1_2.text = "Authoritative sources for financial transactions, live train operations, seat inventory, refunds, and formal grievance resolution."
    pt1_2.font.name = "Arial"
    pt1_2.font.size = Pt(8.5)
    pt1_2.font.color.rgb = COLOR_WHITE

    c1 = s7.shapes.add_textbox(Inches(0.80), Inches(2.72), Inches(5.40), Inches(0.30))
    pc1 = c1.text_frame.paragraphs[0]
    pc1.text = "▲ Directs passengers to authoritative channels  |  Zero system override ▼"
    pc1.font.name = "Arial"
    pc1.font.size = Pt(8.5)
    pc1.font.bold = True
    pc1.font.color.rgb = COLOR_BLUE
    pc1.alignment = PP_ALIGN.CENTER

    t2 = add_card(s7, 0.80, 3.05, 5.40, 1.70, bg_color=COLOR_BLUE, border_color=None)
    tf_t2 = t2.text_frame
    tf_t2.word_wrap = True
    pt2_0 = tf_t2.paragraphs[0]
    pt2_0.text = "INDEPENDENT ADVISORY LAYER (RAILSAHAYAK)"
    pt2_0.font.name = "Arial"
    pt2_0.font.size = Pt(10.5)
    pt2_0.font.bold = True
    pt2_0.font.color.rgb = COLOR_WHITE
    pt2_1 = tf_t2.add_paragraph()
    pt2_1.text = "Procedural Guidance | Intake Structuring | Rule Explanations | Triage"
    pt2_1.font.name = "Arial"
    pt2_1.font.size = Pt(9)
    pt2_1.font.bold = True
    pt2_1.font.color.rgb = RGBColor(221, 240, 245)
    pt2_2 = tf_t2.add_paragraph()
    pt2_2.text = "• No live PRS integration claimed · No payment secrets in prototype scope\n• Explains procedural options & directs users to official portals\n• Local prototype demonstrating structured assistance"
    pt2_2.font.name = "Arial"
    pt2_2.font.size = Pt(8.5)
    pt2_2.font.color.rgb = COLOR_WHITE

    c2 = s7.shapes.add_textbox(Inches(0.80), Inches(4.77), Inches(5.40), Inches(0.30))
    pc2 = c2.text_frame.paragraphs[0]
    pc2.text = "▼ Intended to explore clearer procedural guidance (Unmeasured) ▼"
    pc2.font.name = "Arial"
    pc2.font.size = Pt(8.5)
    pc2.font.bold = True
    pc2.font.color.rgb = COLOR_BLUE
    pc2.alignment = PP_ALIGN.CENTER

    # Clearly labelled as intended, unmeasured potential value
    t3 = add_card(s7, 0.80, 5.10, 5.40, 1.55, bg_color=COLOR_CONTAINER, border_color=COLOR_BORDER)
    tf_t3 = t3.text_frame
    tf_t3.word_wrap = True
    pt3_0 = tf_t3.paragraphs[0]
    pt3_0.text = "POTENTIAL PASSENGER VALUE (INTENDED / UNMEASURED)"
    pt3_0.font.name = "Arial"
    pt3_0.font.size = Pt(10)
    pt3_0.font.bold = True
    pt3_0.font.color.rgb = COLOR_NAVY
    pt3_1 = tf_t3.add_paragraph()
    pt3_1.text = "Explores whether structured guidance can help passengers navigate next steps during failed transactions or procedural questions before contacting official desks. Quantitative passenger benefits remain to be established through authorized evaluation."
    pt3_1.font.name = "Arial"
    pt3_1.font.size = Pt(8.5)
    pt3_1.font.color.rgb = COLOR_DARK_TEXT

    tb_s7_h = s7.shapes.add_textbox(Inches(6.50), Inches(1.05), Inches(6.00), Inches(0.50))
    p_s7_h = tb_s7_h.text_frame.paragraphs[0]
    p_s7_h.text = "RAILSAHAYAK IN THE ECOSYSTEM"
    p_s7_h.font.name = "Arial"
    p_s7_h.font.size = Pt(22)
    p_s7_h.font.bold = True
    p_s7_h.font.color.rgb = COLOR_NAVY

    tb_s7_p = s7.shapes.add_textbox(Inches(6.50), Inches(1.60), Inches(6.00), Inches(0.95))
    tf_s7_p = tb_s7_p.text_frame
    tf_s7_p.word_wrap = True
    p_s7_p = tf_s7_p.paragraphs[0]
    p_s7_p.text = "RailSahayak is intended as a complementary, independent guidance layer. Official railway and payment systems remain the authoritative sources for transactions, operational status, refunds, and formal grievance resolution."
    p_s7_p.font.name = "Arial"
    p_s7_p.font.size = Pt(10.5)
    p_s7_p.font.color.rgb = COLOR_DARK_TEXT

    comparisons = [
        ("01", "OFFICIAL BOOKING SYSTEMS",
         "Official: Handles authorized booking & transaction execution.",
         "RailSahayak Role: Explains selected procedures and guides users toward the relevant official process."),
        ("02", "OFFICIAL TRAIN INFORMATION",
         "Official: Authoritative for live train running status & operational updates.",
         "RailSahayak Role: Explains where and how to check information without falsely claiming live access."),
        ("03", "OFFICIAL GRIEVANCE CHANNELS",
         "Official: Responsible for established formal investigation & dispute resolution.",
         "RailSahayak Role: Organizes selected issue details and explains the next appropriate channel.")
    ]

    comp_y = 2.65
    for num, title, off_role, rs_role in comparisons:
        comp_card = add_card(s7, 6.50, comp_y, 6.00, 1.25, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
        tf_cc = comp_card.text_frame
        tf_cc.word_wrap = True
        p0 = tf_cc.paragraphs[0]
        p0.text = f"{num}  {title}"
        p0.font.name = "Arial"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_cc.add_paragraph()
        p1.text = off_role
        p1.font.name = "Arial"
        p1.font.size = Pt(8.5)
        p1.font.color.rgb = COLOR_DARK_TEXT
        p2 = tf_cc.add_paragraph()
        p2.text = rs_role
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_BLUE
        comp_y += 1.35

    # -------------------------------------------------------------------------
    # SLIDE 8: ENGAGEMENT & ADOPTION STRATEGY
    # -------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Institutional Alignment & Adoption", "Adoption Framework", 8)
    add_footer(s8, 8)

    tb_s8_h = s8.shapes.add_textbox(Inches(0.80), Inches(0.95), Inches(5.80), Inches(0.50))
    p_s8_h = tb_s8_h.text_frame.paragraphs[0]
    p_s8_h.text = "ENGAGEMENT & ADOPTION STRATEGY"
    p_s8_h.font.name = "Arial"
    p_s8_h.font.size = Pt(22)
    p_s8_h.font.bold = True
    p_s8_h.font.color.rgb = COLOR_NAVY

    tb_s8_p = s8.shapes.add_textbox(Inches(0.80), Inches(1.45), Inches(5.80), Inches(0.70))
    tf_s8_p = tb_s8_p.text_frame
    tf_s8_p.word_wrap = True
    p_s8_p = tf_s8_p.paragraphs[0]
    p_s8_p.text = "The first priority is to establish technical credibility, validate guidance, and understand institutional requirements. Any future deployment or public-facing distribution would depend on the appropriate approvals and a clear operational model."
    p_s8_p.font.name = "Arial"
    p_s8_p.font.size = Pt(10.5)
    p_s8_p.font.color.rgb = COLOR_DARK_TEXT

    stages_s8 = [
        ("01", "TECHNICAL REVIEW",
         "Share the prototype, explain its architecture, and invite feedback on implemented features, known limitations, and evidence."),
        ("02", "RULE VALIDATION",
         "Request guidance on validating the railway-related procedural content against current authoritative sources."),
        ("03", "CONTROLLED EVALUATION",
         "If stakeholders consider it appropriate, explore an authorized, limited evaluation with clearly defined scope and safeguards."),
        ("04", "FUTURE PATHWAY",
         "Consider further development, mentorship, academic collaboration, licensing, or handover only if there is mutual interest and an appropriate institutional process.")
    ]

    s8_y = 2.25
    for num, title, desc in stages_s8:
        card = add_card(s8, 0.80, s8_y, 5.80, 1.00, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
        tf_c = card.text_frame
        tf_c.word_wrap = True
        p0 = tf_c.paragraphs[0]
        p0.text = f"Stage {num}  |  {title}"
        p0.font.name = "Arial"
        p0.font.size = Pt(10.5)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_NAVY
        p1 = tf_c.add_paragraph()
        p1.text = desc
        p1.font.name = "Arial"
        p1.font.size = Pt(9)
        p1.font.color.rgb = COLOR_DARK_TEXT
        s8_y += 1.10

    tb_s8_note = s8.shapes.add_textbox(Inches(0.80), Inches(6.65), Inches(5.80), Inches(0.35))
    p_s8_n = tb_s8_note.text_frame.paragraphs[0]
    p_s8_n.text = "Stakeholder engagement roadmap — not a claim of existing formal partnership."
    p_s8_n.font.name = "Arial"
    p_s8_n.font.size = Pt(8.5)
    p_s8_n.font.italic = True
    p_s8_n.font.color.rgb = COLOR_MUTED_TEXT

    right_card8 = add_card(s8, 6.90, 0.95, 5.633, 5.75, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER)
    if os.path.exists(IMG_PIDS):
        s8.shapes.add_picture(IMG_PIDS, Inches(7.10), Inches(1.15), Inches(5.233), Inches(5.00))
    tb_rc8 = s8.shapes.add_textbox(Inches(7.10), Inches(6.25), Inches(5.233), Inches(0.35))
    p_rc8 = tb_rc8.text_frame.paragraphs[0]
    p_rc8.text = "Passenger Information Display (PIDS)  |  Station Operational Feed"
    p_rc8.font.name = "Arial"
    p_rc8.font.size = Pt(8.5)
    p_rc8.font.bold = True
    p_rc8.font.color.rgb = COLOR_NAVY
    p_rc8.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 9: IMPLEMENTATION & EVALUATION PLAN
    # -------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Phased Testing & Evaluation", "Proposed Framework", 9)
    add_footer(s9, 9)

    tb_s9_h = s9.shapes.add_textbox(Inches(0.80), Inches(0.95), Inches(11.733), Inches(0.45))
    p_s9_h = tb_s9_h.text_frame.paragraphs[0]
    p_s9_h.text = "IMPLEMENTATION & EVALUATION PLAN"
    p_s9_h.font.name = "Arial"
    p_s9_h.font.size = Pt(24)
    p_s9_h.font.bold = True
    p_s9_h.font.color.rgb = COLOR_NAVY
    p_s9_h.alignment = PP_ALIGN.CENTER

    tb_s9_p = s9.shapes.add_textbox(Inches(0.80), Inches(1.40), Inches(11.733), Inches(0.35))
    p_s9_p = tb_s9_p.text_frame.paragraphs[0]
    p_s9_p.text = "Any further evaluation should proceed through explicit review stages. The sequence below is a proposed framework, not an approved Indian Railways schedule."
    p_s9_p.font.name = "Arial"
    p_s9_p.font.size = Pt(10)
    p_s9_p.font.color.rgb = COLOR_MUTED_TEXT
    p_s9_p.alignment = PP_ALIGN.CENTER

    plan_stages = [
        ("01", "BASELINE REVIEW",
         "Review source code, architecture, capabilities, limitations, and existing prototype evidence."),
        ("02", "RULE & SECURITY",
         "Validate procedural guidance, access control, privacy, logging, and security requirements."),
        ("03", "AUTHORIZED TESTING",
         "If approved, test in an appropriate environment using authorized or simulated datasets."),
        ("04", "LIMITED EVALUATION",
         "If separately authorized, evaluate bounded use cases with defined safeguards and metrics."),
        ("05", "REVIEW & DECISION",
         "Use evaluation evidence to decide whether to improve, extend, transfer, or discontinue.")
    ]

    p_w = 2.15
    p_gap = 0.245
    p_x = 0.80
    for num, title, desc in plan_stages:
        card = add_card(s9, p_x, 1.85, p_w, 2.00, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
        tf_c = card.text_frame
        tf_c.word_wrap = True
        p0 = tf_c.paragraphs[0]
        p0.text = f"Stage {num}"
        p0.font.name = "Arial"
        p0.font.size = Pt(9)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_BLUE
        p1 = tf_c.add_paragraph()
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_NAVY
        p2 = tf_c.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = COLOR_DARK_TEXT
        p_x += p_w + p_gap

    pano_card = add_card(s9, 0.80, 4.05, 11.733, 2.80, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER)
    if os.path.exists(IMG_PANORAMA):
        s9.shapes.add_picture(IMG_PANORAMA, Inches(0.95), Inches(4.15), Inches(11.433), Inches(2.35))
    tb_pc = s9.shapes.add_textbox(Inches(0.95), Inches(6.55), Inches(11.433), Inches(0.25))
    p_pc = tb_pc.text_frame.paragraphs[0]
    p_pc.text = "Modern Indian Railway Track & Catenary Infrastructure  |  Proposed Phased Evaluation Framework"
    p_pc.font.name = "Arial"
    p_pc.font.size = Pt(8.5)
    p_pc.font.bold = True
    p_pc.font.color.rgb = COLOR_NAVY
    p_pc.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------------------
    # SLIDE 10: CONCLUSION & NEXT STEPS
    # -------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Summary & Request for Guidance", "Next Steps", 10)
    add_footer(s10, 10)

    tb_s10_h = s10.shapes.add_textbox(Inches(0.80), Inches(0.95), Inches(11.733), Inches(0.45))
    p_s10_h = tb_s10_h.text_frame.paragraphs[0]
    p_s10_h.text = "CONCLUSION & NEXT STEPS"
    p_s10_h.font.name = "Arial"
    p_s10_h.font.size = Pt(24)
    p_s10_h.font.bold = True
    p_s10_h.font.color.rgb = COLOR_NAVY

    main_c10 = add_card(s10, 0.80, 1.45, 11.733, 5.45, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)

    b1_s10 = add_card(s10, 1.10, 1.65, 11.133, 1.55, bg_color=COLOR_WHITE, border_color=COLOR_BORDER)
    tf_b1 = b1_s10.text_frame
    tf_b1.word_wrap = True
    pb1_0 = tf_b1.paragraphs[0]
    pb1_0.text = "THE PROPOSAL"
    pb1_0.font.name = "Arial"
    pb1_0.font.size = Pt(11)
    pb1_0.font.bold = True
    pb1_0.font.color.rgb = COLOR_NAVY
    pb1_1 = tf_b1.add_paragraph()
    pb1_1.text = "RailSahayak presents an independent software prototype exploring how selected railway passenger questions can be organized into clearer guidance, structured issue capture, and appropriate official-channel direction."
    pb1_1.font.name = "Arial"
    pb1_1.font.size = Pt(9.5)
    pb1_1.font.color.rgb = COLOR_DARK_TEXT
    pb1_2 = tf_b1.add_paragraph()
    pb1_2.text = "Its current value should be judged by the capabilities demonstrated in the actual prototype, the accuracy of its guidance, the quality of its implementation, and the transparency of its limitations."
    pb1_2.font.name = "Arial"
    pb1_2.font.size = Pt(9.5)
    pb1_2.font.color.rgb = COLOR_DARK_TEXT

    b2_s10 = add_card(s10, 1.10, 3.35, 11.133, 1.80, bg_color=COLOR_WHITE, border_color=COLOR_BORDER)
    tf_b2 = b2_s10.text_frame
    tf_b2.word_wrap = True
    pb2_0 = tf_b2.paragraphs[0]
    pb2_0.text = "THE REQUEST & COLLABORATION PATHWAY"
    pb2_0.font.name = "Arial"
    pb2_0.font.size = Pt(11)
    pb2_0.font.bold = True
    pb2_0.font.color.rgb = COLOR_NAVY
    pb2_1 = tf_b2.add_paragraph()
    pb2_1.text = "We respectfully invite relevant technical stakeholders to review the concept and provide guidance on procedural accuracy, security expectations, authorized testing requirements, and possible future development."
    pb2_1.font.name = "Arial"
    pb2_1.font.size = Pt(9.5)
    pb2_1.font.color.rgb = COLOR_DARK_TEXT
    pb2_2 = tf_b2.add_paragraph()
    pb2_2.text = "If an existing railway system should not be replaced or changed, RailSahayak could still be considered for complementary evaluation, subject to technical, legal, and institutional review. Technical mentorship, skill-development guidance, further development, or a possible handover arrangement may also be discussed if appropriate."
    pb2_2.font.name = "Arial"
    pb2_2.font.size = Pt(9.5)
    pb2_2.font.bold = True
    pb2_2.font.color.rgb = COLOR_BLUE

    b3_s10 = add_card(s10, 1.10, 5.30, 11.133, 1.35, bg_color=COLOR_NAVY, border_color=None)
    tf_b3 = b3_s10.text_frame
    tf_b3.word_wrap = True
    pb3_0 = tf_b3.paragraphs[0]
    pb3_0.text = "THREE CONCRETE NEXT STEPS"
    pb3_0.font.name = "Arial"
    pb3_0.font.size = Pt(10.5)
    pb3_0.font.bold = True
    pb3_0.font.color.rgb = RGBColor(185, 217, 235)
    pb3_1 = tf_b3.add_paragraph()
    pb3_1.text = "1. Review the current prototype and its evidence (Repository: github.com/rajivsharma8757/RailSahayak).\n2. Identify required corrections and institutional prerequisites.\n3. Decide whether any further evaluation is appropriate."
    pb3_1.font.name = "Arial"
    pb3_1.font.size = Pt(9.5)
    pb3_1.font.color.rgb = COLOR_WHITE

    # -------------------------------------------------------------------------
    # SLIDE 11: THANK YOU (Corrected Project Materials Wording)
    # -------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11, RGBColor(248, 250, 252))

    if os.path.exists(IMG_LOGO):
        s11.shapes.add_picture(IMG_LOGO, Inches(0.80), Inches(0.60), Inches(0.55), Inches(0.55))
    tb_b11 = s11.shapes.add_textbox(Inches(1.45), Inches(0.65), Inches(4.5), Inches(0.40))
    p11 = tb_b11.text_frame.paragraphs[0]
    p11.text = "RailSahayak | Independent Technical Exploration"
    p11.font.name = "Arial"
    p11.font.size = Pt(11)
    p11.font.bold = True
    p11.font.color.rgb = COLOR_NAVY

    tb_ty = s11.shapes.add_textbox(Inches(0.80), Inches(1.65), Inches(5.60), Inches(1.00))
    p_ty = tb_ty.text_frame.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.font.name = "Arial"
    p_ty.font.size = Pt(46)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_NAVY

    tb_rs = s11.shapes.add_textbox(Inches(0.80), Inches(2.65), Inches(5.60), Inches(0.50))
    p_rs = tb_rs.text_frame.paragraphs[0]
    p_rs.text = "RAILSAHAYAK"
    p_rs.font.name = "Arial"
    p_rs.font.size = Pt(20)
    p_rs.font.bold = True
    p_rs.font.color.rgb = COLOR_BLUE

    tb_rs_sub = s11.shapes.add_textbox(Inches(0.80), Inches(3.15), Inches(5.60), Inches(0.50))
    tf_sub11 = tb_rs_sub.text_frame
    tf_sub11.word_wrap = True
    p_rs_sub = tf_sub11.paragraphs[0]
    p_rs_sub.text = "Passenger Assistance & Railway Service Support Proposal"
    p_rs_sub.font.name = "Arial"
    p_rs_sub.font.size = Pt(13)
    p_rs_sub.font.color.rgb = COLOR_DARK_TEXT

    div11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.80), Inches(3.75), Inches(5.60), Pt(2))
    div11.fill.solid()
    div11.fill.fore_color.rgb = COLOR_ACCENT
    div11.line.fill.background()

    tb_c11 = s11.shapes.add_textbox(Inches(0.80), Inches(3.95), Inches(5.60), Inches(1.20))
    tf_c11 = tb_c11.text_frame
    tf_c11.word_wrap = True
    p_c11_0 = tf_c11.paragraphs[0]
    p_c11_0.text = "Request for Technical Review and Guidance"
    p_c11_0.font.name = "Arial"
    p_c11_0.font.size = Pt(13)
    p_c11_0.font.bold = True
    p_c11_0.font.color.rgb = COLOR_NAVY
    p_c11_1 = tf_c11.add_paragraph()
    p_c11_1.text = "An independent prototype presented for constructive feedback and possible future evaluation."
    p_c11_1.font.name = "Arial"
    p_c11_1.font.size = Pt(11)
    p_c11_1.font.color.rgb = COLOR_DARK_TEXT

    # Precise, verified wording for technical exploration session
    card_info = add_card(s11, 0.80, 5.35, 5.60, 1.35, bg_color=COLOR_CONTAINER, border_color=COLOR_BORDER)
    tf_ci = card_info.text_frame
    tf_ci.word_wrap = True
    p_ci0 = tf_ci.paragraphs[0]
    p_ci0.text = "STAKEHOLDER EXPLORATION SESSION"
    p_ci0.font.name = "Arial"
    p_ci0.font.size = Pt(9.5)
    p_ci0.font.bold = True
    p_ci0.font.color.rgb = COLOR_NAVY
    p_ci1 = tf_ci.add_paragraph()
    p_ci1.text = "Presented for technical evaluation and institutional guidance.\nPublic Repository: https://github.com/rajivsharma8757/RailSahayak\nOctober 2026"
    p_ci1.font.name = "Arial"
    p_ci1.font.size = Pt(8.5)
    p_ci1.font.color.rgb = COLOR_DARK_TEXT

    hero11 = add_card(s11, 6.70, 0.80, 5.833, 5.90, bg_color=COLOR_LIGHT_BG, border_color=COLOR_BORDER)
    if os.path.exists(IMG_COVER_TRAIN):
        s11.shapes.add_picture(IMG_COVER_TRAIN, Inches(6.90), Inches(1.00), Inches(5.433), Inches(5.10))
    tb_h11 = s11.shapes.add_textbox(Inches(6.90), Inches(6.15), Inches(5.433), Inches(0.40))
    p_h11 = tb_h11.text_frame.paragraphs[0]
    p_h11.text = "Dedicated to Passenger Assistance & Railway Service Support"
    p_h11.font.name = "Arial"
    p_h11.font.size = Pt(8.5)
    p_h11.font.bold = True
    p_h11.font.color.rgb = COLOR_NAVY
    p_h11.alignment = PP_ALIGN.CENTER

    tb_f11 = s11.shapes.add_textbox(Inches(0.80), Inches(7.10), Inches(11.733), Inches(0.30))
    p_f11 = tb_f11.text_frame.paragraphs[0]
    p_f11.text = "Independent Prototype  |  No Official Railway Endorsement Claimed"
    p_f11.font.name = "Arial"
    p_f11.font.size = Pt(8)
    p_f11.font.color.rgb = COLOR_MUTED_TEXT

    prs.save(PPTX_PATH)
    print(f"PPTX saved successfully ({len(prs.slides)} slides): {PPTX_PATH}")


# =============================================================================
# REPORTLAB PDF BUILDER (11 MATCHING PAGES)
# =============================================================================

def build_pdf():
    print(f"Building PDF presentation: {PDF_PATH}...")
    c = canvas.Canvas(PDF_PATH, pagesize=(960, 540))

    def rl_color(hex_str):
        return colors.HexColor(hex_str)

    def draw_bg(color_hex='#FFFFFF'):
        c.setFillColor(rl_color(color_hex))
        c.rect(0, 0, 960, 540, fill=1, stroke=0)

    def draw_header(breadcrumb, pill_text, slide_num):
        if os.path.exists(IMG_LOGO):
            c.drawImage(IMG_LOGO, 58, 540 - 25 - 28, width=28, height=28, mask='auto')
        
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(rl_color(HEX_BLUE))
        c.drawString(94, 540 - 25 - 18, f"RailSahayak  |  {breadcrumb}")

        pill_w = 196
        pill_h = 24
        pill_x = 960 - 58 - pill_w
        pill_y = 540 - 25 - 24
        c.setFillColor(rl_color(HEX_LIGHT_BG))
        c.setStrokeColor(rl_color(HEX_BORDER))
        c.roundRect(pill_x, pill_y, pill_w, pill_h, 6, fill=1, stroke=1)
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(rl_color(HEX_NAVY))
        c.drawCentredString(pill_x + pill_w/2, pill_y + 7, pill_text.upper())

    def draw_footer(slide_num):
        c.setStrokeColor(rl_color(HEX_BORDER))
        c.setLineWidth(1)
        c.line(58, 30, 960 - 58, 30)

        c.setFont("Helvetica", 8)
        c.setFillColor(rl_color(HEX_MUTED_TEXT))
        c.drawString(58, 16, "INDEPENDENT TECHNICAL PROPOSAL | NOT AN OFFICIAL IRCTC/CRIS/INDIAN RAILWAYS RELEASE")

        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(rl_color(HEX_NAVY))
        c.drawRightString(960 - 58, 16, f"Page {slide_num} of {TOTAL_SLIDES}")

    def draw_card_box(x, y, w, h, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=6):
        c.setFillColor(rl_color(bg_hex))
        if border_hex:
            c.setStrokeColor(rl_color(border_hex))
            c.setLineWidth(1)
            c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
        else:
            c.roundRect(x, y, w, h, radius, fill=1, stroke=0)

    def draw_para(text, x, y, width, height, font_size=10, bold=False, color_hex=HEX_DARK_TEXT, align='left'):
        style = ParagraphStyle(
            'DynamicStyle',
            fontName='Helvetica-Bold' if bold else 'Helvetica',
            fontSize=font_size,
            leading=font_size * 1.3,
            textColor=rl_color(color_hex),
            alignment=0 if align == 'left' else (1 if align == 'center' else 2)
        )
        p = Paragraph(text.replace('\n', '<br/>'), style)
        pw, ph = p.wrap(width, height)
        p.drawOn(c, x, y + height - ph)

    # -------------------------------------------------------------------------
    # PAGE 1: COVER
    # -------------------------------------------------------------------------
    draw_bg('#F8FAFC')

    if os.path.exists(IMG_LOGO):
        c.drawImage(IMG_LOGO, 58, 540 - 43 - 38, width=38, height=38, mask='auto')
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(104, 540 - 43 - 24, "RailSahayak | Independent Technical Exploration")

    draw_card_box(58, 540 - 124, 330, 26, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=5)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(70, 540 - 116, "INDEPENDENT TECHNICAL PROPOSAL | OCTOBER 2026")

    c.setFont("Helvetica-Bold", 44)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 180, "RailSahayak")

    draw_para("PASSENGER ASSISTANCE & RAILWAY SERVICE SUPPORT PROPOSAL", 58, 540 - 235, 400, 45, font_size=13.5, bold=True, color_hex=HEX_BLUE)
    draw_para("An Independent Prototype for Clearer Passenger Guidance and Structured Service Support", 58, 540 - 280, 400, 40, font_size=11.5, bold=False, color_hex=HEX_DARK_TEXT)

    c.setStrokeColor(rl_color(HEX_ACCENT))
    c.setLineWidth(2)
    c.line(58, 540 - 298, 458, 540 - 298)

    draw_para("A technology concept designed to help passengers understand next steps for selected railway journey, payment, reservation-guidance, and complaint-tracking scenarios.", 58, 540 - 375, 400, 70, font_size=10.5, color_hex=HEX_MUTED_TEXT)

    draw_card_box(58, 540 - 485, 400, 95, bg_hex=HEX_CONTAINER, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>INDEPENDENT TECHNICAL PROPOSAL</b><br/>Demonstrates local advisory capabilities only. Does not connect to live Indian Railways, IRCTC, or CRIS production systems. No transactional authority claimed.", 70, 540 - 475, 376, 75, font_size=9, color_hex=HEX_NAVY)

    draw_card_box(482, 540 - 58 - 425, 420, 425, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=8)
    if os.path.exists(IMG_COVER_TRAIN):
        c.drawImage(IMG_COVER_TRAIN, 496, 540 - 72 - 365, width=392, height=365, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(482 + 210, 540 - 58 - 412, "Modern Indian Passenger Train  |  Concept for Clearer Journey Guidance")

    c.setFont("Helvetica", 8)
    c.setFillColor(rl_color(HEX_MUTED_TEXT))
    c.drawString(58, 16, "Independent technical exploration prototype  |  October 2026  |  Repository: github.com/rajivsharma8757/RailSahayak")
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 2: PASSENGER NEEDS & OPPORTUNITY
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Context & Journey Touchpoints", "Opportunity Framework", 2)
    draw_footer(2)

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 68 - 24, "PASSENGER NEEDS & OPPORTUNITY")

    draw_para("Railway journeys involve multiple decisions before travel, during booking, and when unexpected issues occur. RailSahayak explores whether clearer, structured guidance can help passengers identify appropriate next steps.", 58, 540 - 140, 415, 42, font_size=9.5)

    needs = [
        ("01", "BEFORE TRAVEL", "Route and Reservation Guidance",
         "Passengers may need help understanding station codes, route options, quota terminology, reservation status, and official information sources."),
        ("02", "WHEN A PAYMENT FAILS", "Understand the Next Step",
         "A payment debit without a generated ticket can leave a passenger uncertain about transaction status, refund procedures, and whether to contact the bank or booking platform."),
        ("03", "RESERVATION & JOURNEY STATUS", "Understand the Applicable Rules",
         "Passengers may need clear explanations of waitlist status, charting, ticket category, and the limits of the information shown by an independent advisory tool."),
        ("04", "AFTER AN INCIDENT", "Find the Appropriate Support Channel",
         "Passengers may need assistance identifying the relevant official channel for a commercial, payment, operational, or safety-related concern.")
    ]

    card_y = 540 - 150 - 62
    for num, cat, title, desc in needs:
        draw_card_box(58, card_y, 415, 62, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=5)
        draw_para(f"<b>{num}  {cat} — {title}</b><br/>{desc}", 68, card_y + 5, 395, 52, font_size=8.5)
        card_y -= 68

    draw_card_box(58, 50, 415, 42, bg_hex=HEX_CONTAINER, border_hex=HEX_BORDER, radius=5)
    draw_para("<b>Opportunity:</b> Make procedural guidance easier to understand without replacing official railway systems.", 68, 56, 395, 30, font_size=9, color_hex=HEX_NAVY, align='center')

    draw_card_box(497, 540 - 68 - 428, 405, 428, bg_hex=HEX_CARD_BG, border_hex=HEX_BORDER, radius=8)
    if os.path.exists(IMG_PLATFORM):
        c.drawImage(IMG_PLATFORM, 511, 540 - 82 - 374, width=377, height=374, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(497 + 202, 540 - 68 - 415, "Indian Railways Platform  |  Point of passenger journey coordination")
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 3: PROBLEM STATEMENT (Evidence-based Cautious Wording)
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Problem Context & Analysis", "Challenge Analysis", 3)
    draw_footer(3)

    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 75 - 26, "THE PROBLEM STATEMENT")

    draw_para("Passengers can face uncertainty when the next step depends on the type of ticket, transaction state, railway rule, or responsible service channel. The proposed focus of RailSahayak is to organize these questions into clearer guidance and structured next steps.", 58, 540 - 200, 390, 85, font_size=11)

    draw_card_box(58, 540 - 365, 390, 155, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>PASSENGER SUPPORT REALITY</b><br/><br/>Payment issues, reservation questions, and operational disruptions can leave passengers uncertain about the appropriate next step. The frequency and impact of these situations should be established through reliable evidence or a future authorized evaluation.", 70, 540 - 355, 366, 135, font_size=9.5)

    draw_para("<i>Boundary Note: This analysis is based on the proposed workflows and interface design; passenger impact remains to be validated. No claims are made regarding institutional workload reduction without authorized field data.</i>", 58, 540 - 455, 390, 75, font_size=8.5, color_hex=HEX_MUTED_TEXT)

    problems = [
        ("01", "TRANSACTION UNCERTAINTY", "Payment Debits & Settlement Lags",
         "A payment debit without ticket generation can create uncertainty about transaction reconciliation, refund procedures, and the appropriate support channel."),
        ("02", "RULE COMPLEXITY", "Reservation Categories & Charting",
         "Reservation status and ticket category can affect what a passenger should do next. Explanations must be accurate, current, and tied to the relevant rules."),
        ("03", "SUPPORT-CHANNEL CONFUSION", "Multi-Agency Support Boundaries",
         "Commercial, payment, operational, and safety issues may require different official channels. Clear routing guidance can help passengers understand where to seek authoritative assistance.")
    ]

    py = 540 - 75 - 122
    for num, title, subtitle, desc in problems:
        draw_card_box(468, py, 434, 122, bg_hex=HEX_CARD_BG, border_hex=HEX_BORDER, radius=6)
        
        c.setFillColor(rl_color(HEX_NAVY))
        c.circle(490, py + 92, 14, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(rl_color(HEX_WHITE))
        c.drawCentredString(490, py + 89, num)

        draw_para(f"<b>{title}</b><br/><font color='{HEX_BLUE}'><b>{subtitle}</b></font><br/>{desc}", 512, py + 8, 376, 106, font_size=9)
        py -= 133
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 4: OUR SOLUTION (Design Boundaries Clarified)
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("System Concept & Architecture", "Solution Architecture", 4)
    draw_footer(4)

    draw_card_box(58, 540 - 72 - 418, 844, 418, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=8)

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(86, 540 - 95 - 28, "OUR SOLUTION")

    draw_para("RailSahayak is an independent advisory prototype that brings selected passenger-support workflows into one interface. It aims to explain possible next steps and point users toward official channels when authoritative action or confirmation is required.", 86, 540 - 245, 360, 110, font_size=11)

    draw_card_box(86, 540 - 450, 360, 185, bg_hex=HEX_WHITE, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>IMPORTANT SYSTEM BOUNDARY</b><br/><br/>RailSahayak does not replace official booking systems. Live railway data and institutional integrations must not be represented as available unless verified and authorized.<br/><br/>• No live PRS integration is claimed.<br/>• Payment credentials and cardholder data are outside the intended prototype workflow; implementation should be verified.<br/>• Clear disclaimers directing passengers to official railway channels", 98, 540 - 440, 336, 165, font_size=8.5)

    c.setStrokeColor(rl_color(HEX_ACCENT))
    c.setLineWidth(2)
    c.line(490, 540 - 110, 490, 540 - 435)

    steps = [
        ("01", "CLARIFY", "Plain-Language Guidance",
         "Explain selected reservation, payment-help, and complaint procedures in clear language based on the functionality actually implemented."),
        ("02", "ORGANIZE", "Structured Issue Capture",
         "Help organize relevant incident details and complaint information without requesting unnecessary payment secrets or sensitive credentials."),
        ("03", "DIRECT", "Appropriate Next Steps",
         "Guide the passenger toward the relevant official service or support channel when an issue requires authoritative information or action.")
    ]

    sy = 540 - 100 - 104
    for num, tag, title, desc in steps:
        c.setFillColor(rl_color(HEX_NAVY))
        c.circle(490, sy + 52, 15, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(rl_color(HEX_WHITE))
        c.drawCentredString(490, sy + 49, num)

        draw_card_box(520, sy, 355, 104, bg_hex=HEX_WHITE, border_hex=HEX_BORDER, radius=6)
        draw_para(f"<b>Step {num}  |  {tag} — {title}</b><br/><br/>{desc}", 532, sy + 8, 331, 88, font_size=9.5)
        sy -= 118
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 5: VALUE PROPOSITION
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Proposed Impact & Principles", "Value Proposition", 5)
    draw_footer(5)

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(480, 540 - 68 - 28, "THE VALUE PROPOSITION")

    c.setFont("Helvetica", 11)
    c.setFillColor(rl_color(HEX_MUTED_TEXT))
    c.drawCentredString(480, 540 - 105 - 14, "Four core principles shaping clearer guidance and disciplined institutional alignment.")

    c.setStrokeColor(rl_color(HEX_ACCENT))
    c.setLineWidth(2)
    c.line(86, 540 - 162, 874, 540 - 162)

    values = [
        ("01", "CLARITY",
         "Organize complex procedural information into short, understandable guidance for everyday passengers."),
        ("02", "STRUCTURE",
         "Capture selected issue details in a consistent format to make the next step easier to understand."),
        ("03", "TRACEABILITY",
         "Where implemented, show complaint identifiers and recorded status changes to help users follow a case within the prototype."),
        ("04", "COMPLEMENTARY DESIGN",
         "Keep official booking, payment, and railway operations under their respective authorized systems.")
    ]

    vx = 58
    vw = 198
    vgap = 17
    for num, title, desc in values:
        c.setFillColor(rl_color(HEX_NAVY))
        c.circle(vx + vw/2, 540 - 162, 17, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(rl_color(HEX_WHITE))
        c.drawCentredString(vx + vw/2, 540 - 165, num)

        draw_card_box(vx, 540 - 195 - 190, vw, 190, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=6)
        draw_para(f"<b>{title}</b><br/><br/>{desc}", vx + 10, 540 - 195 - 180, vw - 20, 170, font_size=9.5, align='center')
        vx += vw + vgap

    draw_card_box(58, 540 - 410 - 75, 844, 75, bg_hex=HEX_CONTAINER, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>CORE ARCHITECTURAL POSITION</b><br/><font size='11'><b>The proposed value is clearer guidance and better-organized next steps — not a replacement for official railway services.</b></font>", 70, 540 - 410 - 65, 820, 55, font_size=9.5, color_hex=HEX_NAVY, align='center')
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 6: TARGET AUDIENCE & USE CASES (Scope Accurately Qualified)
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("User Touchpoints & Scenarios", "Use Cases", 6)
    draw_footer(6)

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 70 - 22, "TARGET AUDIENCE &")
    c.drawString(58, 540 - 70 - 48, "USE CASES")

    draw_para("The initial prototype is intended to explore passenger-facing guidance scenarios. Its usefulness and suitability for different groups must be assessed through stakeholder review and user evaluation.", 58, 540 - 215, 330, 85, font_size=10.5)

    # Qualified scope wording replacing sweeping local testing claim
    draw_card_box(58, 540 - 415, 330, 185, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>EVALUATION SCOPE & SAFEGUARDS</b><br/><br/>The use cases describe the intended scope of the prototype. Individual workflows require verification against the available implementation and test evidence. Claims of usefulness are presented as hypotheses to be evaluated in authorized technical discussions, not as pre-validated user demand.<br/><br/>• No simulated booking confirmation<br/>• No fake live tracking data shown<br/>• Direct referral to official IRCTC / NTES portals", 70, 540 - 405, 306, 165, font_size=8.5)

    use_cases = [
        ("01", "PASSENGERS PLANNING A JOURNEY",
         "Potential use: understanding station codes, route guidance, reservation terminology, and where to find authoritative travel information."),
        ("02", "PASSENGERS WITH PAYMENT QUESTIONS",
         "Potential use: understanding what information to preserve and which official service to contact after a payment issue."),
        ("03", "RESERVATION & WAITLIST GUIDANCE",
         "Potential use: understanding the meaning and limitations of reservation and waitlist information."),
        ("04", "PASSENGERS TRACKING A COMPLAINT",
         "Potential use: recording an issue and following the status available within the RailSahayak prototype.")
    ]

    gw = 234
    gh = 190
    coords = [
        (410, 540 - 75 - 190),
        (668, 540 - 75 - 190),
        (410, 540 - 280 - 190),
        (668, 540 - 280 - 190)
    ]

    for (num, title, desc), (gx, gy) in zip(use_cases, coords):
        draw_card_box(gx, gy, gw, gh, bg_hex=HEX_CARD_BG, border_hex=HEX_BORDER, radius=6)
        draw_para(f"<b>Case {num}  |  {title}</b><br/><br/>{desc}", gx + 12, gy + 10, gw - 24, gh - 20, font_size=9.5)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 7: RAILSAHAYAK IN THE RAILWAY ECOSYSTEM (Unmeasured Benefits Qualified)
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Ecosystem Alignment & Positioning", "Ecosystem Architecture", 7)
    draw_footer(7)

    draw_card_box(58, 540 - 75 - 120, 390, 120, bg_hex=HEX_NAVY, border_hex=None, radius=6)
    draw_para("<b>OFFICIAL RAILWAY & PAYMENT INFRASTRUCTURE</b><br/><font color='#B9D9EB'><b>IRCTC Ticketing | CRIS PRS & NTES | RailMadad | Bank Gateways</b></font><br/>Authoritative sources for financial transactions, live train operations, seat inventory, refunds, and formal grievance resolution.", 70, 540 - 75 - 110, 366, 100, font_size=8.5, color_hex=HEX_WHITE)

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(rl_color(HEX_BLUE))
    c.drawCentredString(58 + 195, 540 - 205, "▲ Directs passengers to authoritative channels  |  Zero system override ▼")

    draw_card_box(58, 540 - 220 - 122, 390, 122, bg_hex=HEX_BLUE, border_hex=None, radius=6)
    draw_para("<b>INDEPENDENT ADVISORY LAYER (RAILSAHAYAK)</b><br/><font color='#DDF0F5'><b>Procedural Guidance | Intake Structuring | Rule Explanations | Triage</b></font><br/>• No live PRS integration claimed · No payment secrets in prototype scope<br/>• Explains procedural options & directs users to official portals<br/>• Local prototype demonstrating structured assistance", 70, 540 - 220 - 112, 366, 102, font_size=8.5, color_hex=HEX_WHITE)

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(rl_color(HEX_BLUE))
    c.drawCentredString(58 + 195, 540 - 355, "▼ Intended to explore clearer procedural guidance (Unmeasured) ▼")

    # Clearly labelled as intended, unmeasured potential value
    draw_card_box(58, 540 - 370 - 112, 390, 112, bg_hex=HEX_CONTAINER, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>POTENTIAL PASSENGER VALUE (INTENDED / UNMEASURED)</b><br/><br/>Explores whether structured guidance can help passengers navigate next steps during failed transactions or procedural questions before contacting official desks. Quantitative passenger benefits remain to be established through authorized evaluation.", 70, 540 - 370 - 102, 366, 92, font_size=8.5, color_hex=HEX_NAVY)

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(468, 540 - 75 - 26, "RAILSAHAYAK IN THE ECOSYSTEM")

    draw_para("RailSahayak is intended as a complementary, independent guidance layer. Official railway and payment systems remain the authoritative sources for transactions, operational status, refunds, and formal grievance resolution.", 468, 540 - 175, 434, 68, font_size=10.5)

    comparisons = [
        ("01", "OFFICIAL BOOKING SYSTEMS",
         "Official: Handles authorized booking & transaction execution.",
         "RailSahayak Role: Explains selected procedures and guides users toward the relevant official process."),
        ("02", "OFFICIAL TRAIN INFORMATION",
         "Official: Authoritative for live train running status & operational updates.",
         "RailSahayak Role: Explains where and how to check information without falsely claiming live access."),
        ("03", "OFFICIAL GRIEVANCE CHANNELS",
         "Official: Responsible for established formal investigation & dispute resolution.",
         "RailSahayak Role: Organizes selected issue details and explains the next appropriate channel.")
    ]

    cy = 540 - 190 - 90
    for num, title, off_role, rs_role in comparisons:
        draw_card_box(468, cy, 434, 90, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=5)
        draw_para(f"<b>{num}  {title}</b><br/>{off_role}<br/><font color='{HEX_BLUE}'><b>{rs_role}</b></font>", 480, cy + 6, 410, 78, font_size=8.5)
        cy -= 98
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 8: ENGAGEMENT & ADOPTION STRATEGY
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Institutional Alignment & Adoption", "Adoption Framework", 8)
    draw_footer(8)

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 68 - 24, "ENGAGEMENT & ADOPTION STRATEGY")

    draw_para("The first priority is to establish technical credibility, validate guidance, and understand institutional requirements. Any future deployment or public-facing distribution would depend on the appropriate approvals and a clear operational model.", 58, 540 - 145, 415, 45, font_size=10)

    stages_s8 = [
        ("01", "TECHNICAL REVIEW",
         "Share the prototype, explain its architecture, and invite feedback on implemented features, known limitations, and evidence."),
        ("02", "RULE VALIDATION",
         "Request guidance on validating the railway-related procedural content against current authoritative sources."),
        ("03", "CONTROLLED EVALUATION",
         "If stakeholders consider it appropriate, explore an authorized, limited evaluation with clearly defined scope and safeguards."),
        ("04", "FUTURE PATHWAY",
         "Consider further development, mentorship, academic collaboration, licensing, or handover only if there is mutual interest and an appropriate institutional process.")
    ]

    sy8 = 540 - 155 - 72
    for num, title, desc in stages_s8:
        draw_card_box(58, sy8, 415, 72, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=5)
        draw_para(f"<b>Stage {num}  |  {title}</b><br/>{desc}", 68, sy8 + 6, 395, 60, font_size=8.5)
        sy8 -= 78

    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColor(rl_color(HEX_MUTED_TEXT))
    c.drawString(58, 42, "Stakeholder engagement roadmap — not a claim of existing formal partnership.")

    draw_card_box(497, 540 - 68 - 428, 405, 428, bg_hex=HEX_CARD_BG, border_hex=HEX_BORDER, radius=8)
    if os.path.exists(IMG_PIDS):
        c.drawImage(IMG_PIDS, 511, 540 - 82 - 374, width=377, height=374, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(497 + 202, 540 - 68 - 415, "Passenger Information Display (PIDS)  |  Station Operational Feed")
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 9: IMPLEMENTATION & EVALUATION PLAN
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Phased Testing & Evaluation", "Proposed Framework", 9)
    draw_footer(9)

    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(480, 540 - 68 - 26, "IMPLEMENTATION & EVALUATION PLAN")

    c.setFont("Helvetica", 10.5)
    c.setFillColor(rl_color(HEX_MUTED_TEXT))
    c.drawCentredString(480, 540 - 102 - 14, "Any further evaluation should proceed through explicit review stages. The sequence below is a proposed framework, not an approved Indian Railways schedule.")

    plan_stages = [
        ("01", "BASELINE REVIEW",
         "Review source code, architecture, capabilities, limitations, and existing prototype evidence."),
        ("02", "RULE & SECURITY",
         "Validate procedural guidance, access control, privacy, logging, and security requirements."),
        ("03", "AUTHORIZED TESTING",
         "If approved, test in an appropriate environment using authorized or simulated datasets."),
        ("04", "LIMITED EVALUATION",
         "If separately authorized, evaluate bounded use cases with defined safeguards and metrics."),
        ("05", "REVIEW & DECISION",
         "Use evaluation evidence to decide whether to improve, extend, transfer, or discontinue.")
    ]

    pw = 154
    pgap = 18
    px = 58
    for num, title, desc in plan_stages:
        draw_card_box(px, 540 - 130 - 140, pw, 140, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=6)
        draw_para(f"<font color='{HEX_BLUE}'><b>Stage {num}</b></font><br/><b>{title}</b><br/><br/>{desc}", px + 10, 540 - 130 - 130, pw - 20, 120, font_size=8.5)
        px += pw + pgap

    draw_card_box(58, 540 - 285 - 210, 844, 210, bg_hex=HEX_CARD_BG, border_hex=HEX_BORDER, radius=8)
    if os.path.exists(IMG_PANORAMA):
        c.drawImage(IMG_PANORAMA, 70, 540 - 295 - 172, width=820, height=172, mask='auto')
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(480, 540 - 285 - 200, "Modern Indian Railway Track & Catenary Infrastructure  |  Proposed Phased Evaluation Framework")
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 10: CONCLUSION & NEXT STEPS
    # -------------------------------------------------------------------------
    draw_bg()
    draw_header("Summary & Request for Guidance", "Next Steps", 10)
    draw_footer(10)

    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 68 - 26, "CONCLUSION & NEXT STEPS")

    draw_card_box(58, 540 - 105 - 390, 844, 390, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=8)

    draw_card_box(80, 540 - 120 - 110, 800, 110, bg_hex=HEX_WHITE, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>THE PROPOSAL</b><br/><br/>RailSahayak presents an independent software prototype exploring how selected railway passenger questions can be organized into clearer guidance, structured issue capture, and appropriate official-channel direction.<br/><br/>Its current value should be judged by the capabilities demonstrated in the actual prototype, the accuracy of its guidance, the quality of its implementation, and the transparency of its limitations.", 94, 540 - 120 - 100, 772, 90, font_size=9)

    draw_card_box(80, 540 - 240 - 130, 800, 130, bg_hex=HEX_WHITE, border_hex=HEX_BORDER, radius=6)
    draw_para(f"<b>THE REQUEST & COLLABORATION PATHWAY</b><br/><br/>We respectfully invite relevant technical stakeholders to review the concept and provide guidance on procedural accuracy, security expectations, authorized testing requirements, and possible future development.<br/><br/><font color='{HEX_BLUE}'><b>If an existing railway system should not be replaced or changed, RailSahayak could still be considered for complementary evaluation, subject to technical, legal, and institutional review. Technical mentorship, skill-development guidance, further development, or a possible handover arrangement may also be discussed if appropriate.</b></font>", 94, 540 - 240 - 120, 772, 110, font_size=9)

    draw_card_box(80, 540 - 380 - 100, 800, 100, bg_hex=HEX_NAVY, border_hex=None, radius=6)
    draw_para("<font color='#B9D9EB'><b>THREE CONCRETE NEXT STEPS</b></font><br/><br/>1. Review the current prototype and its evidence (Repository: github.com/rajivsharma8757/RailSahayak).<br/>2. Identify required corrections and institutional prerequisites.<br/>3. Decide whether any further evaluation is appropriate.", 94, 540 - 380 - 90, 772, 80, font_size=9.5, color_hex=HEX_WHITE)
    c.showPage()

    # -------------------------------------------------------------------------
    # PAGE 11: THANK YOU (Prepared Materials Wording)
    # -------------------------------------------------------------------------
    draw_bg('#F8FAFC')

    if os.path.exists(IMG_LOGO):
        c.drawImage(IMG_LOGO, 58, 540 - 43 - 38, width=38, height=38, mask='auto')
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(104, 540 - 43 - 24, "RailSahayak | Independent Technical Exploration")

    c.setFont("Helvetica-Bold", 46)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawString(58, 540 - 180, "THANK YOU")

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(rl_color(HEX_BLUE))
    c.drawString(58, 540 - 225, "RAILSAHAYAK")

    c.setFont("Helvetica", 13)
    c.setFillColor(rl_color(HEX_DARK_TEXT))
    c.drawString(58, 540 - 252, "Passenger Assistance & Railway Service Support Proposal")

    c.setStrokeColor(rl_color(HEX_ACCENT))
    c.setLineWidth(2)
    c.line(58, 540 - 270, 458, 540 - 270)

    draw_para("<b>Request for Technical Review and Guidance</b><br/><br/>An independent prototype presented for constructive feedback and possible future evaluation.", 58, 540 - 355, 400, 75, font_size=11)

    # Accurate, verified wording with repository URL
    draw_card_box(58, 540 - 485, 400, 105, bg_hex=HEX_CONTAINER, border_hex=HEX_BORDER, radius=6)
    draw_para("<b>STAKEHOLDER EXPLORATION SESSION</b><br/><br/>Presented for technical evaluation and institutional guidance.<br/>Public Repository: <font color='#1D6394'><b>github.com/rajivsharma8757/RailSahayak</b></font><br/>October 2026", 70, 540 - 475, 376, 85, font_size=8.5, color_hex=HEX_NAVY)

    draw_card_box(482, 540 - 58 - 425, 420, 425, bg_hex=HEX_LIGHT_BG, border_hex=HEX_BORDER, radius=8)
    if os.path.exists(IMG_COVER_TRAIN):
        c.drawImage(IMG_COVER_TRAIN, 496, 540 - 72 - 365, width=392, height=365, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(rl_color(HEX_NAVY))
    c.drawCentredString(482 + 210, 540 - 58 - 412, "Dedicated to Passenger Assistance & Railway Service Support")

    c.setFont("Helvetica", 8)
    c.setFillColor(rl_color(HEX_MUTED_TEXT))
    c.drawString(58, 16, "Independent Prototype  |  No Official Railway Endorsement Claimed")
    c.showPage()

    c.save()
    print(f"PDF saved successfully (11 pages): {PDF_PATH}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    build_pptx()
    build_pdf()
    print("Presentation generation completed successfully!")
