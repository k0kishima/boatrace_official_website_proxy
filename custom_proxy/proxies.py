import urllib.request
from . import app
from custom_proxy.files import FileFactory
from custom_proxy.page_types import PageTypeFactory
from custom_proxy.urls import UrlFactory
from custom_proxy.versions import Version, LATEST_VERSION
from flask import request

@app.route('/file', methods=['GET'])
def official_web_site_proxy():
  try:
    version = Version(request.args.get('version', default=LATEST_VERSION, type=int))
  except ValueError:
    return "version is invalid.", 400
  try:
    page_type = PageTypeFactory(request.args.get('page_type', type=str)).create()
  except (ValueError, AttributeError):
    return "page type is invalid.", 400

  args = without_keys(request.args, {'version', 'page_type'})

  cache_file = FileFactory(version=version, page_type=page_type, args=args).create()
  if (request.headers.get('Cache-Control') == 'no-cache') or (cache_file.content() is None):
    url_object = UrlFactory(version=version, page_type=page_type, args=args).create()
    urllib.request.urlretrieve(str(url_object), cache_file.path())

  return cache_file.content()

def without_keys(d, keys):
  return {x: d[x] for x in d if x not in keys}