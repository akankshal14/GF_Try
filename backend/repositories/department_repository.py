# from backend.database.db_manager import DatabaseConnection
# from backend.exceptions import DatabaseException
# from backend.utils.logger import get_logger


# logger = get_logger(__name__)


# class DepartmentRepository:

#     def __init__(self):

#         self.db = DatabaseConnection()

#     def get_all(self):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM Departments
#             ORDER BY DepartmentID
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(query)

#             return cursor.fetchall()

#         except Exception as e:

#             logger.exception(
#                 "Failed to fetch departments."
#             )

#             raise DatabaseException(
#                 f"Failed to fetch departments: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     def get_by_id(self, department_id):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM Departments
#             WHERE DepartmentID = %s
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(
#                 query,
#                 (department_id,)
#             )

#             return cursor.fetchone()

#         except Exception as e:

#             logger.exception(
#                 "Failed to fetch department."
#             )

#             raise DatabaseException(
#                 f"Failed to fetch department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     def get_by_name(self, department_name):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM Departments
#             WHERE DepartmentName = %s
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(
#                 query,
#                 (department_name,)
#             )

#             return cursor.fetchone()

#         except Exception as e:

#             logger.exception(
#                 "Failed to find department."
#             )

#             raise DatabaseException(
#                 f"Failed to find department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     def create(self, department):

#         query = """
#             INSERT INTO Departments
#             (DepartmentName)
#             VALUES (%s)
#         """

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 (department.department_name,)
#             )

#             self.db.commit("oltp")

#             return cursor.lastrowid

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to create department."
#             )

#             raise DatabaseException(
#                 f"Failed to create department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     def update(
#         self,
#         department_id,
#         department_name
#     ):

#         query = """
#             UPDATE Departments
#             SET DepartmentName = %s
#             WHERE DepartmentID = %s
#         """

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 (
#                     department_name,
#                     department_id
#                 )
#             )

#             self.db.commit("oltp")

#             return cursor.rowcount

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to update department."
#             )

#             raise DatabaseException(
#                 f"Failed to update department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     def delete(self, department_id):

#         query = """
#             DELETE FROM Departments
#             WHERE DepartmentID = %s
#         """

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 (department_id,)
#             )

#             self.db.commit("oltp")

#             return cursor.rowcount

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to delete department."
#             )

#             raise DatabaseException(
#                 f"Failed to delete department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()





# import sys
# from pathlib import Path

# # =========================================================
# # PROJECT ROOT
# # =========================================================

# PROJECT_ROOT = Path(__file__).resolve().parents[2]

# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))


# # =========================================================
# # IMPORTS
# # =========================================================

# import streamlit as st

# from utils.helpers import records_to_dataframe

# from backend.services.department_service import DepartmentService
# from backend.models.department import Department


# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="Departments",
#     page_icon="🏢",
#     layout="wide"
# )


# # =========================================================
# # SERVICE
# # =========================================================

# service = DepartmentService()


# # =========================================================
# # TITLE
# # =========================================================

# st.title("🏢 Department Management")

# st.caption(
#     "Create, view, update and delete department records."
# )


# # =========================================================
# # SIDEBAR
# # =========================================================

# operation = st.sidebar.radio(
#     "Department Operations",
#     [
#         "View Departments",
#         "View Department",
#         "Add Department",
#         "Update Department",
#         "Delete Department"
#     ]
# )


# # =========================================================
# # 1. VIEW ALL
# # =========================================================

# if operation == "View Departments":

#     st.header("📋 All Departments")

#     try:

#         departments = (
#             service
#             .get_all_departments()
#         )

#         if not departments:

#             st.info(
#                 "No departments found."
#             )

#         else:

#             df = records_to_dataframe(
#                 departments
#             )

#             st.metric(
#                 "Total Departments",
#                 len(df)
#             )

#             st.dataframe(
#                 df,
#                 width="stretch",
#                 hide_index=True
#             )

#     except Exception as exc:

#         st.error(
#             f"Unable to load departments: {exc}"
#         )


# # =========================================================
# # 2. VIEW SINGLE DEPARTMENT
# # =========================================================

# elif operation == "View Department":

#     st.header("🔍 Find Department")

#     department_id = st.number_input(
#         "Department ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     if st.button(
#         "Search Department",
#         type="primary"
#     ):

#         try:

#             department = (
#                 service
#                 .get_department(
#                     department_id
#                 )
#             )

#             if department:

#                 st.success(
#                     f"Department {department_id} found."
#                 )

#                 df = records_to_dataframe(
#                     [department]
#                 )

#                 st.dataframe(
#                     df,
#                     width="stretch",
#                     hide_index=True
#                 )

#         except Exception as exc:

#             st.error(
#                 f"Unable to find department: {exc}"
#             )


# # =========================================================
# # 3. ADD DEPARTMENT
# # =========================================================

# elif operation == "Add Department":

#     st.header("➕ Add Department")

#     with st.form(
#         "department_create"
#     ):

#         department_name = st.text_input(
#             "Department Name"
#         )

#         submitted = (
#             st.form_submit_button(
#                 "Create Department"
#             )
#         )


#     # =====================================================
#     # CREATE
#     # =====================================================

#     if submitted:

#         if not department_name.strip():

#             st.error(
#                 "Department name is required."
#             )

#         else:

#             try:

#                 department = Department(
#                     department_name=(
#                         department_name.strip()
#                     )
#                 )

#                 result = (
#                     service
#                     .create_department(
#                         department
#                     )
#                 )

#                 st.success(
#                     "Department created successfully."
#                 )

#                 if result is not None:

#                     st.info(
#                         f"Created Department ID: {result}"
#                     )

#             except Exception as exc:

#                 st.error(
#                     f"Unable to create department: {exc}"
#                 )


# # =========================================================
# # 4. UPDATE DEPARTMENT
# # =========================================================

# elif operation == "Update Department":

#     st.header("✏️ Update Department")

#     department_id = st.number_input(
#         "Department ID",
#         min_value=1,
#         step=1,
#         value=1
#     )


#     # =====================================================
#     # LOAD
#     # =====================================================

#     if st.button(
#         "Load Department",
#         type="primary"
#     ):

#         try:

#             department = (
#                 service
#                 .get_department(
#                     department_id
#                 )
#             )

#             st.session_state[
#                 "department_to_update"
#             ] = department

#             st.session_state[
#                 "loaded_department_id"
#             ] = department_id

#             st.success(
#                 "Department loaded successfully."
#             )

#         except Exception as exc:

#             st.error(
#                 f"Unable to load department: {exc}"
#             )


#     # =====================================================
#     # GET CACHED DEPARTMENT
#     # =====================================================

#     department = st.session_state.get(
#         "department_to_update"
#     )


#     if department:

#         # -------------------------------------------------
#         # Extract current name
#         # -------------------------------------------------

#         if isinstance(
#             department,
#             dict
#         ):

#             current_name = (
#                 department.get(
#                     "DepartmentName",
#                     department.get(
#                         "department_name",
#                         ""
#                     )
#                 )
#             )

#         else:

#             # Repository returns tuple:
#             #
#             # (DepartmentID, DepartmentName)

#             try:

#                 current_name = department[1]

#             except (
#                 IndexError,
#                 KeyError,
#                 TypeError
#             ):

#                 current_name = ""


#         # =================================================
#         # UPDATE FORM
#         # =================================================

#         with st.form(
#             "department_update"
#         ):

#             department_name = st.text_input(
#                 "Department Name",
#                 value=str(
#                     current_name or ""
#                 )
#             )

#             submitted = (
#                 st.form_submit_button(
#                     "Update Department"
#                 )
#             )


#         # =================================================
#         # UPDATE
#         # =================================================

#         if submitted:

#             if not department_name.strip():

#                 st.error(
#                     "Department name is required."
#                 )

#             else:

#                 try:

#                     result = (
#                         service
#                         .update_department(
#                             department_id,
#                             department_name.strip()
#                         )
#                     )

#                     st.success(
#                         "Department updated successfully."
#                     )

#                     st.info(
#                         f"Rows updated: {result}"
#                     )

#                     # Clear cached department

#                     st.session_state.pop(
#                         "department_to_update",
#                         None
#                     )

#                     st.session_state.pop(
#                         "loaded_department_id",
#                         None
#                     )

#                 except Exception as exc:

#                     st.error(
#                         f"Unable to update department: {exc}"
#                     )


# # =========================================================
# # 5. DELETE DEPARTMENT
# # =========================================================

# elif operation == "Delete Department":

#     st.header("🗑️ Delete Department")

#     department_id = st.number_input(
#         "Department ID",
#         min_value=1,
#         step=1,
#         value=1
#     )

#     st.warning(
#         "Deleting a department is permanent."
#     )

#     st.info(
#         "A department cannot be deleted if employees "
#         "are still assigned to it."
#     )

#     confirm = st.checkbox(
#         "I confirm that I want to delete this department."
#     )


#     if st.button(
#         "Delete Department",
#         type="primary"
#     ):

#         if not confirm:

#             st.error(
#                 "Please confirm deletion."
#             )

#         else:

#             try:

#                 result = (
#                     service
#                     .delete_department(
#                         department_id
#                     )
#                 )

#                 if result:

#                     st.success(
#                         f"Department {department_id} "
#                         "deleted successfully."
#                     )

#                 else:

#                     st.warning(
#                         "No department was deleted."
#                     )

#             except Exception as exc:

#                 error_message = str(exc)

#                 # MySQL foreign key violation
#                 if (
#                     "1451" in error_message
#                     or "foreign key constraint" in
#                     error_message.lower()
#                 ):

#                     st.error(
#                         "This department cannot be deleted "
#                         "because employees are currently "
#                         "assigned to it."
#                     )

#                     st.info(
#                         "Update or reassign those employees "
#                         "to another department first."
#                     )

#                 else:

#                     st.error(
#                         f"Unable to delete department: {exc}"
#                     )




# from backend.database.db_manager import DatabaseConnection
# from backend.exceptions import DatabaseException
# from backend.utils.logger import get_logger


# logger = get_logger(__name__)


# class DepartmentRepository:

#     def __init__(self):

#         self.db = DatabaseConnection()

#     # =====================================================
#     # GET ALL
#     # =====================================================

#     def get_all(self):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM MINI_PROJECT.Departments
#             ORDER BY DepartmentID
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(query)

#             return cursor.fetchall()

#         except Exception as e:

#             logger.exception(
#                 "Failed to fetch departments."
#             )

#             raise DatabaseException(
#                 f"Failed to fetch departments: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     # =====================================================
#     # GET BY ID
#     # =====================================================

#     def get_by_id(self, department_id):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM MINI_PROJECT.Departments
#             WHERE DepartmentID = %s
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(
#                 query,
#                 (int(department_id),)
#             )

#             return cursor.fetchone()

#         except Exception as e:

#             logger.exception(
#                 "Failed to fetch department."
#             )

#             raise DatabaseException(
#                 f"Failed to fetch department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     # =====================================================
#     # GET BY NAME
#     # =====================================================

#     def get_by_name(self, department_name):

#         query = """
#             SELECT
#                 DepartmentID,
#                 DepartmentName
#             FROM MINI_PROJECT.Departments
#             WHERE DepartmentName = %s
#         """

#         cursor = None

#         try:

#             cursor = self.db.get_cursor("oltp")

#             cursor.execute(
#                 query,
#                 (department_name,)
#             )

#             return cursor.fetchone()

#         except Exception as e:

#             logger.exception(
#                 "Failed to find department."
#             )

#             raise DatabaseException(
#                 f"Failed to find department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     # =====================================================
#     # CREATE
#     # =====================================================

#     def create(self, department):

#         query = """
#             INSERT INTO MINI_PROJECT.Departments
#             (
#                 DepartmentName
#             )
#             VALUES
#             (
#                 %s
#             )
#         """

#         values = (
#             department.department_name,
#         )

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 values
#             )

#             self.db.commit("oltp")

#             return cursor.lastrowid

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to create department."
#             )

#             raise DatabaseException(
#                 f"Failed to create department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     # =====================================================
#     # UPDATE
#     # =====================================================

#     def update(
#         self,
#         department_id,
#         department_name
#     ):

#         query = """
#             UPDATE MINI_PROJECT.Departments
#             SET
#                 DepartmentName = %s
#             WHERE DepartmentID = %s
#         """

#         values = (
#             department_name,
#             int(department_id)
#         )

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 values
#             )

#             self.db.commit("oltp")

#             return cursor.rowcount

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to update department."
#             )

#             raise DatabaseException(
#                 f"Failed to update department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()

#     # =====================================================
#     # DELETE
#     # =====================================================

#     def delete(self, department_id):

#         query = """
#             DELETE FROM MINI_PROJECT.Departments
#             WHERE DepartmentID = %s
#         """

#         cursor = None

#         try:

#             connection = self.db.connect("oltp")

#             cursor = connection.cursor()

#             cursor.execute(
#                 query,
#                 (int(department_id),)
#             )

#             self.db.commit("oltp")

#             return cursor.rowcount

#         except Exception as e:

#             self.db.rollback("oltp")

#             logger.exception(
#                 "Failed to delete department."
#             )

#             raise DatabaseException(
#                 f"Failed to delete department: {e}"
#             )

#         finally:

#             if cursor:
#                 cursor.close()




from backend.database.db_manager import (
    DatabaseConnection
)

from backend.exceptions import (
    DatabaseException
)

from backend.utils.logger import (
    get_logger
)


logger = get_logger(__name__)


class DepartmentRepository:

    def __init__(self):

        self.db = DatabaseConnection()


    # =====================================================
    # GET ALL DEPARTMENTS
    # =====================================================

    def get_all(self):

        query = """
            SELECT
                DepartmentID,
                DepartmentName
            FROM MINI_PROJECT.Departments
            ORDER BY DepartmentID
        """

        cursor = None

        try:

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query
            )

            return cursor.fetchall()

        except Exception as e:

            logger.exception(
                "Failed to fetch departments."
            )

            raise DatabaseException(
                f"Failed to fetch departments: {e}"
            )

        finally:

            if cursor:

                cursor.close()


    # =====================================================
    # GET DEPARTMENT BY ID
    # =====================================================

    def get_by_id(
        self,
        department_id
    ):

        query = """
            SELECT
                DepartmentID,
                DepartmentName
            FROM MINI_PROJECT.Departments
            WHERE DepartmentID = %s
        """

        cursor = None

        try:

            department_id = int(
                department_id
            )

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query,
                (
                    department_id,
                )
            )

            return cursor.fetchone()

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception as e:

            logger.exception(
                "Failed to fetch department."
            )

            raise DatabaseException(
                f"Failed to fetch department: {e}"
            )

        finally:

            if cursor:

                cursor.close()


    # =====================================================
    # GET DEPARTMENT BY NAME
    # =====================================================

    def get_by_name(
        self,
        department_name
    ):

        query = """
            SELECT
                DepartmentID,
                DepartmentName
            FROM MINI_PROJECT.Departments
            WHERE DepartmentName = %s
        """

        cursor = None

        try:

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query,
                (
                    department_name,
                )
            )

            return cursor.fetchone()

        except Exception as e:

            logger.exception(
                "Failed to find department."
            )

            raise DatabaseException(
                f"Failed to find department: {e}"
            )

        finally:

            if cursor:

                cursor.close()


    # =====================================================
    # EXTRACT DEPARTMENT ID
    # =====================================================

    def extract_department_id(
        self,
        department
    ):

        if department is None:

            return None

        # ---------------------------------------------
        # Tuple / list returned by MySQL cursor
        # ---------------------------------------------

        if isinstance(
            department,
            (tuple, list)
        ):

            return int(
                department[0]
            )

        # ---------------------------------------------
        # Dictionary
        # ---------------------------------------------

        if isinstance(
            department,
            dict
        ):

            value = (
                department.get(
                    "DepartmentID"
                )
            )

            if value is None:

                value = (
                    department.get(
                        "department_id"
                    )
                )

            if value is not None:

                return int(value)

        return None


    # =====================================================
    # CREATE DEPARTMENT
    # =====================================================

    def create(
        self,
        department_name
    ):

        query = """
            INSERT INTO MINI_PROJECT.Departments
            (
                DepartmentName
            )
            VALUES
            (
                %s
            )
        """

        cursor = None

        try:

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query,
                (
                    department_name,
                )
            )

            self.db.commit(
                "oltp"
            )

            return cursor.lastrowid

        except Exception as e:

            self.db.rollback(
                "oltp"
            )

            logger.exception(
                "Failed to create department."
            )

            # -----------------------------------------
            # Duplicate department
            # MySQL error 1062
            # -----------------------------------------

            if getattr(
                e,
                "errno",
                None
            ) == 1062:

                raise DatabaseException(
                    "Department already exists."
                )

            raise DatabaseException(
                f"Failed to create department: {e}"
            )

        finally:

            if cursor:

                cursor.close()


    # =====================================================
    # UPDATE DEPARTMENT
    # =====================================================

    def update(
        self,
        department_id,
        department_name
    ):

        query = """
            UPDATE MINI_PROJECT.Departments
            SET
                DepartmentName = %s
            WHERE DepartmentID = %s
        """

        cursor = None

        try:

            department_id = int(
                department_id
            )

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query,
                (
                    department_name,
                    department_id
                )
            )

            self.db.commit(
                "oltp"
            )

            return cursor.rowcount

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception as e:

            self.db.rollback(
                "oltp"
            )

            logger.exception(
                "Failed to update department."
            )

            if getattr(
                e,
                "errno",
                None
            ) == 1062:

                raise DatabaseException(
                    "Another department with "
                    "this name already exists."
                )

            raise DatabaseException(
                f"Failed to update department: {e}"
            )

        finally:

            if cursor:

                cursor.close()


    # =====================================================
    # DELETE DEPARTMENT
    # =====================================================

    def delete(
        self,
        department_id
    ):

        query = """
            DELETE FROM MINI_PROJECT.Departments
            WHERE DepartmentID = %s
        """

        cursor = None

        try:

            department_id = int(
                department_id
            )

            cursor = self.db.get_cursor(
                "oltp"
            )

            cursor.execute(
                query,
                (
                    department_id,
                )
            )

            self.db.commit(
                "oltp"
            )

            return cursor.rowcount

        except ValueError:

            raise ValueError(
                "Department ID must be an integer."
            )

        except Exception as e:

            self.db.rollback(
                "oltp"
            )

            logger.exception(
                "Failed to delete department."
            )

            # -----------------------------------------
            # MySQL FK constraint error 1451
            # -----------------------------------------

            if getattr(
                e,
                "errno",
                None
            ) == 1451:

                raise DatabaseException(
                    "Cannot delete department because "
                    "it is referenced by employees."
                )

            raise DatabaseException(
                f"Failed to delete department: {e}"
            )

        finally:

            if cursor:

                cursor.close()