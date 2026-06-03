# """
# BizDiag — Business Diagnostic Platform
# Streamlit Frontend v9.0
# تمرکز: عارضه‌یابی کسب‌وکار
# """

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import io, json, time

# # ─────────────────────────────────────────────
# # PAGE CONFIG
# # ─────────────────────────────────────────────
# st.set_page_config(
#     page_title="BizDiag — عارضه‌یابی کسب‌وکار",
#     page_icon="🔬",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# API_BASE    = "http://127.0.0.1:8000"
# API_ANALYZE = f"{API_BASE}/analyze"
# API_HEALTH  = f"{API_BASE}/health"
# API_CHAT    = f"{API_BASE}/chat"
# API_EXPORT  = f"{API_BASE}/export/excel"

# # ─────────────────────────────────────────────
# # THEME & CSS — Vazirmatn font + dark luxury
# # ─────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;900&display=swap');

# /* ── Global Reset ── */
# *, *::before, *::after { box-sizing: border-box; }
# html, body, [class*="css"], .stApp {
#     background-color: #060E1E !important;
#     color: #D4DFF5;
#     font-family: 'Vazirmatn', sans-serif !important;
#     direction: rtl;
# }
# .main { background-color: #060E1E !important; }
# .block-container {
#     padding-top: 1rem !important;
#     padding-bottom: 2rem !important;
#     max-width: 1400px !important;
# }

# /* ── Scrollbar ── */
# ::-webkit-scrollbar { width: 6px; height: 6px; }
# ::-webkit-scrollbar-track { background: #0C1628; }
# ::-webkit-scrollbar-thumb { background: #1E3A6E; border-radius: 3px; }
# ::-webkit-scrollbar-thumb:hover { background: #2563EB; }

# /* ── Sidebar ── */
# [data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #0A1628 0%, #060E1E 100%) !important;
#     border-left: 1px solid #1A2F55;
# }
# [data-testid="stSidebar"] * { font-family: 'Vazirmatn', sans-serif !important; }

# /* ── Header Hero ── */
# .bizdiag-hero {
#     background: linear-gradient(135deg, #0C1E3D 0%, #0A1628 50%, #060E1E 100%);
#     border: 1px solid #1A2F55;
#     border-radius: 20px;
#     padding: 2rem 2.5rem;
#     margin-bottom: 1.5rem;
#     position: relative;
#     overflow: hidden;
# }
# .bizdiag-hero::before {
#     content: '';
#     position: absolute;
#     top: -50%;
#     left: -50%;
#     width: 200%;
#     height: 200%;
#     background: radial-gradient(ellipse at 30% 50%, rgba(37,99,235,0.08) 0%, transparent 60%);
#     pointer-events: none;
# }
# .hero-title {
#     font-size: 2.2rem;
#     font-weight: 900;
#     background: linear-gradient(135deg, #60A5FA, #A78BFA, #34D399);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     margin: 0 0 0.3rem 0;
#     line-height: 1.2;
# }
# .hero-sub {
#     color: #4A6FA5;
#     font-size: 0.95rem;
#     margin: 0;
#     font-weight: 400;
# }

# /* ── Section Headers ── */
# .sec-header {
#     display: flex;
#     align-items: center;
#     gap: 0.7rem;
#     background: linear-gradient(90deg, rgba(37,99,235,0.15) 0%, transparent 100%);
#     border-right: 3px solid #2563EB;
#     border-radius: 0 10px 10px 0;
#     padding: 0.65rem 1.2rem 0.65rem 0.8rem;
#     margin: 2rem 0 1rem 0;
#     font-size: 1.05rem;
#     font-weight: 700;
#     color: #93C5FD;
# }
# .sec-icon { font-size: 1.2rem; }

# /* ── KPI Cards ── */
# div[data-testid="metric-container"] {
#     background: linear-gradient(135deg, #0D1F3C, #0A1628) !important;
#     border: 1px solid #1A2F55 !important;
#     padding: 1.2rem 1.4rem !important;
#     border-radius: 16px !important;
#     box-shadow: 0 4px 24px rgba(0,0,0,0.3);
#     transition: all 0.25s ease;
# }
# div[data-testid="metric-container"]:hover {
#     transform: translateY(-3px);
#     border-color: #2563EB !important;
#     box-shadow: 0 8px 32px rgba(37,99,235,0.15);
# }
# div[data-testid="metric-container"] label {
#     color: #6B8DC4 !important;
#     font-size: 0.8rem !important;
#     font-family: 'Vazirmatn', sans-serif !important;
#     font-weight: 500 !important;
# }
# div[data-testid="metric-container"] [data-testid="metric-value"] {
#     color: #E2EBFF !important;
#     font-size: 1.5rem !important;
#     font-weight: 700 !important;
#     font-family: 'Vazirmatn', sans-serif !important;
# }

# /* ── Health Score Bar ── */
# .health-bar {
#     background: linear-gradient(135deg, #0D1F3C, #0A1628);
#     border-radius: 18px;
#     padding: 1.4rem 2rem;
#     margin-bottom: 1.5rem;
#     display: flex;
#     align-items: center;
#     gap: 2rem;
# }
# .health-score {
#     font-size: 3rem;
#     font-weight: 900;
#     min-width: 80px;
#     text-align: center;
# }
# .health-label { font-size: 0.85rem; color: #4A6FA5; margin-top: 2px; }

# /* ── Issue Cards ── */
# .issue-card {
#     border-radius: 14px;
#     padding: 1.2rem 1.4rem;
#     margin: 0.6rem 0;
#     transition: transform 0.2s;
# }
# .issue-card:hover { transform: translateX(-4px); }
# .issue-critical {
#     background: linear-gradient(135deg, #1C0A0A, #160808);
#     border-right: 4px solid #EF4444;
#     border-top: 1px solid #3A1010;
# }
# .issue-warning {
#     background: linear-gradient(135deg, #1C1300, #160F00);
#     border-right: 4px solid #F59E0B;
#     border-top: 1px solid #3A2800;
# }
# .issue-healthy {
#     background: linear-gradient(135deg, #0A1C0C, #08160A);
#     border-right: 4px solid #22C55E;
#     border-top: 1px solid #103A15;
# }
# .issue-title { font-weight: 700; font-size: 1rem; margin-bottom: 0.3rem; }
# .issue-metric { font-size: 0.82rem; color: #8BA3C9; margin-bottom: 0.3rem; }
# .issue-impact { font-size: 0.85rem; color: #6B8DC4; line-height: 1.5; }
# .badge-sev {
#     display: inline-block;
#     padding: 0.2rem 0.6rem;
#     border-radius: 6px;
#     font-size: 0.72rem;
#     font-weight: 700;
#     margin-bottom: 0.5rem;
# }
# .sev-critical { background: #3A1010; color: #EF4444; }
# .sev-warning  { background: #3A2800; color: #F59E0B; }
# .sev-healthy  { background: #103A15; color: #22C55E; }

# /* ── AI Report Box ── */
# .ai-report {
#     background: linear-gradient(135deg, #0A1628, #060E1E);
#     border: 1px solid #1A2F55;
#     border-radius: 18px;
#     padding: 2rem 2.5rem;
#     line-height: 2;
#     white-space: pre-wrap;
#     font-size: 0.95rem;
#     color: #B8CCEE;
#     box-shadow: 0 0 60px rgba(37,99,235,0.1);
# }

# /* ── Insight Cards ── */
# .insight-card {
#     background: linear-gradient(135deg, #0D1F3C, #0A1628);
#     border: 1px solid #1A2F55;
#     border-radius: 12px;
#     padding: 1rem 1.2rem;
#     margin: 0.4rem 0;
#     font-size: 0.9rem;
#     line-height: 1.6;
#     transition: border-color 0.2s;
# }
# .insight-card:hover { border-color: #2563EB; }

# /* ── Recommendation Cards ── */
# .rec-term {
#     background: linear-gradient(135deg, #0D1F3C, #0A1628);
#     border-radius: 14px;
#     padding: 1rem 1.2rem;
#     margin-bottom: 0.8rem;
# }
# .rec-term-title {
#     font-weight: 700;
#     font-size: 0.85rem;
#     margin-bottom: 0.6rem;
#     text-transform: uppercase;
#     letter-spacing: 0.05em;
# }
# .rec-item {
#     padding: 0.5rem 0.8rem;
#     border-right: 3px solid;
#     margin: 0.3rem 0;
#     border-radius: 0 6px 6px 0;
#     font-size: 0.88rem;
#     line-height: 1.5;
# }
# .rec-short { border-color: #EF4444; background: rgba(239,68,68,0.06); }
# .rec-mid   { border-color: #F59E0B; background: rgba(245,158,11,0.06); }
# .rec-long  { border-color: #22C55E; background: rgba(34,197,94,0.06); }

# /* ── Chat Box ── */
# .chat-container {
#     background: linear-gradient(135deg, #0A1628, #060E1E);
#     border: 1px solid #1A2F55;
#     border-radius: 18px;
#     padding: 1.5rem;
#     min-height: 300px;
#     max-height: 500px;
#     overflow-y: auto;
# }
# .chat-user {
#     background: linear-gradient(135deg, #1A2F55, #162647);
#     border-radius: 14px 4px 14px 14px;
#     padding: 0.8rem 1.2rem;
#     margin: 0.5rem 0 0.5rem 2rem;
#     color: #E2EBFF;
#     font-size: 0.9rem;
# }
# .chat-ai {
#     background: linear-gradient(135deg, #0D1F3C, #0A1628);
#     border: 1px solid #1A2F55;
#     border-radius: 4px 14px 14px 14px;
#     padding: 0.8rem 1.2rem;
#     margin: 0.5rem 2rem 0.5rem 0;
#     color: #B8CCEE;
#     font-size: 0.9rem;
#     line-height: 1.7;
# }
# .chat-label {
#     font-size: 0.72rem;
#     color: #4A6FA5;
#     margin-bottom: 0.2rem;
#     font-weight: 600;
# }

# /* ── Final Verdict ── */
# .verdict-box {
#     border-radius: 18px;
#     padding: 1.5rem 2rem;
#     margin: 1rem 0;
#     text-align: center;
#     font-size: 1.05rem;
#     font-weight: 600;
#     line-height: 1.7;
# }
# .verdict-good    { background: linear-gradient(135deg,#0A1C0C,#08160A); border: 1px solid #22C55E; color: #4ADE80; }
# .verdict-medium  { background: linear-gradient(135deg,#1C1300,#160F00); border: 1px solid #F59E0B; color: #FCD34D; }
# .verdict-critical{ background: linear-gradient(135deg,#1C0A0A,#160808); border: 1px solid #EF4444; color: #FCA5A5; }

# /* ── Buttons ── */
# .stButton > button {
#     background: linear-gradient(135deg, #1D4ED8, #1E40AF) !important;
#     color: white !important;
#     border: none !important;
#     border-radius: 10px !important;
#     font-family: 'Vazirmatn', sans-serif !important;
#     font-weight: 600 !important;
#     padding: 0.5rem 1.5rem !important;
#     transition: all 0.2s !important;
# }
# .stButton > button:hover {
#     background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
#     transform: translateY(-1px) !important;
#     box-shadow: 0 4px 16px rgba(37,99,235,0.3) !important;
# }

# /* ── File Uploader ── */
# [data-testid="stFileUploadDropzone"] {
#     background: #0C1628 !important;
#     border: 2px dashed #1A2F55 !important;
#     border-radius: 16px !important;
#     transition: border-color 0.2s;
# }
# [data-testid="stFileUploadDropzone"]:hover { border-color: #2563EB !important; }

# /* ── DataFrames ── */
# .stDataFrame { border-radius: 12px !important; overflow: hidden !important; }

# /* ── Inputs ── */
# .stTextInput > div > div > input, .stTextArea textarea {
#     background: #0C1628 !important;
#     border: 1px solid #1A2F55 !important;
#     color: #D4DFF5 !important;
#     border-radius: 10px !important;
#     font-family: 'Vazirmatn', sans-serif !important;
# }

# /* ── Progress bar ── */
# .stProgress > div > div { border-radius: 8px; }

# /* ── Divider ── */
# hr { border-color: #1A2F55 !important; }

# /* ── Tabs ── */
# .stTabs [data-baseweb="tab-list"] {
#     background: #0A1628 !important;
#     border-radius: 12px !important;
#     padding: 4px !important;
#     gap: 4px !important;
# }
# .stTabs [data-baseweb="tab"] {
#     background: transparent !important;
#     color: #4A6FA5 !important;
#     border-radius: 8px !important;
#     font-family: 'Vazirmatn', sans-serif !important;
#     font-weight: 600 !important;
# }
# .stTabs [aria-selected="true"] {
#     background: #1A2F55 !important;
#     color: #93C5FD !important;
# }

# /* ── Selectbox ── */
# .stSelectbox > div > div {
#     background: #0C1628 !important;
#     border: 1px solid #1A2F55 !important;
#     color: #D4DFF5 !important;
#     border-radius: 10px !important;
# }

# /* ── Expandable ── */
# .streamlit-expanderHeader {
#     background: #0A1628 !important;
#     border-radius: 10px !important;
#     color: #93C5FD !important;
#     font-family: 'Vazirmatn', sans-serif !important;
# }

# /* ── Alerts ── */
# .stAlert { border-radius: 12px !important; }
# </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # CONSTANTS
# # ─────────────────────────────────────────────
# CHART_COLORS = ["#3B82F6","#10B981","#F59E0B","#EF4444",
#                 "#8B5CF6","#EC4899","#06B6D4","#84CC16","#F97316","#A78BFA"]

