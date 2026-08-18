import streamlit as st


st.set_page_config(
    page_title="Enterprise Employee Analytics",
    page_icon="🏢",
    layout="wide"
)


st.title(
    "🏢 Enterprise Employee Analytics & Data Warehouse"
)

st.markdown(
    """
    ## Welcome

    This application provides:

    - 👨‍💼 Employee Management
    - 🏢 Department Management
    - 📁 Project Management
    - 🔗 Employee Project Assignments
    - ⭐ Employee Reviews
    - 📊 Analytics
    - 📈 Executive Dashboard

    Use the sidebar to navigate between modules.
    """
)


# =========================================================
# SYSTEM INFORMATION
# =========================================================

st.divider()

st.subheader("System Architecture")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("**Frontend**\n\nStreamlit")

with col2:
    st.info("**Application**\n\nPython OOP")

with col3:
    st.info("**Database**\n\nMySQL")

with col4:
    st.info("**Analytics**\n\nOLAP / Data Warehouse")