# import sys
# import asyncio
# import logging
# import urllib.parse
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from sqlalchemy import create_engine, text


# # --- 2. PAGE CONFIG (MUST BE AT VERY TOP) ---
# st.set_page_config(
#     page_title="HR & Workforce Analytics",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Render Header immediately so user never sees a blank screen
# st.title("📊 HR Executive & Workforce Analytics")
# st.caption("Real-Time Workforce Intelligence powered by Data Warehouse Star Schema")
# st.divider()

# # --- 3. SECURE & FAST DATABASE CONNECTION ---
# @st.cache_resource(show_spinner=False)
# def get_db_connection():
#     try:
#         raw_password = "I_amsk77"
#         safe_password = urllib.parse.quote_plus(raw_password)
        
#         # Added connect_timeout=5 to prevent hanging endlessly if MySQL is slow
#         engine = create_engine(
#             f"mysql+pymysql://root:{safe_password}@127.0.0.1:3306/mini_project",
#             connect_args={"connect_timeout": 5},
#             pool_recycle=3600
#         )
#         with engine.connect() as conn:
#             conn.execute(text("SELECT 1"))
#         return engine
#     except Exception as e:
#         st.error(f"❌ Database Connection Failed: {e}")
#         st.info("💡 Ensure MySQL Service is running locally on port 3306.")
#         st.stop()

# engine = get_db_connection()

# # --- 4. CACHED QUERY HELPER (PREVENTS FROZEN UI) ---
# @st.cache_data(ttl=600, show_spinner="Loading Data...")
# def run_query(query_str):
#     try:
#         return pd.read_sql(query_str, engine)
#     except Exception as err:
#         st.error(f"Query Error: {err}")
#         return pd.DataFrame()

# # --- 5. SIDEBAR FILTERS ---
# st.sidebar.title("🎛️ Dashboard Filters")

# departments = run_query("SELECT DISTINCT DepartmentName FROM Dim_Department ORDER BY DepartmentName")
# if not departments.empty:
#     dept_list = departments['DepartmentName'].tolist()
#     selected_dept = st.sidebar.multiselect("Filter by Department", options=dept_list, default=dept_list)
# else:
#     selected_dept = []

# if selected_dept:
#     formatted_depts = ", ".join([f"'{dept}'" for dept in selected_dept])
#     dept_filter_sql = f"WHERE d.DepartmentName IN ({formatted_depts})"
# else:
#     dept_filter_sql = "WHERE 1=1"

# # --- 6. TOP SUMMARY METRICS ---
# col_m1, col_m2, col_m3, col_m4 = st.columns(4)

# with col_m1:
#     df_perf = run_query(f"SELECT ROUND(AVG(f.PerformanceRating), 2) AS val FROM Fact_PerformanceReviews f JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK {dept_filter_sql}")
#     val_perf = df_perf['val'].iloc[0] if not df_perf.empty and df_perf['val'].iloc[0] is not None else 0.0
#     st.metric(label="Avg Performance", value=f"{val_perf} / 4.0")

# with col_m2:
#     q_att = f"""
#         SELECT ROUND((COUNT(CASE WHEN e.Attrition = 'Yes' THEN 1 END) / COUNT(*)) * 100, 1) AS val 
#         FROM Dim_Employee e 
#         JOIN Employees oltp_e ON e.EmployeeID = oltp_e.EmployeeID 
#         JOIN Dim_Department d ON oltp_e.DepartmentID = d.DepartmentID 
#         {dept_filter_sql} AND e.IsCurrent = 1
#     """
#     df_att = run_query(q_att)
#     val_att = df_att['val'].iloc[0] if not df_att.empty and df_att['val'].iloc[0] is not None else 0.0
#     st.metric(label="Attrition Rate", value=f"{val_att}%")

