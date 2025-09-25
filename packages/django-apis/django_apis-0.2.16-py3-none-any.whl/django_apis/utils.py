from pydantic import ValidationError

__all__ = [
    "validation_error_format",
]


def validation_error_format(error: ValidationError) -> str:
    messages = []
    for row in error.errors():
        field_names = ",".join(row["loc"])
        field_error = row["msg"]
        message = f"- {field_names}: {field_error}"
        messages.append(message)
    return "\n".join(messages)
