from datetime import date, timedelta, datetime
import errors


DAYS_IN_WEEK = 7


def is_valid_number(number):
    """
    Validates and converts the input to a positive integer if it is a valid numeric string or integer.

    This function checks if the input `number` is either a string that represents a positive integer
    or an integer itself. If it is a valid positive integer, it converts the string to an integer if needed.
    If the input is invalid or not a positive integer, it raises a `PositiveNumberError`.

    :param number: The input to be validated and converted
    :type number: int | str
    :return: The validated number as an integer
    :rtype: int
    :raises PositiveNumberError: If the input is not a valid positive integer
    """
    if isinstance(number, str):
        if number.isdigit():

            number = int(number)
        else:
            errors.PositiveNumberError().raise_error()

    if not isinstance(number, int) or number <= 0:
        errors.PositiveNumberError().raise_error()

    return number


def from_days_to_weeks(days: int | str) -> tuple[int, int]:
    """
    Converts a number of days to a tuple of weeks and remaining days. Only accepts positive integers.

    :param days: The number of days (should be a positive integer)
    :type days: int | str
    :return: A tuple containing the number of weeks and the remaining days
    :rtype: tuple[int, int]
    :raises ValueError: If the input is not a valid positive integer
    """
    days = is_valid_number(days)
    weeks = days // DAYS_IN_WEEK
    remaining_days = days % DAYS_IN_WEEK
    return weeks, remaining_days


def from_weeks_to_days(weeks: int | str) -> int:
    """
    Converts a number of weeks to days. Only accepts positive integers.

    :param weeks: The number of weeks (should be a positive integer)
    :type weeks: int, str
    :return: The number of days equivalent to the input weeks
    :rtype: int
    :raises ValueError: If the input is not a valid positive integer
    """
    weeks = is_valid_number(weeks)

    if isinstance(weeks, int) and weeks > 0:
        return weeks * DAYS_IN_WEEK
    else:
        errors.PositiveNumberError().raise_error()


class DateTimeHelper:
    """
    A helper class to handle basic date-related operations, including calculating the current date,
    returning periods, months before or after, and days until specific events like Christmas.
    """

    DAYS_IN_MONTH = 30
    DISPLAYED_DATE_FORMAT = "%a %d %b %Y"
    RETURN_PERIOD_DAYS = 14
    CHRISTMAS_DAY = 25
    CHRISTMAS_MONTH = 12

    @property
    def today(self):
        """
        Returns today's date.

        :return: Current date
        :rtype: datetime.date
        """
        return date.today()

    @property
    def current_year(self):
        """
        Returns the current year.

        :return: Current year
        :rtype: int
        """
        return self.today.year

    @property
    def next_year(self):
        """
        Returns the year after the current year.

        :return: Next year
        :rtype: int
        """
        return self.current_year + 1

    @property
    def previous_year(self):
        """
        Returns the year before the current year.

        :return: Previous year
        :rtype: int
        """
        return self.current_year - 1

    @property
    def current_month(self):
        """
        Returns the current month.

        :return: Current month
        :rtype: int
        """
        return self.today.month

    @property
    def next_month(self):
        """
        Returns the date 30 days from today (assuming a month has 30 days).

        :return: Date 30 days later
        :rtype: datetime.date
        """
        return self.today + timedelta(days=self.DAYS_IN_MONTH)

    @property
    def previous_month(self):
        """
        Returns the date 30 days before today (assuming a month has 30 days).

        :return: Date 30 days earlier
        :rtype: datetime.date
        """
        return self.today - timedelta(days=self.DAYS_IN_MONTH)

    @property
    def formatted_today(self):
        """
        Formats today's date as a human-readable string based on the defined format.

        :return: Formatted date string
        :rtype: str
        """
        return self.today.strftime(self.DISPLAYED_DATE_FORMAT)

    def return_valid_until(self):
        """
        Returns the last valid date for returning a product (14 days from today).

        :return: Formatted date for valid return period
        :rtype: str
        """
        return (self.today + timedelta(days=self.RETURN_PERIOD_DAYS)).strftime(
            self.DISPLAYED_DATE_FORMAT
        )

    def is_return_valid(self, purchase_date) -> bool:
        """
        Checks if a return is valid (within 14 days of the purchase date).

        :param purchase_date: The date the product was purchased
        :type purchase_date: datetime.date
        :return: True if return is valid, False otherwise
        :rtype: bool
        """
        return self.today <= purchase_date + timedelta(days=self.RETURN_PERIOD_DAYS)

    def days_until_christmas(self):
        """
        Returns the number of days until the next Christmas. If today is after December 25,
        calculates the number of days until next year's Christmas.

        :return: Days until Christmas
        :rtype: datetime.timedelta
        """
        current_year_christmas = date(
            self.current_year, self.CHRISTMAS_MONTH, self.CHRISTMAS_DAY
        )
        if self.today > current_year_christmas:
            next_year_christmas = date(
                self.next_year, self.CHRISTMAS_MONTH, self.CHRISTMAS_DAY
            )
            return next_year_christmas - self.today
        return current_year_christmas - self.today

    @property
    def current_datetime(self):
        """
        Returns the current date and time.

        :return: The current date and time as a datetime object
        :rtype: datetime.datetime
        """
        return datetime.today()

    def next_hours(self, hours=6):
        """
        Returns the date and time after a specified number of hours from the current time.

        :param hours: Number of hours to add to the current datetime (default is 6)
        :type hours: int
        :return: Date and time after the specified number of hours
        :rtype: datetime.datetime
        """
        return self.current_datetime + timedelta(hours=hours)

    def next_weeks(self, weeks=1):
        """
        Returns the date after a specified number of weeks from today.

        :param weeks: Number of weeks to add to the current date (default is 1)
        :type weeks: int
        :return: Date after the specified number of weeks
        :rtype: datetime.date
        """
        return self.today + timedelta(weeks=weeks)


