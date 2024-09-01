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


class SessionGenerator:
    """
       A class to generate sessions of consecutive days.

       This class provides functionality to generate tuples representing sessions of consecutive days.
       Each tuple contains up to 3 consecutive days, starting from 1 up to a specified limit.
       If the limit is not evenly divisible by 3, the last tuple will contain the remaining days.

       Attributes:
           limit (int): The upper limit for the days.
       """

    def __init__(self, limit: int):
        """
        Initialize the SessionGenerator with a specified limit.

        Args:
            limit (int): The upper limit for the days.
        """
        self.limit = limit

    def generate(self) -> List[Tuple[int, ...]]:
        """
        Generate a list of tuples representing sessions of consecutive days.

        Each tuple contains up to 3 consecutive days, starting from 1 up to the specified limit.
        If the limit is not evenly divisible by 3, the last tuple will contain the remaining days.

        Returns:
            List[Tuple[int, ...]]: A list of tuples, where each tuple contains up to 3 consecutive days.
        """
        days: List[Tuple[int, ...]] = []

        for day in range(1, self.limit + 1, 3):
            sessions = tuple(range(day, min(day + 3, self.limit + 1)))
            days.append(sessions)

        return days

    def generate_sessions(self) -> List[Tuple[int, ...]]:
        """
        Generates sessions of consecutive days.

        Returns:
            List[Tuple[int, ...]]: A list of tuples, where each tuple contains up to 3 consecutive days.
        """
        return [tuple(range(day, min(day + 3, self.limit + 1))) for day in range(1, self.limit + 1, 3)]


def main():
    sessions = generate_sessions()
    for session in sessions:
        print(session)


def start():
    session_gntr = SessionGenerator(limit=100)
    session_gntr2 = SessionGenerator(limit=200)
    days = session_gntr.generate()
    for sessions in days:
        print(sessions)

    print("#" * 100)
    days = session_gntr2.generate_sessions()
    for sessions in days:
        print(sessions)


# Example usage:
if __name__ == "__main__":
    # main()
    start()
