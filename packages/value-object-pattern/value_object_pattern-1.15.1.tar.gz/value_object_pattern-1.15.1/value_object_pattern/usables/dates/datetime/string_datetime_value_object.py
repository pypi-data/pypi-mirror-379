"""
StringDatetimeValueObject value object.
"""

from datetime import UTC, datetime
from typing import NoReturn

from dateutil.parser import ParserError, parse
from dateutil.relativedelta import relativedelta

from value_object_pattern.decorators import process, validation
from value_object_pattern.usables import NotEmptyStringValueObject, TrimmedStringValueObject

from .datetime_value_object import DatetimeValueObject


class StringDatetimeValueObject(NotEmptyStringValueObject, TrimmedStringValueObject):
    """
    StringDatetimeValueObject value object ensures the provided value is a valid datetime.

    Example:
    ```python
    from value_object_pattern.usables.dates import StringDatetimeValueObject

    now = '1900-01-01T00:00:00+00:00'
    date = StringDatetimeValueObject(value=now)

    print(repr(date))
    # >>> StringDatetimeValueObject(value='1900-01-01T00:00:00+00:00')
    ```
    """

    _internal_datetime_object: datetime

    @process(order=0)
    def _ensure_value_is_normalized(self, value: str) -> str:
        """
        Ensures the value object value is normalized datetime string (ISO 8601, YYYY-MM-DDTHH:MM:SS).

        Args:
            value (str): Value.

        Returns:
            str: Value with the normalized datetime string.
        """
        return self._internal_datetime_object.isoformat()

    @validation(order=0)
    def _ensure_value_is_date(self, value: str) -> None:
        """
        Ensures the value object value is a datetime.

        Args:
            value (str): Value.

        Raises:
            ValueError: If the value is not a datetime.
        """
        try:
            self._internal_datetime_object = parse(timestr=value).astimezone(tz=UTC)

        except ParserError:
            self._raise_value_is_not_valid_datetime(value=value)

    def _raise_value_is_not_valid_datetime(self, value: str) -> NoReturn:
        """
        Raises a ValueError indicating the provided value is not a valid datetime.

        Args:
            value (str): The invalid datetime value.

        Raises:
            ValueError: If the value is not a valid datetime.
        """
        raise ValueError(f'StringDatetimeValueObject value <<<{value}>>> is not a valid datetime.')

    def is_now(self, *, reference_datetime: datetime) -> bool:
        """
        Determines whether the stored datetime value matches the current datetime.

        Args:
            reference_datetime (datetime): The datetime to compare against.

        Raises:
            TypeError: If the `reference_datetime` is not a datetime.

        Returns:
            bool: True if the stored datetime matches the `reference_datetime`, False otherwise.

        Example:
        ```python
        from datetime import UTC, datetime

        from value_object_pattern.usables.dates import StringDatetimeValueObject

        now = '1900-01-01T08:30:00+00:00'
        today = datetime(year=1900, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        is_now = StringDatetimeValueObject(value=now).is_now(reference_datetime=today)

        print(is_now)
        # >>> False
        ```
        """
        DatetimeValueObject(value=reference_datetime, title='StringDatetimeValueObject', parameter='reference_datetime')

        return self._internal_datetime_object == reference_datetime

    def is_today(self, *, reference_datetime: datetime) -> bool:
        """
        Determines whether the stored datetime value is today's datetime.

        Args:
            reference_datetime (datetime): The datetime to compare against.

        Raises:
            TypeError: If the `reference_datetime` is not a datetime.

        Returns:
            bool: True if the stored datetime matches today's datetime, False otherwise.

        Example:
        ```python
        from datetime import UTC, datetime

        from value_object_pattern.usables.dates import StringDatetimeValueObject

        now = '1900-01-01T08:30:00+00:00'
        today = datetime(year=1900, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        is_today = StringDatetimeValueObject(value=now).is_today(reference_datetime=today)

        print(is_today)
        # >>> True
        ```
        """
        DatetimeValueObject(value=reference_datetime, title='StringDatetimeValueObject', parameter='reference_datetime')

        return self._internal_datetime_object.date() == reference_datetime.date()

    def is_later_than(self, *, reference_datetime: datetime) -> bool:
        """
        Determines whether the stored datetime value is later than the specified datetime.

        Args:
            reference_datetime (datetime): The datetime to compare against.

        Raises:
            TypeError: If the `reference_datetime` is not a datetime.

        Returns:
            bool: True if the stored datetime is later than the `reference_datetime`, False otherwise.

        Example:
        ```python
        from datetime import UTC, datetime

        from value_object_pattern.usables.dates import StringDatetimeValueObject

        now = '1900-01-01T08:30:00+00:00'
        reference_datetime = datetime(year=1899, month=12, day=31, hour=23, minute=59, second=59, tzinfo=UTC)
        is_later_than = StringDatetimeValueObject(value=now).is_later_than(reference_datetime=reference_datetime)

        print(is_later_than)
        # >>> True
        ```
        """
        DatetimeValueObject(value=reference_datetime, title='StringDatetimeValueObject', parameter='reference_datetime')

        return self._internal_datetime_object > reference_datetime

    def is_in_range(self, *, start_datetime: datetime, end_datetime: datetime) -> bool:
        """
        Determines whether the stored datetime value falls within the specified datetime range.

        Args:
            start_datetime (datetime): The beginning of the datetime range (inclusive).
            end_datetime (datetime): The end of the datetime range (inclusive).

        Raises:
            TypeError: If the `start_datetime` is not a datetime.
            TypeError: If the `end_datetime` is not a datetime.
            ValueError: If the `start_datetime` is later than the `end_datetime`.

        Returns:
            bool: True if the stored datetime is within the range, False otherwise.

        Example:
        ```python
        from datetime import UTC, datetime

        from value_object_pattern.usables.dates import StringDatetimeValueObject

        now = '1900-01-01T00:00:00+00:00'
        start_datetime = datetime(year=1899, month=12, day=31, hour=23, minute=59, second=59, tzinfo=UTC)
        end_datetime = datetime(year=1900, month=1, day=2, hour=00, minute=00, second=00, tzinfo=UTC)
        is_in_range = StringDatetimeValueObject(
            value=now,
        ).is_in_range(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )

        print(is_in_range)
        # >>> True
        ```
        """
        DatetimeValueObject(value=start_datetime, title='StringDatetimeValueObject', parameter='start_datetime')
        DatetimeValueObject(value=end_datetime, title='StringDatetimeValueObject', parameter='end_datetime')

        if start_datetime > end_datetime:
            self._raise_start_datetime_is_later_than_end_datetime(
                start_datetime=start_datetime,
                end_datetime=end_datetime,
            )

        return start_datetime <= self._internal_datetime_object <= end_datetime

    def _raise_start_datetime_is_later_than_end_datetime(
        self,
        *,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> NoReturn:
        """
        Raises a ValueError if the start datetime is later than the end datetime.

        Args:
            start_datetime (datetime): The start datetime.
            end_datetime (datetime): The end datetime.

        Raises:
            ValueError: If the `start_datetime` is later than the `end_datetime`.
        """
        raise ValueError(f'StringDatetimeValueObject start_datetime <<<{start_datetime.isoformat()}>>> must be earlier than or equal to end_datetime <<<{end_datetime.isoformat()}>>>.')  # noqa: E501  # fmt: skip

    def calculate_age(self, *, reference_datetime: datetime) -> int:
        """
        Calculates the age of the stored datetime value.

        Args:
            reference_datetime (datetime): The datetime to calculate the age against.

        Raises:
            TypeError: If the `reference_datetime` is not a datetime.
            ValueError: If the stored datetime is later than the `reference_datetime`.

        Returns:
            int: The age in years of the stored datetime.

        Example:
        ```python
        from datetime import UTC, datetime

        from value_object_pattern.usables.dates import StringDatetimeValueObject

        now = '1900-01-01T00:00:00+00:00'
        today = datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        age = StringDatetimeValueObject(value=now).calculate_age(reference_datetime=today)

        print(age)
        # >>> 100
        ```
        """
        DatetimeValueObject(value=reference_datetime, title='StringDatetimeValueObject')

        if self._internal_datetime_object > reference_datetime:
            self._raise_start_datetime_is_later_than_end_datetime(
                start_datetime=self._internal_datetime_object,
                end_datetime=reference_datetime,
            )

        return relativedelta(dt1=reference_datetime, dt2=self._internal_datetime_object).years
