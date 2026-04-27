from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorResponse:
    code: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message}


INVALID_SIZE = ErrorResponse("INVALID_SIZE", "Grid must be 4x4.")
INVALID_VALUE_RANGE = ErrorResponse("INVALID_VALUE_RANGE", "Each cell must be 0 or 1..16.")
INVALID_ZERO_COUNT = ErrorResponse(
    "INVALID_ZERO_COUNT", "There must be exactly two zeros (empty cells)."
)
DUPLICATE_VALUES = ErrorResponse(
    "DUPLICATE_VALUES", "Values 1..16 must not duplicate (excluding zeros)."
)
NO_SOLUTION = ErrorResponse(
    "NO_SOLUTION", "No placement makes a 4x4 magic square with magic sum 34."
)
