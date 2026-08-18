import streamlit as st
import pandas as pd

from utils.helpers import records_to_dataframe
from backend.services.analytics_service import AnalyticsService


st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Analytics")

service = AnalyticsService()


# =========================================================
# KPI
# =========================================================

try:

    employee_data = service.get_employee_statistics()

    df = records_to_dataframe(
        employee_data
    )

    if not df.empty:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Employees",
                len(df)
            )

        with col2:
            if "monthly_income" in df.columns:
                st.metric(
                    "Average Salary",
                    f"₹{df['monthly_income'].mean():,.0f}"
                )

        with col3:
            if "age" in df.columns:
                st.metric(
                    "Average Age",
                    f"{df['age'].mean():.1f}"
                )

        with col4:
            if "is_active" in df.columns:
                st.metric(
                    "Active Employees",
                    int(df["is_active"].sum())
                )


except Exception as exc:

    st.error(
        f"Unable to load analytics: {exc}"
    )


# =========================================================
# DEPARTMENT ANALYSIS
# =========================================================

st.header("Employees by Department")

try:

    department_data = (
        service.get_employees_by_department()
    )

    department_df = records_to_dataframe(
        department_data
    )

    if not department_df.empty:

        st.bar_chart(
            department_df
        )

        st.dataframe(
            department_df,
            use_container_width=True
        )

except Exception as exc:

    st.error(
        f"Unable to load department analytics: {exc}"
    )


# =========================================================
# ATTRITION
# =========================================================

st.header("Attrition Analysis")

try:

    attrition_data = (
        service.get_attrition_statistics()
    )

    attrition_df = records_to_dataframe(
        attrition_data
    )

    if not attrition_df.empty:

        st.bar_chart(
            attrition_df
        )

        st.dataframe(
            attrition_df,
            use_container_width=True
        )

except Exception as exc:

    st.error(
        f"Unable to load attrition analytics: {exc}"
    )


# =========================================================
# PROJECT ALLOCATION
# =========================================================

st.header("Project Allocation")

try:

    allocation_data = (
        service.get_project_allocation()
    )

    allocation_df = records_to_dataframe(
        allocation_data
    )

    if not allocation_df.empty:

        st.dataframe(
            allocation_df,
            use_container_width=True
        )

except Exception as exc:

    st.error(
        f"Unable to load project allocation analytics: {exc}"
    )