# with col_m3:
#     df_prom = run_query("SELECT COUNT(e.EmployeeSK) - COUNT(DISTINCT e.EmployeeID) AS val FROM Dim_Employee e")
#     val_prom = df_prom['val'].iloc[0] if not df_prom.empty and df_prom['val'].iloc[0] is not None else 0
#     st.metric(label="SCD2 Promotions", value=f"{int(val_prom)}")

# with col_m4:
#     q_avg_sal = f"""
#         SELECT ROUND(AVG(e.MonthlyIncome), 0) AS val 
#         FROM Dim_Employee e 
#         JOIN Employees oltp_e ON e.EmployeeID = oltp_e.EmployeeID 
#         JOIN Dim_Department d ON oltp_e.DepartmentID = d.DepartmentID 
#         {dept_filter_sql} AND e.IsCurrent = 1
#     """
#     df_sal = run_query(q_avg_sal)
#     val_sal = df_sal['val'].iloc[0] if not df_sal.empty and df_sal['val'].iloc[0] is not None else 0
#     st.metric(label="Avg Monthly Salary", value=f"${val_sal:,.0f}")

# st.divider()

# # --- 7. CHARTS & TAB SECTIONS ---
# tab1, tab2, tab3, tab4 = st.tabs([
#     "📈 Performance & Trends", 
#     "🎯 Workload & Performers", 
#     "🚀 Strategic HR Insights",
#     "👤 Individual Employee Spotlight"
# ])

# with tab1:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("YoY Performance Trend")
#         q_kpi1 = f"""
#             SELECT dt.Year, ROUND(AVG(f.PerformanceRating), 2) AS AvgPerformance
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Date dt ON f.ReviewDateKey = dt.DateKey
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#             GROUP BY dt.Year ORDER BY dt.Year ASC
#         """
#         df_kpi1 = run_query(q_kpi1)
#         if not df_kpi1.empty:
#             fig1 = px.line(df_kpi1, x='Year', y='AvgPerformance', markers=True)
#             st.plotly_chart(fig1, use_container_width=True)

#     with col2:
#         st.subheader("Department Performance Comparison")
#         q_kpi8 = f"""
#             SELECT d.DepartmentName, ROUND(AVG(f.PerformanceRating), 2) AS AvgPerformance
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#             GROUP BY d.DepartmentName ORDER BY AvgPerformance DESC
#         """
#         df_kpi8 = run_query(q_kpi8)
#         if not df_kpi8.empty:
#             fig8 = px.bar(df_kpi8, x='DepartmentName', y='AvgPerformance', color='DepartmentName')
#             st.plotly_chart(fig8, use_container_width=True)

# with tab2:
#     st.subheader("🏆 Top Performers by Department (SQL Window Functions)")
    
#     # Interactive control to let HR select how many top performers per department to view
#     top_n = st.slider("Select Top N Employees per Department:", min_value=1, max_value=10, value=3)

#     q_kpi2 = f"""
#         WITH DepartmentRankedEmployees AS (
#             SELECT 
#                 e.EmployeeID,
#                 COALESCE(e.FirstName, '') AS FirstName,
#                 COALESCE(e.LastName, '') AS LastName,
#                 e.JobRole,
#                 d.DepartmentName,
#                 f.PerformanceRating,
#                 f.AllocatedHours,
#                 ROW_NUMBER() OVER (
#                     PARTITION BY d.DepartmentName 
#                     ORDER BY f.PerformanceRating DESC, f.AllocatedHours DESC, e.EmployeeID ASC
#                 ) AS DeptRank
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Employee e ON f.EmployeeSK = e.EmployeeSK AND e.IsCurrent = 1
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#         )
#         SELECT 
#             DeptRank AS `Rank`,
#             EmployeeID,
#             CONCAT(FirstName, ' ', LastName) AS EmployeeName,
#             JobRole
#         FROM DepartmentRankedEmployees
#         WHERE DeptRank <= {top_n}
#         ORDER BY DepartmentName ASC, DeptRank ASC;
#     """
    
#     df_kpi2 = run_query(q_kpi2)
    
