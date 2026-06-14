import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Налаштування сторінки
st.set_page_config(
    page_title="OFM Dashboard",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Темна тема
st.markdown("""
<style>
    .stApp {
        background-color: #0F0F12;
        color: #E0E0E0;
    }
    .metric-card {
        background-color: #1A1A24;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #C026D3;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("💎 OFM Dashboard")
st.sidebar.markdown("**AI OnlyFans Models Hub**")

page = st.sidebar.radio("Навігація", [
    "🏠 Головна", 
    "👤 Мої Моделі", 
    "💬 Telegram Чати", 
    "📊 Аналітика", 
    "💰 Фінанси"
])

# ==================== ГОЛОВНА ====================
if page == "🏠 Головна":
    st.title("👋 Ласкаво просимо до OFM Dashboard")
    st.markdown("**Центральне управління твоїми AI персонажами**")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Активні моделі", "8", "↑2")
    with col2:
        st.metric("Повідомлень сьогодні", "247", "↑18%")
    with col3:
        st.metric("Прибуток місяць", "$18,450", "↑24%")
    with col4:
        st.metric("Загальна аудиторія", "312K", "↑5.2K")

    col_g1, col_g2 = st.columns([2, 1])
    with col_g1:
        st.subheader("Прибуток за 30 днів")
        dates = pd.date_range(end=datetime.today(), periods=30)
        revenue = [1200, 890, 2100, 3400, 2800, 1500, 4200, 3800, 2900, 5100,
                  4600, 3200, 6700, 5900, 4800, 7200, 8100, 6500, 9300, 8800,
                  7100, 10500, 9800, 8200, 12400, 11200, 9800, 13700, 12800, 18450]
        df_rev = pd.DataFrame({"Дата": dates, "Прибуток": revenue})
        fig = px.bar(df_rev, x="Дата", y="Прибуток", template="plotly_dark")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col_g2:
        st.subheader("Зростання підписників")
        platforms = ["Instagram", "TikTok", "OnlyFans"]
        growth = [12400, 8300, 5200]
        fig2 = px.pie(names=platforms, values=growth, template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🔥 Гарячі чати")
    hot_chats = pd.DataFrame({
        "Модель": ["Lila Rose", "Nova Lux", "Mia Star", "Luna Eve"],
        "Останнє повідомлення": ["Ти сьогодні вільний? 😏", "Надіслала тобі приватне...", "Хочеш ексклюзив?", "Пиши мені в особистий..."],
        "Час": ["2 хв", "11 хв", "27 хв", "1 год"]
    })
    st.dataframe(hot_chats, use_container_width=True, hide_index=True)

# ==================== МОЇ МОДЕЛІ ====================
elif page == "👤 Мої Моделі":
    st.title("👤 Мої AI Моделі")
    
    if st.button("➕ Додати нову модель", type="primary"):
        st.success("Форма додавання (в розробці)")

    cols = st.columns(3)
    models = [
        ("Lila Rose", "45.2K", "$4,820", "🟢"),
        ("Nova Lux", "32.1K", "$3,150", "🟢"),
        ("Mia Star", "28.7K", "$2,980", "🔴")
    ]
    
    for i, (name, subs, earn, status) in enumerate(models):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background-color:#1A1A24; padding:20px; border-radius:12px; border:2px solid #C026D3; margin-bottom:15px;">
                <h3>{name} {status}</h3>
                <p><strong>Підписники:</strong> {subs}</p>
                <p><strong>Заробіток:</strong> {earn}</p>
                <p><strong>Telegram:</strong> @lilarose_of</p>
                <button style="background:#C026D3; color:white; border:none; padding:10px 20px; border-radius:8px; width:100%;">💬 Відкрити чат</button>
            </div>
            """, unsafe_allow_html=True)

# ==================== ІНШІ СТОРІНКИ ====================
else:
    st.info("Ця сторінка знаходиться в розробці... Скоро додамо повноцінний чат з Telegram та AI.")

st.sidebar.markdown("---")
st.sidebar.caption("OFM Dashboard v0.1 | Створено з Grok")
