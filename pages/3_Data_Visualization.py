import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils.ui_utils import load_css
from utils.data_utils import get_dataset_summary, build_distribution_dataframe, load_sample_images
from PIL import Image

st.set_page_config(page_title="Data Visualization | Intelligent Accident Monitoring System", page_icon="📊", layout="wide")
load_css()

summary = get_dataset_summary()
df_dist = build_distribution_dataframe(summary)

st.markdown("""
# 📈 Data Visualization
**Explore dataset patterns, class balance, and image-level insights.**
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    fig_bar = px.bar(df_dist, x="Class", y="Images", color="Class", template="plotly_dark")
    fig_bar.update_layout(title="Train Set Class Distribution", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)
with col2:
    fig_pie = px.pie(df_dist, names="Class", values="Images", hole=0.45, template="plotly_dark")
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("## Sample image grid")
sample_images = load_sample_images(n_samples=4)
if sample_images:
    for label, paths in sample_images.items():
        st.markdown(f"### {label}")
        cols = st.columns(4)
        for col, path in zip(cols, paths):
            with col:
                st.image(path, use_column_width=True)
else:
    st.info("No sample images found for visualization.")

with st.expander("Pixel intensity visualization"):
    if sample_images:
        hist_data = []
        labels = []
        for label, paths in sample_images.items():
            for path in paths[:2]:
                image = Image.open(path).convert("L")
                hist_data.append(np.array(image).ravel())
                labels.append(label)
        fig = go.Figure()
        for intensity, label in zip(hist_data, labels):
            fig.add_trace(go.Histogram(x=intensity, name=label, opacity=0.7))
        fig.update_layout(barmode='overlay', title='Pixel intensity distribution', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Add sample images to enable pixel intensity charts.")

with st.expander("Image dimension analysis"):
    dims = []
    for split in ["train", "test", "val"]:
        for cls in summary.get(split, {}):
            cls_path = os.path.join("datasets/data", split, cls)
            if os.path.isdir(cls_path):
                for item in os.listdir(cls_path)[:40]:
                    try:
                        with Image.open(os.path.join(cls_path, item)) as img:
                            dims.append(img.size)
                    except Exception:
                        continue
    if dims:
        width, height = zip(*dims)
        fig = px.scatter(x=width, y=height, labels={"x":"Width", "y":"Height"}, title="Image resolution distribution", template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No images available to analyze dimensions.")

st.markdown("## Insights")
st.write(
    "- The distribution chart shows whether the training data is balanced across accident and non-accident examples.\n"
    "- Strong class balance helps the CNN learn both classes and improves confidence calibration.\n"
    "- Visualizing pixel histograms reveals whether accident images contain more high-contrast or low-light patterns."
)
