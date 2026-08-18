# import pandas as pd
# import mysql.connector


# # --------------------------------------------------
# # 1. Load CSV
# # --------------------------------------------------

# csv_file = "IBM_HR_Unified_100k.csv"

# df = pd.read_csv(csv_file, encoding="latin1")

# print(f"CSV loaded successfully: {len(df)} rows")
# print(f"CSV column count: {len(df.columns)}")
# print("CSV columns:")
# print(list(df.columns))


# # --------------------------------------------------
# # 2. Connect to MySQL
# # --------------------------------------------------

# connection = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="Akanksha_1455",
#     database="MINI_PROJECT"
# )

# cursor = connection.cursor()

# print("Connected to MySQL successfully")


# # --------------------------------------------------
# # 3. Insert into staging table
# # --------------------------------------------------

# query = """
# INSERT INTO stg_employees (
#     EmployeeID,
#     FirstName,
#     LastName,
#     Age,
#     Gender,
#     MaritalStatus,
#     DepartmentName,
#     JobRole,
#     JobLevel,
#     MonthlyIncome,
#     DailyRate,
#     HourlyRate,
#     MonthlyRate,
#     PercentSalaryHike,
#     StockOptionLevel,
#     OverTime,
#     BusinessTravel,
#     DistanceFromHome,
#     Education,
#     EducationField,
#     EnvironmentSatisfaction,
#     JobInvolvement,
#     JobSatisfaction,
#     RelationshipSatisfaction,
#     WorkLifeBalance,
#     TotalWorkingYears,
#     TrainingTimesLastYear,
#     YearsAtCompany,
#     YearsInCurrentRole,
#     YearsSinceLastPromotion,
#     YearsWithCurrManager,
#     IsActive,
#     HireDate,
#     TerminationDate,
#     LatestPerformanceRating,
#     AssignedProjectName,
#     ProjectAllocationPercentage,
#     ActiveProjectCount,
#     Attrition
# )
# VALUES (
#     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#     %s, %s, %s, %s, %s, %s, %s, %s,%s
# )
# """


# # --------------------------------------------------
# # 4. Convert DataFrame to records
# # --------------------------------------------------

# records = []

# for _, row in df.iterrows():

#     record = tuple(
#         None if pd.isna(value) else value
#         for value in row
#     )

#     records.append(record)


# # --------------------------------------------------
# # 5. Insert records in batches
# # --------------------------------------------------

# batch_size = 5000

# for i in range(0, len(records), batch_size):

#     batch = records[i:i + batch_size]

#     cursor.executemany(query, batch)

#     connection.commit()

#     print(
#         f"Inserted {min(i + batch_size, len(records))} "
#         f"/ {len(records)} rows"
#     )


# # --------------------------------------------------
# # 6. Close connection
# # --------------------------------------------------

# cursor.close()
# connection.close()

# print("Staging data loaded successfully!")

import pandas as pd
import mysql.connector


# --------------------------------------------------
# 1. Load CSV
# --------------------------------------------------

csv_file = "IBM_HR_Unified_100k.csv"

df = pd.read_csv(csv_file, encoding="latin1")

print(f"CSV loaded successfully: {len(df)} rows")
print(f"CSV column count: {len(df.columns)}")
print("CSV columns:")
print(list(df.columns))


# --------------------------------------------------
# 2. Connect to MySQL
# --------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Akanksha_1455",
    database="MINI_PROJECT"
)

cursor = connection.cursor()

print("Connected to MySQL successfully")


# --------------------------------------------------
# 3. Insert into staging table
# --------------------------------------------------

query = """
INSERT INTO stg_employees (
    EmployeeID,
    FirstName,
    LastName,
    Age,
    Gender,
    MaritalStatus,
    DepartmentName,
    JobRole,
    JobLevel,
    MonthlyIncome,
    DailyRate,
    HourlyRate,
    MonthlyRate,
    PercentSalaryHike,
    StockOptionLevel,
    OverTime,
    BusinessTravel,
    DistanceFromHome,
    Education,
    EducationField,
    EnvironmentSatisfaction,
    JobInvolvement,
    JobSatisfaction,
    RelationshipSatisfaction,
    WorkLifeBalance,
    TotalWorkingYears,
    TrainingTimesLastYear,
    YearsAtCompany,
    YearsInCurrentRole,
    YearsSinceLastPromotion,
    YearsWithCurrManager,
    IsActive,
    HireDate,
    TerminationDate,
    LatestPerformanceRating,
    AssignedProjectName,
    ProjectAllocationPercentage,
    ActiveProjectCount,
    Attrition
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""


# --------------------------------------------------
# 4. Convert date columns to MySQL DATE format
# --------------------------------------------------

df["HireDate"] = pd.to_datetime(
    df["HireDate"],
    format="%d-%m-%Y",
    errors="coerce"
).dt.strftime("%Y-%m-%d")

df["TerminationDate"] = pd.to_datetime(
    df["TerminationDate"],
    format="%d-%m-%Y",
    errors="coerce"
).dt.strftime("%Y-%m-%d")


# --------------------------------------------------
# 5. Convert DataFrame to records
# --------------------------------------------------

records = []

for _, row in df.iterrows():

    record = tuple(
        None if pd.isna(value) else value
        for value in row
    )

    records.append(record)


# --------------------------------------------------
# 6. Insert records in batches
# --------------------------------------------------

batch_size = 5000

for i in range(0, len(records), batch_size):

    batch = records[i:i + batch_size]

    cursor.executemany(query, batch)

    connection.commit()

    print(
        f"Inserted {min(i + batch_size, len(records))} "
        f"/ {len(records)} rows"
    )


# --------------------------------------------------
# 7. Close connection
# --------------------------------------------------

cursor.close()
connection.close()

print("Staging data loaded successfully!")