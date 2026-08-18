from backend.repositories.analytics_repository import (
    AnalyticsRepository
)

from backend.utils.logger import get_logger


logger = get_logger(__name__)


class AnalyticsService:

    def __init__(self):

        self.repository = AnalyticsRepository()

    def get_employee_count(self):

        try:

            return (
                self.repository
                .get_employee_count()
            )

        except Exception:

            logger.exception(
                "Failed to get employee count."
            )

            raise

    def get_department_performance(self):

        try:

            return (
                self.repository
                .get_department_performance()
            )

        except Exception:

            logger.exception(
                "Failed to get department performance."
            )

            raise

    def get_yearly_performance(self):

        try:

            return (
                self.repository
                .get_yearly_performance()
            )

        except Exception:

            logger.exception(
                "Failed to get yearly performance."
            )

            raise

    def get_top_employees(self):

        try:

            return (
                self.repository
                .get_top_employees()
            )

        except Exception:

            logger.exception(
                "Failed to get top employees."
            )

            raise

    def get_project_performance(self):

        try:

            return (
                self.repository
                .get_project_performance()
            )

        except Exception:

            logger.exception(
                "Failed to get project performance."
            )

            raise

    def get_rating_distribution(self):

        try:

            return (
                self.repository
                .get_rating_distribution()
            )

        except Exception:

            logger.exception(
                "Failed to get rating distribution."
            )

            raise

    def get_overtime_performance(self):

        try:

            return (
                self.repository
                .get_overtime_performance()
            )

        except Exception:

            logger.exception(
                "Failed to get overtime performance."
            )

            raise

    def get_monthly_performance(self):

        try:

            return (
                self.repository
                .get_monthly_performance()
            )

        except Exception:

            logger.exception(
                "Failed to get monthly performance."
            )

            raise