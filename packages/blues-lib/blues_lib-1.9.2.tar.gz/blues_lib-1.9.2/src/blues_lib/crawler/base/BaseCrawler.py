from blues_lib.behavior.BhvExecutor import BhvExecutor
from blues_lib.type.output.STDOut import STDOut
from blues_lib.type.model.Model import Model
from blues_lib.namespace.CrawlerName import CrawlerName
from blues_lib.crawler.Crawler import Crawler

class BaseCrawler(Crawler):

  def _before_crawled(self):
    # main crawler
    self._crawler_meta = self._meta.get(CrawlerName.Field.CRAWLER.value)
    self._crawler_conf = self._conf.get(CrawlerName.Field.CRAWLER.value)

    # head crawler
    self._head_meta:dict = self._meta.get(CrawlerName.Field.HEAD_CRAWL.value)
    self._head_conf:dict = self._conf.get(CrawlerName.Field.HEAD_CRAWL.value)

    # foot crawler
    self._foot_meta:dict = self._meta.get(CrawlerName.Field.FOOT_CRAWL.value)
    self._foot_conf:dict = self._conf.get(CrawlerName.Field.FOOT_CRAWL.value)

  def _head(self)->any:
    # execute the head crawler
    if self._head_meta:
      # must pass the meta and bizdata, some behavior need to calculate the model
      model = Model(self._head_meta,self._bizdata)
      return self._invoke(model)

  def _foot(self,output:STDOut)->any:
    # execute the head crawler
    if self._foot_meta:
      # must pass the meta and bizdata, some behavior need to calculate the model
      model = Model(self._foot_meta,self._bizdata)
      return self._invoke(model)

  def _invoke(self,model:Model)->STDOut:
    try:
      bhv = BhvExecutor(model,self._browser)
      stdout:STDOut = bhv.execute()
      if isinstance(stdout.data,dict):
        stdout.data = stdout.data.get(CrawlerName.Field.DATA.value)
      return stdout
    except Exception as e:
      message = f'[{self.NAME}] Failed to crawl - {e}'
      self._logger.error(message)
      return STDOut(500,message)
  