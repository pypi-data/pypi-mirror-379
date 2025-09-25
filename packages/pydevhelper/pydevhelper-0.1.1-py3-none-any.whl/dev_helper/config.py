import os

class MissingEnvVarsError(Exception):
    """Raised when one or more required environment variables are missing."""

    def __init__(self, missing_vars: list[str]):
        self.missing_vars = missing_vars
        message = f"Missing environment variables: {missing_vars}"
        super().__init__(message)


def require_vars(vars: list[str]) -> None:
    """Ensure that all required environment variables exist and are not empty.

    Args:
        vars (list[str]): List of environment variable names to check.

    Raises:
        MissingEnvVarsError: If one or more variables are missing or empty.
    """
    missing = [var for var in vars if not os.getenv(var)]
    if missing:
        raise MissingEnvVarsError(missing)