# PLOTLY = dict(
#     paper_bgcolor="rgba(0,0,0,0)",
#     plot_bgcolor="rgba(13,31,60,0.5)",
#     font=dict(color="#8BA3C9", family="Vazirmatn, sans-serif", size=12),
#     margin=dict(l=20, r=20, t=45, b=20),
#     legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#8BA3C9")),
#     xaxis=dict(gridcolor="#1A2F55", zerolinecolor="#1A2F55"),
#     yaxis=dict(gridcolor="#1A2F55", zerolinecolor="#1A2F55"),
# )

# # ─────────────────────────────────────────────
# # HELPERS
# # ─────────────────────────────────────────────
# def money(v):
#     try: return f"{float(v):,.0f}"
#     except: return "0"

# def pct(v):
#     try: return f"{float(v):.1f}%"
#     except: return "0%"

# def sv(d, key, default=0):
#     try: return d.get(key, default) if d else default
#     except: return default

# def sec(icon, title):
#     st.markdown(
#         f'<div class="sec-header"><span class="sec-icon">{icon}</span>{title}</div>',
#         unsafe_allow_html=True
#     )

# def issue_card(issue: dict):
#     sev = issue.get("severity","warning")
#     sev_map = {"critical":"🔴 بحرانی","warning":"🟡 هشدار","healthy":"🟢 سالم"}
#     sev_cls  = {"critical":"sev-critical","warning":"sev-warning","healthy":"sev-healthy"}
#     card_cls = {"critical":"issue-critical","warning":"issue-warning","healthy":"issue-healthy"}
#     st.markdown(f"""
# <div class="issue-card {card_cls.get(sev,'issue-warning')}">
#   <span class="badge-sev {sev_cls.get(sev,'sev-warning')}">{sev_map.get(sev,'هشدار')}</span>
#   <div class="issue-title">{issue.get('title','')}</div>
#   <div class="issue-metric">📊 {issue.get('metric','')}</div>
#   <div class="issue-impact">💡 {issue.get('impact','')}</div>
# </div>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # HEADER
# # ─────────────────────────────────────────────
# st.markdown("""
# <div class="bizdiag-hero">
#   <div class="hero-title">🔬 BizDiag — سامانه عارضه‌یابی کسب‌وکار</div>
#   <p class="hero-sub">
#     تحلیل هوشمند داده‌های فروش · شناسایی عارضه‌های کسب‌وکار · پشتیبانی از CSV، Excel، PDF، Word، TXT
#   </p>
# </div>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # BACKEND CHECK
# # ─────────────────────────────────────────────
# try:
#     h = requests.get(API_HEALTH, timeout=4)
#     hd = h.json()
#     ai_ok = hd.get("groq_enabled", False)
#     status_color = "#22C55E" if h.status_code == 200 else "#EF4444"
#     ai_color = "#22C55E" if ai_ok else "#F59E0B"
#     st.markdown(f"""
# <div style="display:flex;gap:1rem;align-items:center;padding:0.6rem 1rem;
#             background:#0A1628;border:1px solid #1A2F55;border-radius:12px;margin-bottom:1rem;">
#   <span style="color:{status_color};font-size:0.85rem;font-weight:600;">● بک‌اند متصل</span>
#   <span style="color:{ai_color};font-size:0.85rem;font-weight:600;">
#     {'✅ هوش مصنوعی فعال' if ai_ok else '⚠ کلید API تنظیم نشده — تحلیل آماری فعال است'}</span>
# </div>
# """, unsafe_allow_html=True)
# except Exception as e:
#     st.error(f"❌ بک‌اند در دسترس نیست. اجرا کنید: `uvicorn main:app --reload`\nخطا: {e}")
#     st.stop()

# # ─────────────────────────────────────────────
# # SIDEBAR
# # ─────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("### ⚙️ تنظیمات داشبورد")
#     show_summary   = st.checkbox("جمع‌بندی مدیریتی",      value=True)
#     show_kpis      = st.checkbox("شاخص‌های کلیدی",         value=True)
#     show_funnel    = st.checkbox("قیف فروش",               value=True)
#     show_trends    = st.checkbox("روند زمانی",              value=True)
#     show_products  = st.checkbox("تحلیل محصولات",          value=True)
#     show_customers = st.checkbox("تحلیل مشتریان",          value=True)
#     show_sources   = st.checkbox("تحلیل کانال‌ها",         value=True)
#     show_reps      = st.checkbox("تحلیل فروشندگان",        value=True)
#     show_issues    = st.checkbox("عارضه‌یابی کسب‌وکار",   value=True)
#     show_insights  = st.checkbox("بینش‌های کلیدی",         value=True)
#     show_recs      = st.checkbox("پیشنهادهای اجرایی",      value=True)
#     show_ai        = st.checkbox("گزارش اجرایی AI",         value=True)
#     show_chat      = st.checkbox("چت با هوش مصنوعی",       value=True)
#     show_raw       = st.checkbox("پیش‌نمایش داده‌ها",       value=False)

#     st.markdown("---")
#     st.markdown("### 📂 راهنمای فرمت‌ها")
#     st.markdown("""
# - **CSV/Excel**: داده‌های جدولی فروش
# - **PDF**: گزارش‌های متنی کسب‌وکار
# - **Word (DOCX)**: اسناد و گزارش‌ها
# - **TXT**: متن ساده
# """)
#     st.markdown("---")
#     st.markdown("### 🔑 ستون‌های پشتیبانی‌شده")
#     st.caption("date, revenue, leads, closed_deals, marketing_cost, sales_rep, product, region, lead_source, complaint")

# # ─────────────────────────────────────────────
# # FILE UPLOADER
# # ─────────────────────────────────────────────
# sec("📂", "آپلود فایل داده‌های کسب‌وکار")
# uploaded = st.file_uploader(
#     "فرمت‌های پشتیبانی‌شده: CSV · Excel · PDF · Word (DOCX) · متن (TXT)",
#     type=["csv","xlsx","xls","pdf","docx","doc","txt"],
#     help="فایل داده‌های فروش، گزارش، یا هر سند کسب‌وکاری خود را آپلود کنید"
# )

# if not uploaded:
#     st.markdown("""
# <div style="text-align:center;padding:3rem;background:#0A1628;border:1px dashed #1A2F55;
#             border-radius:18px;margin:1rem 0;">
#   <div style="font-size:3rem;">🔬</div>
#   <div style="color:#4A6FA5;font-size:1.1rem;margin-top:0.8rem;">
#     فایل خود را آپلود کنید تا تحلیل عارضه‌یابی شروع شود
#   </div>
#   <div style="color:#2A3F5F;font-size:0.85rem;margin-top:0.4rem;">
#     CSV · Excel · PDF · Word · TXT
#   </div>
# </div>
# """, unsafe_allow_html=True)
#     st.stop()

# st.success(f"✅ فایل آپلود شد: **{uploaded.name}** ({uploaded.size/1024:.1f} KB)")

# # ─────────────────────────────────────────────
# # ANALYZE
# # ─────────────────────────────────────────────
# if "analysis_data" not in st.session_state:
#     st.session_state.analysis_data = None
# if "analysis_filename" not in st.session_state:
#     st.session_state.analysis_filename = None
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "raw_text" not in st.session_state:
#     st.session_state.raw_text = ""

# if st.session_state.analysis_filename != uploaded.name:
#     with st.spinner("🧠 در حال تحلیل با هوش مصنوعی ..."):
#         try:
#             ext = uploaded.name.split(".")[-1].lower()
#             mime_map = {
#                 "csv":"text/csv",
#                 "xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#                 "xls":"application/vnd.ms-excel",
#                 "pdf":"application/pdf",
#                 "docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#                 "doc":"application/msword",
#                 "txt":"text/plain",
#             }
#             uploaded.seek(0)
#             resp = requests.post(
#                 API_ANALYZE,
#                 files={"file":(uploaded.name, uploaded.getvalue(), mime_map.get(ext,"application/octet-stream"))},
#                 timeout=300,
#             )
#             if resp.status_code == 200:
#                 data = resp.json()
#                 st.session_state.analysis_data = data
#                 st.session_state.analysis_filename = uploaded.name
#                 st.session_state.raw_text = data.get("raw_text","")
#                 st.session_state.chat_history = []
#             else:
#                 st.error(f"❌ خطای بک‌اند: {resp.status_code}")
#                 st.stop()
#         except requests.exceptions.ConnectionError:
#             st.error("❌ اتصال به بک‌اند قطع شد. uvicorn را اجرا کنید.")
#             st.stop()
#         except Exception as e:
#             st.error(f"❌ خطا: {e}")
#             st.stop()

# data = st.session_state.analysis_data
# if not data or not data.get("success"):
#     st.error(data.get("error","خطای ناشناخته") if data else "خطا")
#     st.stop()

# # ─────────────────────────────────────────────
# # EXTRACT DATA
# # ─────────────────────────────────────────────
# kpis      = data.get("kpis", {})
# adv       = data.get("advanced_analysis", {})
# ai_report = data.get("ai_report", "")
# funnel_d  = data.get("funnel", {})
# src_data  = data.get("source_analysis", [])
# rep_data  = data.get("rep_analysis", [])
# ts_data   = data.get("time_series", [])
# monthly   = data.get("monthly_trend", [])
# prod_data = data.get("product_analysis", [])
# reg_data  = data.get("region_analysis", [])
# cust_data = data.get("customer_analysis", {})
# comp_data = data.get("complaint_analysis", {})
# sample    = data.get("sample_data", [])
# shape     = data.get("dataset_shape", {})
# issues    = adv.get("main_issues", [])
# sub_issues= adv.get("sub_issues", [])
# insights  = adv.get("insights", [])
# recs      = adv.get("recommendations", {})
# issue_chart = adv.get("issue_chart_data", [])
# health    = adv.get("health_score", 0)
# verdict   = adv.get("final_verdict", "")
# mode      = data.get("mode","tabular")

