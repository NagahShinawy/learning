from datetime import date, timedelta, datetime


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
        return (self.today + timedelta(days=self.RETURN_PERIOD_DAYS)).strftime(self.DISPLAYED_DATE_FORMAT)

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
        current_year_christmas = date(self.current_year, self.CHRISTMAS_MONTH, self.CHRISTMAS_DAY)
        if self.today > current_year_christmas:
            next_year_christmas = date(self.next_year, self.CHRISTMAS_MONTH, self.CHRISTMAS_DAY)
            return next_year_christmas - self.today
        return current_year_christmas - self.today


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
    print(f"Is return valid (14 days from {purchase_date1})? {dt_helper.is_return_valid(purchase_date1)}")
    print(f"Is return valid (14 days from {purchase_date2})? {dt_helper.is_return_valid(purchase_date2)}")

    # Christmas countdown
    print(f"Days until Christmas: {dt_helper.days_until_christmas().days} days")


if __name__ == '__main__':
    main()