#     if not df_kpi2.empty:
#         st.dataframe(df_kpi2, use_container_width=True, hide_index=True)
#     else:
#         st.info("No records match the selected department filters.")


# with tab3:
#     col_a, col_b = st.columns(2)
    
#     with col_a:
#         # ADVANCED KPI 1: Flight Risk Matrix
#         st.subheader("⚠️ Flight Risk Matrix")
#         q_flight_risk = f"""
#             SELECT 
#                 CONCAT(COALESCE(e.FirstName, 'Emp'), ' ', COALESCE(e.LastName, CAST(e.EmployeeID AS CHAR))) AS EmployeeName,
#                 e.JobRole,
#                 d.DepartmentName,
#                 f.AllocatedHours,
#                 f.WorkLifeBalance,
#                 f.PerformanceRating,
#                 CASE 
#                     WHEN f.AllocatedHours > 45 AND f.WorkLifeBalance <= 2 AND f.PerformanceRating >= 3 THEN 'High Risk'
#                     WHEN f.AllocatedHours > 40 AND f.WorkLifeBalance <= 2 THEN 'Medium Risk'
#                     ELSE 'Low Risk'
#                 END AS FlightRiskCategory
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Employee e ON f.EmployeeSK = e.EmployeeSK AND e.IsCurrent = 1
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#         """
#         df_risk = run_query(q_flight_risk)
#         if not df_risk.empty:
#             fig_risk = px.scatter(
#                 df_risk,
#                 x="AllocatedHours",
#                 y="WorkLifeBalance",
#                 color="FlightRiskCategory",
#                 size="PerformanceRating",
#                 hover_data=["EmployeeName", "JobRole", "DepartmentName"],
#                 color_discrete_map={'High Risk': '#E71D36', 'Medium Risk': '#FF9F1C', 'Low Risk': '#2EC4B6'},
#                 labels={"AllocatedHours": "Weekly Hours", "WorkLifeBalance": "Work-Life Balance (1-4)"}
#             )
#             st.plotly_chart(fig_risk, use_container_width=True)

#     with col_b:
#         # ADVANCED KPI 2: Gender / Role Pay Equity
#         st.subheader("⚖️ Pay Equity & Gender Distribution")
#         q_pay_equity = f"""
#             SELECT 
#                 d.DepartmentName,
#                 e.Gender,
#                 ROUND(AVG(e.MonthlyIncome), 2) AS AvgMonthlySalary
#             FROM Dim_Employee e
#             JOIN Employees oltp_e ON e.EmployeeID = oltp_e.EmployeeID
#             JOIN Dim_Department d ON oltp_e.DepartmentID = d.DepartmentID
#             {dept_filter_sql} AND e.IsCurrent = 1
#             GROUP BY d.DepartmentName, e.Gender
#             ORDER BY d.DepartmentName
#         """
#         df_pay = run_query(q_pay_equity)
#         if not df_pay.empty:
#             fig_pay = px.bar(
#                 df_pay,
#                 x="DepartmentName",
#                 y="AvgMonthlySalary",
#                 color="Gender",
#                 barmode="group",
#                 color_discrete_sequence=["#00B4D8", "#F72585"],
#                 labels={"AvgMonthlySalary": "Avg Monthly Salary ($)", "DepartmentName": "Department"}
#             )
#             st.plotly_chart(fig_pay, use_container_width=True)

#     st.divider()

#     col_c, col_d = st.columns(2)

