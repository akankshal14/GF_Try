from backend.database.db_manager import (
    DatabaseConnection
)

from backend.services.employee_service import (
    EmployeeService
)

from backend.services.department_service import (
    DepartmentService
)

from backend.services.project_service import (
    ProjectService
)

from backend.services.assignment_service import (
    AssignmentService
)

from backend.services.review_service import (
    ReviewService
)

from backend.services.analytics_service import (
    AnalyticsService
)

from backend.exceptions import BackendException

from backend.utils.logger import get_logger


logger = get_logger(__name__)


def main():

    db = DatabaseConnection()

    try:

        logger.info(
            "========================================"
        )

        logger.info(
            "Starting backend test."
        )

        logger.info(
            "========================================"
        )

        # ------------------------------------
        # Test OLTP
        # ------------------------------------

        oltp = db.connect("oltp")

        logger.info(
            "OLTP database connected successfully."
        )

        cursor = oltp.cursor()

        cursor.execute(
            "SELECT DATABASE()"
        )

        logger.info(
            "OLTP database: %s",
            cursor.fetchone()
        )

        cursor.close()

        # ------------------------------------
        # Test OLAP
        # ------------------------------------

        olap = db.connect("olap")

        logger.info(
            "OLAP database connected successfully."
        )

        cursor = olap.cursor()

        cursor.execute(
            "SELECT DATABASE()"
        )

        logger.info(
            "OLAP database: %s",
            cursor.fetchone()
        )

        cursor.close()

        # ------------------------------------
        # Initialize services
        # ------------------------------------

        employee_service = (
            EmployeeService()
        )

        department_service = (
            DepartmentService()
        )

        project_service = (
            ProjectService()
        )

        assignment_service = (
            AssignmentService()
        )

        review_service = (
            ReviewService()
        )

        analytics_service = (
            AnalyticsService()
        )

        # ------------------------------------
        # Employee
        # ------------------------------------

        employees = (
            employee_service
            .get_all_employees()
        )

        print(
            f"Employees: {len(employees)}"
        )

        # ------------------------------------
        # Departments
        # ------------------------------------

        departments = (
            department_service
            .get_all_departments()
        )

        print(
            f"Departments: {len(departments)}"
        )

        # ------------------------------------
        # Projects
        # ------------------------------------

        projects = (
            project_service
            .get_all_projects()
        )

        print(
            f"Projects: {len(projects)}"
        )

        # ------------------------------------
        # Assignments
        # ------------------------------------

        assignments = (
            assignment_service
            .get_all_assignments()
        )

        print(
            f"Assignments: {len(assignments)}"
        )

        # ------------------------------------
        # Reviews
        # ------------------------------------

        reviews = (
            review_service
            .get_all_reviews()
        )

        print(
            f"Reviews: {len(reviews)}"
        )

        # ------------------------------------
        # Analytics
        # ------------------------------------

        employee_count = (
            analytics_service
            .get_employee_count()
        )

        print(
            f"OLAP Employee Count: "
            f"{employee_count}"
        )

        department_performance = (
            analytics_service
            .get_department_performance()
        )

        print(
            "Department Performance:",
            len(department_performance)
        )

        yearly = (
            analytics_service
            .get_yearly_performance()
        )

        print(
            "Yearly Performance:",
            len(yearly)
        )

        top_employees = (
            analytics_service
            .get_top_employees()
        )

        print(
            "Top Employees:",
            len(top_employees)
        )

        project_performance = (
            analytics_service
            .get_project_performance()
        )

        print(
            "Project Performance:",
            len(project_performance)
        )

        rating_distribution = (
            analytics_service
            .get_rating_distribution()
        )

        print(
            "Rating Distribution:",
            len(rating_distribution)
        )

        print()
        print(
            "========================================"
        )
        print(
            "BACKEND TEST COMPLETED SUCCESSFULLY"
        )
        print(
            "========================================"
        )

    except BackendException as e:

        logger.exception(
            "Backend error occurred."
        )

        print(
            f"Backend Error: {e}"
        )

    except Exception as e:

        logger.exception(
            "Unexpected error occurred."
        )

        print(
            f"Unexpected Error: {e}"
        )

    finally:

        db.close()


if __name__ == "__main__":
    main()