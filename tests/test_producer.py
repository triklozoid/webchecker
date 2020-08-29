from webchecker.producer import check
from webchecker.schemas import Site


def test(requests_mock):
    url = 'https://example.com/'
    site = Site(id=1, url=url)
    requests_mock.get(url)
    metric = check(site)

    assert metric.status_code == 200
    assert metric.error is None
