import streamlit as st
from utils.ui_utils import load_css

st.set_page_config(page_title="Business Impact | Intelligent Accident Monitoring System", page_icon="💼", layout="wide")
load_css()

st.markdown("""
# 💼 Business Impact
**AI-powered accident detection can transform road safety, emergency response, and traffic intelligence.**
""", unsafe_allow_html=True)

st.markdown("## Why this matters for cities")
st.write(
    "- Automated accident detection reduces response time and helps emergency teams reach the scene faster.\n"
    "- CCTV monitoring with AI enables traffic authorities to detect incidents without constant human supervision.\n"
    "- It supports smart city goals by integrating with control rooms, dispatch systems, and analytics dashboards."
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🚦 Road safety")
    st.write("AI detects high-risk collisions and alerts operators before secondary accidents happen.")
    st.markdown("### 🌐 Smart city")
    st.write("The system can feed into city dashboards, traffic management centers, and public safety applications.")
with col2:
    st.markdown("### ⏱️ Emergency response")
    st.write("Faster detection enables better ambulance routing, police dispatch, and on-scene coordination.")
    st.markdown("### 📈 Operational benefits")
    st.write("Automated monitoring improves coverage, reduces false positives, and creates actionable incident summaries.")

st.markdown("## Recommendation cards")
st.markdown(
    "<div class='grid-container'>"
    "<div class='glass-card'><h3>Improve CCTV coverage</h3><p>Deploy more cameras in high-risk intersections and highway segments.</p></div>"
    "<div class='glass-card'><h3>Integrate alerts</h3><p>Connect predictions to dispatch systems for faster emergency response.</p></div>"
    "<div class='glass-card'><h3>Use analytics</h3><p>Leverage detection logs for patterns, peak-hour accidents, and city planning.</p></div>"
    "</div>",
    unsafe_allow_html=True,
)

with st.expander("Future scope"):
    st.write(
        "Future enhancements include multi-camera fusion, motion-based video pipelines, and edge deployment for low-latency CCTV inference."
    )
