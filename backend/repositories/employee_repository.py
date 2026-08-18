from backend.database.db_manager import DatabaseConnection
from backend.exceptions import DatabaseException
from backend.utils.logger import get_logger


logger = get_logger(__name__)


class EmployeeRepository:

    def __init__(self):

        self.db = DatabaseConnection()

        logger.info(
            "EmployeeRepository initialized."
        )

    def get_all(self):

        query = """
            SELECT
                EmployeeID,
                FirstName,
                LastName,
                Age,
                Gender,
                MaritalStatus,
                DepartmentID,
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
                TerminationDate
            FROM Employees
            ORDER BY EmployeeID
        """

        cursor = None

        try:

            logger.info(
                "Fetching all employees."
            )

            cursor = self.db.get_cursor("oltp")

            cursor.execute(query)

            result = cursor.fetchall()

            logger.info(
                "Fetched %d employees.",
                len(result)
            )

            return result

        except Exception as e:

            logger.exception(
                "Failed to fetch employees."
            )

            raise DatabaseException(
                f"Failed to fetch employees: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_by_id(self, employee_id):

        query = """
            SELECT *
            FROM Employees
            WHERE EmployeeID = %s
        """

        cursor = None

        try:

            logger.info(
                "Fetching employee %s.",
                employee_id
            )

            cursor = self.db.get_cursor("oltp")

            cursor.execute(
                query,
                (employee_id,)
            )

            result = cursor.fetchone()

            return result

        except Exception as e:

            logger.exception(
                "Failed to fetch employee %s.",
                employee_id
            )

            raise DatabaseException(
                f"Failed to fetch employee: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def create(self, employee):

        query = """
            INSERT INTO Employees
            (
                EmployeeID,
                FirstName,
                LastName,
                Age,
                Gender,
                MaritalStatus,
                DepartmentID,
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
                TerminationDate
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s
            )
        """

        values = (
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.age,
            employee.gender,
            employee.marital_status,
            employee.department_id,
            employee.job_role,
            employee.job_level,
            employee.monthly_income,
            employee.daily_rate,
            employee.hourly_rate,
            employee.monthly_rate,
            employee.percent_salary_hike,
            employee.stock_option_level,
            employee.over_time,
            employee.business_travel,
            employee.distance_from_home,
            employee.education,
            employee.education_field,
            employee.environment_satisfaction,
            employee.job_involvement,
            employee.job_satisfaction,
            employee.relationship_satisfaction,
            employee.work_life_balance,
            employee.total_working_years,
            employee.training_times_last_year,
            employee.years_at_company,
            employee.years_in_current_role,
            employee.years_since_last_promotion,
            employee.years_with_curr_manager,
            employee.is_active,
            employee.hire_date,
            employee.termination_date
        )

        cursor = None

        try:

            connection = self.db.connect("oltp")

            cursor = connection.cursor()

            cursor.execute(
                query,
                values
            )

            self.db.commit("oltp")

            logger.info(
                "Employee %s created.",
                employee.employee_id
            )

            return employee.employee_id

        except Exception as e:

            self.db.rollback("oltp")

            logger.exception(
                "Failed to create employee."
            )

            raise DatabaseException(
                f"Failed to create employee: {e}"
            )

        finally:

            if cursor:
                cursor.close()
    

    def update(self, employee_id, data):

        query = """
            UPDATE Employees
            SET
                FirstName = %s,
                LastName = %s,
                DepartmentID = %s,
                JobRole = %s,
                JobLevel = %s,
                MonthlyIncome = %s,
                OverTime = %s,
                IsActive = %s,
                TerminationDate = %s
            WHERE EmployeeID = %s
        """

        values = (
            data["first_name"],
            data["last_name"],
            data["department_id"],
            data["job_role"],
            data["job_level"],
            data["monthly_income"],
            data["over_time"],
            data["is_active"],
            data["termination_date"],
            employee_id
        )

        cursor = None

        try:

            connection = self.db.connect("oltp")

            cursor = connection.cursor()

            cursor.execute(
                query,
                values
            )

            self.db.commit("oltp")

            return cursor.rowcount

        except Exception as e:

            self.db.rollback("oltp")

            logger.exception(
                "Failed to update employee %s.",
                employee_id
            )

            raise DatabaseException(
                f"Failed to update employee: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def delete(self, employee_id):

        query = """
            DELETE FROM Employees
            WHERE EmployeeID = %s
        """

        cursor = None

        try:

            connection = self.db.connect("oltp")

            cursor = connection.cursor()

            cursor.execute(
                query,
                (employee_id,)
            )

            self.db.commit("oltp")

            return cursor.rowcount

        except Exception as e:

            self.db.rollback("oltp")

            logger.exception(
                "Failed to delete employee %s.",
                employee_id
            )

            raise DatabaseException(
                f"Failed to delete employee: {e}"
            )

        finally:

            if cursor:
                cursor.close()