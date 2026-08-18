from datetime import date

from backend.exceptions import ValidationException


def validate_required(value, field_name):

    if value is None:
        raise ValidationException(
            f"{field_name} is required."
        )

    if isinstance(value, str) and not value.strip():

        raise ValidationException(
            f"{field_name} is required."
        )

    return True


def validate_positive(value, field_name):

    if value is None:
        raise ValidationException(
            f"{field_name} is required."
        )

    if value <= 0:

        raise ValidationException(
            f"{field_name} must be greater than 0."
        )

    return True


def validate_non_negative(value, field_name):

    if value is None:
        return True

    if value < 0:

        raise ValidationException(
            f"{field_name} cannot be negative."
        )

    return True


def validate_rating(
    value,
    field_name="Performance rating"
):

    validate_required(
        value,
        field_name
    )

    if value < 1 or value > 5:

        raise ValidationException(
            f"{field_name} must be between 1 and 5."
        )

    return True


def validate_percentage(
    value,
    field_name="Percentage"
):

    validate_required(
        value,
        field_name
    )

    if value < 0 or value > 100:

        raise ValidationException(
            f"{field_name} must be between 0 and 100."
        )

    return True


def validate_date(
    value,
    field_name="Date"
):

    validate_required(
        value,
        field_name
    )

    if not isinstance(value, date):

        raise ValidationException(
            f"{field_name} must be a valid date."
        )

    return True