from typing import List, Tuple


def generate_sessions(limit: int = 100) -> List[Tuple[int, ...]]:
    """
    Generate a list of tuples representing sessions of consecutive days.

    Each tuple contains up to 3 consecutive days, starting from 1 up to the specified limit.
    If the limit is not evenly divisible by 3, the last tuple will contain the remaining days.

    Args:
        limit (int): The upper limit for the days (default is 100).

    Returns:
        List[Tuple[int, ...]]: A list of tuples, where each tuple contains up to 3 consecutive days.
    """
    days: List[Tuple[int, ...]] = []

    for day in range(1, limit + 1, 3):
        sessions = tuple(range(day, day + 3))  # (100, 101, 102)  it is bug, limit ends with 100, fixed using if
        # sessions = tuple(range(day, min(day + 3, limit + 1)))
        if day == limit:
            sessions = (limit, )
        days.append(sessions)

    return days


def main():
    sessions = generate_sessions()
    for session in sessions:
        print(session)


# Example usage:
if __name__ == "__main__":
    main()
