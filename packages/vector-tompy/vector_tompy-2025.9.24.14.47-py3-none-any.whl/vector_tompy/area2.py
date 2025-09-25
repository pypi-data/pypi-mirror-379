from decimal import Decimal


class Area2:

    def __init__(self, width: Decimal, height: Decimal) -> None:
        self._width: Decimal = width
        self._height: Decimal = height

    @property
    def width(self) -> Decimal:
        return self._width

    @property
    def height(self) -> Decimal:
        return self._height

    @property
    def area(self) -> Decimal:
        return self.width * self.height
