import streamlit as st
import pandas as pd
from utils.ui_utils import load_css
from utils.data_utils import get_dataset_summary, build_distribution_dataframe, load_sample_images

st.set_page_config(page_title="About Dataset | Intelligent Accident Monitoring System", page_icon="📁", layout="wide")
load_css()

summary = get_dataset_summary()
df_dist = build_distribution_dataframe(summary)

st.markdown("""
# 📦 About Dataset
**A balanced CCTV accident dataset designed for supervised CNN training.**
""", unsafe_allow_html=True)

st.markdown("## Dataset summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Images", summary["totals"]["images"])
col2.metric("Accident Samples", summary["totals"]["accidents"])
col3.metric("Non-Accident Samples", summary["totals"]["non_accidents"])
col4.metric("Classes", summary["totals"]["classes"])

st.markdown("## Class distribution")
st.dataframe(df_dist.style.background_gradient(cmap="Blues"), use_container_width=True)

with st.expander("Dataset details and preprocessing steps"):
    st.markdown(
        "- The dataset is arranged into `train`, `test`, and `val` folders with `Accident` and `Non Accident` labels.\n"
        "- Images are resized to 256x256 pixels and normalized to `[0, 1]` before inference.\n"
        "- Class balancing and augmentation reduce bias and improve model generalization.\n"
        "- CNNs are particularly effective for spatial pattern detection in traffic and CCTV imagery."
    )

st.markdown("## Sample images by class")
images = load_sample_images(n_samples=3)
if images:
    for label, paths in images.items():
        st.markdown(f"### {label}")
        cols = st.columns(min(len(paths), 3))
        for col, image_path in zip(cols, paths):
            with col:
                st.image(image_path, caption=label, use_column_width=True)
else:
    st.info("No sample images found. Confirm that the dataset directory is present.")

with st.expander("Why dataset balancing matters"):
    st.write(
        "Balanced datasets help the CNN learn both accident and non-accident patterns equally. If one class dominates, the model may produce misleading confidence scores and fail in real traffic scenarios."
    )

with st.expander("Why image augmentation is important"):
    st.write(
        "Augmentation creates synthetic variations by flipping, rotating, and zooming images. This mimics real CCTV conditions and reduces overfitting when the training set is limited."
    )

with st.expander("Why CNN is suitable for this task"):
    st.write(
        "CNNs capture edges, textures, and object shapes from image pixels. They excel in identifying accident-related features such as damaged vehicles, road debris, and unusual motion blur."
    )
