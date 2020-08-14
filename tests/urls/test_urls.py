from custom_proxy.versions import Version
from custom_proxy.page_types import PageType
from custom_proxy.urls import UrlFactory

def test_to_create_race_profile_page_url():
  args = { 'registration_number': 4444 }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.RACER_PROFILE_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/data/racersearch/profile?toban=4444"

def test_to_create_monthly_schedule_page_url():
  args = { 'year': 2020, 'month': 3 }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.EVENT_SCHEDULE_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/monthlyschedule?ym=202003"

def test_to_create_daily_schedule_page_url():
  args = { 'date': '2020-03-20' }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.EVENT_SCHEDULE_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/index?hd=20200320"

def test_to_create_event_entries_page_url():
  stadium_tel_code = 4
  args = { 'stadium_tel_code': stadium_tel_code, 'event_starts_on': '2020-03-17' }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.EVENT_ENTRIES_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/rankingmotor?jcd=04&hd=20200317"

def test_to_create_race_information_page_url():
  stadium_tel_code = 4
  race_number = 6
  args = { 'stadium_tel_code': stadium_tel_code, 'race_opened_on': '2020-03-20', 'race_number': race_number }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.RACE_INFORMATION_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/racelist?rno=6&jcd=04&hd=20200320"

def test_to_create_race_result_page_url():
  stadium_tel_code = 4
  race_number = 6
  args = { 'stadium_tel_code': stadium_tel_code, 'race_opened_on': '2020-03-20', 'race_number': race_number }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.RACE_RESULT_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/raceresult?rno=6&jcd=04&hd=20200320"

def test_to_create_race_exhibition_page_url():
  stadium_tel_code = 4
  race_number = 6
  args = { 'stadium_tel_code': stadium_tel_code, 'race_opened_on': '2020-03-20', 'race_number': race_number }
  factory = UrlFactory(version=Version.V1707, page_type=PageType.RACE_EXHIBITION_INFORMATION_PAGE, args=args)
  assert str(factory.create()) == "https://boatrace.jp/owpc/pc/race/beforeinfo?rno=6&jcd=04&hd=20200320"

