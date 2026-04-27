from unittest.mock import Mock

from magicsquare.boundary.input_validator import InputValidator
from magicsquare.control.use_case import SolveMagicSquareUseCase


def test_u06_invalid_input_does_not_call_domain_resolver() -> None:
    invalid_grid = [[1, 2], [3, 4]]
    resolver = Mock()
    use_case = SolveMagicSquareUseCase(validator=InputValidator(), resolver=resolver)

    result = use_case.solve(invalid_grid)

    assert result == {"code": "INVALID_SIZE", "message": "Grid must be 4x4."}
    resolver.resolve.assert_not_called()
