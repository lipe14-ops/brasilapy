import pytest


@pytest.fixture
def registro_br_domain_json():
    return {
        "status_code": 2,
        "status": "REGISTERED",
        "fqdn": "testdomain.com.br",
        "fqdnace": "",
        "exempt": False,
        "hosts": ["d.sec.dns.br", "f.sec.dns.br"],
        "publication-status": "published",
        "expires-at": "2024-08-10T00:00:00-03:00",
        "suggestions": [
            "agr.br",
            "app.br",
            "art.br",
            "blog.br",
            "dev.br",
            "eco.br",
            "esp.br",
            "etc.br",
            "far.br",
            "flog.br",
            "imb.br",
            "ind.br",
            "inf.br",
            "log.br",
            "net.br",
            "ong.br",
            "rec.br",
            "seg.br",
            "srv.br",
            "tec.br",
            "tmp.br",
            "tur.br",
            "tv.br",
            "vlog.br",
            "wiki.br",
        ],
    }