#     with col_c:
#         # ADVANCED KPI 3: Promotion Stagnation Index
#         st.subheader("⏳ Career Stagnation Index")
#         q_stagnation = f"""
#             SELECT 
#                 e.JobRole,
#                 ROUND(AVG(f.YearsInCurrentRole), 1) AS AvgYearsInRole,
#                 ROUND(AVG(f.YearsSinceLastPromotion), 1) AS AvgYearsSincePromotion
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Employee e ON f.EmployeeSK = e.EmployeeSK AND e.IsCurrent = 1
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#             GROUP BY e.JobRole
#             ORDER BY AvgYearsSincePromotion DESC
#         """
#         df_stag = run_query(q_stagnation)
#         if not df_stag.empty:
#             fig_stag = px.bar(
#                 df_stag,
#                 x="JobRole",
#                 y=["AvgYearsInRole", "AvgYearsSincePromotion"],
#                 barmode="group",
#                 color_discrete_sequence=["#3A0CA3", "#4CC9F0"],
#                 labels={"value": "Years", "JobRole": "Job Role", "variable": "Tenure Metric"}
#             )
#             st.plotly_chart(fig_stag, use_container_width=True)

#     with col_d:
#         # ADVANCED KPI 4: Upskilling & Training ROI
#         st.subheader("🎓 Training Impact on Performance & Salary Growth")
#         q_training_roi = f"""
#             SELECT 
#                 f.TrainingTimesLastYear AS TrainingSessions,
#                 ROUND(AVG(f.PerformanceRating), 2) AS AvgPerformance,
#                 ROUND(AVG(e.PercentSalaryHike), 2) AS AvgSalaryHikePercentage
#             FROM Fact_PerformanceReviews f
#             JOIN Dim_Employee e ON f.EmployeeSK = e.EmployeeSK AND e.IsCurrent = 1
#             JOIN Dim_Department d ON f.DepartmentSK = d.DepartmentSK
#             {dept_filter_sql}
#             GROUP BY f.TrainingTimesLastYear
#             ORDER BY f.TrainingTimesLastYear ASC
#         """
#         df_roi = run_query(q_training_roi)
#         if not df_roi.empty:
#             fig_roi = px.line(
#                 df_roi,
#                 x="TrainingSessions",
#                 y=["AvgPerformance", "AvgSalaryHikePercentage"],
#                 markers=True,
#                 labels={"value": "Score / Percentage (%)", "TrainingSessions": "Training Sessions Last Year"}
#             )
#             st.plotly_chart(fig_roi, use_container_width=True)

# # --- TAB 4: INDIVIDUAL EMPLOYEE SPOTLIGHT (SEARCHABLE) ---
# with tab4:
#     st.subheader("👤 Individual Employee Search & Performance Profile")
    
#     # 1. Search Bar Input
#     search_query = st.text_input(
#         "🔎 Search Employee by ID, First Name, or Last Name:", 
#         placeholder="Type ID (e.g., 102) or Name (e.g., John)..."
#     ).strip()

#     if search_query:
#         # Clean search term to avoid SQL injection / formatting errors
#         clean_query = search_query.replace("'", "''")
        
#         # NOTE: %% is used to escape % for PyMySQL / SQLAlchemy execution
#         q_search = f"""
#             SELECT DISTINCT 
#                 e.EmployeeID, 
#                 COALESCE(e.FirstName, '') AS FirstName, 
#                 COALESCE(e.LastName, '') AS LastName, 
#                 e.JobRole,
#                 d.DepartmentName
#             FROM Dim_Employee e
#             JOIN Employees oltp_e ON e.EmployeeID = oltp_e.EmployeeID
#             JOIN Dim_Department d ON oltp_e.DepartmentID = d.DepartmentID
#             WHERE e.IsCurrent = 1
#               AND (
#                   CAST(e.EmployeeID AS CHAR) LIKE '%%{clean_query}%%'
#                OR LOWER(e.FirstName) LIKE LOWER('%%{clean_query}%%')
#                OR LOWER(e.LastName) LIKE LOWER('%%{clean_query}%%')
#               )
#             ORDER BY e.EmployeeID ASC
#             LIMIT 20
#         """
#         search_results = run_query(q_search)

#         if not search_results.empty:
#             # 2. Selectbox populated only with matching search results
#             search_results['FullLabel'] = search_results.apply(
#                 lambda r: f"ID: {r['EmployeeID']} - {r['FirstName']} {r['LastName']} ({r['JobRole']} | {r['DepartmentName']})", 
#                 axis=1
#             )
            
