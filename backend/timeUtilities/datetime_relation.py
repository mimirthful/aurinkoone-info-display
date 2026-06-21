import datetime as dt


class DateTimeRelation:
    """ compares datetime instances together

    Tracks if time_b has different date or hour compared to time_a, and tells if
    the time_b is on the future or past related to time_a
    """

    def __init__(self, time_a: dt.datetime, time_b: dt.datetime):
        # datetimes
        self.time_to_compare = time_b
        self.time_now = time_a
        # bools
        self.is_diff_date = True
        self.is_diff_hour = True
        self.is_in_future = False
        # updates the bools
        self._update_properties()

    def _update_properties(self):
        # checks date
        self.is_diff_date = self.time_now.date() != self.time_to_compare.date()
        # checks if in future
        self.is_in_future = self.time_now.date() < self.time_to_compare.date()

        # checks if in different hour if not in different date
        if not self.is_diff_date:
            self.is_diff_hour = self.time_now.hour != self.time_to_compare.hour
            if self.is_diff_hour:
                self.is_in_future = self.time_now.hour < self.time_to_compare.hour
