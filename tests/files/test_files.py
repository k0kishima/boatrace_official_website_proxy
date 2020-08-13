import datetime
from custom_proxy.files import RacerProfileFile, MonthlyEventScheduleFile, EventEntryFile,\
  RaceInformationFile, RaceExhibitionInformationFile, RaceResultFile, RaceOddsFile
from custom_proxy.versions import Version

def test_racer_profile_file_path():
  current_year = datetime.date.today().year
  file = RacerProfileFile(version=Version.V1707, registration_number=4444)
  assert file.path() == "caches/v1707/{}/racer_profiles/4444.html".format(current_year)

def test_event_schedule_file_path():
  file = MonthlyEventScheduleFile(version=Version.V1707, year=2020, month=8)
  assert file.path() == 'caches/v1707/2020/event_schedules/monthly/8.html'

def test_event_entry_file_path():
  event_starts_on = datetime.datetime.strptime('2020-08-14', '%Y-%m-%d').date()
  file = EventEntryFile(version=Version.V1707, event_starts_on=event_starts_on, stadium_tel_code=4)
  assert file.path() == 'caches/v1707/2020/event_entries/2020-08-14/04#.html'

def test_race_information_file_path():
  race_opened_on = datetime.datetime.strptime('2020-08-14', '%Y-%m-%d').date()
  file = RaceInformationFile(version=Version.V1707, race_opened_on=race_opened_on, stadium_tel_code=4, race_number=12)
  assert file.path() == 'caches/v1707/2020/races/information/2020-08-14/04#/12R.html'

def test_race_exhibition_information_file_path():
  race_opened_on = datetime.datetime.strptime('2020-08-14', '%Y-%m-%d').date()
  file = RaceExhibitionInformationFile(version=Version.V1707, race_opened_on=race_opened_on, stadium_tel_code=4, race_number=12)
  assert file.path() == 'caches/v1707/2020/races/exhibition_information/2020-08-14/04#/12R.html'

def test_race_result_file_path():
  race_opened_on = datetime.datetime.strptime('2020-08-14', '%Y-%m-%d').date()
  file = RaceResultFile(version=Version.V1707, race_opened_on=race_opened_on, stadium_tel_code=4, race_number=12)
  assert file.path() == 'caches/v1707/2020/races/results/2020-08-14/04#/12R.html'

def test_race_odds_file_path():
  race_opened_on = datetime.datetime.strptime('2020-08-14', '%Y-%m-%d').date()
  file = RaceOddsFile(version=Version.V1707, race_opened_on=race_opened_on, stadium_tel_code=4, race_number=12)
  assert file.path() == 'caches/v1707/2020/races/odds/2020-08-14/04#/12R.html'