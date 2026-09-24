import streamlit as st
from PIL import Image
import time

# ── 1. 頁面設定（頂部標題、Icon 與寬度） ──
st.set_page_config(
    page_title="VisionStudio AI | Streamlit Demo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── 2. 注入精緻微 CSS：自訂主視覺漸層與陰影卡片效果 ──
st.markdown("""
<style>
    /* 標題漸層文字特效 */
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F6B, #6C5CE7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        color: #636e72;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── 3. 側邊欄（Sidebar）：放置說明與控制項 ──
with st.sidebar:
    st.image("https://huggingface.co/front/assets/huggingface_logo-noborder.svg", width=60)
    st.title("控制面板")
    st.caption("ISOM5240 • Streamlit Components Showcase")
    st.divider()
    
    st.markdown("### ⚙️ 系統狀態")
    st.success("🟢 伺服器運作正常 (Online)")
    
    # 互動小彩蛋
    st.divider()
    st.markdown("### 💡 關於本工具")
    st.info("本範例演示圖片非同步載入、動態進度條、雙欄版面排版以及即時互動元件。")

# ── 4. 主畫面橫幅（Hero Section） ──
st.markdown('<div class="hero-title">✨ VisionStudio AI Showcase</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">探索 Streamlit 現代化介面與互動元件的極致魅力</div>', unsafe_allow_html=True)

# ── 5. 雙欄排版佈局（Columns） ──
col_upload, col_preview = st.columns([1, 1], gap="large")

with col_upload:
    with st.container(border=True):
        st.subheader("📤 上傳區塊")
        st.write("支援 JPG, JPEG, PNG 格式的圖片檔案。")
        
        uploaded_image = st.file_uploader(
            "選擇或拖曳圖片至此：",
            type=["jpg", "jpeg", "png"],
            help="請上傳清晰的日常或藝術圖片進行展示"
        )
        
        # 互動按鈕與回饋區
        st.divider()
        st.subheader("🎯 互動觸發")
        st.caption("點擊下方按鈕觸發即時事件回饋：")
        
        if st.button("點擊解鎖驚喜 🚀", use_container_width=True, type="primary"):
            st.balloons()  # 繽紛氣球動畫！
            st.toast("🎉 成功點擊按鈕！事件已觸發！", icon="🎈")
            st.success("✨ **恭喜！你成功觸發了按鈕事件！**")

with col_preview:
    with st.container(border=True):
        st.subheader("🖼️ 圖片即時預覽")
        
        if uploaded_image is not None:
            # 模擬進度條與微載入
            progress_bar = st.progress(0, text="圖片解碼中...")
            for percent in range(1, 101, 25):
                time.sleep(0.08)
                progress_bar.progress(percent, text=f"正在載入核心檔案... {percent}%")
            progress_bar.empty()  # 載入完成清除進度條

            image = Image.open(uploaded_image)
            
            # 圖片卡片展示
            st.image(image, caption="📸 上傳影像即時渲染視圖", use_container_width=True)
            
            # 附加資訊面板 (Metrics)
            st.divider()
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric(label="圖片寬高 (Dimensions)", value=f"{image.size[0]} × {image.size[1]} px")
            with m_col2:
                st.metric(label="色彩模式 (Format)", value=image.format or "RGB")
        else:
            # 留白空狀態引導
            st.info("👈 尚未收到圖片，請在左側面板上傳檔案以預覽。")

# ── 6. 頁尾資訊 ──
st.divider()
st.caption("© 2026 VisionStudio Demo • Built with Streamlit & Python")
