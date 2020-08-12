def format_day(number):
  return str(number).zfill(2)

def format_stadium_tel_code(number):
  return str(number).zfill(2)

def format_date_in_query_string(date):
  return date.strftime('%Y%m%d')