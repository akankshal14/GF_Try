from datetime import date

from backend.models.employee import Employee
from backend.services.employee_service import EmployeeService
from backend.utils.logger import get_logger


logger = get_logger(__name__)


def test_employee_crud():

    service = EmployeeService()

    employee = Employee(
        employee_id=999999,
        first_name="CRUD",
        last_name="Test",
        age=28,
        gender="Male",
        marital_status="Single",
        department_id=1,
        job_role="Software Engineer",
        job_level=2,
        monthly_income=60000,
        daily_rate=1000,
        hourly_rate=100,
        monthly_rate=30000,
        percent_salary_hike=10,
        stock_option_level=1,
        over_time=0,
        business_travel="Travel_Rarely",
        distance_from_home=5,
        education=3,
        education_field="Technical Degree",
        environment_satisfaction=4,
        job_involvement=3,
        job_satisfaction=4,
        relationship_satisfaction=3,
        work_life_balance=4,
        total_working_years=5,
        training_times_last_year=3,
        years_at_company=3,
        years_in_current_role=2,
        years_since_last_promotion=1,
        years_with_curr_manager=2,
        is_active=True,
        hire_date=date(2023, 1, 10),
        termination_date=None
    )

    # ==========================
    # CREATE
    # ==========================

    print("\n========== CREATE ==========")

    created_id = service.create_employee(employee)

    print("Created Employee ID:", created_id)

    # ==========================
    # READ
    # ==========================

    print("\n========== READ ==========")

    result = service.get_employee(999999)

    print("Employee from database:")
    print(result)

    # ==========================
    # UPDATE
    # ==========================

    print("\n========== UPDATE ==========")

    update_data = {
        "first_name": "CRUD_UPDATED",
        "last_name": "TEST_UPDATED",
        "department_id": 2,
        "job_role": "Senior Software Engineer",
        "job_level": 3,
        "monthly_income": 75000,
        "over_time": 1,
        "is_active": True,
        "termination_date": None
    }

    affected = service.update_employee(
        999999,
        update_data
    )

    print("Rows updated:", affected)

    updated_employee = service.get_employee(999999)

    print("Updated employee:")
    print(updated_employee)

    # ==========================
    # STOP HERE
    # ==========================

    print("\n================================")
    print("CRUD CREATE + READ + UPDATE")
    print("COMPLETED")
    print("Employee 999999 is still in DB.")
    print("================================")


if __name__ == "__main__":
    test_employee_crud()