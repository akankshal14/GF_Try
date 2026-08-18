# # from backend.exceptions import (
# #     ValidationException,
# #     NotFoundException,
# #     DuplicateException
# # )

# # from backend.repositories.department_repository import (
# #     DepartmentRepository
# # )

# # from backend.utils.logger import get_logger
# # from backend.utils.validators import validate_required


# # logger = get_logger(__name__)


# # class DepartmentService:

# #     def __init__(self):

# #         self.repository = DepartmentRepository()

# #     def get_all_departments(self):

# #         try:

# #             return self.repository.get_all()

# #         except Exception:

# #             logger.exception(
# #                 "Failed to get departments."
# #             )

# #             raise

# #     def get_department(
# #         self,
# #         department_id
# #     ):

# #         try:

# #             department = (
# #                 self.repository
# #                 .get_by_id(department_id)
# #             )

# #             if not department:

# #                 raise NotFoundException(
# #                     f"Department "
# #                     f"{department_id} not found."
# #                 )

# #             return department

# #         except Exception:

# #             logger.exception(
# #                 "Failed to get department."
# #             )

# #             raise

# #     def create_department(
# #         self,
# #         department
# #     ):

# #         try:

# #             validate_required(
# #                 department.department_name,
# #                 "Department name"
# #             )

# #             existing = (
# #                 self.repository
# #                 .get_by_name(
# #                     department.department_name
# #                 )
# #             )

# #             if existing:

# #                 raise DuplicateException(
# #                     "Department already exists."
# #                 )

# #             return self.repository.create(
# #                 department
# #             )

# #         except Exception:

# #             logger.exception(
# #                 "Failed to create department."
# #             )

# #             raise

# #     def update_department(
# #         self,
# #         department_id,
# #         department_name
# #     ):

# #         try:

# #             validate_required(
# #                 department_name,
# #                 "Department name"
# #             )

# #             existing = (
# #                 self.repository
# #                 .get_by_id(department_id)
# #             )

# #             if not existing:

# #                 raise NotFoundException(
# #                     "Department not found."
# #                 )

# #             return self.repository.update(
# #                 department_id,
# #                 department_name
# #             )

# #         except Exception:

# #             logger.exception(
# #                 "Failed to update department."
# #             )

# #             raise

# #     def delete_department(
# #         self,
# #         department_id
# #     ):

# #         try:

# #             existing = (
# #                 self.repository
# #                 .get_by_id(department_id)
# #             )

# #             if not existing:

# #                 raise NotFoundException(
# #                     "Department not found."
# #                 )

# #             return self.repository.delete(
# #                 department_id
# #             )

# #         except Exception:

# #             logger.exception(
# #                 "Failed to delete department."
# #             )

# #             raise


# from backend.exceptions import (
#     ValidationException,
#     NotFoundException,
#     DuplicateException
# )

# from backend.repositories.department_repository import (
#     DepartmentRepository
# )

# from backend.utils.logger import get_logger
# from backend.utils.validators import validate_required


# logger = get_logger(__name__)


# class DepartmentService:

#     def __init__(self):

#         self.repository = DepartmentRepository()


#     # =====================================================
#     # GET ALL
#     # =====================================================

#     def get_all_departments(self):

#         try:

#             return self.repository.get_all()

#         except Exception:

#             logger.exception(
#                 "Failed to get departments."
#             )

#             raise


#     # =====================================================
#     # GET BY ID
#     # =====================================================

#     def get_department(
#         self,
#         department_id
#     ):

#         try:

#             department = (
#                 self.repository
#                 .get_by_id(department_id)
#             )

#             if not department:

#                 raise NotFoundException(
#                     f"Department {department_id} not found."
#                 )

#             return department

#         except Exception:

#             logger.exception(
#                 "Failed to get department."
#             )

#             raise


#     # =====================================================
#     # CREATE
#     # =====================================================

#     def create_department(
#         self,
#         department
#     ):

#         try:

#             validate_required(
#                 department.department_name,
#                 "Department name"
#             )

#             existing = (
#                 self.repository
#                 .get_by_name(
#                     department.department_name
#                 )
#             )

#             if existing:

#                 raise DuplicateException(
#                     "Department already exists."
#                 )

#             return self.repository.create(
#                 department
#             )

#         except Exception:

#             logger.exception(
#                 "Failed to create department."
#             )

#             raise


#     # =====================================================
#     # UPDATE
#     # =====================================================

#     def update_department(
#         self,
#         department_id,
#         department_name
#     ):

#         try:

#             validate_required(
#                 department_name,
#                 "Department name"
#             )

#             existing = (
#                 self.repository
#                 .get_by_id(
#                     department_id
#                 )
#             )

#             if not existing:

#                 raise NotFoundException(
#                     "Department not found."
#                 )


#             # ---------------------------------------------
#             # Prevent duplicate department names
#             # ---------------------------------------------

#             duplicate = (
#                 self.repository
#                 .get_by_name(
#                     department_name
#                 )
#             )

#             if duplicate:

