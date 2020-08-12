from . import BASE_URL
import datetime
import urllib.parse
from custom_proxy.formatters import format_stadium_tel_code, format_date_in_query_string, format_day

class _PageUrl:
  def __str__(self):
    return "{}{}?{}".format(BASE_URL, self._path(), urllib.parse.urlencode(self._query_string()))

class RacerProfilePageUrl(_PageUrl):
  def __init__(self, registration_number):
    self._registration_number = registration_number

  def _path(self):
    return "/owpc/pc/data/racersearch/profile"

  def _query_string(self):
    return { 'toban': self._registration_number }

class StadiumEventSchedulePageUrl:
  def __init__(self, date=None, year=None, month=None):
    if date is not None:
      self._to_be_delegate = _DailySchedulePageUrl(date)
    elif (year is not None) and (month is not None):
      self._to_be_delegate = _MonthlySchedulePageUrl(year=year, month=month)

  def __str__(self):
    return str(self._to_be_delegate)

class _MonthlySchedulePageUrl(_PageUrl):
  def __init__(self, year, month):
    self._year = year
    self._month = month

  def _path(self):
    return "/owpc/pc/race/monthlyschedule"

  def _query_string(self):
    return { 'ym': "{}{}".format(self._year, format_day(self._month)) }

class _DailySchedulePageUrl(_PageUrl):
  def __init__(self, date):
    self._date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

  def _path(self):
    return "/owpc/pc/race/index"

  def _query_string(self):
    return { 'hd': format_date_in_query_string(self._date) }

class EventEntriesPageUrl(_PageUrl):
  def __init__(self, stadium_tel_code, event_starts_on):
    self._stadium_tel_code = stadium_tel_code
    self._event_starts_on = datetime.datetime.strptime(event_starts_on, '%Y-%m-%d').date()

  def _path(self):
    return "/owpc/pc/race/rankingmotor"

  def _query_string(self):
    return {
      'jcd': format_stadium_tel_code(self._stadium_tel_code),
      'hd': format_date_in_query_string(self._event_starts_on)
     }

class _RacePage(_PageUrl):
  def __init__(self, stadium_tel_code, race_opened_on, race_number):
    self._stadium_tel_code = stadium_tel_code
    self._race_opened_on = race_opened_on
    self._race_opened_on = datetime.datetime.strptime(race_opened_on, '%Y-%m-%d').date()
    self._race_number = race_number

  def _query_string(self):
    return {
      'rno': self._race_number,
      'jcd': format_stadium_tel_code(self._stadium_tel_code),
      'hd': format_date_in_query_string(self._race_opened_on)
    }

class RaceInformationPageUrl(_RacePage):
  def _path(self):
    return "/owpc/pc/race/racelist"

class RaceResultPageUrl(_RacePage):
  def _path(self):
    return "/owpc/pc/race/raceresult"

class RaceExhibitionPageUrl(_RacePage):
  def _path(self):
    return "/owpc/pc/race/beforeinfo"