#             selected_emp_label = st.selectbox("Select Matching Employee:", options=search_results['FullLabel'].tolist())
#             selected_emp_id = int(search_results[search_results['FullLabel'] == selected_emp_label]['EmployeeID'].values[0])

#             # 3. Query Detailed Performance Metrics for Selected Employee
#             q_single_emp = f"""
#                 SELECT 
#                     e.EmployeeID, COALESCE(e.FirstName, '') AS FirstName, COALESCE(e.LastName, '') AS LastName, 
#                     e.JobRole, e.JobLevel, e.MonthlyIncome, 
#                     e.PercentSalaryHike, e.OverTime, e.Attrition, e.Age, e.Gender, e.MaritalStatus,
#                     d.DepartmentName,
#                     f.PerformanceRating, f.AllocatedHours, f.ActiveProjectCount, f.WorkLifeBalance,
#                     f.EnvironmentSatisfaction, f.JobInvolvement, f.JobSatisfaction,
#                     f.TrainingTimesLastYear, f.YearsAtCompany, f.YearsInCurrentRole, f.YearsSinceLastPromotion
#                 FROM Dim_Employee e
#                 JOIN Employees oltp_e ON e.EmployeeID = oltp_e.EmployeeID
#                 JOIN Dim_Department d ON oltp_e.DepartmentID = d.DepartmentID
#                 LEFT JOIN Fact_PerformanceReviews f ON e.EmployeeSK = f.EmployeeSK
#                 WHERE e.EmployeeID = {selected_emp_id} AND e.IsCurrent = 1
#                 LIMIT 1
#             """
#             emp_data = run_query(q_single_emp)

#             if not emp_data.empty:
#                 row = emp_data.iloc[0]
#                 st.divider()

#                 # --- EMPLOYEE HEADER & METRIC CARDS ---
#                 col_p1, col_p2, col_p3, col_p4 = st.columns(4)
#                 with col_p1:
#                     st.markdown(f"### {row['FirstName']} {row['LastName']}")
#                     st.caption(f"**ID:** {row['EmployeeID']} | **Role:** {row['JobRole']} (L{row['JobLevel']})")
#                     st.caption(f"**Department:** {row['DepartmentName']}")
#                 with col_p2:
#                     st.metric(label="Performance Rating", value=f"⭐ {row['PerformanceRating']} / 4.0")
#                     st.metric(label="Monthly Income", value=f"💰 ${row['MonthlyIncome']:,.0f}")
#                 with col_p3:
#                     st.metric(label="Weekly Hours", value=f"⏰ {row['AllocatedHours']} hrs")
#                     st.metric(label="Active Projects", value=f"📁 {row['ActiveProjectCount']} projects")
#                 with col_p4:
#                     # Risk evaluation
#                     if row['AllocatedHours'] > 45 and row['WorkLifeBalance'] <= 2:
#                         st.error("🚨 Burnout Risk: High")
#                     elif row['YearsSinceLastPromotion'] >= 3:
#                         st.warning("⚠️ Stagnation Risk: Promo Due")
#                     else:
#                         st.success("✅ Retention Status: Healthy")
#                     st.metric(label="Work-Life Balance", value=f"⚖️ {row['WorkLifeBalance']} / 4.0")

#                 st.divider()

#                 # --- SATISFACTION RADAR & CAREER PROGRESS ---
#                 col_d1, col_d2 = st.columns(2)
                
#                 with col_d1:
#                     st.markdown("#### 📊 Employee Satisfaction & Engagement Radar")
#                     categories = ['Work-Life Balance', 'Environment Sat.', 'Job Involvement', 'Job Satisfaction']
#                     scores = [row['WorkLifeBalance'], row['EnvironmentSatisfaction'], row['JobInvolvement'], row['JobSatisfaction']]
                    
