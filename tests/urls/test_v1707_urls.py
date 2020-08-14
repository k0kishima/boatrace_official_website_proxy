import custom_proxy.urls.v1707 as v1707_url_module

def test_to_create_race_profile_page_url():
  url = v1707_url_module.RacerProfilePageUrl(4444)
  assert str(url) == "https://boatrace.jp/owpc/pc/data/racersearch/profile?toban=4444"

def test_to_create_monthly_schedule_page_url():
  url = v1707_url_module.EventSchedulePageUrl(year=2020, month=3)
  assert str(url) == "https://boatrace.jp/owpc/pc/race/monthlyschedule?ym=202003"

def test_to_create_daily_schedule_page_url():
  url = v1707_url_module.EventSchedulePageUrl(date='2020-03-20')
  assert str(url) == "https://boatrace.jp/owpc/pc/race/index?hd=20200320"

def test_to_create_event_entries_page_url():
  url = v1707_url_module.EventEntriesPageUrl(event_starts_on='2020-03-17', stadium_tel_code=4)
  assert str(url) == "https://boatrace.jp/owpc/pc/race/rankingmotor?jcd=04&hd=20200317"

def test_to_create_race_information_page_url():
  date = '2020-03-20'
  stadium_tel_code = 4
  race_number=6
  url = v1707_url_module.RaceInformationPageUrl(race_opened_on=date, stadium_tel_code=stadium_tel_code, race_number=race_number)
  assert str(url) == "https://boatrace.jp/owpc/pc/race/racelist?rno=6&jcd=04&hd=20200320"

def test_to_create_race_result_page_url():
  date = '2020-03-20'
  stadium_tel_code = 4
  race_number=6
  url = v1707_url_module.RaceResultPageUrl(race_opened_on=date, stadium_tel_code=stadium_tel_code, race_number=race_number)
  assert str(url) == "https://boatrace.jp/owpc/pc/race/raceresult?rno=6&jcd=04&hd=20200320"

def test_to_create_race_exhibition_page_url():
  date = '2020-03-20'
  stadium_tel_code = 4
  race_number=6
  url = v1707_url_module.RaceExhibitionInformationPageUrl(race_opened_on=date, stadium_tel_code=stadium_tel_code, race_number=race_number)
  assert str(url) == "https://boatrace.jp/owpc/pc/race/beforeinfo?rno=6&jcd=04&hd=20200320"
