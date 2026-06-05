def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b


def divide(a: float, b: float) -> float:
    """Делит a на b. При делении на ноль возвращает None"""
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a / b


def is_even(number: int) -> bool:
    """Проверяет, является ли число чётным"""
    return number % 2 == 0