#                     fig_radar = go.Figure(data=go.Scatterpolar(
#                         r=scores, theta=categories, fill='toself', line_color='#00B4D8'
#                     ))
#                     fig_radar.update_layout(
#                         polar=dict(radialaxis=dict(visible=True, range=[0, 4])),
#                         showlegend=False, height=300
#                     )
#                     st.plotly_chart(fig_radar, use_container_width=True)

#                 with col_d2:
#                     st.markdown("#### ⏳ Career Tenure Progress")
#                     st.write(f"**Years at Company:** {row['YearsAtCompany']} yrs")
#                     st.progress(min(int(row['YearsAtCompany']) * 10, 100))
                    
#                     st.write(f"**Years in Current Role:** {row['YearsInCurrentRole']} yrs")
#                     st.progress(min(int(row['YearsInCurrentRole']) * 15, 100))
                    
#                     st.write(f"**Years Since Last Promotion:** {row['YearsSinceLastPromotion']} yrs")
#                     st.progress(min(int(row['YearsSinceLastPromotion']) * 20, 100))

#                 st.divider()

#                 # --- SCD TYPE 2 CAREER HISTORY TABLE ---
#                 st.markdown("#### 📜 Career Version History (SCD Type 2)")
#                 q_scd_history = f"""
#                     SELECT 
#                         EmployeeSK, JobRole, MonthlyIncome, Attrition, 
#                         EffectiveDate, ExpirationDate, IsCurrent
#                     FROM Dim_Employee
#                     WHERE EmployeeID = {selected_emp_id}
#                     ORDER BY EffectiveDate DESC
#                 """
#                 df_history = run_query(q_scd_history)
#                 st.dataframe(df_history, use_container_width=True, hide_index=True)
#         else:
#             st.warning("⚠️ No matching employee records found.")
#     else:
#         st.info("💡 Enter an Employee ID or Name above to view their performance profile.")


import logging
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from backend.repositories.kpi_repository import KPIRepository

logging.getLogger("asyncio").setLevel(logging.CRITICAL)
import os
import sys
from pathlib import Path

# Force the project root (GF_Try) into Python's search path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# 1. PAGE CONFIG
st.set_page_config(
    page_title="HR & Workforce Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize 

kpi_repo = KPIRepository()

# Header
st.title("📊 HR Executive & Workforce Analytics")
st.caption("Real-Time Workforce Intelligence powered by Data Warehouse Star Schema")
st.divider()

# 2. SIDEBAR FILTERS
st.sidebar.title("🎛️ Dashboard Filters")

departments_df = kpi_repo.get_departments()
if not departments_df.empty:
    dept_list = departments_df['DepartmentName'].tolist()
    selected_dept = st.sidebar.multiselect("Filter by Department", options=dept_list, default=dept_list)
else:
    selected_dept = []

if selected_dept:
    formatted_depts = ", ".join([f"'{dept}'" for dept in selected_dept])
    dept_filter_sql = f"WHERE d.DepartmentName IN ({formatted_depts})"
else:
    dept_filter_sql = "WHERE 1=1"

# 3. TOP SUMMARY METRICS CARDS
metrics = kpi_repo.get_top_summary_metrics(dept_filter_sql)
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.metric(label="Avg Performance", value=f"{metrics['avg_perf']} / 4.0")
with col_m2:
    st.metric(label="Attrition Rate", value=f"{metrics['att_rate']}%")
with col_m3:
    st.metric(label="SCD2 Promotions", value=f"{int(metrics['promotions'])}")
with col_m4:
    st.metric(label="Avg Monthly Salary", value=f"${metrics['avg_salary']:,.0f}")

st.divider()

# 4. TABS & CHARTS
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Performance & Trends", 
    "🎯 Workload & Performers", 
    "🚀 Strategic HR Insights",
    "👤 Individual Employee Spotlight"
])

