from backend.database.db_manager import DatabaseConnection
from backend.exceptions import DatabaseException
from backend.utils.logger import get_logger


logger = get_logger(__name__)


class AnalyticsRepository:

    def __init__(self):

        self.db = DatabaseConnection()

    def get_employee_count(self):

        query = """
            SELECT COUNT(*) AS EmployeeCount
            FROM Dim_Employee
            WHERE IsCurrent = 1
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            result = cursor.fetchone()

            return result["EmployeeCount"]

        except Exception as e:

            logger.exception(
                "Failed to get employee count."
            )

            raise DatabaseException(
                f"Failed to get employee count: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_department_performance(self):

        query = """
            SELECT
                d.DepartmentName,
                AVG(
                    f.PerformanceRating
                ) AS AverageRating,
                COUNT(
                    f.PerformanceReviewSK
                ) AS ReviewCount
            FROM Fact_PerformanceReviews f
            INNER JOIN Dim_Department d
                ON f.DepartmentSK = d.DepartmentSK
            GROUP BY
                d.DepartmentName
            ORDER BY
                AverageRating DESC
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get department performance."
            )

            raise DatabaseException(
                f"Failed to get department performance: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_yearly_performance(self):

        query = """
            SELECT
                d.Year,
                AVG(
                    f.PerformanceRating
                ) AS AverageRating,
                COUNT(
                    f.PerformanceReviewSK
                ) AS ReviewCount
            FROM Fact_PerformanceReviews f
            INNER JOIN Dim_Date d
                ON f.ReviewDateKey = d.DateKey
            GROUP BY
                d.Year
            ORDER BY
                d.Year
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get yearly performance."
            )

            raise DatabaseException(
                f"Failed to get yearly performance: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_top_employees(self):

        query = """
            WITH EmployeePerformance AS
            (
                SELECT
                    e.EmployeeID,
                    e.JobRole,
                    AVG(
                        f.PerformanceRating
                    ) AS AverageRating
                FROM Fact_PerformanceReviews f
                INNER JOIN Dim_Employee e
                    ON f.EmployeeSK = e.EmployeeSK
                WHERE e.IsCurrent = 1
                GROUP BY
                    e.EmployeeID,
                    e.JobRole
            ),

            RankedEmployees AS
            (
                SELECT
                    EmployeeID,
                    JobRole,
                    AverageRating,
                    DENSE_RANK() OVER
                    (
                        ORDER BY
                            AverageRating DESC
                    ) AS EmployeeRank
                FROM EmployeePerformance
            )

            SELECT
                EmployeeID,
                JobRole,
                AverageRating,
                EmployeeRank
            FROM RankedEmployees
            WHERE EmployeeRank <= 10
            ORDER BY EmployeeRank
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get top employees."
            )

            raise DatabaseException(
                f"Failed to get top employees: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_project_performance(self):

        query = """
            SELECT
                p.ProjectID,
                p.ProjectName,
                AVG(
                    f.PerformanceRating
                ) AS AverageRating,
                COUNT(
                    f.PerformanceReviewSK
                ) AS ReviewCount
            FROM Fact_PerformanceReviews f
            INNER JOIN Dim_Project p
                ON f.ProjectSK = p.ProjectSK
            GROUP BY
                p.ProjectID,
                p.ProjectName
            ORDER BY
                AverageRating DESC
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get project performance."
            )

            raise DatabaseException(
                f"Failed to get project performance: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_rating_distribution(self):

        query = """
            SELECT
                PerformanceRating,
                COUNT(*) AS RatingCount
            FROM Fact_PerformanceReviews
            GROUP BY PerformanceRating
            ORDER BY PerformanceRating
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get rating distribution."
            )

            raise DatabaseException(
                f"Failed to get rating distribution: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_overtime_performance(self):

        query = """
            SELECT
                e.OverTime,
                AVG(
                    f.PerformanceRating
                ) AS AverageRating,
                COUNT(*) AS EmployeeReviews
            FROM Fact_PerformanceReviews f
            INNER JOIN Dim_Employee e
                ON f.EmployeeSK = e.EmployeeSK
            WHERE e.IsCurrent = 1
            GROUP BY e.OverTime
            ORDER BY AverageRating DESC
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get overtime performance."
            )

            raise DatabaseException(
                f"Failed to get overtime performance: {e}"
            )

        finally:

            if cursor:
                cursor.close()

    def get_monthly_performance(self):

        query = """
            SELECT
                d.Year,
                d.Month,
                d.MonthName,
                AVG(
                    f.PerformanceRating
                ) AS AverageRating,
                COUNT(*) AS ReviewCount
            FROM Fact_PerformanceReviews f
            INNER JOIN Dim_Date d
                ON f.ReviewDateKey = d.DateKey
            GROUP BY
                d.Year,
                d.Month,
                d.MonthName
            ORDER BY
                d.Year,
                d.Month
        """

        cursor = None

        try:

            cursor = self.db.get_cursor("olap")

            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to get monthly performance."
            )

            raise DatabaseException(
                f"Failed to get monthly performance: {e}"
            )

        finally:

            if cursor:
                cursor.close()