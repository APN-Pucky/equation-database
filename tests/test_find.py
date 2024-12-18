import equation_database as edb


def test_find_arxiv():
    fpaper = edb.find(eprint="2202.13416")
    from equation_database import arxiv_2202_13416 as ipaper

    assert fpaper == ipaper
