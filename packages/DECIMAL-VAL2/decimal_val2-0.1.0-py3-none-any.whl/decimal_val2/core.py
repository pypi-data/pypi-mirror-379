from decimal import Decimal, ROUND_HALF_UP
from typing import Union, TypeAlias

# Type alias for accepted numeric inputs
Number: TypeAlias = Union[str, int, float, Decimal]

def to_two_decimal(value: Number) -> Decimal:
    """
    Convert a number to a Decimal with 2 decimal places (rounded half-up).

    Examples:
        >>> to_two_decimal(10.567)
        Decimal('10.57')
        >>> to_two_decimal("99.999")
        Decimal('100.00')
    """
    d = Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return d
