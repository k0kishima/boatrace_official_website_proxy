import urllib.request
from . import app
from custom_proxy.files import FileFactory
from custom_proxy.page_types import PageTypeFactory
from custom_proxy.urls import UrlFactory
from custom_proxy.versions import Version, LATEST_VERSION
from flask import request, redirect

@app.route('/file', methods=['GET'])
def file():
  version = _get_version()
  page_type = _get_page_type()
  args = _without_keys(request.args, {'version', 'page_type'})
  cache_file = FileFactory(version=version, page_type=page_type, args=args).create()
  # HACK: `cache_file.content() is None` を先に評価しないと `FileNotFoundError` が発生してしまうバギーなコード
  # ディレクトリの生成自体は `cache_file.content() is None` でやってるから、`request.headers.get('Cache-Control') == 'no-cache'` を or で
  # 先に評価して真になったらディレクトリの生成が行われずに前述したエラーとなる
  if (cache_file.content() is None) or (request.headers.get('Cache-Control') == 'no-cache'):
    url_object = UrlFactory(version=version, page_type=page_type, args=args).create()
    urllib.request.urlretrieve(str(url_object), cache_file.path())
  return cache_file.content()

@app.route('/redirection', methods=['GET'])
def redirection():
  version = _get_version()
  page_type = _get_page_type()
  args = _without_keys(request.args, {'version', 'page_type'})
  url_object = UrlFactory(version=version, page_type=page_type, args=args).create()
  return redirect(str(url_object), code=302)

def _get_version():
  try:
    return Version(request.args.get('version', default=LATEST_VERSION, type=int))
  except ValueError:
    return "version is invalid.", 400

def _get_page_type():
  try:
    return PageTypeFactory(request.args.get('page_type', type=str)).create()
  except (ValueError, AttributeError):
    return "page type is invalid.", 400

def _without_keys(d, keys):
  return {x: d[x] for x in d if x not in keys}