# # ─────────────────────────────────────────────
# # TEXT-ONLY MODE
# # ─────────────────────────────────────────────
# if mode == "text_only":
#     st.info("📄 این فایل متنی است. داده‌ای جدولی شناسایی نشد — تحلیل متن توسط AI انجام شد.")
#     if data.get("ai_summary"):
#         sec("🤖","تحلیل محتوا توسط AI")
#         st.markdown(f'<div class="ai-report">{data["ai_summary"]}</div>', unsafe_allow_html=True)
#     if data.get("raw_text"):
#         with st.expander("📄 محتوای فایل"):
#             st.text(data["raw_text"][:3000])
#     # Chat still works — inline render (no separate function needed)
#     if show_chat:
#         sec("💬","چت درباره فایل")
#         if "chat_history" not in st.session_state:
#             st.session_state.chat_history = []
#         if "raw_text" not in st.session_state:
#             st.session_state.raw_text = data.get("raw_text", "")
#         st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#         if not st.session_state.chat_history:
#             st.markdown("""
# <div class="chat-ai">
#   <div class="chat-label">🤖 دستیار AI</div>
#   سلام! درباره محتوای این فایل هر سوالی دارید بپرسید.
# </div>
# """, unsafe_allow_html=True)
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 st.markdown(f'<div class="chat-user"><div class="chat-label">👤 شما</div>{msg["content"]}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="chat-ai"><div class="chat-label">🤖 دستیار AI</div>{msg["content"]}</div>', unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#         with st.form("chat_form_text", clear_on_submit=True):
#             user_q = st.text_input("سوال خود را بنویسید:", placeholder="مثال: خلاصه این فایل چیست؟", label_visibility="collapsed")
#             if st.form_submit_button("📤 ارسال", use_container_width=True) and user_q.strip():
#                 st.session_state.chat_history.append({"role": "user", "content": user_q})
#                 with st.spinner("در حال پردازش..."):
#                     try:
#                         resp_chat = requests.post(
#                             API_CHAT,
#                             data={"question": user_q, "analysis_json": "{}", "raw_text": st.session_state.raw_text[:2000]},
#                             timeout=60
#                         )
#                         answer = resp_chat.json().get("answer", "خطا") if resp_chat.status_code == 200 else "خطا در اتصال"
#                     except Exception as e:
#                         answer = f"خطا: {e}"
#                 st.session_state.chat_history.append({"role": "ai", "content": answer})
#                 st.rerun()
#     st.stop()

# # ─────────────────────────────────────────────
# # HEALTH SCORE
# # ─────────────────────────────────────────────
# hcol   = "#22C55E" if health >= 70 else "#F59E0B" if health >= 45 else "#EF4444"
# hlabel = "عالی 🚀" if health >= 70 else "متوسط ⚠️" if health >= 45 else "بحرانی 🔴"
# st.markdown(f"""
# <div class="health-bar" style="border: 1px solid {hcol}20;">
#   <div class="health-score" style="color:{hcol};">{health:.0f}</div>
#   <div>
#     <div style="font-size:1.3rem;font-weight:800;color:{hcol};">
#       امتیاز سلامت کسب‌وکار: {hlabel}
#     </div>
#     <div class="health-label">بر اساس ROI، نرخ تبدیل، نرخ برد و عارضه‌های شناسایی‌شده</div>
#   </div>
#   <div style="flex:1; text-align:left;">
#     <div style="color:{hcol};font-size:0.85rem;font-weight:600;margin-bottom:4px;">{health:.0f}/100</div>
#   </div>
# </div>
# """, unsafe_allow_html=True)
# st.progress(min(health/100, 1.0))

# # ─────────────────────────────────────────────
# # SECTION 1: MANAGEMENT SUMMARY
# # ─────────────────────────────────────────────
# if show_summary:
#     sec("📋","جمع‌بندی مدیریتی")
#     s1c1, s1c2, s1c3 = st.columns(3)
#     with s1c1:
#         st.markdown(f"""
# <div class="insight-card">
#   <div style="color:#60A5FA;font-weight:700;margin-bottom:0.5rem;">💰 وضعیت مالی</div>
#   <div>کل درآمد: <b>{money(sv(kpis,'total_revenue'))}</b></div>
#   <div>هزینه بازاریابی: <b>{money(sv(kpis,'marketing_cost'))}</b></div>
#   <div>ROI: <b style="color:{'#22C55E' if sv(kpis,'roi',0)>0 else '#EF4444'}">{pct(sv(kpis,'roi'))}</b></div>
#   <div>حاشیه سود: <b>{pct(sv(kpis,'profit_margin'))}</b></div>
# </div>
# """, unsafe_allow_html=True)
#     with s1c2:
#         st.markdown(f"""
# <div class="insight-card">
#   <div style="color:#34D399;font-weight:700;margin-bottom:0.5rem;">📊 قیف فروش</div>
#   <div>کل لیدها: <b>{sv(kpis,'total_leads',0):,}</b></div>
#   <div>معاملات بسته: <b>{sv(kpis,'total_closed_deals',0):,}</b></div>
#   <div>نرخ تبدیل: <b>{pct(sv(kpis,'conversion_rate'))}</b></div>
#   <div>نرخ برد: <b>{pct(sv(kpis,'win_rate'))}</b></div>
# </div>
# """, unsafe_allow_html=True)
#     with s1c3:
#         st.markdown(f"""
# <div class="insight-card">
#   <div style="color:#A78BFA;font-weight:700;margin-bottom:0.5rem;">🎯 بهره‌وری</div>
#   <div>ROAS: <b>{sv(kpis,'roas',0):.2f}x</b></div>
#   <div>CAC: <b>{money(sv(kpis,'cac'))}</b></div>
#   <div>میانگین معامله: <b>{money(sv(kpis,'average_deal_size'))}</b></div>
#   <div>رشد ماهانه: <b style="color:{'#22C55E' if sv(adv,'mom_growth', data.get('mom_growth',0))>=0 else '#EF4444'}">{sv(adv,'mom_growth', data.get('mom_growth',0)):+.1f}%</b></div>
# </div>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # SECTION 2: KPI METRICS
# # ─────────────────────────────────────────────
# if show_kpis:
#     sec("📈","شاخص‌های کلیدی عملکرد")
#     c1,c2,c3,c4 = st.columns(4)
#     c1.metric("💰 کل درآمد",        money(kpis.get("total_revenue")))
#     c2.metric("📉 نرخ تبدیل",       pct(kpis.get("conversion_rate")))
#     c3.metric("📊 ROI",              pct(kpis.get("roi")))
#     c4.metric("💸 هزینه بازاریابی", money(kpis.get("marketing_cost")))
#     c5,c6,c7,c8 = st.columns(4)
#     c5.metric("👥 کل لیدها",         f"{sv(kpis,'total_leads',0):,}")
#     c6.metric("🤝 معاملات بسته",     f"{sv(kpis,'total_closed_deals',0):,}")
#     c7.metric("🏆 نرخ برد",          pct(kpis.get("win_rate")))
#     c8.metric("💵 میانگین معامله",   money(kpis.get("average_deal_size")))
#     c9,c10,c11,c12 = st.columns(4)
#     c9.metric("🏷 CAC",              money(kpis.get("cac")))
#     c10.metric("📐 ROAS",            f"{sv(kpis,'roas',0):.2f}x")
#     c11.metric("🔄 حاشیه سود",       pct(kpis.get("profit_margin")))
#     c12.metric("📈 رشد ماهانه",      f"{sv(adv,'mom_growth', data.get('mom_growth', 0)):+.1f}%")
#     if sv(kpis,"total_complaints",0) > 0:
#         cc1,cc2 = st.columns(2)
#         cc1.metric("📣 کل شکایات",   f"{sv(kpis,'total_complaints',0):,}")
#         cc2.metric("⚠️ نرخ شکایت",   pct(kpis.get("complaint_rate")))

# # ─────────────────────────────────────────────
# # SECTION 3: SALES FUNNEL
# # ─────────────────────────────────────────────
# if show_funnel and funnel_d:
#     sec("🔽","روند قیف فروش")
#     funnel_stages = ["لیدها","واجد شرایط","دمو","پروپوزال","معاملات بسته"]
#     funnel_vals   = [
#         sv(kpis,"total_leads",0), sv(kpis,"total_qualified_leads",0),
#         sv(kpis,"total_demos",0), sv(kpis,"total_proposals",0),
#         sv(kpis,"total_closed_deals",0)
#     ]
#     fc1, fc2 = st.columns([3,2])
#     with fc1:
#         fig_f = go.Figure(go.Funnel(
#             y=funnel_stages, x=funnel_vals,
#             textinfo="value+percent initial",
#             marker=dict(color=CHART_COLORS[:5]),
#         ))
#         fig_f.update_layout(title="قیف فروش کامل", **PLOTLY)
#         st.plotly_chart(fig_f, use_container_width=True)
#     with fc2:
#         st.markdown("#### نرخ تبدیل هر مرحله")
#         funnel_df = pd.DataFrame({
#             "مرحله": ["لید → واجد","واجد → دمو","دمو → پروپوزال","پروپوزال → بسته"],
#             "نرخ(%)": [
#                 funnel_d.get("leads_to_qualified",0),
#                 funnel_d.get("qualified_to_demo",0),
#                 funnel_d.get("demo_to_proposal",0),
#                 funnel_d.get("proposal_to_closed",0),
#             ]
#         })
#         def color_rate(val):
#             if val >= 50: return "background-color:#0B1A0E;color:#22C55E"
#             if val >= 25: return "background-color:#1A1400;color:#F59E0B"
#             return "background-color:#1A0B0B;color:#EF4444"
#         st.dataframe(
#             funnel_df.style.map(color_rate, subset=["نرخ(%)"]),
#             use_container_width=True, hide_index=True
#         )
#         weak = data.get("weakest_funnel_stage","")
#         weak_pct = data.get("weakest_funnel_pct", 0)
#         if weak:
#             st.warning(f"⚠️ ضعیف‌ترین مرحله: **{weak}** — نرخ: {weak_pct:.1f}٪")

# # ─────────────────────────────────────────────
# # SECTION 4: TIME TRENDS
# # ─────────────────────────────────────────────
# if show_trends:
#     trend_tabs = st.tabs(["📅 روند ماهانه","📈 روند هفتگی"])
#     with trend_tabs[0]:
#         if monthly:
#             sec("📅","روند ماهانه فروش")
#             m_df = pd.DataFrame(monthly)
#             tt1,tt2 = st.columns(2)
#             with tt1:
#                 fig_m = px.bar(m_df, x="date", y="revenue", title="درآمد ماهانه",
#                                color_discrete_sequence=["#3B82F6"])
#                 fig_m.update_layout(**PLOTLY)
#                 st.plotly_chart(fig_m, use_container_width=True)
#             with tt2:
#                 fig_ml = px.line(m_df, x="date", y="closed", markers=True,
#                                  title="معاملات بسته ماهانه",
#                                  color_discrete_sequence=["#10B981"])
#                 fig_ml.update_layout(**PLOTLY)
#                 fig_ml.update_traces(line_width=3)
#                 st.plotly_chart(fig_ml, use_container_width=True)
#         else:
#             st.info("ستون تاریخ در داده‌ها یافت نشد")

#     with trend_tabs[1]:
#         if ts_data:
#             sec("📈","روند زمانی هفتگی فروش")
#             ts_df = pd.DataFrame(ts_data)
#             if "date" in ts_df.columns:
#                 ts_df["date"] = pd.to_datetime(ts_df["date"])
#                 tc1,tc2 = st.columns(2)
#                 with tc1:
#                     fig_ts = px.line(ts_df, x="date", y="revenue", markers=True,
#                                      title="روند درآمد هفتگی",
#                                      color_discrete_sequence=["#3B82F6"])
#                     fig_ts.update_layout(**PLOTLY)
#                     fig_ts.update_traces(line_width=3)
#                     st.plotly_chart(fig_ts, use_container_width=True)
#                 with tc2:
#                     fig_area = px.area(ts_df, x="date", y="leads",
#                                        title="روند لیدها هفتگی",
#                                        color_discrete_sequence=["#10B981"])
#                     fig_area.update_layout(**PLOTLY)
#                     st.plotly_chart(fig_area, use_container_width=True)
#         else:
#             st.info("داده‌های زمانی در دسترس نیست")

# # ─────────────────────────────────────────────
# # SECTION 5: PRODUCT ANALYSIS
# # ─────────────────────────────────────────────
# if show_products and prod_data:
#     sec("📦","تحلیل محصولات — نمودار فروش به تفکیک محصول")
#     prod_df = pd.DataFrame(prod_data)
#     pc1,pc2 = st.columns(2)
#     with pc1:
#         fig_p = px.bar(prod_df, x="product", y="revenue",
#                        color="product", title="درآمد به تفکیک محصول",
#                        color_discrete_sequence=CHART_COLORS)
#         fig_p.update_layout(**PLOTLY)
#         st.plotly_chart(fig_p, use_container_width=True)
#     with pc2:
#         fig_pp = px.pie(prod_df, names="product", values="revenue",
#                         title="سهم درآمد هر محصول",
#                         color_discrete_sequence=CHART_COLORS, hole=0.4)
#         fig_pp.update_layout(**PLOTLY)
#         st.plotly_chart(fig_pp, use_container_width=True)
#     if "avg_deal" in prod_df.columns:
#         fig_pd = px.bar(prod_df, x="product", y="avg_deal",
#                         color="product", title="میانگین ارزش معامله به تفکیک محصول",
#                         color_discrete_sequence=CHART_COLORS)
#         fig_pd.update_layout(**PLOTLY)
#         st.plotly_chart(fig_pd, use_container_width=True)
#     st.dataframe(prod_df, use_container_width=True, hide_index=True)

# # ─────────────────────────────────────────────
# # SECTION 6: CUSTOMER ANALYSIS
# # ─────────────────────────────────────────────
# if show_customers:
#     sec("👥","تحلیل مشتریان")
#     if cust_data and cust_data.get("top_customers"):
#         ca1,ca2,ca3 = st.columns(3)
#         ca1.metric("مشتریان منحصربه‌فرد", f"{sv(cust_data,'total_unique',0):,}")
#         ca2.metric("میانگین درآمد هر مشتری", money(sv(cust_data,'avg_revenue_per_customer')))
#         ca3.metric("تعداد مشتریان برتر", len(cust_data.get("top_customers",[])))
#         top_cust = pd.DataFrame(cust_data["top_customers"])
#         fig_c = px.bar(top_cust, x="customer", y="revenue",
#                        color="revenue", title="۱۰ مشتری برتر",
#                        color_discrete_sequence=CHART_COLORS)
#         fig_c.update_layout(**PLOTLY)
#         st.plotly_chart(fig_c, use_container_width=True)
#     else:
#         st.info("ستون مشتری (customer) در دیتاست یافت نشد")

#     # Complaint analysis
#     sec("📣","تحلیل شکایات مشتریان")
#     if comp_data:
#         cp1,cp2,cp3 = st.columns(3)
#         cp1.metric("کل شکایات", f"{sv(comp_data,'total_complaints',0):,}")
#         cp2.metric("نرخ شکایت", pct(sv(comp_data,'complaint_rate')))
#         cp3.metric("شدت شکایت", comp_data.get("complaint_severity","N/A"))
#         if comp_data.get("by_source"):
#             comp_src_df = pd.DataFrame(comp_data["by_source"])
#             fig_cs = px.bar(comp_src_df, x="lead_source", y="complaints",
#                             color="lead_source", title="شکایات به تفکیک کانال",
#                             color_discrete_sequence=CHART_COLORS)
#             fig_cs.update_layout(**PLOTLY)
#             st.plotly_chart(fig_cs, use_container_width=True)
#     else:
#         st.info("ستون شکایت (complaint) در دیتاست یافت نشد")

# # ─────────────────────────────────────────────
# # SECTION 7: CHANNEL & REP ANALYSIS
# # ─────────────────────────────────────────────
# if show_sources and src_data:
#     sec("📡","تحلیل کانال‌های بازاریابی")
#     src_df = pd.DataFrame(src_data)
#     sc1,sc2 = st.columns(2)
#     with sc1:
#         fig_src = px.bar(src_df, x="lead_source", y="revenue",
#                          color="lead_source", title="درآمد به تفکیک کانال",
#                          color_discrete_sequence=CHART_COLORS)
#         fig_src.update_layout(**PLOTLY)
#         st.plotly_chart(fig_src, use_container_width=True)
#     with sc2:
#         fig_roi_s = px.bar(src_df, x="lead_source", y="roi",
#                            color="lead_source", title="ROI به تفکیک کانال(%)",
#                            color_discrete_sequence=CHART_COLORS)
#         fig_roi_s.update_layout(**PLOTLY)
#         st.plotly_chart(fig_roi_s, use_container_width=True)
#     sc3,sc4 = st.columns(2)
#     with sc3:
#         fig_conv = px.bar(src_df, x="lead_source", y="conversion",
#                           color="lead_source", title="نرخ تبدیل به تفکیک کانال(%)",
#                           color_discrete_sequence=CHART_COLORS)
#         fig_conv.update_layout(**PLOTLY)
#         st.plotly_chart(fig_conv, use_container_width=True)
#     with sc4:
#         if "roas" in src_df.columns and src_df["roas"].sum() > 0:
#             fig_roas_p = px.pie(src_df, names="lead_source", values="roas",
#                                 title="ROAS به تفکیک کانال", hole=0.45,
#                                 color_discrete_sequence=CHART_COLORS)
#             fig_roas_p.update_layout(**PLOTLY)
#             st.plotly_chart(fig_roas_p, use_container_width=True)
#         else:
#             st.info("داده ROAS برای نمودار دایره‌ای کافی نیست")
#     # Scatter: cost vs revenue — only if cost column present
#     if "cost" in src_df.columns and src_df["cost"].sum() > 0:
#         max_v = max(src_df["cost"].max(), src_df["revenue"].max())
#         if max_v > 0:
#             fig_sc = px.scatter(src_df, x="cost", y="revenue", color="lead_source",
#                                 size="closed", text="lead_source", size_max=50,
#                                 title="هزینه vs درآمد به تفکیک کانال",
#                                 color_discrete_sequence=CHART_COLORS)
#             fig_sc.add_shape(type="line", x0=0,y0=0,x1=max_v,y1=max_v,
#                              line=dict(color="#64748B",dash="dot"))
#             fig_sc.add_annotation(x=max_v*0.8, y=max_v*0.8, text="نقطه سربه‌سر",
#                                   font=dict(color="#64748B"))
#             fig_sc.update_layout(**PLOTLY)
#             st.plotly_chart(fig_sc, use_container_width=True)
#     st.dataframe(src_df, use_container_width=True, hide_index=True)

# if show_reps and rep_data:
#     sec("🏆","تحلیل عملکرد فروشندگان")
#     rep_df = pd.DataFrame(rep_data)
#     rc1,rc2 = st.columns(2)
#     with rc1:
#         fig_r = px.bar(rep_df, x="sales_rep", y="revenue",
#                        color="sales_rep", title="درآمد به تفکیک فروشنده",
#                        color_discrete_sequence=CHART_COLORS)
#         fig_r.update_layout(**PLOTLY)
#         st.plotly_chart(fig_r, use_container_width=True)
#     with rc2:
#         fig_rd = px.bar(rep_df, x="sales_rep", y="avg_deal",
#                         color="sales_rep", title="میانگین معامله به تفکیک فروشنده",
#                         color_discrete_sequence=CHART_COLORS)
#         fig_rd.update_layout(**PLOTLY)
#         st.plotly_chart(fig_rd, use_container_width=True)
#     if len(rep_df) >= 2:
#         fig_rb = px.scatter(rep_df, x="leads", y="revenue", size="closed",
#                             color="sales_rep", text="sales_rep", size_max=60,
#                             title="لیدها vs درآمد فروشندگان",
#                             color_discrete_sequence=CHART_COLORS)
#         fig_rb.update_layout(**PLOTLY)
#         st.plotly_chart(fig_rb, use_container_width=True)
#     st.dataframe(rep_df, use_container_width=True, hide_index=True)

# # Region
# if reg_data:
#     sec("🗺️","تحلیل مناطق")
#     reg_df = pd.DataFrame(reg_data)
#     rg1,rg2 = st.columns(2)
#     with rg1:
#         fig_rg = px.pie(reg_df, names="region", values="revenue",
#                         title="درآمد به تفکیک منطقه",
#                         color_discrete_sequence=CHART_COLORS, hole=0.4)
#         fig_rg.update_layout(**PLOTLY)
#         st.plotly_chart(fig_rg, use_container_width=True)
#     with rg2:
#         fig_rg2 = px.bar(reg_df, x="region", y="revenue",
#                          color="region", title="مقایسه درآمد مناطق",
#                          color_discrete_sequence=CHART_COLORS)
#         fig_rg2.update_layout(**PLOTLY)
#         st.plotly_chart(fig_rg2, use_container_width=True)

# # ─────────────────────────────────────────────
# # SECTION 8: BUSINESS PATHOLOGY (عارضه‌یابی)
# # ─────────────────────────────────────────────
# if show_issues:
#     sec("🔬","عارضه‌یابی کسب‌وکار — عارضه‌های اصلی و فرعی")
#     issue_tab1, issue_tab2 = st.tabs(["⚠️ عارضه‌های اصلی","📊 عارضه‌های فرعی"])
#     with issue_tab1:
#         if issues:
#             for issue in issues:
#                 issue_card(issue)
#         else:
#             st.success("✅ هیچ عارضه بحرانی شناسایی نشد")
#     with issue_tab2:
#         if sub_issues:
#             for issue in sub_issues:
#                 issue_card(issue)
#         else:
#             st.success("✅ هیچ عارضه فرعی شناسایی نشد")

#     # Issue frequency chart
#     sec("📊","نمودار تعداد رخدادهای عارضه‌های کسب‌وکار")
#     if issue_chart:
#         ic_df = pd.DataFrame(issue_chart)
#         color_map = {"critical":"#EF4444","warning":"#F59E0B","healthy":"#22C55E"}
#         colors = [color_map.get(s,"#3B82F6") for s in ic_df["severity"].tolist()]
#         fig_ic = go.Figure(go.Bar(
#             x=ic_df["count"], y=ic_df["name"],
#             orientation="h",
#             marker_color=colors,
#             text=ic_df["count"],
#             textposition="outside"
#         ))
#         fig_ic.update_layout(
#             title="تعداد رخداد هر عارضه در دیتاست",
#             xaxis_title="تعداد رخداد",
#             yaxis_title="عارضه",
#             **PLOTLY
#         )
#         st.plotly_chart(fig_ic, use_container_width=True)

#     # Detailed analysis
#     sec("🔍","تحلیل دقیق عارضه‌های کسب‌وکار")
#     all_issues = issues + sub_issues
#     for issue in all_issues:
#         if issue.get("severity") == "healthy":
#             continue
#         with st.expander(f"{'🔴' if issue.get('severity')=='critical' else '🟡'} {issue.get('title','')}"):
#             st.markdown(f"**شاخص:** {issue.get('metric','N/A')}")
#             st.markdown(f"**تاثیر کسب‌وکاری:** {issue.get('impact','')}")
#             st.markdown(f"**شدت:** {'بحرانی — نیاز به اقدام فوری' if issue.get('severity')=='critical' else 'هشدار — نیاز به پایش'}")

# # ─────────────────────────────────────────────
# # SECTION 9: KEY INSIGHTS
# # ─────────────────────────────────────────────
# if show_insights and insights:
#     sec("💡","مهمترین بینش‌ها")
#     cols_i = st.columns(3)
#     for i, ins in enumerate(insights):
#         cols_i[i % 3].markdown(
#             f'<div class="insight-card">{ins}</div>',
#             unsafe_allow_html=True
#         )

# # ─────────────────────────────────────────────
# # SECTION 10: RECOMMENDATIONS
# # ─────────────────────────────────────────────
# if show_recs and recs:
#     sec("🚀","پیشنهادهای اجرایی")
#     r1,r2,r3 = st.columns(3)
#     with r1:
#         st.markdown("""
# <div class="rec-term">
#   <div class="rec-term-title" style="color:#EF4444;">⚡ کوتاه‌مدت (۱-۳۰ روز)</div>
# """, unsafe_allow_html=True)
#         for item in recs.get("short_term",[]):
#             st.markdown(f'<div class="rec-item rec-short">{item}</div>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
#     with r2:
#         st.markdown("""
# <div class="rec-term">
#   <div class="rec-term-title" style="color:#F59E0B;">📅 میان‌مدت (۱-۳ ماه)</div>
# """, unsafe_allow_html=True)
#         for item in recs.get("mid_term",[]):
#             st.markdown(f'<div class="rec-item rec-mid">{item}</div>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)
#     with r3:
#         st.markdown("""
# <div class="rec-term">
#   <div class="rec-term-title" style="color:#22C55E;">🌱 بلندمدت (۳-۱۲ ماه)</div>
# """, unsafe_allow_html=True)
#         for item in recs.get("long_term",[]):
#             st.markdown(f'<div class="rec-item rec-long">{item}</div>', unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # SECTION 11: AI REPORT
# # ─────────────────────────────────────────────
# if show_ai:
#     sec("🤖","گزارش اجرایی هوش مصنوعی")
#     if ai_report:
#         st.markdown(f'<div class="ai-report">{ai_report}</div>', unsafe_allow_html=True)
#     else:
#         st.warning("گزارش AI در دسترس نیست. GROQ_API_KEY را تنظیم کنید.")

# # ─────────────────────────────────────────────
# # SECTION 12: FINAL VERDICT
# # ─────────────────────────────────────────────
# sec("🏁","نتیجه نهایی")
# verdict_cls = "verdict-good" if health >= 70 else "verdict-medium" if health >= 45 else "verdict-critical"
# st.markdown(f'<div class="verdict-box {verdict_cls}">{verdict}</div>', unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # SECTION 13: AI CHAT
# # ─────────────────────────────────────────────
# if show_chat:
#     sec("💬","چت با هوش مصنوعی — درباره فایل خود بپرسید")
#     chat_container = st.container()
#     with chat_container:
#         st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#         if not st.session_state.chat_history:
#             st.markdown("""
# <div class="chat-ai">
#   <div class="chat-label">🤖 دستیار AI</div>
#   سلام! من دستیار تحلیل کسب‌وکار شما هستم. درباره داده‌های فایل آپلود شده هر سوالی دارید بپرسید.
#   مثال: «بزرگترین مشکل کسب‌وکار من چیست؟» یا «چطور ROI را بهبود دهم؟»
# </div>
# """, unsafe_allow_html=True)
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 st.markdown(f"""
# <div class="chat-user">
#   <div class="chat-label">👤 شما</div>
#   {msg["content"]}
# </div>
# """, unsafe_allow_html=True)
#             else:
#                 st.markdown(f"""
# <div class="chat-ai">
#   <div class="chat-label">🤖 دستیار AI</div>
#   {msg["content"]}
# </div>
# """, unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     with st.form("chat_form", clear_on_submit=True):
#         user_q = st.text_input(
#             "سوال خود را بنویسید:",
#             placeholder="مثال: بزرگترین عارضه کسب‌وکار من چیست؟",
#             label_visibility="collapsed"
#         )
#         chat_btn = st.form_submit_button("📤 ارسال", use_container_width=True)

#     if chat_btn and user_q.strip():
#         st.session_state.chat_history.append({"role":"user","content":user_q})
#         with st.spinner("🤔 در حال پردازش ..."):
#             try:
#                 analysis_context = json.dumps({
#                     "kpis": kpis,
#                     "advanced_analysis": adv,
#                     "funnel": funnel_d,
#                 }, ensure_ascii=False)[:4000]
#                 resp_chat = requests.post(
#                     API_CHAT,
#                     data={
#                         "question": user_q,
#                         "analysis_json": analysis_context,
#                         "raw_text": st.session_state.raw_text[:2000]
#                     },
#                     timeout=60
#                 )
#                 answer = resp_chat.json().get("answer","خطا در دریافت پاسخ") if resp_chat.status_code == 200 else "خطا در اتصال"
#             except Exception as e:
#                 answer = f"خطا: {str(e)}"
#         st.session_state.chat_history.append({"role":"ai","content":answer})
#         st.rerun()

# # ─────────────────────────────────────────────
# # SECTION 14: EXPORT
# # ─────────────────────────────────────────────
# sec("📤","خروجی گزارش")
# exp1, exp2 = st.columns(2)
# with exp1:
#     if st.button("⬇️ دانلود گزارش اکسل", use_container_width=True):
#         with st.spinner("در حال آماده‌سازی فایل اکسل ..."):
#             try:
#                 export_data = {
#                     "kpis": kpis,
#                     "monthly_trend": monthly,
#                     "source_analysis": src_data,
#                     "rep_analysis": rep_data,
#                     "product_analysis": prod_data,
#                     "advanced_analysis": adv,
#                 }
#                 resp_exp = requests.post(
#                     API_EXPORT,
#                     data={"analysis_json": json.dumps(export_data, ensure_ascii=False)},
#                     timeout=60
#                 )
#                 if resp_exp.status_code == 200:
#                     st.download_button(
#                         "💾 ذخیره فایل Excel",
#                         data=resp_exp.content,
#                         file_name=f"bizdiag_report_{uploaded.name}.xlsx",
#                         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                     )
#                 else:
#                     st.error("خطا در تولید اکسل")
#             except Exception as e:
#                 st.error(f"خطا: {e}")

# with exp2:
#     if st.button("📋 کپی گزارش متنی", use_container_width=True):
#         report_text = f"""
# گزارش BizDiag
# ==============
# فایل: {uploaded.name}

# KPI های کلیدی:
# - کل درآمد: {money(kpis.get('total_revenue'))}
# - ROI: {pct(kpis.get('roi'))}
# - نرخ تبدیل: {pct(kpis.get('conversion_rate'))}
# - نرخ برد: {pct(kpis.get('win_rate'))}
# - امتیاز سلامت: {health:.0f}/100

# عارضه‌های اصلی:
# {chr(10).join(f"- {i.get('title','')}: {i.get('metric','')}" for i in issues)}

# نتیجه نهایی:
# {verdict}

# گزارش AI:
# {ai_report[:1000] if ai_report else 'N/A'}
# """
#         st.text_area("گزارش متنی:", report_text, height=200)

# # ─────────────────────────────────────────────
# # DATASET PREVIEW
# # ─────────────────────────────────────────────
# if show_raw and sample:
#     sec("🗂","پیش‌نمایش داده‌های خام")
#     info_c1,info_c2,info_c3 = st.columns(3)
#     info_c1.metric("تعداد ردیف‌ها", f"{sv(shape,'rows',0):,}")
#     info_c2.metric("تعداد ستون‌ها", sv(shape,"columns",0))
#     info_c3.metric("کانال‌های شناسایی‌شده", len(src_data))
#     det = data.get("detected_columns",[])
#     if det:
#         st.code(", ".join(det), language=None)
#     st.dataframe(pd.DataFrame(sample), use_container_width=True, hide_index=True)

# # ─────────────────────────────────────────────
# # FOOTER
# # ─────────────────────────────────────────────
# st.markdown("---")
# st.markdown("""
# <div style="text-align:center;color:#1A2F55;font-size:0.8rem;padding:1rem 0;font-family:'Vazirmatn',sans-serif;">
#   BizDiag v9.0 · سامانه عارضه‌یابی کسب‌وکار · پشتیبانی: CSV · Excel · PDF · Word · TXT
#   <br>Powered by Groq LLaMA-3.3-70B · Claude Sonnet
# </div>
# """, unsafe_allow_html=True)



# """
# BizDiag — Business Diagnostics
# Minimal Dark UI · No Sidebar · English Metric Labels · Persian Interface
# """

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import json

# # ─────────────────────────────────────────────
# # PAGE CONFIG
# # ─────────────────────────────────────────────
# st.set_page_config(
#     page_title="BizDiag",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ─────────────────────────────────────────────
# # HIDE SIDEBAR COMPLETELY
# # ─────────────────────────────────────────────
# st.markdown("""
# <style>
#     [data-testid="stSidebar"] { display: none; }
#     [data-testid="stSidebarCollapsedControl"] { display: none; }
# </style>
# """, unsafe_allow_html=True)

# API_BASE = "http://127.0.0.1:8000"
# API_ANALYZE = f"{API_BASE}/analyze"
# API_HEALTH = f"{API_BASE}/health"
# API_CHAT = f"{API_BASE}/chat"
# API_EXPORT = f"{API_BASE}/export/excel"

# # ─────────────────────────────────────────────
# # CSS – Minimal Dark, No Sidebar, English metric names
# # ─────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700&display=swap');

# * {
#     font-family: 'Vazirmatn', sans-serif;
#     margin: 0;
#     padding: 0;
#     box-sizing: border-box;
# }

# html, body, .stApp {
#     background-color: #0A0A0F;
#     color: #EDEDF0;
# }

# .block-container {
#     padding-top: 1rem;
#     padding-bottom: 2rem;
#     max-width: 1300px;
#     margin: 0 auto;
# }

# /* Scrollbar */
# ::-webkit-scrollbar { width: 4px; height: 4px; }
# ::-webkit-scrollbar-track { background: #1A1A22; }
# ::-webkit-scrollbar-thumb { background: #3A3A4A; border-radius: 4px; }

# /* Tabs */
# .stTabs [data-baseweb="tab-list"] {
#     gap: 0rem;
#     background: transparent;
#     border-bottom: 1px solid #22222A;
#     margin-bottom: 1.5rem;
# }
# .stTabs [data-baseweb="tab"] {
#     background: transparent;
#     color: #8A8A9A;
#     font-weight: 500;
#     font-size: 0.85rem;
#     padding: 0.5rem 1.2rem;
#     border-radius: 0;
#     transition: all 0.2s;
# }
# .stTabs [aria-selected="true"] {
#     color: #FFFFFF;
#     border-bottom: 2px solid #2563EB;
#     background: transparent;
# }

# /* Cards – minimal */
# .card {
#     background: #111118;
#     border: 1px solid #22222A;
#     border-radius: 14px;
#     padding: 1rem 1.2rem;
#     transition: border 0.2s;
# }
# .card:hover {
#     border-color: #2A2A35;
# }
# .metric-card {
#     background: #111118;
#     border: 1px solid #22222A;
#     border-radius: 14px;
#     padding: 0.8rem;
#     text-align: center;
# }
# .metric-value {
#     font-size: 1.6rem;
#     font-weight: 600;
#     color: #FFFFFF;
#     letter-spacing: -0.01em;
# }
# .metric-label {
#     font-size: 0.7rem;
#     text-transform: uppercase;
#     letter-spacing: 0.02em;
#     color: #8A8A9A;
#     margin-top: 0.25rem;
# }

# /* Health hero */
# .health-hero {
#     background: #111118;
#     border: 1px solid #22222A;
#     border-radius: 20px;
#     padding: 1.2rem 1.8rem;
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     margin-bottom: 1.5rem;
# }
# .health-score {
#     font-size: 2.5rem;
#     font-weight: 700;
# }
# .health-label {
#     font-size: 0.7rem;
#     color: #8A8A9A;
# }

# /* Issue cards */
# .issue-card {
#     border-right: 3px solid;
#     background: #111118;
#     border-left: 1px solid #22222A;
#     border-top: 1px solid #22222A;
#     border-bottom: 1px solid #22222A;
#     border-radius: 10px;
#     padding: 0.8rem 1rem;
#     margin-bottom: 0.75rem;
# }
# .issue-critical { border-right-color: #EF4444; }
# .issue-warning  { border-right-color: #F59E0B; }
# .issue-title {
#     font-weight: 600;
#     font-size: 0.85rem;
#     margin-bottom: 0.2rem;
# }
# .issue-metric {
#     font-size: 0.7rem;
#     color: #A1A1B0;
#     margin-bottom: 0.2rem;
# }
# .issue-impact {
#     font-size: 0.75rem;
#     color: #C1C1D0;
# }
# .badge {
#     display: inline-block;
#     font-size: 0.6rem;
#     padding: 0.1rem 0.5rem;
#     border-radius: 6px;
#     margin-bottom: 0.4rem;
# }
# .badge-critical { background: #2A1010; color: #F87171; }
# .badge-warning  { background: #2A1E10; color: #FBBF24; }

# /* Insights */
# .insight-text {
#     font-size: 0.85rem;
#     padding: 0.5rem 0;
#     border-bottom: 1px solid #1E1E2A;
#     color: #D1D1DC;
# }

# /* Recommendations */
# .rec-section {
#     margin-bottom: 1rem;
# }
# .rec-header {
#     font-weight: 600;
#     font-size: 0.7rem;
#     text-transform: uppercase;
#     color: #8A8A9A;
#     margin-bottom: 0.5rem;
# }
# .rec-item {
#     font-size: 0.8rem;
#     padding: 0.3rem 0 0.3rem 0.8rem;
#     border-right: 2px solid;
#     margin-bottom: 0.4rem;
# }
# .rec-short { border-right-color: #EF4444; }
# .rec-mid   { border-right-color: #F59E0B; }
# .rec-long  { border-right-color: #10B981; }

# /* Chat */
# .chat-container {
#     background: #0F0F14;
#     border: 1px solid #22222A;
#     border-radius: 16px;
#     padding: 1rem;
#     max-height: 500px;
#     overflow-y: auto;
# }
# .chat-user {
#     background: #1A1A24;
#     border-radius: 16px 16px 4px 16px;
#     padding: 0.6rem 1rem;
#     margin: 0.5rem 0 0.5rem 2rem;
#     font-size: 0.85rem;
# }
# .chat-ai {
#     background: #111118;
#     border: 1px solid #22222A;
#     border-radius: 16px 16px 16px 4px;
#     padding: 0.6rem 1rem;
#     margin: 0.5rem 2rem 0.5rem 0;
#     font-size: 0.85rem;
#     line-height: 1.5;
# }
# .chat-label {
#     font-size: 0.65rem;
#     color: #8A8A9A;
#     margin-bottom: 0.2rem;
# }

# /* Buttons */
# .stButton > button {
#     background: #2563EB;
#     color: white;
#     border: none;
#     border-radius: 8px;
#     font-weight: 500;
#     padding: 0.4rem 1rem;
#     font-size: 0.8rem;
# }
# .stButton > button:hover {
#     background: #3B82F6;
# }

# /* File uploader */
# [data-testid="stFileUploadDropzone"] {
#     background: #0F0F14;
#     border: 1px dashed #2A2A35;
#     border-radius: 14px;
#     padding: 1rem;
# }

# /* Dividers */
# hr {
#     margin: 1rem 0;
#     border-color: #1E1E2A;
# }

# /* Inputs */
# .stTextInput > div > div > input {
#     background: #0F0F14;
#     border: 1px solid #22222A;
#     color: #EDEDF0;
#     border-radius: 8px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ─────────────────────────────────────────────
# # HELPERS
# # ─────────────────────────────────────────────
# def money(v):
#     try:
#         return f"{float(v):,.0f}"
#     except:
#         return "0"

# def pct(v):
#     try:
#         return f"{float(v):.1f}%"
#     except:
#         return "0%"

# def sv(d, key, default=0):
#     try:
#         return d.get(key, default) if d else default
#     except:
#         return default

# # ─────────────────────────────────────────────
# # BACKEND CHECK
# # ─────────────────────────────────────────────
# try:
#     h = requests.get(API_HEALTH, timeout=4)
#     if h.status_code != 200:
#         st.error("❌ Backend not reachable. Run: uvicorn main:app --reload")
#         st.stop()
#     ai_ok = h.json().get("groq_enabled", False)
# except:
#     st.error("❌ Connection failed.")
#     st.stop()

# # ─────────────────────────────────────────────
# # MAIN AREA – NO SIDEBAR
# # ─────────────────────────────────────────────
# st.markdown("<h1 style='font-size:1.6rem; font-weight:600; margin-bottom:0.25rem;'>BizDiag</h1>", unsafe_allow_html=True)
# st.markdown("<p style='color:#8A8A9A; margin-bottom:1.5rem;'>Business diagnostics · AI‑powered analysis</p>", unsafe_allow_html=True)

# # File upload at top
# uploaded = st.file_uploader(
#     "Upload CSV, Excel, PDF, Word, or TXT",
#     type=["csv", "xlsx", "xls", "pdf", "docx", "doc", "txt"],
#     label_visibility="collapsed"
# )

# if not uploaded:
#     st.markdown("""
#     <div style="text-align:center; padding:3rem; background:#111118; border:1px solid #22222A; border-radius:20px; margin-top:1rem;">
#         <div style="font-size:2rem;">⚡</div>
#         <p style="color:#8A8A9A; margin-top:0.5rem;">Upload a file to start the analysis</p>
#     </div>
#     """, unsafe_allow_html=True)
#     st.stop()

# st.success(f"✅ Loaded: **{uploaded.name}**")

# # ─────────────────────────────────────────────
# # ANALYSIS STATE
# # ─────────────────────────────────────────────
# if "analysis_data" not in st.session_state:
#     st.session_state.analysis_data = None
# if "analysis_filename" not in st.session_state:
#     st.session_state.analysis_filename = None
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "raw_text" not in st.session_state:
#     st.session_state.raw_text = ""

# if st.session_state.analysis_filename != uploaded.name:
#     with st.spinner("Analyzing with AI..."):
#         try:
#             ext = uploaded.name.split(".")[-1].lower()
#             mime_map = {
#                 "csv": "text/csv",
#                 "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#                 "xls": "application/vnd.ms-excel",
#                 "pdf": "application/pdf",
#                 "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#                 "doc": "application/msword",
#                 "txt": "text/plain",
#             }
#             uploaded.seek(0)
#             resp = requests.post(
#                 API_ANALYZE,
#                 files={"file": (uploaded.name, uploaded.getvalue(), mime_map.get(ext, "application/octet-stream"))},
#                 timeout=300,
#             )
#             if resp.status_code == 200:
#                 data = resp.json()
#                 st.session_state.analysis_data = data
#                 st.session_state.analysis_filename = uploaded.name
#                 st.session_state.raw_text = data.get("raw_text", "")
#                 st.session_state.chat_history = []
#             else:
#                 st.error(f"Backend error: {resp.status_code}")
#                 st.stop()
#         except Exception as e:
#             st.error(f"Error: {e}")
#             st.stop()

# data = st.session_state.analysis_data
# if not data or not data.get("success"):
#     st.error(data.get("error", "Unknown error"))
#     st.stop()

# # Extract data
# kpis = data.get("kpis", {})
# adv = data.get("advanced_analysis", {})
# ai_report = data.get("ai_report", "")
# funnel_d = data.get("funnel", {})
# src_data = data.get("source_analysis", [])
# rep_data = data.get("rep_analysis", [])
# monthly = data.get("monthly_trend", [])
# prod_data = data.get("product_analysis", [])
# reg_data = data.get("region_analysis", [])
# issues = adv.get("main_issues", [])
# sub_issues = adv.get("sub_issues", [])
# insights = adv.get("insights", [])
# recs = adv.get("recommendations", {})
# issue_chart = adv.get("issue_chart_data", [])
# health = adv.get("health_score", 50)
# verdict = adv.get("final_verdict", "")
# mode = data.get("mode", "tabular")
# sample = data.get("sample_data", [])
# shape = data.get("dataset_shape", {})

# # Plotly config
# PLOTLY_DARK = {
#     "paper_bgcolor": "rgba(0,0,0,0)",
#     "plot_bgcolor": "rgba(0,0,0,0)",
#     "font": {"family": "Vazirmatn", "color": "#C1C1D0", "size": 11},
#     "margin": {"l": 20, "r": 20, "t": 35, "b": 20},
#     "xaxis": {"gridcolor": "#22222A", "zerolinecolor": "#22222A"},
#     "yaxis": {"gridcolor": "#22222A", "zerolinecolor": "#22222A"},
#     "legend": {"bgcolor": "rgba(0,0,0,0)"},
# }

# # Text-only mode handling
# if mode == "text_only":
#     st.info("Text file uploaded. AI summary and chat are available.")
#     if data.get("ai_summary"):
#         st.markdown("### AI Summary")
#         st.write(data["ai_summary"])
#     with st.expander("File content"):
#         st.text(data.get("raw_text", "")[:3000])
#     # Chat only
#     st.subheader("Chat with AI")
#     chat_cont = st.container()
#     with chat_cont:
#         st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#         if not st.session_state.chat_history:
#             st.markdown('<div class="chat-ai"><div class="chat-label">AI</div>Ask anything about this document.</div>', unsafe_allow_html=True)
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 st.markdown(f'<div class="chat-user"><div class="chat-label">You</div>{msg["content"]}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="chat-ai"><div class="chat-label">AI</div>{msg["content"]}</div>', unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with st.form("chat_text", clear_on_submit=True):
#         q = st.text_input("Your question:", label_visibility="collapsed")
#         if st.form_submit_button("Send") and q.strip():
#             st.session_state.chat_history.append({"role": "user", "content": q})
#             with st.spinner("Thinking..."):
#                 try:
#                     resp = requests.post(API_CHAT, data={"question": q, "analysis_json": "{}", "raw_text": st.session_state.raw_text[:2000]}, timeout=60)
#                     ans = resp.json().get("answer", "Error") if resp.status_code == 200 else "Error"
#                 except:
#                     ans = "Connection error"
#             st.session_state.chat_history.append({"role": "ai", "content": ans})
#             st.rerun()
#     st.stop()

# # ─────────────────────────────────────────────
# # TABS (Persian labels, but metric names in English)
# # ─────────────────────────────────────────────
# tabs = st.tabs(["Dashboard", "Data Analysis", "Pathology", "Insights", "Chat", "Export"])

# # ---------- TAB 1: DASHBOARD ----------
# with tabs[0]:
#     health_color = "#10B981" if health >= 70 else "#F59E0B" if health >= 45 else "#EF4444"
#     health_label = "Excellent" if health >= 70 else "Moderate" if health >= 45 else "Critical"
#     st.markdown(f"""
#     <div class="health-hero">
#         <div>
#             <div class="health-score" style="color:{health_color};">{health:.0f}</div>
#             <div class="health-label">Health Score</div>
#         </div>
#         <div style="text-align:right;">
#             <div style="font-weight:500;">{health_label}</div>
#             <div class="health-label">Based on ROI, conversion, issues</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown(f'<div class="metric-card"><div class="metric-value">{money(kpis.get("total_revenue"))}</div><div class="metric-label">Revenue</div></div>', unsafe_allow_html=True)
#     with col2:
#         st.markdown(f'<div class="metric-card"><div class="metric-value">{pct(kpis.get("conversion_rate"))}</div><div class="metric-label">Conversion Rate</div></div>', unsafe_allow_html=True)
#     with col3:
#         st.markdown(f'<div class="metric-card"><div class="metric-value">{pct(kpis.get("roi"))}</div><div class="metric-label">ROI</div></div>', unsafe_allow_html=True)
#     with col4:
#         st.markdown(f'<div class="metric-card"><div class="metric-value">{money(kpis.get("average_deal_size"))}</div><div class="metric-label">Avg. Deal Size</div></div>', unsafe_allow_html=True)

#     st.markdown(f'<div class="card"><div style="font-weight:500; margin-bottom:0.3rem;">Executive Summary</div><div style="font-size:0.85rem; color:#C1C1D0;">{verdict}</div></div>', unsafe_allow_html=True)

#     with st.expander("View all metrics"):
#         a1, a2, a3 = st.columns(3)
#         a1.metric("Leads", f"{sv(kpis,'total_leads',0):,}")
#         a1.metric("Closed Deals", f"{sv(kpis,'total_closed_deals',0):,}")
#         a2.metric("Win Rate", pct(kpis.get('win_rate')))
#         a2.metric("Marketing Cost", money(kpis.get('marketing_cost')))
#         a3.metric("CAC", money(kpis.get('cac')))
#         a3.metric("MoM Growth", f"{sv(adv,'mom_growth',0):+.1f}%")

# # ---------- TAB 2: DATA ANALYSIS ----------
# with tabs[1]:
#     if funnel_d:
#         st.subheader("Sales Funnel")
#         stages = ["Leads", "Qualified", "Demo", "Proposal", "Closed"]
#         values = [sv(kpis,"total_leads",0), sv(kpis,"total_qualified_leads",0), sv(kpis,"total_demos",0), sv(kpis,"total_proposals",0), sv(kpis,"total_closed_deals",0)]
#         fig = go.Figure(go.Funnel(y=stages, x=values, textinfo="value+percent initial", marker={"color": "#2563EB"}))
#         fig.update_layout(**PLOTLY_DARK, height=400)
#         st.plotly_chart(fig, use_container_width=True)

#     if monthly:
#         st.subheader("Monthly Trends")
#         df = pd.DataFrame(monthly)
#         c1, c2 = st.columns(2)
#         with c1:
#             fig1 = px.bar(df, x="date", y="revenue", title="Revenue", color_discrete_sequence=["#2563EB"])
#             fig1.update_layout(**PLOTLY_DARK)
#             st.plotly_chart(fig1, use_container_width=True)
#         with c2:
#             fig2 = px.line(df, x="date", y="closed", markers=True, title="Closed Deals", color_discrete_sequence=["#10B981"])
#             fig2.update_layout(**PLOTLY_DARK)
#             st.plotly_chart(fig2, use_container_width=True)

#     if prod_data:
#         st.subheader("Product Performance")
#         df = pd.DataFrame(prod_data)
#         fig = px.bar(df, x="product", y="revenue", color="product", title="Revenue by Product")
#         fig.update_layout(**PLOTLY_DARK, showlegend=False)
#         st.plotly_chart(fig, use_container_width=True)

#     if src_data:
#         st.subheader("Marketing Channels")
#         df = pd.DataFrame(src_data)
#         fig = px.bar(df, x="lead_source", y="revenue", color="lead_source", title="Revenue by Channel")
#         fig.update_layout(**PLOTLY_DARK, showlegend=False)
#         st.plotly_chart(fig, use_container_width=True)

#     if rep_data:
#         st.subheader("Sales Rep Performance")
#         df = pd.DataFrame(rep_data)
#         fig = px.bar(df, x="sales_rep", y="revenue", color="sales_rep", title="Revenue by Rep")
#         fig.update_layout(**PLOTLY_DARK, showlegend=False)
#         st.plotly_chart(fig, use_container_width=True)

#     if reg_data:
#         st.subheader("Regional Breakdown")
#         df = pd.DataFrame(reg_data)
#         fig = px.pie(df, names="region", values="revenue", title="Revenue by Region", hole=0.4)
#         fig.update_layout(**PLOTLY_DARK)
#         st.plotly_chart(fig, use_container_width=True)

# # ---------- TAB 3: PATHOLOGY ----------
# with tabs[2]:
#     if issues:
#         st.subheader("Critical Issues")
#         for issue in issues:
#             cls = "issue-critical" if issue.get("severity")=="critical" else "issue-warning"
#             badge_cls = "badge-critical" if issue.get("severity")=="critical" else "badge-warning"
#             sev_text = "CRITICAL" if issue.get("severity")=="critical" else "WARNING"
#             st.markdown(f"""
#             <div class="issue-card {cls}">
#                 <div class="badge {badge_cls}">{sev_text}</div>
#                 <div class="issue-title">{issue.get('title','')}</div>
#                 <div class="issue-metric">Metric: {issue.get('metric','')}</div>
#                 <div class="issue-impact">{issue.get('impact','')}</div>
#             </div>
#             """, unsafe_allow_html=True)
#     if sub_issues:
#         st.subheader("Sub‑Issues")
#         for issue in sub_issues:
#             st.markdown(f"""
#             <div class="issue-card issue-warning">
#                 <div class="badge badge-warning">WARNING</div>
#                 <div class="issue-title">{issue.get('title','')}</div>
#                 <div class="issue-metric">Metric: {issue.get('metric','')}</div>
#                 <div class="issue-impact">{issue.get('impact','')}</div>
#             </div>
#             """, unsafe_allow_html=True)

#     if issue_chart:
#         st.subheader("Issue Frequency")
#         df = pd.DataFrame(issue_chart)
#         colors = ["#EF4444" if s=="critical" else "#F59E0B" for s in df["severity"]]
#         fig = go.Figure(go.Bar(x=df["count"], y=df["name"], orientation="h", marker_color=colors, text=df["count"], textposition="outside"))
#         fig.update_layout(**PLOTLY_DARK, height=400)
#         st.plotly_chart(fig, use_container_width=True)

#     if not issues and not sub_issues:
#         st.success("✅ No major issues detected.")

# # ---------- TAB 4: INSIGHTS ----------
# with tabs[3]:
#     if insights:
#         st.subheader("Key Insights")
#         for ins in insights:
#             st.markdown(f'<div class="insight-text">• {ins}</div>', unsafe_allow_html=True)

#     if recs:
#         st.subheader("Recommendations")
#         c1, c2, c3 = st.columns(3)
#         with c1:
#             st.markdown('<div class="rec-section"><div class="rec-header">Short‑term</div>', unsafe_allow_html=True)
#             for item in recs.get("short_term", []):
#                 st.markdown(f'<div class="rec-item rec-short">{item}</div>', unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)
#         with c2:
#             st.markdown('<div class="rec-section"><div class="rec-header">Mid‑term</div>', unsafe_allow_html=True)
#             for item in recs.get("mid_term", []):
#                 st.markdown(f'<div class="rec-item rec-mid">{item}</div>', unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)
#         with c3:
#             st.markdown('<div class="rec-section"><div class="rec-header">Long‑term</div>', unsafe_allow_html=True)
#             for item in recs.get("long_term", []):
#                 st.markdown(f'<div class="rec-item rec-long">{item}</div>', unsafe_allow_html=True)
#             st.markdown('</div>', unsafe_allow_html=True)

#     if ai_report:
#         st.subheader("AI Executive Report")
#         st.markdown(f'<div class="card" style="white-space:pre-wrap;">{ai_report}</div>', unsafe_allow_html=True)

#     st.subheader("Final Verdict")
#     vcolor = "#10B981" if health>=70 else "#F59E0B" if health>=45 else "#EF4444"
#     st.markdown(f'<div class="card" style="border-right:4px solid {vcolor};">{verdict}</div>', unsafe_allow_html=True)

# # ---------- TAB 5: CHAT ----------
# with tabs[4]:
#     st.subheader("AI Assistant")
#     chat_container = st.container()
#     with chat_container:
#         st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#         if not st.session_state.chat_history:
#             st.markdown('<div class="chat-ai"><div class="chat-label">AI</div>Ask me about your business data. Example: "What is causing low conversion?"</div>', unsafe_allow_html=True)
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 st.markdown(f'<div class="chat-user"><div class="chat-label">You</div>{msg["content"]}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="chat-ai"><div class="chat-label">AI</div>{msg["content"]}</div>', unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     with st.form("chat_form", clear_on_submit=True):
#         q = st.text_input("Your question:", placeholder="e.g., How can I improve ROI?", label_visibility="collapsed")
#         if st.form_submit_button("Send", use_container_width=True) and q.strip():
#             st.session_state.chat_history.append({"role": "user", "content": q})
#             with st.spinner("Thinking..."):
#                 try:
#                     ctx = json.dumps({"kpis": kpis, "advanced_analysis": adv, "funnel": funnel_d}, ensure_ascii=False)[:4000]
#                     r = requests.post(API_CHAT, data={"question": q, "analysis_json": ctx, "raw_text": st.session_state.raw_text[:2000]}, timeout=60)
#                     ans = r.json().get("answer", "No response") if r.status_code == 200 else "Error"
#                 except Exception as e:
#                     ans = f"Error: {e}"
#             st.session_state.chat_history.append({"role": "ai", "content": ans})
#             st.rerun()

# # ---------- TAB 6: EXPORT ----------
# with tabs[5]:
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Download Excel Report", use_container_width=True):
#             with st.spinner("Generating..."):
#                 try:
#                     export_payload = {
#                         "kpis": kpis,
#                         "monthly_trend": monthly,
#                         "source_analysis": src_data,
#                         "rep_analysis": rep_data,
#                         "product_analysis": prod_data,
#                         "advanced_analysis": adv,
#                     }
#                     r = requests.post(API_EXPORT, data={"analysis_json": json.dumps(export_payload, ensure_ascii=False)}, timeout=60)
#                     if r.status_code == 200:
#                         st.download_button("Save file", data=r.content, file_name=f"bizdiag_report_{uploaded.name}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#                     else:
#                         st.error("Export failed")
#                 except Exception as e:
#                     st.error(f"Error: {e}")
#     with col2:
#         show_raw = st.checkbox("Show raw data", value=False)
#         if show_raw and sample:
#             st.subheader("Data Sample")
#             st.dataframe(pd.DataFrame(sample), use_container_width=True)

"""
BizDiag — Business Diagnostics
Redesigned UI: Minimal Dark · DM Sans + DM Mono · Indigo Accent · No Sidebar
"""

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="BizDiag",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# HIDE SIDEBAR
# ─────────────────────────────────────────────
st.markdown("""
<style>
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stSidebarCollapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)

API_BASE   = "http://127.0.0.1:8000"
API_ANALYZE = f"{API_BASE}/analyze"
API_HEALTH  = f"{API_BASE}/health"
API_CHAT    = f"{API_BASE}/chat"
API_EXPORT  = f"{API_BASE}/export/excel"

# ─────────────────────────────────────────────
# CSS — Redesigned Dark Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after {
    font-family: 'DM Sans', sans-serif;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, .stApp {
    background-color: #080810;
    color: #E8E8F0;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2A2A3A; border-radius: 99px; }

/* ── Topbar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2rem;
}
.logo {
    display: flex;
    align-items: center;
    gap: 10px;
}
.logo-mark {
    width: 30px;
    height: 30px;
    background: #4F46E5;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.logo-name {
    font-size: 15px;
    font-weight: 500;
    letter-spacing: -0.01em;
    color: #E8E8F0;
}
.chip {
    background: #12121E;
    border: 0.5px solid #2A2A3A;
    border-radius: 99px;
    padding: 4px 12px;
    font-size: 11px;
    color: #9090A8;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}
.chip.live::before {
    content: '';
    display: inline-block;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #10B981;
}

/* ── Upload Zone ── */
[data-testid="stFileUploadDropzone"] {
    background: #0D0D18 !important;
    border: 1px dashed #2A2A3A !important;
    border-radius: 16px !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploadDropzone"]:hover {
    border-color: #4F46E5 !important;
}

/* ── Health Hero ── */
.health-hero {
    display: grid;
    grid-template-columns: auto 1px 1fr auto;
    align-items: center;
    gap: 20px;
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.health-num {
    font-family: 'DM Mono', monospace;
    font-size: 42px;
    font-weight: 500;
    color: #A78BFA;
    letter-spacing: -0.03em;
    line-height: 1;
}
.health-divider {
    height: 44px;
    background: #1E1E2E;
    width: 1px;
}
.health-section-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #5A5A72;
    margin-bottom: 5px;
}
.health-verdict-text {
    font-size: 13px;
    color: #C8C8DC;
    line-height: 1.6;
}
.health-badge {
    background: #1A143A;
    border: 0.5px solid #3D3270;
    border-radius: 6px;
    padding: 5px 12px;
    font-size: 11px;
    color: #A78BFA;
    white-space: nowrap;
}
.health-badge.critical {
    background: #2A1010;
    border-color: #5A2020;
    color: #F87171;
}
.health-badge.moderate {
    background: #2A1E10;
    border-color: #5A3A10;
    color: #FBBF24;
}

/* ── KPI Grid ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 16px;
}
.kpi-card {
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 12px;
    padding: 16px;
}
.kpi-val {
    font-family: 'DM Mono', monospace;
    font-size: 22px;
    font-weight: 500;
    color: #E8E8F0;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}
.kpi-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #5A5A72;
}
.kpi-delta {
    font-size: 11px;
    margin-top: 6px;
}
.kpi-delta.up   { color: #4ADE80; }
.kpi-delta.down { color: #F87171; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background: transparent;
    border-bottom: 0.5px solid #1E1E2E;
    margin-bottom: 20px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #5A5A72;
    font-weight: 400;
    font-size: 12px;
    padding: 8px 16px;
    border-radius: 0;
    transition: color 0.2s;
}
.stTabs [aria-selected="true"] {
    color: #E8E8F0;
    border-bottom: 1.5px solid #4F46E5;
    background: transparent;
}

/* ── Cards ── */
.card {
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 14px;
    padding: 18px;
}
.card-title {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #5A5A72;
    margin-bottom: 14px;
}

/* ── Funnel Bars ── */
.funnel-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 5px;
}
.funnel-label {
    font-size: 11px;
    color: #9090A8;
    width: 76px;
    text-align: right;
    flex-shrink: 0;
}
.funnel-bar-wrap {
    flex: 1;
    height: 26px;
    background: #12121E;
    border-radius: 4px;
    overflow: hidden;
}
.funnel-bar {
    height: 100%;
    border-radius: 4px;
    display: flex;
    align-items: center;
    padding-left: 10px;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    color: #E8E8F0;
}
.funnel-pct {
    font-size: 10px;
    color: #5A5A72;
    width: 34px;
    text-align: left;
    flex-shrink: 0;
    font-family: 'DM Mono', monospace;
}

/* ── Issue Cards ── */
.issue-card {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 12px;
    background: #12121E;
    border: 0.5px solid #1E1E2E;
    border-radius: 10px;
    margin-bottom: 8px;
}
.issue-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    margin-top: 4px;
    flex-shrink: 0;
}
.issue-dot.critical { background: #F87171; }
.issue-dot.warning  { background: #FBBF24; }
.issue-name {
    font-size: 12px;
    color: #D8D8EC;
    margin-bottom: 3px;
    font-weight: 500;
}
.issue-desc {
    font-size: 11px;
    color: #6A6A82;
    line-height: 1.5;
}
.mini-tag {
    display: inline-block;
    background: #1A1A2A;
    border: 0.5px solid #2A2A3A;
    border-radius: 4px;
    padding: 1px 6px;
    font-size: 10px;
    color: #9090A8;
    font-family: 'DM Mono', monospace;
    margin-left: 4px;
    font-weight: 400;
}

/* ── Insights ── */
.insight-item {
    padding: 9px 0;
    border-bottom: 0.5px solid #1A1A2A;
    font-size: 12px;
    color: #B0B0C8;
    line-height: 1.6;
    display: flex;
    gap: 8px;
}
.insight-item:last-child { border-bottom: none; }
.insight-arrow {
    color: #4F46E5;
    font-family: 'DM Mono', monospace;
    flex-shrink: 0;
    margin-top: 1px;
}

/* ── Recommendations ── */
.rec-cols {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}
.rec-col-title {
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #5A5A72;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}
.rec-col-title::before {
    content: '';
    display: inline-block;
    width: 5px;
    height: 5px;
    border-radius: 50%;
}
.rec-short .rec-col-title::before { background: #F87171; }
.rec-mid   .rec-col-title::before { background: #FBBF24; }
.rec-long  .rec-col-title::before { background: #4ADE80; }
.rec-item-row {
    font-size: 11px;
    color: #B0B0C8;
    padding: 6px 0;
    border-bottom: 0.5px solid #1A1A2A;
    line-height: 1.5;
}
.rec-item-row:last-child { border-bottom: none; }

/* ── Chat ── */
.chat-container {
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 14px;
    overflow: hidden;
}
.chat-msgs {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-height: 420px;
    overflow-y: auto;
    min-height: 160px;
}
.bubble {
    padding: 10px 14px;
    font-size: 12px;
    line-height: 1.6;
    max-width: 82%;
}
.bubble.ai {
    background: #12121E;
    border: 0.5px solid #1E1E2E;
    border-radius: 12px 12px 12px 3px;
    color: #C8C8DC;
    align-self: flex-start;
}
.bubble.user {
    background: #1A1466;
    border: 0.5px solid #2D2080;
    border-radius: 12px 12px 3px 12px;
    color: #D8D8EC;
    align-self: flex-end;
}
.bubble-label {
    font-size: 9px;
    color: #5A5A72;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ── Export Buttons ── */
.export-btn-wrap {
    display: flex;
    gap: 10px;
}

/* ── Buttons override ── */
.stButton > button {
    background: #0D0D18;
    color: #D8D8EC;
    border: 0.5px solid #2A2A3A;
    border-radius: 10px;
    font-weight: 400;
    font-size: 12px;
    padding: 10px 16px;
    transition: border-color 0.2s;
}
.stButton > button:hover {
    background: #12121E;
    border-color: #4F46E5;
}
.stButton > button:focus {
    box-shadow: none;
    border-color: #4F46E5;
}

/* ── Text inputs ── */
.stTextInput > div > div > input {
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 8px;
    color: #E8E8F0;
    font-size: 12px;
}
.stTextInput > div > div > input:focus {
    border-color: #4F46E5;
    box-shadow: none;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #0D0D18;
    border: 0.5px solid #1E1E2E;
    border-radius: 10px;
    color: #9090A8;
    font-size: 12px;
}

/* ── Success / Info ── */
.stSuccess, .stInfo {
    background: #0F1A0F;
    border: 0.5px solid #1A3A1A;
    border-radius: 10px;
    color: #4ADE80;
    font-size: 12px;
}

/* ── Plotly tweaks ── */
.js-plotly-plot .plotly .modebar { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def money(v):
    try:
        return f"{float(v):,.0f}"
    except:
        return "0"

def pct(v):
    try:
        return f"{float(v):.1f}%"
    except:
        return "0%"

def sv(d, key, default=0):
    try:
        return d.get(key, default) if d else default
    except:
        return default

def health_class(score):
    if score >= 70:
        return "good"
    elif score >= 45:
        return "moderate"
    return "critical"

def health_label(score):
    if score >= 70:
        return "Good"
    elif score >= 45:
        return "Moderate"
    return "Critical"

# ─────────────────────────────────────────────
# PLOTLY DARK CONFIG
# ─────────────────────────────────────────────
PLOTLY_DARK = {
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor":  "rgba(0,0,0,0)",
    "font": {"family": "DM Sans", "color": "#9090A8", "size": 11},
    "margin": {"l": 16, "r": 16, "t": 32, "b": 16},
    "xaxis": {"gridcolor": "#1E1E2E", "zerolinecolor": "#1E1E2E", "tickfont": {"size": 10}},
    "yaxis": {"gridcolor": "#1E1E2E", "zerolinecolor": "#1E1E2E", "tickfont": {"size": 10}},
    "legend": {"bgcolor": "rgba(0,0,0,0)", "font": {"size": 10}},
    "colorway": ["#4F46E5", "#7C6FEB", "#A78BFA", "#C4B5FD", "#6358E8"],
}

# ─────────────────────────────────────────────
# BACKEND CHECK
# ─────────────────────────────────────────────
try:
    h = requests.get(API_HEALTH, timeout=4)
    if h.status_code != 200:
        st.error("❌ Backend not reachable. Run: uvicorn main:app --reload")
        st.stop()
    ai_ok = h.json().get("groq_enabled", False)
except:
    st.error("❌ Connection failed.")
    st.stop()

# ─────────────────────────────────────────────
# TOPBAR
# ─────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="logo">
    <div class="logo-mark">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"
           xmlns="http://www.w3.org/2000/svg">
        <polyline points="2,10 5,6 8,8 12,3"
                  stroke="#ffffff" stroke-width="2"
                  stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <span class="logo-name">BizDiag</span>
  </div>
  <div style="display:flex;gap:8px;align-items:center;">
    <span class="chip live">AI online</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FILE UPLOAD
# ─────────────────────────────────────────────
uploaded = st.file_uploader(
    "Upload CSV, Excel, PDF, Word, or TXT",
    type=["csv", "xlsx", "xls", "pdf", "docx", "doc", "txt"],
    label_visibility="collapsed",
)

if not uploaded:
    st.markdown("""
    <div style="text-align:center;padding:3rem 2rem;background:#0D0D18;
                border:1px dashed #2A2A3A;border-radius:16px;margin-top:1rem;">
        <div style="width:40px;height:40px;background:#12121E;border-radius:10px;
                    display:flex;align-items:center;justify-content:center;margin:0 auto 12px;">
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none"
                 stroke="#5A5A72" stroke-width="1.5" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 12V4M6 7l3-3 3 3M3 14h12"/>
            </svg>
        </div>
        <p style="color:#5A5A72;font-size:13px;">Drop a file to start analysis</p>
        <p style="color:#3A3A52;font-size:11px;margin-top:4px;">CSV · Excel · PDF · Word · TXT</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

st.markdown(f"""
<div style="display:inline-flex;align-items:center;gap:6px;background:#0F1A0F;
            border:0.5px solid #1A3A1A;border-radius:8px;padding:6px 12px;
            margin-bottom:16px;font-size:12px;color:#4ADE80;">
    <svg width="13" height="13" viewBox="0 0 13 13" fill="none"
         stroke="#4ADE80" stroke-width="2" xmlns="http://www.w3.org/2000/svg">
        <path d="M2 2h6l3 3v7H2V2z"/><path d="M8 2v3h3"/>
    </svg>
    {uploaded.name} · loaded
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "analysis_data"     not in st.session_state: st.session_state.analysis_data     = None
if "analysis_filename" not in st.session_state: st.session_state.analysis_filename = None
if "chat_history"      not in st.session_state: st.session_state.chat_history      = []
if "raw_text"          not in st.session_state: st.session_state.raw_text          = ""

if st.session_state.analysis_filename != uploaded.name:
    with st.spinner("Analyzing…"):
        try:
            ext = uploaded.name.split(".")[-1].lower()
            mime_map = {
                "csv":  "text/csv",
                "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "xls":  "application/vnd.ms-excel",
                "pdf":  "application/pdf",
                "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "doc":  "application/msword",
                "txt":  "text/plain",
            }
            uploaded.seek(0)
            resp = requests.post(
                API_ANALYZE,
                files={"file": (uploaded.name, uploaded.getvalue(), mime_map.get(ext, "application/octet-stream"))},
                timeout=300,
            )
            if resp.status_code == 200:
                data = resp.json()
                st.session_state.analysis_data     = data
                st.session_state.analysis_filename = uploaded.name
                st.session_state.raw_text          = data.get("raw_text", "")
                st.session_state.chat_history      = []
            else:
                st.error(f"Backend error: {resp.status_code}")
                st.stop()
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

data = st.session_state.analysis_data
if not data or not data.get("success"):
    st.error(data.get("error", "Unknown error"))
    st.stop()

# ─────────────────────────────────────────────
# EXTRACT DATA
# ─────────────────────────────────────────────
kpis      = data.get("kpis", {})
adv       = data.get("advanced_analysis", {})
ai_report = data.get("ai_report", "")
funnel_d  = data.get("funnel", {})
src_data  = data.get("source_analysis", [])
rep_data  = data.get("rep_analysis", [])
monthly   = data.get("monthly_trend", [])
prod_data = data.get("product_analysis", [])
reg_data  = data.get("region_analysis", [])
issues    = adv.get("main_issues", [])
sub_issues= adv.get("sub_issues", [])
insights  = adv.get("insights", [])
recs      = adv.get("recommendations", {})
issue_chart=adv.get("issue_chart_data", [])
health    = adv.get("health_score", 50)
verdict   = adv.get("final_verdict", "")
mode      = data.get("mode", "tabular")
sample    = data.get("sample_data", [])

# ─────────────────────────────────────────────
# TEXT-ONLY MODE
# ─────────────────────────────────────────────
if mode == "text_only":
    st.info("Text file uploaded — AI summary and chat available.")
    if data.get("ai_summary"):
        st.markdown("### AI Summary")
        st.write(data["ai_summary"])
    with st.expander("File content"):
        st.text(data.get("raw_text", "")[:3000])

    st.markdown('<div class="card"><div class="card-title">Chat</div>', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        role_cls = "user" if msg["role"] == "user" else "ai"
        label    = "You" if msg["role"] == "user" else "AI Assistant"
        st.markdown(f'<div class="bubble {role_cls}"><div class="bubble-label">{label}</div>{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.form("chat_text", clear_on_submit=True):
        q = st.text_input("Your question:", label_visibility="collapsed", placeholder="Ask about the document…")
        if st.form_submit_button("Send") and q.strip():
            st.session_state.chat_history.append({"role": "user", "content": q})
            with st.spinner("Thinking…"):
                try:
                    resp = requests.post(API_CHAT, data={"question": q, "analysis_json": "{}", "raw_text": st.session_state.raw_text[:2000]}, timeout=60)
                    ans = resp.json().get("answer", "Error") if resp.status_code == 200 else "Error"
                except:
                    ans = "Connection error"
            st.session_state.chat_history.append({"role": "ai", "content": ans})
            st.rerun()
    st.stop()

# ─────────────────────────────────────────────
# HEALTH HERO
# ─────────────────────────────────────────────
h_cls   = health_class(health)
h_label = health_label(health)
h_color_map = {"good": "#A78BFA", "moderate": "#FBBF24", "critical": "#F87171"}
h_num_color = h_color_map.get(h_cls, "#A78BFA")

st.markdown(f"""
<div class="health-hero">
  <div>
    <div class="health-section-label">Health Score</div>
    <div class="health-num" style="color:{h_num_color};">{health:.0f}</div>
  </div>
  <div class="health-divider"></div>
  <div style="flex:1;">
    <div class="health-section-label">Executive Summary</div>
    <div class="health-verdict-text">{verdict}</div>
  </div>
  <div>
    <span class="health-badge {h_cls}">{h_label}</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# KPI GRID
# ─────────────────────────────────────────────
mom = sv(adv, "mom_growth", 0)
mom_cls = "up" if mom >= 0 else "down"
mom_arrow = "↑" if mom >= 0 else "↓"

st.markdown(f"""
<div class="kpi-grid">
  <div class="kpi-card">
    <div class="kpi-val">{money(kpis.get("total_revenue"))}</div>
    <div class="kpi-label">Revenue</div>
    <div class="kpi-delta {mom_cls}">{mom_arrow} {abs(mom):.1f}% MoM</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-val">{pct(kpis.get("conversion_rate"))}</div>
    <div class="kpi-label">Conversion Rate</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-val">{pct(kpis.get("roi"))}</div>
    <div class="kpi-label">ROI</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-val">{money(kpis.get("average_deal_size"))}</div>
    <div class="kpi-label">Avg. Deal Size</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tabs = st.tabs(["Dashboard", "Data Analysis", "Pathology", "Insights", "Chat", "Export"])

# ══════════════════════════════════════════════
# TAB 1 — DASHBOARD
# ══════════════════════════════════════════════
with tabs[0]:
    col1, col2 = st.columns(2, gap="small")

    # Funnel
    with col1:
        st.markdown('<div class="card"><div class="card-title">Sales Funnel</div>', unsafe_allow_html=True)
        stages = [
            ("Leads",    sv(kpis, "total_leads", 0)),
            ("Qualified",sv(kpis, "total_qualified_leads", 0)),
            ("Demo",     sv(kpis, "total_demos", 0)),
            ("Proposal", sv(kpis, "total_proposals", 0)),
            ("Closed",   sv(kpis, "total_closed_deals", 0)),
        ]
        top = stages[0][1] or 1
        colors = ["#4F46E5", "#6358E8", "#7C6FEB", "#9689EE", "#B0A3F1"]
        for i, (label, val) in enumerate(stages):
            w = int(val / top * 100)
            st.markdown(f"""
            <div class="funnel-row">
              <div class="funnel-label">{label}</div>
              <div class="funnel-bar-wrap">
                <div class="funnel-bar" style="width:{w}%;background:{colors[i]};">{int(val):,}</div>
              </div>
              <div class="funnel-pct">{w}%</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Monthly chart
    with col2:
        if monthly:
            df = pd.DataFrame(monthly)
            fig = px.bar(
                df, x="date", y="revenue",
                title="Monthly Revenue",
                color_discrete_sequence=["#4F46E5"],
            )
            fig.update_traces(marker_line_width=0, opacity=0.9)
            fig.update_layout(**PLOTLY_DARK, height=240, title_font_size=11)
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    # All metrics expander
    with st.expander("All metrics"):
        a1, a2, a3 = st.columns(3)
        a1.metric("Leads",        f"{sv(kpis,'total_leads',0):,}")
        a1.metric("Closed Deals", f"{sv(kpis,'total_closed_deals',0):,}")
        a2.metric("Win Rate",     pct(kpis.get("win_rate")))
        a2.metric("Marketing Cost", money(kpis.get("marketing_cost")))
        a3.metric("CAC",          money(kpis.get("cac")))
        a3.metric("MoM Growth",   f"{sv(adv,'mom_growth',0):+.1f}%")

# ══════════════════════════════════════════════
# TAB 2 — DATA ANALYSIS
# ══════════════════════════════════════════════
with tabs[1]:
    if src_data or rep_data:
        c1, c2 = st.columns(2, gap="small")
        if src_data:
            with c1:
                df = pd.DataFrame(src_data)
                fig = px.bar(df, x="revenue", y="lead_source", orientation="h",
                             title="Revenue by Channel", color_discrete_sequence=["#4F46E5"])
                fig.update_layout(**PLOTLY_DARK, height=260, title_font_size=11)
                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        if rep_data:
            with c2:
                df = pd.DataFrame(rep_data)
                fig = px.bar(df, x="revenue", y="sales_rep", orientation="h",
                             title="Revenue by Rep", color_discrete_sequence=["#7C6FEB"])
                fig.update_layout(**PLOTLY_DARK, height=260, title_font_size=11)
                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    if monthly:
        df = pd.DataFrame(monthly)
        c1, c2 = st.columns(2, gap="small")
        with c1:
            fig = px.line(df, x="date", y="closed", markers=True,
                          title="Closed Deals Trend", color_discrete_sequence=["#A78BFA"])
            fig.update_traces(line_width=2, marker_size=5)
            fig.update_layout(**PLOTLY_DARK, height=220, title_font_size=11)
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        with c2:
            if prod_data:
                df2 = pd.DataFrame(prod_data)
                fig = px.bar(df2, x="product", y="revenue",
                             title="Revenue by Product", color_discrete_sequence=["#6358E8"])
                fig.update_layout(**PLOTLY_DARK, height=220, title_font_size=11, showlegend=False)
                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    if reg_data:
        df = pd.DataFrame(reg_data)
        fig = px.pie(df, names="region", values="revenue",
                     title="Revenue by Region", hole=0.5,
                     color_discrete_sequence=["#4F46E5","#6358E8","#7C6FEB","#9689EE","#B0A3F1"])
        fig.update_layout(**PLOTLY_DARK, height=280, title_font_size=11)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ══════════════════════════════════════════════
# TAB 3 — PATHOLOGY
# ══════════════════════════════════════════════
with tabs[2]:
    if not issues and not sub_issues:
        st.success("✅ No major issues detected.")
    else:
        if issues:
            st.markdown('<div class="card"><div class="card-title">Critical Issues</div>', unsafe_allow_html=True)
            for issue in issues:
                sev = issue.get("severity", "warning")
                dot_cls = "critical" if sev == "critical" else "warning"
                st.markdown(f"""
                <div class="issue-card">
                  <div class="issue-dot {dot_cls}"></div>
                  <div>
                    <div class="issue-name">{issue.get('title','')}
                      <span class="mini-tag">{issue.get('metric','')}</span>
                    </div>
                    <div class="issue-desc">{issue.get('impact','')}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if sub_issues:
            st.markdown('<br>', unsafe_allow_html=True)
            st.markdown('<div class="card"><div class="card-title">Sub-Issues</div>', unsafe_allow_html=True)
            for issue in sub_issues:
                st.markdown(f"""
                <div class="issue-card">
                  <div class="issue-dot warning"></div>
                  <div>
                    <div class="issue-name">{issue.get('title','')}
                      <span class="mini-tag">{issue.get('metric','')}</span>
                    </div>
                    <div class="issue-desc">{issue.get('impact','')}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    if issue_chart:
        df = pd.DataFrame(issue_chart)
        colors = ["#F87171" if s == "critical" else "#FBBF24" for s in df["severity"]]
        fig = go.Figure(go.Bar(
            x=df["count"], y=df["name"], orientation="h",
            marker_color=colors, text=df["count"], textposition="outside",
        ))
        fig.update_layout(**PLOTLY_DARK, height=320, title="Issue Frequency", title_font_size=11)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ══════════════════════════════════════════════
# TAB 4 — INSIGHTS
# ══════════════════════════════════════════════
with tabs[3]:
    col1, col2 = st.columns(2, gap="small")

    with col1:
        if insights:
            st.markdown('<div class="card"><div class="card-title">Key Insights</div>', unsafe_allow_html=True)
            for ins in insights:
                st.markdown(f'<div class="insight-item"><span class="insight-arrow">→</span>{ins}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if recs:
            st.markdown('<div class="card"><div class="card-title">Recommendations</div><div class="rec-cols">', unsafe_allow_html=True)
            for col_cls, col_key, col_label in [
                ("rec-short", "short_term", "Short-term"),
                ("rec-mid",   "mid_term",   "Mid-term"),
                ("rec-long",  "long_term",  "Long-term"),
            ]:
                items = recs.get(col_key, [])
                rows  = "".join(f'<div class="rec-item-row">{item}</div>' for item in items)
                st.markdown(f"""
                <div class="{col_cls}">
                  <div class="rec-col-title">{col_label}</div>
                  {rows}
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div></div>', unsafe_allow_html=True)

    if ai_report:
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><div class="card-title">AI Executive Report</div>'
                    f'<div style="font-size:13px;color:#C8C8DC;line-height:1.7;white-space:pre-wrap;">{ai_report}</div></div>',
                    unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 5 — CHAT
# ══════════════════════════════════════════════
with tabs[4]:
    st.markdown('<div class="chat-container"><div class="chat-msgs">', unsafe_allow_html=True)

    if not st.session_state.chat_history:
        st.markdown(
            '<div class="bubble ai">'
            '<div class="bubble-label">AI Assistant</div>'
            'Ask anything about your business data. Example: "What is causing low conversion?"'
            '</div>',
            unsafe_allow_html=True,
        )

    for msg in st.session_state.chat_history:
        role_cls = "user" if msg["role"] == "user" else "ai"
        label    = "You" if msg["role"] == "user" else "AI Assistant"
        st.markdown(
            f'<div class="bubble {role_cls}">'
            f'<div class="bubble-label">{label}</div>'
            f'{msg["content"]}'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)  # close .chat-msgs

    with st.form("chat_form", clear_on_submit=True):
        q = st.text_input(
            "question",
            placeholder="e.g. How can I improve ROI?",
            label_visibility="collapsed",
        )
        if st.form_submit_button("Send", use_container_width=True) and q.strip():
            st.session_state.chat_history.append({"role": "user", "content": q})
            with st.spinner("Thinking…"):
                try:
                    ctx = json.dumps(
                        {"kpis": kpis, "advanced_analysis": adv, "funnel": funnel_d},
                        ensure_ascii=False,
                    )[:4000]
                    r = requests.post(
                        API_CHAT,
                        data={"question": q, "analysis_json": ctx,
                              "raw_text": st.session_state.raw_text[:2000]},
                        timeout=60,
                    )
                    ans = r.json().get("answer", "No response") if r.status_code == 200 else "Error"
                except Exception as e:
                    ans = f"Error: {e}"
            st.session_state.chat_history.append({"role": "ai", "content": ans})
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)  # close .chat-container

# ══════════════════════════════════════════════
# TAB 6 — EXPORT
# ══════════════════════════════════════════════
with tabs[5]:
    st.markdown('<div class="card"><div class="card-title">Export</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="small")

    with col1:
        if st.button("⬇  Download Excel Report", use_container_width=True):
            with st.spinner("Generating…"):
                try:
                    export_payload = {
                        "kpis": kpis,
                        "monthly_trend":    monthly,
                        "source_analysis":  src_data,
                        "rep_analysis":     rep_data,
                        "product_analysis": prod_data,
                        "advanced_analysis": adv,
                    }
                    r = requests.post(
                        API_EXPORT,
                        data={"analysis_json": json.dumps(export_payload, ensure_ascii=False)},
                        timeout=60,
                    )
                    if r.status_code == 200:
                        st.download_button(
                            "Save .xlsx",
                            data=r.content,
                            file_name=f"bizdiag_{uploaded.name}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        )
                    else:
                        st.error("Export failed.")
                except Exception as e:
                    st.error(f"Error: {e}")

    with col2:
        show_raw = st.checkbox("Show raw data sample", value=False)
        if show_raw and sample:
            st.dataframe(pd.DataFrame(sample), use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)