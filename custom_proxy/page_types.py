from enum import Enum, auto

class PageType(Enum):
  RACER_PROFILE_PAGE = auto()
  EVENT_SCHEDULE_PAGE = auto()
  EVENT_HOLDINGS_PAGE = auto()
  EVENT_ENTRIES_PAGE = auto()
  RACE_INFORMATION_PAGE = auto()
  RACE_EXHIBITION_INFORMATION_PAGE = auto()
  RACE_RESULT_PAGE = auto()
  RACE_ODDS_PAGE = auto()

class PageTypeFactory:
  def __init__(self, page_type_string):
    self._page_type_string = page_type_string

  def create(self):
    return PageType[self._page_type_string.upper()]
