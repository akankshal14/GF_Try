# import sys
# from pathlib import Path

# # ============================================================
# # PROJECT ROOT
# # ============================================================

# PROJECT_ROOT = Path(__file__).resolve().parents[2]

# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))


# # ============================================================
# # IMPORTS
# # ============================================================

# import streamlit as st
# import pandas as pd
# from datetime import date

# from backend.services.employee_service import EmployeeService
# from backend.models.employee import Employee


# # ============================================================
# # PAGE CONFIGURATION
# # ============================================================

# st.set_page_config(
#     page_title="Employees",
#     page_icon="👨‍💼",
#     layout="wide"
# )


# # ============================================================
# # SERVICES
# # ============================================================

# employee_service = EmployeeService()


# # ============================================================
# # DATABASE COLUMN NAMES
# # ============================================================

# EMPLOYEE_COLUMNS = [
#     "EmployeeID",
#     "FirstName",
#     "LastName",
#     "Age",
#     "Gender",
#     "MaritalStatus",
#     "DepartmentID",
#     "JobRole",
#     "JobLevel",
#     "MonthlyIncome",
#     "DailyRate",
#     "HourlyRate",
#     "MonthlyRate",
#     "PercentSalaryHike",
#     "StockOptionLevel",
#     "OverTime",
#     "BusinessTravel",
#     "DistanceFromHome",
#     "Education",
#     "EducationField",
#     "EnvironmentSatisfaction",
#     "JobInvolvement",
#     "JobSatisfaction",
#     "RelationshipSatisfaction",
#     "WorkLifeBalance",
#     "TotalWorkingYears",
#     "TrainingTimesLastYear",
#     "YearsAtCompany",
#     "YearsInCurrentRole",
#     "YearsSinceLastPromotion",
#     "YearsWithCurrManager",
#     "IsActive",
#     "HireDate",
#     "TerminationDate"
# ]


# # ============================================================
# # HELPER FUNCTIONS
# # ============================================================

# def employees_to_dataframe(employees):
#     """
#     Convert repository result tuples into a pandas DataFrame.
#     """

#     return pd.DataFrame(
#         employees,
#         columns=EMPLOYEE_COLUMNS
#     )


# def convert_optional_date(value):
#     """
#     Convert Streamlit date value to a database-friendly value.
#     """

#     if value is None:
#         return None

#     return value


# # ============================================================
# # PAGE TITLE
# # ============================================================

# st.title("👨‍💼 Employee Management")

# st.caption(
#     "Create, view, update and delete employee records."
# )


# # ============================================================
# # SIDEBAR
# # ============================================================

# operation = st.sidebar.radio(
#     "Employee Operations",
#     [
#         "View Employees",
#         "View Employee",
#         "Add Employee",
#         "Update Employee",
#         "Delete Employee"
#     ]
# )


# # ============================================================
# # 1. VIEW ALL EMPLOYEES
# # ============================================================

# if operation == "View Employees":

#     st.header("📋 All Employees")

#     try:

#         employees = employee_service.get_all_employees()

#         if not employees:

#             st.info("No employees found.")

#         else:

#             df = employees_to_dataframe(employees)

#             st.metric(
#                 "Total Employees",
#                 len(df)
#             )

#             st.dataframe(
#                 df,
#                 width="stretch",
#                 hide_index=True
#             )

#     except Exception as exc:

#         st.error(
#             f"Unable to load employees: {exc}"
#         )


# # ============================================================
# # 2. VIEW SINGLE EMPLOYEE
# # ============================================================

# elif operation == "View Employee":

#     st.header("🔍 Find Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     if st.button(
#         "Search Employee",
#         type="primary"
#     ):

#         try:

#             employee = employee_service.get_employee(
#                 employee_id
#             )

#             if employee:

#                 st.success(
#                     f"Employee {employee_id} found."
#                 )

#                 df = employees_to_dataframe(
#                     [employee]
#                 )

#                 st.dataframe(
#                     df,
#                     width="stretch",
#                     hide_index=True
#                 )

#         except Exception as exc:

#             st.error(
#                 f"Unable to find employee: {exc}"
#             )


# # ============================================================
# # 3. CREATE EMPLOYEE
# # ============================================================

# elif operation == "Add Employee":

#     st.header("➕ Add Employee")

#     with st.form("add_employee_form"):

#         # ----------------------------------------------------
#         # BASIC INFORMATION
#         # ----------------------------------------------------