#                 # Handle tuple result
#                 if isinstance(
#                     duplicate,
#                     (tuple, list)
#                 ):

#                     duplicate_id = duplicate[0]

#                     if duplicate_id != department_id:

#                         raise DuplicateException(
#                             "Another department with this "
#                             "name already exists."
#                         )

#                 # Handle dict result
#                 elif isinstance(
#                     duplicate,
#                     dict
#                 ):

#                     duplicate_id = (
#                         duplicate.get("DepartmentID")
#                         or duplicate.get("department_id")
#                     )

#                     if duplicate_id != department_id:

#                         raise DuplicateException(
#                             "Another department with this "
#                             "name already exists."
#                         )

#             return self.repository.update(
#                 department_id,
#                 department_name
#             )

#         except Exception:

#             logger.exception(
#                 "Failed to update department."
#             )

#             raise


#     # =====================================================
#     # DELETE
#     # =====================================================

#     def delete_department(
#         self,
#         department_id
#     ):

#         try:

#             existing = (
#                 self.repository
#                 .get_by_id(
#                     department_id
#                 )
#             )

#             if not existing:

#                 raise NotFoundException(
#                     "Department not found."
#                 )

#             return self.repository.delete(
#                 department_id
#             )

#         except Exception:

#             logger.exception(
#                 "Failed to delete department."
#             )

#             raise





from backend.exceptions import (
    NotFoundException,
    DuplicateException
)

from backend.repositories.department_repository import (
    DepartmentRepository
)

from backend.utils.logger import get_logger
from backend.utils.validators import validate_required


logger = get_logger(__name__)


class DepartmentService:

    def __init__(self):

        self.repository = DepartmentRepository()


    # =====================================================
    # GET ALL DEPARTMENTS
    # =====================================================

    def get_all_departments(self):

        try:

            return self.repository.get_all()

        except Exception:

            logger.exception(
                "Failed to get departments."
            )

            raise


    # =====================================================
    # GET DEPARTMENT BY ID
    # =====================================================

    def get_department(
        self,
        department_id
    ):

        try:

            department_id = int(
                department_id
            )

            department = (
                self.repository
                .get_by_id(
                    department_id
                )
            )

            if not department:

                raise NotFoundException(
                    f"Department {department_id} "
                    f"not found."
                )

            return department

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception:

            logger.exception(
                "Failed to get department."
            )

            raise


    # =====================================================
    # CREATE DEPARTMENT
    # =====================================================

    def create_department(
        self,
        department_name
    ):

        try:

            # ---------------------------------------------
            # Validate ID/name input
            # ---------------------------------------------

            validate_required(
                department_name,
                "Department name"
            )

            department_name = (
                department_name.strip()
            )

            # ---------------------------------------------
            # Check duplicate
            # ---------------------------------------------

            existing = (
                self.repository
                .get_by_name(
                    department_name
                )
            )

            if existing:

                raise DuplicateException(
                    "Department already exists."
                )

            # ---------------------------------------------
            # Insert
            # ---------------------------------------------

            return self.repository.create(
                department_name
            )

        except Exception:

            logger.exception(
                "Failed to create department."
            )

            raise


    # =====================================================
    # UPDATE DEPARTMENT
    # =====================================================

    def update_department(
        self,
        department_id,
        department_name
    ):

        try:

            department_id = int(
                department_id
            )

            # ---------------------------------------------
            # Validate name
            # ---------------------------------------------

            validate_required(
                department_name,
                "Department name"
            )

            department_name = (
                department_name.strip()
            )

            # ---------------------------------------------
            # Check existing department
            # ---------------------------------------------

            existing = (
                self.repository
                .get_by_id(
                    department_id
                )
            )

            if not existing:

                raise NotFoundException(
                    f"Department {department_id} "
                    f"not found."
                )

            # ---------------------------------------------
            # Check duplicate name
            # ---------------------------------------------

            duplicate = (
                self.repository
                .get_by_name(
                    department_name
                )
            )

            if duplicate:

                duplicate_id = (
                    self.repository
                    .extract_department_id(
                        duplicate
                    )
                )

                if (
                    duplicate_id != department_id
                ):

                    raise DuplicateException(
                        "Another department with "
                        "this name already exists."
                    )

            # ---------------------------------------------
            # Update
            # ---------------------------------------------

            return self.repository.update(
                department_id,
                department_name
            )

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception:

            logger.exception(
                "Failed to update department."
            )

            raise


    # =====================================================
    # DELETE DEPARTMENT
    # =====================================================

    def delete_department(
        self,
        department_id
    ):

        try:

            department_id = int(
                department_id
            )

            # ---------------------------------------------
            # Check department exists
            # ---------------------------------------------

            existing = (
                self.repository
                .get_by_id(
                    department_id
                )
            )

            if not existing:

                raise NotFoundException(
                    f"Department {department_id} "
                    f"not found."
                )

            # ---------------------------------------------
            # Delete
            # ---------------------------------------------

            return self.repository.delete(
                department_id
            )

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception:

            logger.exception(
                "Failed to delete department."
            )

            raise