# TAB 1: PERFORMANCE TRENDS
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("YoY Performance Trend")
        df_kpi1 = kpi_repo.get_yoy_performance(dept_filter_sql)
        if not df_kpi1.empty:
            fig1 = px.line(df_kpi1, x='Year', y='AvgPerformance', markers=True)
            st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Department Performance Comparison")
        df_kpi8 = kpi_repo.get_department_performance(dept_filter_sql)
        if not df_kpi8.empty:
            fig8 = px.bar(df_kpi8, x='DepartmentName', y='AvgPerformance', color='DepartmentName')
            st.plotly_chart(fig8, use_container_width=True)

# TAB 2: WORKLOAD & PERFORMERS
with tab2:
    st.subheader("🏆 Top Performers by Department (SQL Window Functions)")
    top_n = st.slider("Select Top N Employees per Department:", min_value=1, max_value=10, value=3)
    df_kpi2 = kpi_repo.get_top_performers_by_dept(dept_filter_sql, top_n)
    
    if not df_kpi2.empty:
        st.dataframe(df_kpi2, use_container_width=True, hide_index=True)
    else:
        st.info("No records match the selected department filters.")

# TAB 3: STRATEGIC INSIGHTS
with tab3:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("⚠️ Flight Risk Matrix")
        df_risk = kpi_repo.get_flight_risk(dept_filter_sql)
        if not df_risk.empty:
            fig_risk = px.scatter(
                df_risk, x="AllocatedHours", y="WorkLifeBalance",
                color="FlightRiskCategory", size="PerformanceRating",
                hover_data=["EmployeeName", "JobRole", "DepartmentName"],
                color_discrete_map={'High Risk': '#E71D36', 'Medium Risk': '#FF9F1C', 'Low Risk': '#2EC4B6'},
                labels={"AllocatedHours": "Weekly Hours", "WorkLifeBalance": "Work-Life Balance (1-4)"}
            )
            st.plotly_chart(fig_risk, use_container_width=True)

    with col_b:
        st.subheader("⚖️ Pay Equity & Gender Distribution")
        df_pay = kpi_repo.get_pay_equity(dept_filter_sql)
        if not df_pay.empty:
            fig_pay = px.bar(
                df_pay, x="DepartmentName", y="AvgMonthlySalary", color="Gender", barmode="group",
                color_discrete_sequence=["#00B4D8", "#F72585"],
                labels={"AvgMonthlySalary": "Avg Monthly Salary ($)", "DepartmentName": "Department"}
            )
            st.plotly_chart(fig_pay, use_container_width=True)

    st.divider()
    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("⏳ Career Stagnation Index")
        df_stag = kpi_repo.get_career_stagnation(dept_filter_sql)
        if not df_stag.empty:
            fig_stag = px.bar(
                df_stag, x="JobRole", y=["AvgYearsInRole", "AvgYearsSincePromotion"], barmode="group",
                color_discrete_sequence=["#3A0CA3", "#4CC9F0"],
                labels={"value": "Years", "JobRole": "Job Role", "variable": "Tenure Metric"}
            )
            st.plotly_chart(fig_stag, use_container_width=True)

    with col_d:
        st.subheader("🎓 Training Impact on Performance & Salary Growth")
        df_roi = kpi_repo.get_training_roi(dept_filter_sql)
        if not df_roi.empty:
            fig_roi = px.line(
                df_roi, x="TrainingSessions", y=["AvgPerformance", "AvgSalaryHikePercentage"], markers=True,
                labels={"value": "Score / Percentage (%)", "TrainingSessions": "Training Sessions Last Year"}
            )
            st.plotly_chart(fig_roi, use_container_width=True)

