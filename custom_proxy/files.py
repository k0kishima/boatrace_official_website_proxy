import os
import dataclasses
from datetime import date
from custom_proxy.versions import Version
from custom_proxy.formatters import format_stadium_tel_code

class _CacheFile:
  def content(self):
    os.makedirs(self._dir(), exist_ok=True)
    if os.path.isfile(self.path()):
      with open(self.path()) as f:
        return f.read()
    else:
      return None

  def path(self):
    return '/'.join([self._dir(), self._file_name()])

  def _cache_root_dir(self):
    return 'caches'

  def _versioning_dir(self):
    return "v{}".format(int(self.version))

  # NOTE:
  # 年毎ではなく級別審査期間毎に分けるのが運用上一番都合がいいのだが、
  # 級別審査期間をAPIで都度取得すると処理速度が遅くなり、このサービスの存在価値が下がってしまう（キャッシュ効かせて高速化も要件のひとつ）、
  # かといってここで審査期間の知識を持ってしまうのも責務の重複（不必要な繰り返し）が発生してしまう
  # そういう理由で年毎で分ける妥協した
  def _year_dir(self):
    return str(self._year())

  def _dir(self):
    return '/'.join([self._cache_root_dir(), self._versioning_dir(), self._year_dir(), self._peculiar_dir()])

  def _year(self):
    raise NotImplemented

  def _peculiar_dir(self):
    raise NotImplemented

  def _file_name(self):
    raise NotImplemented

@dataclasses.dataclass
class RacerProfileFile(_CacheFile):
  version: Version
  registration_number: int

  def _year(self):
    return date.today().year

  def _peculiar_dir(self):
    return "racer_profiles"

  def _file_name(self):
    return "{}.html".format(self.registration_number)

@dataclasses.dataclass
class MonthlyEventScheduleFile(_CacheFile):
  version: Version
  year: int
  month: int

  def _year(self):
    return self.year

  def _peculiar_dir(self):
    return 'event_schedules/monthly'

  def _file_name(self):
    return "{}.html".format(self.month)

@dataclasses.dataclass
class EventEntryFile(_CacheFile):
  version: Version
  event_starts_on: date
  stadium_tel_code: int

  def _year(self):
    return self.event_starts_on.year

  def _peculiar_dir(self):
    return "event_entries/{}".format(self.event_starts_on)

  def _file_name(self):
    return "{}#.html".format(format_stadium_tel_code(self.stadium_tel_code))

@dataclasses.dataclass
class _RaceFile(_CacheFile):
  version: Version
  race_opened_on: date
  stadium_tel_code: int
  race_number: int

  def _year(self):
    return self.race_opened_on.year

  def _peculiar_dir(self):
    return "races/{}/{}/{}#".format(self._page_type_dir(), self.race_opened_on, format_stadium_tel_code(self.stadium_tel_code))

  def _file_name(self):
    return "{}R.html".format(self.race_number)

  def _page_type_dir(self):
    raise NotImplemented

class RaceInformationFile(_RaceFile):
  def _page_type_dir(self):
    return 'information'

class RaceExhibitionInformationFile(_RaceFile):
  def _page_type_dir(self):
    return 'exhibition_information'

class RaceResultFile(_RaceFile):
  def _page_type_dir(self):
    return 'results'

class RaceOddsFile(_RaceFile):
  def _page_type_dir(self):
    return 'odds'
