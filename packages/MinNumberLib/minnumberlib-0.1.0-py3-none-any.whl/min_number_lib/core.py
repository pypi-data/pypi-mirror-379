
def find_min(numbers: list) -> float:
    if not numbers:
        raise ValueError("The list is empty")
    return min(numbers)