# TAB 4: INDIVIDUAL SEARCH
with tab4:
    st.subheader("👤 Individual Employee Search & Performance Profile")
    search_query = st.text_input(
        "🔎 Search Employee by ID, First Name, or Last Name:", 
        placeholder="Type ID (e.g., 102) or Name (e.g., John)..."
    ).strip()

    if search_query:
        clean_query = search_query.replace("'", "''")
        search_results = kpi_repo.search_employees(clean_query)

        if not search_results.empty:
            search_results['FullLabel'] = search_results.apply(
                lambda r: f"ID: {r['EmployeeID']} - {r['FirstName']} {r['LastName']} ({r['JobRole']} | {r['DepartmentName']})", 
                axis=1
            )
            selected_emp_label = st.selectbox("Select Matching Employee:", options=search_results['FullLabel'].tolist())
            selected_emp_id = int(search_results[search_results['FullLabel'] == selected_emp_label]['EmployeeID'].values[0])

            emp_data = kpi_repo.get_employee_details(selected_emp_id)

            if not emp_data.empty:
                row = emp_data.iloc[0]
                st.divider()

                col_p1, col_p2, col_p3, col_p4 = st.columns(4)
                with col_p1:
                    st.markdown(f"### {row['FirstName']} {row['LastName']}")
                    st.caption(f"**ID:** {row['EmployeeID']} | **Role:** {row['JobRole']} (L{row['JobLevel']})")
                    st.caption(f"**Department:** {row['DepartmentName']}")
                with col_p2:
                    st.metric(label="Performance Rating", value=f"⭐ {row['PerformanceRating']} / 4.0")
                    st.metric(label="Monthly Income", value=f"💰 ${row['MonthlyIncome']:,.0f}")
                with col_p3:
                    st.metric(label="Weekly Hours", value=f"⏰ {row['AllocatedHours']} hrs")
                    st.metric(label="Active Projects", value=f"📁 {row['ActiveProjectCount']} projects")
                with col_p4:
                    if row['AllocatedHours'] > 45 and row['WorkLifeBalance'] <= 2:
                        st.error("🚨 Burnout Risk: High")
                    elif row['YearsSinceLastPromotion'] >= 3:
                        st.warning("⚠️ Stagnation Risk: Promo Due")
                    else:
                        st.success("✅ Retention Status: Healthy")
                    st.metric(label="Work-Life Balance", value=f"⚖️ {row['WorkLifeBalance']} / 4.0")

                st.divider()

                col_d1, col_d2 = st.columns(2)
                with col_d1:
                    st.markdown("#### 📊 Employee Satisfaction & Engagement Radar")
                    categories = ['Work-Life Balance', 'Environment Sat.', 'Job Involvement', 'Job Satisfaction']
                    scores = [row['WorkLifeBalance'], row['EnvironmentSatisfaction'], row['JobInvolvement'], row['JobSatisfaction']]
                    
                    fig_radar = go.Figure(data=go.Scatterpolar(
                        r=scores, theta=categories, fill='toself', line_color='#00B4D8'
                    ))
                    fig_radar.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 4])),
                        showlegend=False, height=300
                    )
                    st.plotly_chart(fig_radar, use_container_width=True)

                with col_d2:
                    st.markdown("#### ⏳ Career Tenure Progress")
                    st.write(f"**Years at Company:** {row['YearsAtCompany']} yrs")
                    st.progress(min(int(row['YearsAtCompany']) * 10, 100))
                    
                    st.write(f"**Years in Current Role:** {row['YearsInCurrentRole']} yrs")
                    st.progress(min(int(row['YearsInCurrentRole']) * 15, 100))
                    
                    st.write(f"**Years Since Last Promotion:** {row['YearsSinceLastPromotion']} yrs")
                    st.progress(min(int(row['YearsSinceLastPromotion']) * 20, 100))

                st.divider()

                st.markdown("#### 📜 Career Version History (SCD Type 2)")
                df_history = kpi_repo.get_employee_scd_history(selected_emp_id)
                st.dataframe(df_history, use_container_width=True, hide_index=True)
        else:
            st.warning("⚠️ No matching employee records found.")
    else:
        st.info("💡 Enter an Employee ID or Name above to view their performance profile.")