def main():
    dt_helper = DateTimeHelper()

    print(f"Today's Date: {dt_helper.today}")
    print(f"Current Year: {dt_helper.current_year}")
    print(f"Next Year: {dt_helper.next_year}")
    print(f"Previous Year: {dt_helper.previous_year}")
    print(f"Date Next Month: {dt_helper.next_month}")
    print(f"Date Previous Month: {dt_helper.previous_month}")
    print(f"Formatted Today's Date: {dt_helper.formatted_today}")
    print(f"Valid Return Until: {dt_helper.return_valid_until()}")

    # Check if return is valid for two sample purchase dates
    purchase_date1 = date(2024, 8, 20)
    purchase_date2 = date(2024, 9, 2)
    print(
        f"Is return valid (14 days from {purchase_date1})? {dt_helper.is_return_valid(purchase_date1)}"
    )
    print(
        f"Is return valid (14 days from {purchase_date2})? {dt_helper.is_return_valid(purchase_date2)}"
    )

    # Christmas countdown
    print(f"Days until Christmas: {dt_helper.days_until_christmas().days} days")
    """
           # Normalize everything to days, seconds, microseconds.
        days += weeks*7
        seconds += minutes*60 + hours*3600
        microseconds += milliseconds*1000
    """
    # print(f"Days until Christmas: {dt_helper.days_until_christmas().hours} hours")  # error
    print(
        f"Current datetime is [ {dt_helper.current_datetime} ] and after 6 hours will be [{dt_helper.next_hours()}]"
    )
    print(
        f"Current date is [ {dt_helper.today} ] and after 1 week will be [{dt_helper.next_weeks()}]"
    )

    # ################### # ################### # ################### # ################### # ###################
    print("#" * 100)
    tmdelat = timedelta(days=4, hours=10, weeks=3)
    print(f"Days are: {tmdelat.days}")  # 3 weeks + 4 days = 21 days + 4 days = 25
    print(f"Hours are: {tmdelat.seconds}")  # 10 Hours = 3600 seconds
    print(
        f"After 10 hours from now is {dt_helper.current_datetime + timedelta(hours=10)}"
    )
    print(dt_helper.current_datetime + timedelta(hours=10))


if __name__ == "__main__":
    main()
    print(from_weeks_to_days(3))  # OK
    print(from_weeks_to_days("3"))  # OK
    # print(from_weeks_to_days("3.5"))  # error
    # print(from_weeks_to_days(0))   # error
    # print(from_weeks_to_days(3.5))   # error

    print(from_days_to_weeks(15))
    print(from_days_to_weeks("15"))
    # # print(from_days_to_weeks("15.7"))
    # print(from_days_to_weeks(0))
    # print(from_days_to_weeks("0"))