#         st.subheader("Basic Information")

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             employee_id = st.number_input(
#                 "Employee ID",
#                 min_value=1,
#                 step=1
#             )

#             first_name = st.text_input(
#                 "First Name"
#             )

#             last_name = st.text_input(
#                 "Last Name"
#             )

#             age = st.number_input(
#                 "Age",
#                 min_value=18,
#                 max_value=100,
#                 value=25
#             )

#         with col2:

#             gender = st.selectbox(
#                 "Gender",
#                 [
#                     "Male",
#                     "Female",
#                     "Other"
#                 ]
#             )

#             marital_status = st.selectbox(
#                 "Marital Status",
#                 [
#                     "Single",
#                     "Married",
#                     "Divorced"
#                 ]
#             )

#             department_id = st.number_input(
#                 "Department ID",
#                 min_value=1,
#                 step=1
#             )

#             job_role = st.text_input(
#                 "Job Role"
#             )

#         with col3:

#             job_level = st.number_input(
#                 "Job Level",
#                 min_value=1,
#                 max_value=10,
#                 value=1
#             )

#             monthly_income = st.number_input(
#                 "Monthly Income",
#                 min_value=0.0,
#                 step=100.0
#             )

#             daily_rate = st.number_input(
#                 "Daily Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#             hourly_rate = st.number_input(
#                 "Hourly Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#         # ----------------------------------------------------
#         # EMPLOYMENT INFORMATION
#         # ----------------------------------------------------

#         st.subheader("Employment Information")

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             monthly_rate = st.number_input(
#                 "Monthly Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#             percent_salary_hike = st.number_input(
#                 "Percent Salary Hike",
#                 min_value=0.0,
#                 step=1.0
#             )

#             stock_option_level = st.number_input(
#                 "Stock Option Level",
#                 min_value=0,
#                 step=1
#             )

#         with col2:

#             # IMPORTANT:
#             # Database stores OverTime as INTEGER.
#             #
#             # Yes -> 1
#             # No  -> 0

#             over_time_choice = st.selectbox(
#                 "OverTime",
#                 [
#                     "Yes",
#                     "No"
#                 ]
#             )

#             over_time = (
#                 1
#                 if over_time_choice == "Yes"
#                 else 0
#             )

#             business_travel = st.selectbox(
#                 "Business Travel",
#                 [
#                     "Non-Travel",
#                     "Travel_Rarely",
#                     "Travel_Frequently"
#                 ]
#             )

#             distance_from_home = st.number_input(
#                 "Distance From Home",
#                 min_value=0,
#                 step=1
#             )

#         with col3:

#             education = st.number_input(
#                 "Education",
#                 min_value=0,
#                 step=1
#             )

#             education_field = st.text_input(
#                 "Education Field"
#             )

#         # ----------------------------------------------------
#         # SATISFACTION & PERFORMANCE
#         # ----------------------------------------------------

#         st.subheader(
#             "Satisfaction & Performance"
#         )

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             environment_satisfaction = st.number_input(
#                 "Environment Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             job_involvement = st.number_input(
#                 "Job Involvement",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             job_satisfaction = st.number_input(
#                 "Job Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#         with col2:

#             relationship_satisfaction = st.number_input(
#                 "Relationship Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             work_life_balance = st.number_input(
#                 "Work Life Balance",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#         with col3:

#             total_working_years = st.number_input(
#                 "Total Working Years",
#                 min_value=0,
#                 step=1
#             )

#             training_times_last_year = st.number_input(
#                 "Training Times Last Year",
#                 min_value=0,
#                 step=1
#             )

#         # ----------------------------------------------------
#         # COMPANY HISTORY
#         # ----------------------------------------------------

#         st.subheader(
#             "Company History"
#         )

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             years_at_company = st.number_input(
#                 "Years At Company",
#                 min_value=0,
#                 step=1
#             )

#             years_in_current_role = st.number_input(
#                 "Years In Current Role",
#                 min_value=0,
#                 step=1
#             )

#         with col2:

#             years_since_last_promotion = st.number_input(
#                 "Years Since Last Promotion",
#                 min_value=0,
#                 step=1
#             )

#             years_with_curr_manager = st.number_input(
#                 "Years With Current Manager",
#                 min_value=0,
#                 step=1
#             )

#         with col3:

#             is_active = st.checkbox(
#                 "Active Employee",
#                 value=True
#             )

#             hire_date = st.date_input(
#                 "Hire Date",
#                 value=date.today()
#             )

#             termination_date = st.date_input(
#                 "Termination Date",
#                 value=None
#             )

#         # ----------------------------------------------------
#         # SUBMIT
#         # ----------------------------------------------------

#         submitted = st.form_submit_button(
#             "Create Employee",
#             width="stretch"
#         )

#     # ========================================================
#     # CREATE OPERATION
#     # ========================================================

#     if submitted:

#         # ----------------------------------------------------
#         # BASIC VALIDATION
#         # ----------------------------------------------------

#         if not first_name.strip():

#             st.error(
#                 "First name is required."
#             )

#         elif not last_name.strip():

#             st.error(
#                 "Last name is required."
#             )

#         elif not job_role.strip():

#             st.error(
#                 "Job role is required."
#             )

#         else:

#             try:

#                 # ------------------------------------------------
#                 # CREATE EMPLOYEE OBJECT
#                 # ------------------------------------------------

#                 employee = Employee(

#                     employee_id=employee_id,

#                     first_name=first_name.strip(),

#                     last_name=last_name.strip(),

#                     age=age,

#                     gender=gender,

#                     marital_status=marital_status,

#                     department_id=department_id,

#                     job_role=job_role.strip(),

#                     job_level=job_level,

#                     monthly_income=monthly_income,

#                     daily_rate=daily_rate,

#                     hourly_rate=hourly_rate,

#                     monthly_rate=monthly_rate,

#                     percent_salary_hike=percent_salary_hike,

#                     stock_option_level=stock_option_level,

#                     # IMPORTANT:
#                     # 1 or 0, NOT "Yes"/"No"
#                     over_time=over_time,

#                     business_travel=business_travel,

#                     distance_from_home=distance_from_home,

#                     education=education,

#                     education_field=education_field,

#                     environment_satisfaction=(
#                         environment_satisfaction
#                     ),

#                     job_involvement=(
#                         job_involvement
#                     ),

#                     job_satisfaction=(
#                         job_satisfaction
#                     ),

#                     relationship_satisfaction=(
#                         relationship_satisfaction
#                     ),

#                     work_life_balance=(
#                         work_life_balance
#                     ),

#                     total_working_years=(
#                         total_working_years
#                     ),

#                     training_times_last_year=(
#                         training_times_last_year
#                     ),

#                     years_at_company=(
#                         years_at_company
#                     ),

#                     years_in_current_role=(
#                         years_in_current_role
#                     ),

#                     years_since_last_promotion=(
#                         years_since_last_promotion
#                     ),

#                     years_with_curr_manager=(
#                         years_with_curr_manager
#                     ),

#                     is_active=is_active,

#                     hire_date=hire_date,

#                     termination_date=termination_date
#                 )

#                 # ------------------------------------------------
#                 # SERVICE CALL
#                 # ------------------------------------------------

#                 result = (
#                     employee_service
#                     .create_employee(
#                         employee
#                     )
#                 )

#                 st.success(
#                     f"Employee {result} created successfully."
#                 )

#             except Exception as exc:

#                 st.error(
#                     f"Unable to create employee: {exc}"
#                 )


# # ============================================================
# # 4. UPDATE EMPLOYEE
# # ============================================================

# # elif operation == "Update Employee":

# #     st.header("✏️ Update Employee")

# #     employee_id = st.number_input(
# #         "Employee ID",
# #         min_value=1,
# #         step=1,
# #         value=1
# #     )

# #     if st.button(
# #         "Load Employee",
# #         type="primary"
# #     ):

# #         try:

# #             employee = (
# #                 employee_service
# #                 .get_employee(
# #                     employee_id
# #                 )
# #             )

# #             st.session_state[
# #                 "employee_to_update"
# #             ] = employee

# #             st.success(
# #                 "Employee loaded successfully."
# #             )

# #         except Exception as exc:

# #             st.error(
# #                 f"Unable to load employee: {exc}"
# #             )

# #     employee = st.session_state.get(
# #         "employee_to_update"
# #     )

# #     if employee:

# #         # ----------------------------------------------------
# #         # DATABASE get_by_id() RETURNS TUPLE
# #         #
# #         # SELECT * follows:
# #         #
# #         # 0 EmployeeID
# #         # 1 FirstName
# #         # 2 LastName
# #         # 3 Age
# #         # 4 Gender
# #         # 5 MaritalStatus
# #         # 6 DepartmentID
# #         # 7 JobRole
# #         # 8 JobLevel
# #         # 9 MonthlyIncome
# #         # ...
# #         # 15 OverTime
# #         # ...
# #         # 31 IsActive
# #         # 32 HireDate
# #         # 33 TerminationDate
# #         # ----------------------------------------------------

# #         def get_value(index):

# #             return employee[index]

# #         st.subheader(
# #             f"Updating Employee {employee_id}"
# #         )

# #         with st.form(
# #             "update_employee_form"
# #         ):

# #             col1, col2 = st.columns(2)

# #             with col1:

# #                 first_name = st.text_input(
# #                     "First Name",
# #                     value=str(
# #                         get_value(1)
# #                         or ""
# #                     )
# #                 )

# #                 last_name = st.text_input(
# #                     "Last Name",
# #                     value=str(
# #                         get_value(2)
# #                         or ""
# #                     )
# #                 )

# #                 department_id = st.number_input(
# #                     "Department ID",
# #                     min_value=1,
# #                     value=int(
# #                         get_value(6)
# #                         or 1
# #                     )
# #                 )

# #                 job_role = st.text_input(
# #                     "Job Role",
# #                     value=str(
# #                         get_value(7)
# #                         or ""
# #                     )
# #                 )

# #                 job_level = st.number_input(
# #                     "Job Level",
# #                     min_value=1,
# #                     value=int(
# #                         get_value(8)
# #                         or 1
# #                     )
# #                 )

# #             with col2:

# #                 monthly_income = st.number_input(
# #                     "Monthly Income",
# #                     min_value=0.0,
# #                     value=float(
# #                         get_value(9)
# #                         or 0
# #                     )
# #                 )

# #                 # --------------------------------------------
# #                 # FIX:
# #                 # Database returns 1/0 for OverTime
# #                 # UI shows Yes/No
# #                 # --------------------------------------------

# #                 current_overtime = get_value(15)

# #                 if current_overtime in (
# #                     1,
# #                     "1",
# #                     True
# #                 ):
# #                     overtime_index = 0
# #                 else:
# #                     overtime_index = 1

# #                 over_time_choice = st.selectbox(
# #                     "OverTime",
# #                     [
# #                         "Yes",
# #                         "No"
# #                     ],
# #                     index=overtime_index
# #                 )

# #                 over_time = (
# #                     1
# #                     if over_time_choice == "Yes"
# #                     else 0
# #                 )

# #                 current_active = get_value(31)

# #                 is_active = st.checkbox(
# #                     "Active Employee",
# #                     value=(
# #                         True
# #                         if current_active in (
# #                             1,
# #                             "1",
# #                             True
# #                         )
# #                         else False
# #                     )
# #                 )

# #                 current_termination = (
# #                     get_value(33)
# #                 )

# #                 if current_termination:

# #                     if hasattr(
# #                         current_termination,
# #                         "date"
# #                     ):

# #                         current_termination = (
# #                             current_termination.date()
# #                         )

# #                 termination_date = st.date_input(
# #                     "Termination Date",
# #                     value=current_termination
# #                 )

# #             submitted = st.form_submit_button(
# #                 "Update Employee",
# #                 width="stretch"
# #             )

# #         # ----------------------------------------------------
# #         # UPDATE OPERATION
# #         # ----------------------------------------------------

# #         if submitted:

# #             if not first_name.strip():

# #                 st.error(
# #                     "First name is required."
# #                 )

# #             elif not last_name.strip():

# #                 st.error(
# #                     "Last name is required."
# #                 )

# #             elif not job_role.strip():

# #                 st.error(
# #                     "Job role is required."
# #                 )

# #             else:

# #                 try:

# #                     data = {

# #                         "first_name":
# #                             first_name.strip(),

# #                         "last_name":
# #                             last_name.strip(),

# #                         "department_id":
# #                             department_id,

# #                         "job_role":
# #                             job_role.strip(),

# #                         "job_level":
# #                             job_level,

# #                         "monthly_income":
# #                             monthly_income,

# #                         # IMPORTANT:
# #                         # 1 or 0
# #                         "over_time":
# #                             over_time,

# #                         "is_active":
# #                             is_active,

# #                         "termination_date":
# #                             termination_date
# #                     }

# #                     result = (
# #                         employee_service
# #                         .update_employee(
# #                             employee_id,
# #                             data
# #                         )
# #                     )

# #                     st.success(
# #                         "Employee updated successfully."
# #                     )

# #                     st.info(
# #                         f"Rows updated: {result}"
# #                     )

# #                     # Clear loaded employee

# #                     if (
# #                         "employee_to_update"
# #                         in st.session_state
# #                     ):

# #                         del st.session_state[
# #                             "employee_to_update"
# #                         ]

# #                 except Exception as exc:

# #                     st.error(
# #                         f"Unable to update employee: {exc}"
# #                     )


# # ============================================================
# # 4. UPDATE EMPLOYEE
# # ============================================================

# elif operation == "Update Employee":

#     st.header("✏️ Update Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     if st.button(
#         "Load Employee",
#         type="primary"
#     ):

#         try:

#             employee = employee_service.get_employee(
#                 employee_id
#             )

#             st.session_state["employee_to_update"] = employee

#             st.success(
#                 "Employee loaded successfully."
#             )

#         except Exception as exc:

#             st.error(
#                 f"Unable to load employee: {exc}"
#             )

#     employee = st.session_state.get(
#         "employee_to_update"
#     )

#     if employee:

#         st.subheader(
#             f"Updating Employee {employee_id}"
#         )

#         # ----------------------------------------------------
#         # HANDLE DICTIONARY RESPONSE
#         # ----------------------------------------------------

#         # Your repository/service is returning a dictionary.
#         # Convert keys safely because database column names
#         # may appear in different cases.

#         if isinstance(employee, dict):

#             def get_value(key, default=None):

#                 # Exact key
#                 if key in employee:
#                     return employee[key]

#                 # Case-insensitive search
#                 for existing_key in employee.keys():

#                     if str(existing_key).lower() == key.lower():
#                         return employee[existing_key]

#                 return default

#         else:

#             # Fallback in case the repository returns a tuple
#             def get_value(index, default=None):

#                 try:
#                     return employee[index]
#                 except (IndexError, KeyError, TypeError):
#                     return default


#         # ----------------------------------------------------
#         # CURRENT VALUES
#         # ----------------------------------------------------

#         current_first_name = get_value(
#             "FirstName",
#             ""
#         )

#         current_last_name = get_value(
#             "LastName",
#             ""
#         )

#         current_department_id = get_value(
#             "DepartmentID",
#             1
#         )

#         current_job_role = get_value(
#             "JobRole",
#             ""
#         )

#         current_job_level = get_value(
#             "JobLevel",
#             1
#         )

#         current_monthly_income = get_value(
#             "MonthlyIncome",
#             0
#         )

#         current_overtime = get_value(
#             "OverTime",
#             0
#         )

#         current_is_active = get_value(
#             "IsActive",
#             1
#         )

#         current_termination_date = get_value(
#             "TerminationDate",
#             None
#         )


#         # ----------------------------------------------------
#         # CONVERT VALUES
#         # ----------------------------------------------------

#         try:
#             current_department_id = int(
#                 current_department_id or 1
#             )
#         except (ValueError, TypeError):
#             current_department_id = 1


#         try:
#             current_job_level = int(
#                 current_job_level or 1
#             )
#         except (ValueError, TypeError):
#             current_job_level = 1


#         try:
#             current_monthly_income = float(
#                 current_monthly_income or 0
#             )
#         except (ValueError, TypeError):
#             current_monthly_income = 0.0


#         # ----------------------------------------------------
#         # OVERTIME
#         # DATABASE: 1 = YES, 0 = NO
#         # ----------------------------------------------------

#         if str(current_overtime).lower() in (
#             "1",
#             "yes",
#             "true"
#         ):

#             overtime_index = 0

#         else:

#             overtime_index = 1


#         # ----------------------------------------------------
#         # ACTIVE STATUS
#         # ----------------------------------------------------

#         if str(current_is_active).lower() in (
#             "1",
#             "yes",
#             "true"
#         ):

#             current_is_active = True

#         else:

#             current_is_active = False


#         # ----------------------------------------------------
#         # TERMINATION DATE
#         # ----------------------------------------------------

#         if current_termination_date:

#             if hasattr(
#                 current_termination_date,
#                 "date"
#             ):

#                 current_termination_date = (
#                     current_termination_date.date()
#                 )


#         # ----------------------------------------------------
#         # UPDATE FORM
#         # ----------------------------------------------------

#         with st.form(
#             "update_employee_form"
#         ):

#             col1, col2 = st.columns(2)

#             # ------------------------------------------------
#             # LEFT COLUMN
#             # ------------------------------------------------

#             with col1:

#                 first_name = st.text_input(
#                     "First Name",
#                     value=str(
#                         current_first_name or ""
#                     )
#                 )

#                 last_name = st.text_input(
#                     "Last Name",
#                     value=str(
#                         current_last_name or ""
#                     )
#                 )

#                 department_id = st.number_input(
#                     "Department ID",
#                     min_value=1,
#                     value=current_department_id
#                 )

#                 job_role = st.text_input(
#                     "Job Role",
#                     value=str(
#                         current_job_role or ""
#                     )
#                 )

#                 job_level = st.number_input(
#                     "Job Level",
#                     min_value=1,
#                     value=current_job_level
#                 )


#             # ------------------------------------------------
#             # RIGHT COLUMN
#             # ------------------------------------------------

#             with col2:

#                 monthly_income = st.number_input(
#                     "Monthly Income",
#                     min_value=0.0,
#                     value=current_monthly_income
#                 )

#                 over_time_choice = st.selectbox(
#                     "OverTime",
#                     [
#                         "Yes",
#                         "No"
#                     ],
#                     index=overtime_index
#                 )

#                 # IMPORTANT:
#                 # Convert Yes/No to database integer

#                 over_time = (
#                     1
#                     if over_time_choice == "Yes"
#                     else 0
#                 )


#                 is_active = st.checkbox(
#                     "Active Employee",
#                     value=current_is_active
#                 )


#                 termination_date = st.date_input(
#                     "Termination Date",
#                     value=current_termination_date
#                 )


#             # ------------------------------------------------
#             # SUBMIT
#             # ------------------------------------------------

#             submitted = st.form_submit_button(
#                 "Update Employee",
#                 width="stretch"
#             )


#         # ----------------------------------------------------
#         # UPDATE DATABASE
#         # ----------------------------------------------------

#         if submitted:

#             if not first_name.strip():

#                 st.error(
#                     "First name is required."
#                 )

#             elif not last_name.strip():

#                 st.error(
#                     "Last name is required."
#                 )

#             elif not job_role.strip():

#                 st.error(
#                     "Job role is required."
#                 )

#             else:

#                 try:

#                     data = {

#                         "first_name":
#                             first_name.strip(),

#                         "last_name":
#                             last_name.strip(),

#                         "department_id":
#                             department_id,

#                         "job_role":
#                             job_role.strip(),

#                         "job_level":
#                             job_level,

#                         "monthly_income":
#                             monthly_income,

#                         # 1 = Yes
#                         # 0 = No
#                         "over_time":
#                             over_time,

#                         "is_active":
#                             is_active,

#                         "termination_date":
#                             termination_date
#                     }


#                     result = (
#                         employee_service
#                         .update_employee(
#                             employee_id,
#                             data
#                         )
#                     )


#                     st.success(
#                         "Employee updated successfully."
#                     )


#                     st.info(
#                         f"Rows updated: {result}"
#                     )


#                     # Remove cached employee
#                     # so the next load gets fresh data

#                     if (
#                         "employee_to_update"
#                         in st.session_state
#                     ):

#                         del st.session_state[
#                             "employee_to_update"
#                         ]


#                 except Exception as exc:

#                     st.error(
#                         f"Unable to update employee: {exc}"
#                     )






# # ============================================================
# # 5. DELETE EMPLOYEE
# # ============================================================

# elif operation == "Delete Employee":

#     st.header("🗑️ Delete Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     st.warning(
#         "Deleting an employee is permanent."
#     )

#     confirm = st.checkbox(
#         "I confirm that I want to delete this employee."
#     )

#     if st.button(
#         "Delete Employee",
#         type="primary"
#     ):

#         if not confirm:

#             st.error(
#                 "Please confirm deletion first."
#             )

#         else:

#             try:

#                 result = (
#                     employee_service
#                     .delete_employee(
#                         employee_id
#                     )
#                 )

#                 if result:

#                     st.success(
#                         f"Employee {employee_id} "
#                         "deleted successfully."
#                     )

#                 else:

#                     st.warning(
#                         "Employee was not deleted."
#                     )

#             except Exception as exc:

#                 error_message = str(exc)

#                 if "1451" in error_message:

#                     st.error(
#                         "This employee cannot be deleted "
#                         "because they are linked to existing "
#                         "assignment records."
#                     )

#                     st.info(
#                         "Use Update Employee to mark this "
#                         "employee as inactive instead of "
#                         "physically deleting the record."
#                     )

#                 else:

#                     st.error(
#                         f"Unable to delete employee: {exc}"
#                     )



# import sys
# from pathlib import Path

# # ============================================================
# # PROJECT ROOT
# # ============================================================

# PROJECT_ROOT = Path(__file__).resolve().parents[2]

# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))


# # ============================================================
# # IMPORTS
# # ============================================================

# import streamlit as st
# import pandas as pd
# from datetime import date

# from backend.services.employee_service import EmployeeService
# from backend.models.employee import Employee


# # ============================================================
# # PAGE CONFIGURATION
# # ============================================================

# st.set_page_config(
#     page_title="Employees",
#     page_icon="👨‍💼",
#     layout="wide"
# )


# # ============================================================
# # SERVICES
# # ============================================================

# employee_service = EmployeeService()


# # ============================================================
# # DATABASE COLUMN NAMES
# # ============================================================

# EMPLOYEE_COLUMNS = [
#     "EmployeeID",
#     "FirstName",
#     "LastName",
#     "Age",
#     "Gender",
#     "MaritalStatus",
#     "DepartmentID",
#     "JobRole",
#     "JobLevel",
#     "MonthlyIncome",
#     "DailyRate",
#     "HourlyRate",
#     "MonthlyRate",
#     "PercentSalaryHike",
#     "StockOptionLevel",
#     "OverTime",
#     "BusinessTravel",
#     "DistanceFromHome",
#     "Education",
#     "EducationField",
#     "EnvironmentSatisfaction",
#     "JobInvolvement",
#     "JobSatisfaction",
#     "RelationshipSatisfaction",
#     "WorkLifeBalance",
#     "TotalWorkingYears",
#     "TrainingTimesLastYear",
#     "YearsAtCompany",
#     "YearsInCurrentRole",
#     "YearsSinceLastPromotion",
#     "YearsWithCurrManager",
#     "IsActive",
#     "HireDate",
#     "TerminationDate"
# ]


# # ============================================================
# # HELPER FUNCTIONS
# # ============================================================

# def employees_to_dataframe(employees):
#     """
#     Convert repository result tuples into a pandas DataFrame.
#     """

#     return pd.DataFrame(
#         employees,
#         columns=EMPLOYEE_COLUMNS
#     )


# def convert_optional_date(value):
#     """
#     Convert Streamlit date value to a database-friendly value.
#     """

#     if value is None:
#         return None

#     return value


# # ============================================================
# # PAGE TITLE
# # ============================================================

# st.title("👨‍💼 Employee Management")

# st.caption(
#     "Create, view, update and delete employee records."
# )


# # ============================================================
# # SIDEBAR
# # ============================================================

# operation = st.sidebar.radio(
#     "Employee Operations",
#     [
#         "View Employees",
#         "View Employee",
#         "Add Employee",
#         "Update Employee",
#         "Delete Employee"
#     ]
# )


# # ============================================================
# # 1. VIEW ALL EMPLOYEES
# # ============================================================

# if operation == "View Employees":

#     st.header("📋 All Employees")

#     try:

#         employees = employee_service.get_all_employees()

#         if not employees:

#             st.info("No employees found.")

#         else:

#             df = employees_to_dataframe(employees)

#             st.metric(
#                 "Total Employees",
#                 len(df)
#             )

#             st.dataframe(
#                 df,
#                 width="stretch",
#                 hide_index=True
#             )

#     except Exception as exc:

#         st.error(
#             f"Unable to load employees: {exc}"
#         )


# # ============================================================
# # 2. VIEW SINGLE EMPLOYEE
# # ============================================================

# elif operation == "View Employee":

#     st.header("🔍 Find Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     if st.button(
#         "Search Employee",
#         type="primary"
#     ):

#         try:

#             employee = employee_service.get_employee(
#                 employee_id
#             )

#             if employee:

#                 st.success(
#                     f"Employee {employee_id} found."
#                 )

#                 df = employees_to_dataframe(
#                     [employee]
#                 )

#                 st.dataframe(
#                     df,
#                     width="stretch",
#                     hide_index=True
#                 )

#         except Exception as exc:

#             st.error(
#                 f"Unable to find employee: {exc}"
#             )


# # ============================================================
# # 3. CREATE EMPLOYEE
# # ============================================================

# elif operation == "Add Employee":

#     st.header("➕ Add Employee")

#     with st.form("add_employee_form"):

#         # ----------------------------------------------------
#         # BASIC INFORMATION
#         # ----------------------------------------------------

#         st.subheader("Basic Information")

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             employee_id = st.number_input(
#                 "Employee ID",
#                 min_value=1,
#                 step=1
#             )

#             first_name = st.text_input(
#                 "First Name"
#             )

#             last_name = st.text_input(
#                 "Last Name"
#             )

#             age = st.number_input(
#                 "Age",
#                 min_value=18,
#                 max_value=100,
#                 value=25
#             )

#         with col2:

#             gender = st.selectbox(
#                 "Gender",
#                 [
#                     "Male",
#                     "Female",
#                     "Other"
#                 ]
#             )

#             marital_status = st.selectbox(
#                 "Marital Status",
#                 [
#                     "Single",
#                     "Married",
#                     "Divorced"
#                 ]
#             )

#             department_id = st.number_input(
#                 "Department ID",
#                 min_value=1,
#                 step=1
#             )

#             job_role = st.text_input(
#                 "Job Role"
#             )

#         with col3:

#             job_level = st.number_input(
#                 "Job Level",
#                 min_value=1,
#                 max_value=10,
#                 value=1
#             )

#             monthly_income = st.number_input(
#                 "Monthly Income",
#                 min_value=0.0,
#                 step=100.0
#             )

#             daily_rate = st.number_input(
#                 "Daily Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#             hourly_rate = st.number_input(
#                 "Hourly Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#         # ----------------------------------------------------
#         # EMPLOYMENT INFORMATION
#         # ----------------------------------------------------

#         st.subheader("Employment Information")

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             monthly_rate = st.number_input(
#                 "Monthly Rate",
#                 min_value=0.0,
#                 step=1.0
#             )

#             percent_salary_hike = st.number_input(
#                 "Percent Salary Hike",
#                 min_value=0.0,
#                 step=1.0
#             )

#             stock_option_level = st.number_input(
#                 "Stock Option Level",
#                 min_value=0,
#                 step=1
#             )

#         with col2:

#             # IMPORTANT:
#             # Database stores OverTime as INTEGER.
#             #
#             # Yes -> 1
#             # No  -> 0

#             over_time_choice = st.selectbox(
#                 "OverTime",
#                 [
#                     "Yes",
#                     "No"
#                 ]
#             )

#             over_time = (
#                 1
#                 if over_time_choice == "Yes"
#                 else 0
#             )

#             business_travel = st.selectbox(
#                 "Business Travel",
#                 [
#                     "Non-Travel",
#                     "Travel_Rarely",
#                     "Travel_Frequently"
#                 ]
#             )

#             distance_from_home = st.number_input(
#                 "Distance From Home",
#                 min_value=0,
#                 step=1
#             )

#         with col3:

#             education = st.number_input(
#                 "Education",
#                 min_value=0,
#                 step=1
#             )

#             education_field = st.text_input(
#                 "Education Field"
#             )

#         # ----------------------------------------------------
#         # SATISFACTION & PERFORMANCE
#         # ----------------------------------------------------

#         st.subheader(
#             "Satisfaction & Performance"
#         )

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             environment_satisfaction = st.number_input(
#                 "Environment Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             job_involvement = st.number_input(
#                 "Job Involvement",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             job_satisfaction = st.number_input(
#                 "Job Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#         with col2:

#             relationship_satisfaction = st.number_input(
#                 "Relationship Satisfaction",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#             work_life_balance = st.number_input(
#                 "Work Life Balance",
#                 min_value=0,
#                 max_value=5,
#                 value=3
#             )

#         with col3:

#             total_working_years = st.number_input(
#                 "Total Working Years",
#                 min_value=0,
#                 step=1
#             )

#             training_times_last_year = st.number_input(
#                 "Training Times Last Year",
#                 min_value=0,
#                 step=1
#             )

#         # ----------------------------------------------------
#         # COMPANY HISTORY
#         # ----------------------------------------------------

#         st.subheader(
#             "Company History"
#         )

#         col1, col2, col3 = st.columns(3)

#         with col1:

#             years_at_company = st.number_input(
#                 "Years At Company",
#                 min_value=0,
#                 step=1
#             )

#             years_in_current_role = st.number_input(
#                 "Years In Current Role",
#                 min_value=0,
#                 step=1
#             )

#         with col2:

#             years_since_last_promotion = st.number_input(
#                 "Years Since Last Promotion",
#                 min_value=0,
#                 step=1
#             )

#             years_with_curr_manager = st.number_input(
#                 "Years With Current Manager",
#                 min_value=0,
#                 step=1
#             )

#         with col3:

#             is_active = st.checkbox(
#                 "Active Employee",
#                 value=True
#             )

#             hire_date = st.date_input(
#                 "Hire Date",
#                 value=date.today()
#             )

#             termination_date = st.date_input(
#                 "Termination Date",
#                 value=None
#             )

#         # ----------------------------------------------------
#         # SUBMIT
#         # ----------------------------------------------------

#         submitted = st.form_submit_button(
#             "Create Employee"
#         )

#     # ========================================================
#     # CREATE OPERATION
#     # ========================================================

#     if submitted:

#         # ----------------------------------------------------
#         # BASIC VALIDATION
#         # ----------------------------------------------------

#         if not first_name.strip():

#             st.error(
#                 "First name is required."
#             )

#         elif not last_name.strip():

#             st.error(
#                 "Last name is required."
#             )

#         elif not job_role.strip():

#             st.error(
#                 "Job role is required."
#             )

#         else:

#             try:

#                 # ------------------------------------------------
#                 # CREATE EMPLOYEE OBJECT
#                 # ------------------------------------------------

#                 employee = Employee(

#                     employee_id=employee_id,

#                     first_name=first_name.strip(),

#                     last_name=last_name.strip(),

#                     age=age,

#                     gender=gender,

#                     marital_status=marital_status,

#                     department_id=department_id,

#                     job_role=job_role.strip(),

#                     job_level=job_level,

#                     monthly_income=monthly_income,

#                     daily_rate=daily_rate,

#                     hourly_rate=hourly_rate,

#                     monthly_rate=monthly_rate,

#                     percent_salary_hike=percent_salary_hike,

#                     stock_option_level=stock_option_level,

#                     # IMPORTANT:
#                     # 1 or 0, NOT "Yes"/"No"
#                     over_time=over_time,

#                     business_travel=business_travel,

#                     distance_from_home=distance_from_home,

#                     education=education,

#                     education_field=education_field,

#                     environment_satisfaction=(
#                         environment_satisfaction
#                     ),

#                     job_involvement=(
#                         job_involvement
#                     ),

#                     job_satisfaction=(
#                         job_satisfaction
#                     ),

#                     relationship_satisfaction=(
#                         relationship_satisfaction
#                     ),

#                     work_life_balance=(
#                         work_life_balance
#                     ),

#                     total_working_years=(
#                         total_working_years
#                     ),

#                     training_times_last_year=(
#                         training_times_last_year
#                     ),

#                     years_at_company=(
#                         years_at_company
#                     ),

#                     years_in_current_role=(
#                         years_in_current_role
#                     ),

#                     years_since_last_promotion=(
#                         years_since_last_promotion
#                     ),

#                     years_with_curr_manager=(
#                         years_with_curr_manager
#                     ),

#                     is_active=is_active,

#                     hire_date=hire_date,

#                     termination_date=termination_date
#                 )

#                 # ------------------------------------------------
#                 # SERVICE CALL
#                 # ------------------------------------------------

#                 result = (
#                     employee_service
#                     .create_employee(
#                         employee
#                     )
#                 )

#                 st.success(
#                     f"Employee {result} created successfully."
#                 )

#             except Exception as exc:

#                 st.error(
#                     f"Unable to create employee: {exc}"
#                 )


# # ============================================================
# # 4. UPDATE EMPLOYEE
# # ============================================================

# elif operation == "Update Employee":

#     st.header("✏️ Update Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     if st.button(
#         "Load Employee",
#         type="primary"
#     ):

#         try:

#             employee = employee_service.get_employee(
#                 employee_id
#             )

#             st.session_state["employee_to_update"] = employee

#             st.success(
#                 "Employee loaded successfully."
#             )

#         except Exception as exc:

#             st.error(
#                 f"Unable to load employee: {exc}"
#             )

#     employee = st.session_state.get(
#         "employee_to_update"
#     )

#     if employee:

#         st.subheader(
#             f"Updating Employee {employee_id}"
#         )

#         # ----------------------------------------------------
#         # HANDLE DICTIONARY RESPONSE
#         # ----------------------------------------------------

#         if isinstance(employee, dict):

#             def get_value(key, default=None):

#                 if key in employee:
#                     return employee[key]

#                 for existing_key in employee.keys():

#                     if str(existing_key).lower() == key.lower():
#                         return employee[existing_key]

#                 return default

#         else:

#             # Fallback in case the repository returns a tuple

#             def get_value(index, default=None):

#                 try:
#                     return employee[index]

#                 except (
#                     IndexError,
#                     KeyError,
#                     TypeError
#                 ):
#                     return default


#         # ----------------------------------------------------
#         # CURRENT VALUES
#         # ----------------------------------------------------

#         current_first_name = get_value(
#             "FirstName",
#             ""
#         )

#         current_last_name = get_value(
#             "LastName",
#             ""
#         )

#         current_department_id = get_value(
#             "DepartmentID",
#             1
#         )

#         current_job_role = get_value(
#             "JobRole",
#             ""
#         )

#         current_job_level = get_value(
#             "JobLevel",
#             1
#         )

#         current_monthly_income = get_value(
#             "MonthlyIncome",
#             0
#         )

#         current_overtime = get_value(
#             "OverTime",
#             0
#         )

#         current_is_active = get_value(
#             "IsActive",
#             1
#         )

#         current_termination_date = get_value(
#             "TerminationDate",
#             None
#         )


#         # ----------------------------------------------------
#         # CONVERT VALUES
#         # ----------------------------------------------------

#         try:

#             current_department_id = int(
#                 current_department_id or 1
#             )

#         except (
#             ValueError,
#             TypeError
#         ):

#             current_department_id = 1


#         try:

#             current_job_level = int(
#                 current_job_level or 1
#             )

#         except (
#             ValueError,
#             TypeError
#         ):

#             current_job_level = 1


#         try:

#             current_monthly_income = float(
#                 current_monthly_income or 0
#             )

#         except (
#             ValueError,
#             TypeError
#         ):

#             current_monthly_income = 0.0


#         # ----------------------------------------------------
#         # OVERTIME
#         # DATABASE: 1 = YES, 0 = NO
#         # ----------------------------------------------------

#         if str(current_overtime).lower() in (
#             "1",
#             "yes",
#             "true"
#         ):

#             overtime_index = 0

#         else:

#             overtime_index = 1


#         # ----------------------------------------------------
#         # ACTIVE STATUS
#         # ----------------------------------------------------

#         if str(current_is_active).lower() in (
#             "1",
#             "yes",
#             "true"
#         ):

#             current_is_active = True

#         else:

#             current_is_active = False


#         # ----------------------------------------------------
#         # TERMINATION DATE
#         # ----------------------------------------------------

#         if current_termination_date:

#             if hasattr(
#                 current_termination_date,
#                 "date"
#             ):

#                 current_termination_date = (
#                     current_termination_date.date()
#                 )


#         # ----------------------------------------------------
#         # UPDATE FORM
#         # ----------------------------------------------------

#         with st.form(
#             "update_employee_form"
#         ):

#             col1, col2 = st.columns(2)

#             # ------------------------------------------------
#             # LEFT COLUMN
#             # ------------------------------------------------

#             with col1:

#                 first_name = st.text_input(
#                     "First Name",
#                     value=str(
#                         current_first_name or ""
#                     )
#                 )

#                 last_name = st.text_input(
#                     "Last Name",
#                     value=str(
#                         current_last_name or ""
#                     )
#                 )

#                 department_id = st.number_input(
#                     "Department ID",
#                     min_value=1,
#                     value=current_department_id
#                 )

#                 job_role = st.text_input(
#                     "Job Role",
#                     value=str(
#                         current_job_role or ""
#                     )
#                 )

#                 job_level = st.number_input(
#                     "Job Level",
#                     min_value=1,
#                     value=current_job_level
#                 )


#             # ------------------------------------------------
#             # RIGHT COLUMN
#             # ------------------------------------------------

#             with col2:

#                 monthly_income = st.number_input(
#                     "Monthly Income",
#                     min_value=0.0,
#                     value=current_monthly_income
#                 )

#                 over_time_choice = st.selectbox(
#                     "OverTime",
#                     [
#                         "Yes",
#                         "No"
#                     ],
#                     index=overtime_index
#                 )

#                 # IMPORTANT:
#                 # Convert Yes/No to database integer

#                 over_time = (
#                     1
#                     if over_time_choice == "Yes"
#                     else 0
#                 )


#                 is_active = st.checkbox(
#                     "Active Employee",
#                     value=current_is_active
#                 )


#                 termination_date = st.date_input(
#                     "Termination Date",
#                     value=current_termination_date
#                 )


#             # ------------------------------------------------
#             # SUBMIT
#             # ------------------------------------------------

#             submitted = st.form_submit_button(
#                 "Update Employee"
#             )


#         # ----------------------------------------------------
#         # UPDATE DATABASE
#         # ----------------------------------------------------

#         if submitted:

#             if not first_name.strip():

#                 st.error(
#                     "First name is required."
#                 )

#             elif not last_name.strip():

#                 st.error(
#                     "Last name is required."
#                 )

#             elif not job_role.strip():

#                 st.error(
#                     "Job role is required."
#                 )

#             else:

#                 try:

#                     data = {

#                         "first_name":
#                             first_name.strip(),

#                         "last_name":
#                             last_name.strip(),

#                         "department_id":
#                             department_id,

#                         "job_role":
#                             job_role.strip(),

#                         "job_level":
#                             job_level,

#                         "monthly_income":
#                             monthly_income,

#                         # 1 = Yes
#                         # 0 = No
#                         "over_time":
#                             over_time,

#                         "is_active":
#                             is_active,

#                         "termination_date":
#                             termination_date
#                     }


#                     result = (
#                         employee_service
#                         .update_employee(
#                             employee_id,
#                             data
#                         )
#                     )


#                     st.success(
#                         "Employee updated successfully."
#                     )


#                     st.info(
#                         f"Rows updated: {result}"
#                     )


#                     # Remove cached employee
#                     # so the next load gets fresh data

#                     if (
#                         "employee_to_update"
#                         in st.session_state
#                     ):

#                         del st.session_state[
#                             "employee_to_update"
#                         ]


#                 except Exception as exc:

#                     st.error(
#                         f"Unable to update employee: {exc}"
#                     )


# # ============================================================
# # 5. DELETE EMPLOYEE
# # ============================================================

# elif operation == "Delete Employee":

#     st.header("🗑️ Delete Employee")

#     employee_id = st.number_input(
#         "Employee ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     st.warning(
#         "Deleting an employee is permanent."
#     )

#     confirm = st.checkbox(
#         "I confirm that I want to delete this employee."
#     )

#     if st.button(
#         "Delete Employee",
#         type="primary"
#     ):

#         if not confirm:

#             st.error(
#                 "Please confirm deletion first."
#             )

#         else:

#             try:

#                 result = (
#                     employee_service
#                     .delete_employee(
#                         employee_id
#                     )
#                 )

#                 if result:

#                     st.success(
#                         f"Employee {employee_id} "
#                         "deleted successfully."
#                     )

#                 else:

#                     st.warning(
#                         "Employee was not deleted."
#                     )

#             except Exception as exc:

#                 error_message = str(exc)

#                 if "1451" in error_message:

#                     st.error(
#                         "This employee cannot be deleted "
#                         "because they are linked to existing "
#                         "assignment records."
#                     )

#                     st.info(
#                         "Use Update Employee to mark this "
#                         "employee as inactive instead of "
#                         "physically deleting the record."
#                     )

#                 else:

#                     st.error(
#                         f"Unable to delete employee: {exc}"
#                     )


import sys
from pathlib import Path
from datetime import date

# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
import pandas as pd

from backend.services.employee_service import EmployeeService
from backend.models.employee import Employee


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employees",
    page_icon="👨‍💼",
    layout="wide"
)


# ============================================================
# SERVICE
# ============================================================

employee_service = EmployeeService()


# ============================================================
# DATABASE COLUMN NAMES
# ============================================================

EMPLOYEE_COLUMNS = [
    "EmployeeID",
    "FirstName",
    "LastName",
    "Age",
    "Gender",
    "MaritalStatus",
    "DepartmentID",
    "JobRole",
    "JobLevel",
    "MonthlyIncome",
    "DailyRate",
    "HourlyRate",
    "MonthlyRate",
    "PercentSalaryHike",
    "StockOptionLevel",
    "OverTime",
    "BusinessTravel",
    "DistanceFromHome",
    "Education",
    "EducationField",
    "EnvironmentSatisfaction",
    "JobInvolvement",
    "JobSatisfaction",
    "RelationshipSatisfaction",
    "WorkLifeBalance",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
    "IsActive",
    "HireDate",
    "TerminationDate"
]


# ============================================================
# HELPER: CONVERT ANY DATABASE RESULT TO DATAFRAME
# ============================================================

def employees_to_dataframe(employees):
    """
    Safely converts employee repository results into a DataFrame.

    Supports:
        - dictionaries
        - tuples
        - named tuples
        - objects
    """

    if employees is None:
        return pd.DataFrame()

    # --------------------------------------------------------
    # Convert single record into list
    # --------------------------------------------------------

    if isinstance(employees, dict):
        employees = [employees]

    elif not isinstance(employees, (list, tuple)):
        employees = [employees]

    if len(employees) == 0:
        return pd.DataFrame()

    # --------------------------------------------------------
    # DICTIONARY RESULT
    # --------------------------------------------------------

    if isinstance(employees[0], dict):

        df = pd.DataFrame(employees)

        return df

    # --------------------------------------------------------
    # NAMED TUPLE
    # --------------------------------------------------------

    if hasattr(employees[0], "_asdict"):

        return pd.DataFrame(
            [row._asdict() for row in employees]
        )

    # --------------------------------------------------------
    # OBJECT RESULT
    # --------------------------------------------------------

    if hasattr(employees[0], "__dict__"):

        rows = []

        for employee in employees:

            row = {}

            for key, value in vars(employee).items():

                if not key.startswith("_"):
                    row[key] = value

            rows.append(row)

        return pd.DataFrame(rows)

    # --------------------------------------------------------
    # NORMAL TUPLES
    # --------------------------------------------------------

    rows = []

    for employee in employees:

        try:
            rows.append(list(employee))

        except TypeError:
            rows.append([employee])

    # --------------------------------------------------------
    # IMPORTANT:
    # Only use fixed column names if the number of
    # returned values exactly matches the database columns.
    # --------------------------------------------------------

    if len(rows[0]) == len(EMPLOYEE_COLUMNS):

        return pd.DataFrame(
            rows,
            columns=EMPLOYEE_COLUMNS
        )

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    return pd.DataFrame(rows)


# ============================================================
# HELPER: CONVERT SINGLE EMPLOYEE TO DATAFRAME
# ============================================================

def single_employee_to_dataframe(employee):

    if employee is None:
        return pd.DataFrame()

    return employees_to_dataframe([employee])


# ============================================================
# HELPER: GET VALUE FROM EMPLOYEE
# ============================================================

def get_employee_value(
    employee,
    key,
    default=None
):

    if employee is None:
        return default

    # --------------------------------------------------------
    # DICTIONARY
    # --------------------------------------------------------

    if isinstance(employee, dict):

        if key in employee:
            return employee[key]

        key_lower = key.lower()

        for existing_key, value in employee.items():

            if str(existing_key).lower() == key_lower:
                return value

        return default

    # --------------------------------------------------------
    # NAMED TUPLE
    # --------------------------------------------------------

    if hasattr(employee, "_asdict"):

        data = employee._asdict()

        if key in data:
            return data[key]

        key_lower = key.lower()

        for existing_key, value in data.items():

            if str(existing_key).lower() == key_lower:
                return value

        return default

    # --------------------------------------------------------
    # OBJECT
    # --------------------------------------------------------

    if hasattr(employee, key):

        return getattr(employee, key)

    # --------------------------------------------------------
    # NORMAL TUPLE
    #
    # EmployeeID = index 0
    # FirstName  = index 1
    # LastName   = index 2
    # etc.
    # --------------------------------------------------------

    if isinstance(employee, (tuple, list)):

        try:

            index = EMPLOYEE_COLUMNS.index(key)

            return employee[index]

        except (
            ValueError,
            IndexError
        ):

            return default

    return default


# ============================================================
# PAGE TITLE
# ============================================================

st.title("👨‍💼 Employee Management")

st.caption(
    "Create, view, update and delete employee records."
)


# ============================================================
# SIDEBAR
# ============================================================

operation = st.sidebar.radio(
    "Employee Operations",
    [
        "View Employees",
        "View Employee",
        "Add Employee",
        "Update Employee",
        "Delete Employee"
    ]
)


# ============================================================
# 1. VIEW ALL EMPLOYEES
# ============================================================

if operation == "View Employees":

    st.header("📋 All Employees")

    try:

        employees = (
            employee_service
            .get_all_employees()
        )

        # ----------------------------------------------------
        # DEBUG INFORMATION
        # ----------------------------------------------------

        if employees is None:

            st.info(
                "No employees found."
            )

        elif len(employees) == 0:

            st.info(
                "No employees found."
            )

        else:

            df = employees_to_dataframe(
                employees
            )

            if df.empty:

                st.warning(
                    "Employees were fetched from the database, "
                    "but no displayable records were returned."
                )

            else:

                st.metric(
                    "Total Employees",
                    len(df)
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

    except Exception as exc:

        st.error(
            "Unable to load employees."
        )

        st.exception(exc)


# ============================================================
# 2. VIEW SINGLE EMPLOYEE
# ============================================================

elif operation == "View Employee":

    st.header("🔍 Find Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1,
        value=1,
        key="view_employee_id"
    )

    if st.button(
        "Search Employee",
        type="primary"
    ):

        try:

            employee = (
                employee_service
                .get_employee(
                    int(employee_id)
                )
            )

            # ------------------------------------------------
            # EMPLOYEE FOUND
            # ------------------------------------------------

            if employee:

                st.success(
                    f"Employee {int(employee_id)} found."
                )

                df = single_employee_to_dataframe(
                    employee
                )

                if df.empty:

                    st.warning(
                        "Employee was found, but the "
                        "returned data could not be displayed."
                    )

                else:

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

            # ------------------------------------------------
            # EMPLOYEE NOT FOUND
            # ------------------------------------------------

            else:

                st.warning(
                    f"No employee found with Employee ID "
                    f"{int(employee_id)}."
                )

        except Exception as exc:

            st.error(
                f"Unable to find employee: {exc}"
            )

            st.exception(exc)


# ============================================================
# 3. ADD EMPLOYEE
# ============================================================

elif operation == "Add Employee":

    st.header("➕ Add Employee")

    # --------------------------------------------------------
    # FIND NEXT EMPLOYEE ID
    # --------------------------------------------------------

    try:

        existing_employees = (
            employee_service
            .get_all_employees()
        )

        if existing_employees:

            existing_ids = []

            for employee in existing_employees:

                employee_id_value = get_employee_value(
                    employee,
                    "EmployeeID"
                )

                if employee_id_value is not None:

                    try:

                        existing_ids.append(
                            int(employee_id_value)
                        )

                    except (
                        ValueError,
                        TypeError
                    ):
                        pass

            if existing_ids:

                next_employee_id = (
                    max(existing_ids) + 1
                )

            else:

                next_employee_id = 1

        else:

            next_employee_id = 1

    except Exception:

        next_employee_id = 1

    # --------------------------------------------------------
    # FORM
    # --------------------------------------------------------

    with st.form(
        "add_employee_form"
    ):

        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        st.subheader(
            "Basic Information"
        )

        st.info(
            f"Suggested Employee ID for the new employee: "
            f"{next_employee_id}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            employee_id = st.number_input(
                "Employee ID",
                min_value=1,
                value=next_employee_id,
                step=1
            )

            first_name = st.text_input(
                "First Name"
            )

            last_name = st.text_input(
                "Last Name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

        with col2:

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other"
                ]
            )

            marital_status = st.selectbox(
                "Marital Status",
                [
                    "Single",
                    "Married",
                    "Divorced"
                ]
            )

            department_id = st.number_input(
                "Department ID",
                min_value=1,
                step=1
            )

            job_role = st.text_input(
                "Job Role"
            )

        with col3:

            job_level = st.number_input(
                "Job Level",
                min_value=1,
                max_value=10,
                value=1
            )

            monthly_income = st.number_input(
                "Monthly Income",
                min_value=0.0,
                step=100.0
            )

            daily_rate = st.number_input(
                "Daily Rate",
                min_value=0.0,
                step=1.0
            )

            hourly_rate = st.number_input(
                "Hourly Rate",
                min_value=0.0,
                step=1.0
            )

        # ----------------------------------------------------
        # EMPLOYMENT INFORMATION
        # ----------------------------------------------------

        st.subheader(
            "Employment Information"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            monthly_rate = st.number_input(
                "Monthly Rate",
                min_value=0.0,
                step=1.0
            )

            percent_salary_hike = st.number_input(
                "Percent Salary Hike",
                min_value=0.0,
                step=1.0
            )

            stock_option_level = st.number_input(
                "Stock Option Level",
                min_value=0,
                step=1
            )

        with col2:

            over_time_choice = st.selectbox(
                "OverTime",
                [
                    "Yes",
                    "No"
                ]
            )

            over_time = (
                1
                if over_time_choice == "Yes"
                else 0
            )

            business_travel = st.selectbox(
                "Business Travel",
                [
                    "Non-Travel",
                    "Travel_Rarely",
                    "Travel_Frequently"
                ]
            )

            distance_from_home = st.number_input(
                "Distance From Home",
                min_value=0,
                step=1
            )

        with col3:

            education = st.number_input(
                "Education",
                min_value=0,
                step=1
            )

            education_field = st.text_input(
                "Education Field"
            )

        # ----------------------------------------------------
        # SATISFACTION & PERFORMANCE
        # ----------------------------------------------------

        st.subheader(
            "Satisfaction & Performance"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            environment_satisfaction = st.number_input(
                "Environment Satisfaction",
                min_value=0,
                max_value=5,
                value=3
            )

            job_involvement = st.number_input(
                "Job Involvement",
                min_value=0,
                max_value=5,
                value=3
            )

            job_satisfaction = st.number_input(
                "Job Satisfaction",
                min_value=0,
                max_value=5,
                value=3
            )

        with col2:

            relationship_satisfaction = st.number_input(
                "Relationship Satisfaction",
                min_value=0,
                max_value=5,
                value=3
            )

            work_life_balance = st.number_input(
                "Work Life Balance",
                min_value=0,
                max_value=5,
                value=3
            )

        with col3:

            total_working_years = st.number_input(
                "Total Working Years",
                min_value=0,
                step=1
            )

            training_times_last_year = st.number_input(
                "Training Times Last Year",
                min_value=0,
                step=1
            )

        # ----------------------------------------------------
        # COMPANY HISTORY
        # ----------------------------------------------------

        st.subheader(
            "Company History"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            years_at_company = st.number_input(
                "Years At Company",
                min_value=0,
                step=1
            )

            years_in_current_role = st.number_input(
                "Years In Current Role",
                min_value=0,
                step=1
            )

        with col2:

            years_since_last_promotion = st.number_input(
                "Years Since Last Promotion",
                min_value=0,
                step=1
            )

            years_with_curr_manager = st.number_input(
                "Years With Current Manager",
                min_value=0,
                step=1
            )

        with col3:

            is_active = st.checkbox(
                "Active Employee",
                value=True
            )

            hire_date = st.date_input(
                "Hire Date",
                value=date.today()
            )

            termination_date = st.date_input(
                "Termination Date",
                value=None
            )

        # ----------------------------------------------------
        # SUBMIT
        # ----------------------------------------------------

        submitted = st.form_submit_button(
            "Create Employee"
        )

    # ========================================================
    # CREATE OPERATION
    # ========================================================

    if submitted:

        if not first_name.strip():

            st.error(
                "First name is required."
            )

        elif not last_name.strip():

            st.error(
                "Last name is required."
            )

        elif not job_role.strip():

            st.error(
                "Job role is required."
            )

        else:

            try:

                employee = Employee(

                    employee_id=int(employee_id),

                    first_name=first_name.strip(),

                    last_name=last_name.strip(),

                    age=int(age),

                    gender=gender,

                    marital_status=marital_status,

                    department_id=int(department_id),

                    job_role=job_role.strip(),

                    job_level=int(job_level),

                    monthly_income=float(monthly_income),

                    daily_rate=float(daily_rate),

                    hourly_rate=float(hourly_rate),

                    monthly_rate=float(monthly_rate),

                    percent_salary_hike=float(
                        percent_salary_hike
                    ),

                    stock_option_level=int(
                        stock_option_level
                    ),

                    over_time=int(over_time),

                    business_travel=business_travel,

                    distance_from_home=int(
                        distance_from_home
                    ),

                    education=int(education),

                    education_field=education_field,

                    environment_satisfaction=int(
                        environment_satisfaction
                    ),

                    job_involvement=int(
                        job_involvement
                    ),

                    job_satisfaction=int(
                        job_satisfaction
                    ),

                    relationship_satisfaction=int(
                        relationship_satisfaction
                    ),

                    work_life_balance=int(
                        work_life_balance
                    ),

                    total_working_years=int(
                        total_working_years
                    ),

                    training_times_last_year=int(
                        training_times_last_year
                    ),

                    years_at_company=int(
                        years_at_company
                    ),

                    years_in_current_role=int(
                        years_in_current_role
                    ),

                    years_since_last_promotion=int(
                        years_since_last_promotion
                    ),

                    years_with_curr_manager=int(
                        years_with_curr_manager
                    ),

                    is_active=is_active,

                    hire_date=hire_date,

                    termination_date=termination_date
                )

                result = (
                    employee_service
                    .create_employee(
                        employee
                    )
                )

                st.success(
                    f"Employee {result} created successfully."
                )

            except Exception as exc:

                error_message = str(exc)

                if (
                    "1062" in error_message
                    or "Duplicate" in error_message
                    or "already exists" in error_message
                ):

                    st.error(
                        f"Employee ID {employee_id} "
                        "already exists. Please use "
                        "the suggested Employee ID shown above."
                    )

                else:

                    st.error(
                        f"Unable to create employee: {exc}"
                    )


# ============================================================
# 4. UPDATE EMPLOYEE
# ============================================================

elif operation == "Update Employee":

    st.header("✏️ Update Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1,
        value=1,
        key="update_employee_id"
    )

    if st.button(
        "Load Employee",
        type="primary"
    ):

        try:

            employee = (
                employee_service
                .get_employee(
                    int(employee_id)
                )
            )

            if employee:

                st.session_state[
                    "employee_to_update"
                ] = employee

                st.session_state[
                    "loaded_employee_id"
                ] = int(employee_id)

                st.success(
                    "Employee loaded successfully."
                )

            else:

                st.warning(
                    f"Employee {employee_id} not found."
                )

        except Exception as exc:

            st.error(
                f"Unable to load employee: {exc}"
            )

    employee = st.session_state.get(
        "employee_to_update"
    )

    loaded_employee_id = st.session_state.get(
        "loaded_employee_id"
    )

    if employee:

        st.subheader(
            f"Updating Employee {loaded_employee_id}"
        )

        current_first_name = get_employee_value(
            employee,
            "FirstName",
            ""
        )

        current_last_name = get_employee_value(
            employee,
            "LastName",
            ""
        )

        current_department_id = get_employee_value(
            employee,
            "DepartmentID",
            1
        )

        current_job_role = get_employee_value(
            employee,
            "JobRole",
            ""
        )

        current_job_level = get_employee_value(
            employee,
            "JobLevel",
            1
        )

        current_monthly_income = get_employee_value(
            employee,
            "MonthlyIncome",
            0
        )

        current_overtime = get_employee_value(
            employee,
            "OverTime",
            0
        )

        current_is_active = get_employee_value(
            employee,
            "IsActive",
            1
        )

        current_termination_date = get_employee_value(
            employee,
            "TerminationDate",
            None
        )

        # ----------------------------------------------------
        # CONVERT VALUES
        # ----------------------------------------------------

        try:

            current_department_id = int(
                current_department_id or 1
            )

        except (
            ValueError,
            TypeError
        ):

            current_department_id = 1

        try:

            current_job_level = int(
                current_job_level or 1
            )

        except (
            ValueError,
            TypeError
        ):

            current_job_level = 1

        try:

            current_monthly_income = float(
                current_monthly_income or 0
            )

        except (
            ValueError,
            TypeError
        ):

            current_monthly_income = 0.0

        # ----------------------------------------------------
        # OVERTIME
        # ----------------------------------------------------

        if str(current_overtime).lower() in (
            "1",
            "yes",
            "true"
        ):

            overtime_index = 0

        else:

            overtime_index = 1

        # ----------------------------------------------------
        # ACTIVE
        # ----------------------------------------------------

        current_is_active = (
            str(current_is_active).lower()
            in (
                "1",
                "yes",
                "true"
            )
        )

        # ----------------------------------------------------
        # TERMINATION DATE
        # ----------------------------------------------------

        if current_termination_date:

            if hasattr(
                current_termination_date,
                "date"
            ):

                current_termination_date = (
                    current_termination_date.date()
                )

        # ----------------------------------------------------
        # UPDATE FORM
        # ----------------------------------------------------

        with st.form(
            "update_employee_form"
        ):

            col1, col2 = st.columns(2)

            with col1:

                first_name = st.text_input(
                    "First Name",
                    value=str(
                        current_first_name or ""
                    )
                )

                last_name = st.text_input(
                    "Last Name",
                    value=str(
                        current_last_name or ""
                    )
                )

                department_id = st.number_input(
                    "Department ID",
                    min_value=1,
                    value=current_department_id
                )

                job_role = st.text_input(
                    "Job Role",
                    value=str(
                        current_job_role or ""
                    )
                )

                job_level = st.number_input(
                    "Job Level",
                    min_value=1,
                    value=current_job_level
                )

            with col2:

                monthly_income = st.number_input(
                    "Monthly Income",
                    min_value=0.0,
                    value=current_monthly_income
                )

                over_time_choice = st.selectbox(
                    "OverTime",
                    [
                        "Yes",
                        "No"
                    ],
                    index=overtime_index
                )

                over_time = (
                    1
                    if over_time_choice == "Yes"
                    else 0
                )

                is_active = st.checkbox(
                    "Active Employee",
                    value=current_is_active
                )

                termination_date = st.date_input(
                    "Termination Date",
                    value=current_termination_date
                )

            submitted = st.form_submit_button(
                "Update Employee"
            )

        # ----------------------------------------------------
        # UPDATE
        # ----------------------------------------------------

        if submitted:

            if not first_name.strip():

                st.error(
                    "First name is required."
                )

            elif not last_name.strip():

                st.error(
                    "Last name is required."
                )

            elif not job_role.strip():

                st.error(
                    "Job role is required."
                )

            else:

                try:

                    data = {

                        "first_name":
                            first_name.strip(),

                        "last_name":
                            last_name.strip(),

                        "department_id":
                            int(department_id),

                        "job_role":
                            job_role.strip(),

                        "job_level":
                            int(job_level),

                        "monthly_income":
                            float(monthly_income),

                        "over_time":
                            int(over_time),

                        "is_active":
                            is_active,

                        "termination_date":
                            termination_date
                    }

                    result = (
                        employee_service
                        .update_employee(
                            int(loaded_employee_id),
                            data
                        )
                    )

                    st.success(
                        "Employee updated successfully."
                    )

                    st.info(
                        f"Rows updated: {result}"
                    )

                    st.session_state.pop(
                        "employee_to_update",
                        None
                    )

                    st.session_state.pop(
                        "loaded_employee_id",
                        None
                    )

                except Exception as exc:

                    st.error(
                        f"Unable to update employee: {exc}"
                    )


# ============================================================
# 5. DELETE EMPLOYEE
# ============================================================

elif operation == "Delete Employee":

    st.header("🗑️ Delete Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1,
        value=1,
        key="delete_employee_id"
    )

    st.warning(
        "Deleting an employee is permanent."
    )

    confirm = st.checkbox(
        "I confirm that I want to delete this employee."
    )

    if st.button(
        "Delete Employee",
        type="primary"
    ):

        if not confirm:

            st.error(
                "Please confirm deletion first."
            )

        else:

            try:

                result = (
                    employee_service
                    .delete_employee(
                        int(employee_id)
                    )
                )

                if result:

                    st.success(
                        f"Employee {employee_id} "
                        "deleted successfully."
                    )

                else:

                    st.warning(
                        "Employee was not deleted."
                    )

            except Exception as exc:

                error_message = str(exc)

                if (
                    "1451" in error_message
                    or
                    "foreign key constraint"
                    in error_message.lower()
                ):

                    st.error(
                        "This employee cannot be deleted "
                        "because they are linked to existing "
                        "assignment records."
                    )

                    st.info(
                        "Use Update Employee to mark this "
                        "employee as inactive instead of "
                        "physically deleting the record."
                    )

                else:

                    st.error(
                        f"Unable to delete employee: {exc}"
                    )