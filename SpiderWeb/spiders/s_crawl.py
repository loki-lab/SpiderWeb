from crawl import JobSpider
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from time import strftime, gmtime


def crawl_job():
    settings = get_project_settings()
    configure_logging()
    runner = CrawlerRunner(settings=settings)

    return runner.crawl(JobSpider)

def schedule_next_crawl(null, sleep_time):

    reactor.callLater(sleep_time, crawl)

def crawl():

    d = crawl_job
    d.addCallback(schedule_next_crawl, 60 * 60 * 6)
    d.addErrback(catch_error)

def catch_error(failure):
    print(failure.value)

if __name__ == "main":
    print('chanhtuoi')
    print(strftime("%Y-%m-%d $H:%M:%S", gmtime()))
    crawl()
    reactor.run()
