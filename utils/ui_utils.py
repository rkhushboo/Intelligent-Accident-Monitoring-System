import streamlit as st
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css_file:
            st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

def section_header(title: str, subtitle: str = None, icon: str = ""): 
    st.markdown(f"<div class='section-header'><h1>{icon} {title}</h1>{('<p>' + subtitle + '</p>') if subtitle else ''}</div>", unsafe_allow_html=True)

def render_hero_banner(summary, model_status):
    insurance_score = int(summary["totals"]["images"] / 10) if summary["totals"]["images"] else 0
    status = "Ready" if model_status["status"] == "loaded" else "Unavailable"
    st.markdown(
        "<div class='hero-card'>"
        "<div><h2>Modern AI accident detection for CCTV monitoring</h2>"
        "<p>Use this dashboard to upload images or CCTV clips, visualize prediction confidence, and explore model behavior with industry-level analytics.</p></div>"
        "<div class='hero-stats'>"
        "<div class='metric-box'><span>Total Images</span><strong>{}</strong></div>"
        "<div class='metric-box'><span>Accident Samples</span><strong>{}</strong></div>"
        "<div class='metric-box'><span>Non-Accident Samples</span><strong>{}</strong></div>"
        "<div class='metric-box'><span>Model Status</span><strong>{}</strong></div>"
        "</div></div>".format(
            summary["totals"]["images"],
            summary["totals"]["accidents"],
            summary["totals"]["non_accidents"],
            status,
        ),
        unsafe_allow_html=True,
    )

def render_impact_cards():
    st.markdown(
        "<div class='grid-container'>"
        "<div class='glass-card'><h3>🚨 Real-time alert ready</h3><p>Fast inference with a CNN architecture optimized for CCTV frames.</p></div>"
        "<div class='glass-card'><h3>📊 Business impact</h3><p>Designed for traffic surveillance, emergency response, and automated risk detection.</p></div>"
        "<div class='glass-card'><h3>🧠 AI-powered</h3><p>Uses deep learning confidence scores and explainable visuals to build trust.</p></div>"
        "</div>",
        unsafe_allow_html=True,
    )

def status_label(label: str, value: str, color: str = "#1abc9c"):
    st.markdown(
        f"<div class='status-chip' style='border-color:{color}; color:{color};'>{label}: {value}</div>", unsafe_allow_html=True
    )
