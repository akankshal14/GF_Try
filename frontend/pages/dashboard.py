import streamlit as st

from backend.services.analytics_service import AnalyticsService


st.set_page_config(
    page_title="Employee Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Enterprise Employee Analytics")
st.markdown(
    "### Employee Performance, Attrition & Project Allocation"
)

service = AnalyticsService()


# =========================================================
# KPI CARDS
# =========================================================

try:

    stats = service.get_dashboard_statistics()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Employees",
            stats.get(
                "total_employees",
                0
            )
        )

    with col2:

        st.metric(
            "Active Employees",
            stats.get(
                "active_employees",
                0
            )
        )

    with col3:

        st.metric(
            "Total Projects",
            stats.get(
                "total_projects",
                0
            )
        )

    with col4:

        st.metric(
            "Active Projects",
            stats.get(
                "active_projects",
                0
            )
        )


except Exception as exc:

    st.error(
        f"Unable to load dashboard: {exc}"
    )


# =========================================================
# CHARTS
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "Employees by Department"
    )

    try:

        data = service.get_employees_by_department()

        import pandas as pd

        if isinstance(data, list):

            df = pd.DataFrame(data)

        else:

            df = data

        if not df.empty:

            st.bar_chart(df)

    except Exception as exc:

        st.error(str(exc))


with col2:

    st.subheader(
        "Employee Attrition"
    )

    try:

        data = service.get_attrition_statistics()

        import pandas as pd

        if isinstance(data, list):

            df = pd.DataFrame(data)

        else:

            df = data

        if not df.empty:

            st.bar_chart(df)

    except Exception as exc:

        st.error(str(exc))


# =========================================================
# PROJECT ALLOCATION
# =========================================================

st.subheader(
    "Project Allocation"
)

try:

    data = service.get_project_allocation()

    import pandas as pd

    if isinstance(data, list):

        df = pd.DataFrame(data)

    else:

        df = data

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

except Exception as exc:

    st.error(str(exc))


st.divider()

st.info(
    "Use the pages in the sidebar to manage employees, "
    "departments, projects, assignments and reviews."
)