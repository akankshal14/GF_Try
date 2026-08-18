from backend.exceptions import (
    ValidationException,
    NotFoundException,
    DuplicateException
)

from backend.repositories.employee_repository import (
    EmployeeRepository
)

from backend.utils.logger import get_logger

from backend.utils.validators import (
    validate_required,
    validate_positive,
    validate_non_negative
)


logger = get_logger(__name__)


class EmployeeService:

    def __init__(self):

        self.repository = EmployeeRepository()

    def get_all_employees(self):

        try:

            logger.info(
                "Service: fetching all employees."
            )

            return self.repository.get_all()

        except Exception:

            logger.exception(
                "Failed to get employees."
            )

            raise

    def get_employee(self, employee_id):

        try:

            validate_positive(
                employee_id,
                "Employee ID"
            )

            employee = (
                self.repository
                .get_by_id(employee_id)
            )

            if not employee:

                raise NotFoundException(
                    f"Employee {employee_id} not found."
                )

            return employee

        except Exception:

            logger.exception(
                "Failed to get employee."
            )

            raise

    def create_employee(
        self,
        employee
    ):

        try:

            validate_positive(
                employee.employee_id,
                "Employee ID"
            )

            validate_required(
                employee.first_name,
                "First name"
            )

            validate_required(
                employee.last_name,
                "Last name"
            )

            if employee.age is not None:

                if employee.age < 18:

                    raise ValidationException(
                        "Employee age must be at least 18."
                    )

            if employee.monthly_income is not None:

                validate_non_negative(
                    employee.monthly_income,
                    "Monthly income"
                )

            existing = (
                self.repository
                .get_by_id(
                    employee.employee_id
                )
            )

            if existing:

                raise DuplicateException(
                    f"Employee "
                    f"{employee.employee_id} "
                    f"already exists."
                )

            return self.repository.create(
                employee
            )

        except Exception:

            logger.exception(
                "Failed to create employee."
            )

            raise

    def update_employee(
        self,
        employee_id,
        data
    ):

        try:

            existing = (
                self.repository
                .get_by_id(employee_id)
            )

            if not existing:

                raise NotFoundException(
                    f"Employee {employee_id} not found."
                )

            if data.get("monthly_income") is not None:

                validate_non_negative(
                    data["monthly_income"],
                    "Monthly income"
                )

            return self.repository.update(
                employee_id,
                data
            )

        except Exception:

            logger.exception(
                "Failed to update employee."
            )

            raise

    def delete_employee(
        self,
        employee_id
    ):

        try:

            existing = (
                self.repository
                .get_by_id(employee_id)
            )

            if not existing:

                raise NotFoundException(
                    f"Employee {employee_id} not found."
                )

            return self.repository.delete(
                employee_id
            )

        except Exception:

            logger.exception(
                "Failed to delete employee."
            )

            raise