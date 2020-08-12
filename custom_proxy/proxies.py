from . import app
from .factories.url_factories import UrlFactory
from flask import request
import importlib
import urllib.request
import os

@app.route('/<version>/<page_type>', methods=['GET'])
def official_web_site_proxy(version, page_type):
  cache_file = _CacheFile(version=version, page_type=page_type, args=request.args)
  if (request.headers.get("Cache-Control") == 'no-cache') or (cache_file.content() is None):
    # FIXME request.args で渡してるけど新しいパラメーター増やした瞬間バグる
    # 結合度的に言えばスタンプ結合的なやつ？
    url_object = UrlFactory(version=version, page_type=_get_page_type_enum(page_type), args=request.args).create()
    urllib.request.urlretrieve(str(url_object), cache_file._path())
  return cache_file.content()

def _get_page_type_enum(page_type):
  module = importlib.import_module("custom_proxy.page_types")
  return getattr(module.PageType, page_type.upper())

class _CacheFile:
  def __init__(self, version, page_type, args):
    self._version = version
    self._page_type = page_type
    self._args = args
    os.makedirs(self._dir(), exist_ok=True)

  def content(self):
    if os.path.isfile(self._path()):
      with open(self._path()) as f:
        return f.read()
    else:
      return None

  def _path(self):
    return '/'.join([self._dir(), self._signature()])

  def _signature(self):
    return '_'.join([str(value) for value in self._args.values()])

  def _dir(self):
    return "caches/v{}/{}".format(self._version, self._page_type)
