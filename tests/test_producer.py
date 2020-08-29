import requests

from webchecker.producer import check_site
from webchecker.schemas import Site


def test(requests_mock):
    site = Site(id=1, url='https://example.com/')
    requests_mock.get(site.url)
    metric = check_site(site)

    assert metric.status_code == 200
    assert metric.error is None
    assert metric.site_id == site.id

def test_error(requests_mock):
    site = Site(id=1, url='https://example.com/')
    requests_mock.get(site.url, exc=requests.exceptions.ConnectTimeout)
    metric = check_site(site)

    assert metric.status_code is None
    assert metric.error == requests.exceptions.ConnectTimeout.__name__
    assert metric.site_id == site.id
