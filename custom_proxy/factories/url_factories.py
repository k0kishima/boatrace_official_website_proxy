import importlib
from custom_proxy.page_types import PageType

class UrlFactory:
  def __init__(self, version, page_type, args):
    self._module = importlib.import_module("custom_proxy.factories.v{}.url_factories".format(version))
    self._page_type = page_type
    self._args = args

  def create(self):
    return getattr(self._module, self._get_class_name())(**self._args)

  def _get_class_name(self):
    if self._page_type is PageType.RACER_PROFILE_PAGE:
      return 'RacerProfilePageUrl'
    elif self._page_type is PageType.EVENT_SCHEDULE_PAGE:
      return 'EventSchedulePageUrl'
    elif self._page_type is PageType.EVENT_ENTRIES_PAGE:
      return 'EventEntriesPageUrl'
    elif self._page_type is PageType.RACE_INFORMATION_PAGE:
      return 'RaceInformationPageUrl'
    elif self._page_type is PageType.RACE_RESULT_PAGE:
      return 'RaceResultPageUrl'
    elif self._page_type is PageType.RACE_EXHIBITION_INFORMATION_PAGE:
      return 'RaceExhibitionInformationPageUrl'
    elif self._page_type is PageType.RACE_ODDS_PAGE:
      raise NotImplemented
    else:
      raise ValueError("unknown page type specified")
