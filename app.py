import streamlit as st
from PIL import Image
import time

# ── 1. Page Configuration ──
st.set_page_config(
    page_title="Streamlit Demo on Hugging Face",
    page_icon="✦",
    layout="centered"
)

# ── 2. Editorial Minimalist Custom CSS ──
st.markdown("""
<style>
    /* Google Fonts Import: Inter & Plus Jakarta Sans */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Inter:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Editorial Headline Styling */
    .art-badge {
        display: inline-block;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #6366f1;
        background: rgba(99, 102, 241, 0.08);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 9999px;
        margin-bottom: 12px;
    }

    .art-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 2.35rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.2;
        background: linear-gradient(135deg, #0f172a 0%, #334155 45%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }

    .art-subtitle {
        font-size: 1.02rem;
        color: #64748b;
        font-weight: 400;
        line-height: 1.6;
        margin-bottom: 28px;
    }

    /* Polished File Uploader Container */
    [data-testid="stFileUploader"] {
        background: #fafafa;
        border: 1px dashed #cbd5e1;
        border-radius: 16px;
        padding: 16px;
        transition: all 0.25s ease-in-out;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #6366f1;
        background: #f8fafc;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.06);
    }

    /* Polished Minimalist Image Frame */
    [data-testid="stImage"] img {
        border-radius: 16px;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.08), 0 4px 12px -2px rgba(0, 0, 0, 0.03);
        border: 1px solid #f1f5f9;
    }

    /* Interactive Button Styling */
    .stButton > button {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 600;
        border-radius: 12px;
        padding: 10px 24px;
        border: 1px solid #e2e8f0;
        background: #ffffff;
        color: #0f172a;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .stButton > button:hover {
        border-color: #6366f1;
        color: #6366f1;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.15);
    }

    /* Feedback Banner */
    .success-pill {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
        padding: 14px 20px;
        border-radius: 12px;
        font-size: 0.95rem;
        font-weight: 600;
        margin-top: 14px;
        animation: fadeIn 0.4s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# ── 3. App Header & Description ──
st.markdown('<span class="art-badge">Showcase</span>', unsafe_allow_html=True)
st.markdown('<h1 class="art-title">Streamlit Demo on Hugging Face</h1>', unsafe_allow_html=True)
st.markdown('<p class="art-subtitle">Welcome to a demo app showcasing basic Streamlit components!</p>', unsafe_allow_html=True)

# ── 4. File Uploader for Image ──
uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# ── 5. Image Rendering with Custom Spinner ──
if uploaded_image is not None:
    with st.spinner("Processing visual render..."):
        time.sleep(1)  # Simulate a delay
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

st.write("")  # Whitespace balance

# ── 6. Button Interaction ──
if st.button("Click Me"):
    st.markdown('<div class="success-pill">🎉 You clicked the button!</div>', unsafe_allow_html=True)
