import equation_database as edb


def test_find_arxiv():
    fpaper = edb.find(eprint="2202.13416")
    from equation_database import arxiv_2202_13416 as ipaper

    assert fpaper == ipaper


def test_find_doi():
    fpaper = edb.find(eprint="10.1103/PhysRev.176.1700")
    from equation_database import doi_10_1103_physrev_176_1700 as ipaper

    assert fpaper == ipaper


def test_find_inspire():
    fpaper = edb.find(eprint="Field:1989uq")
    from equation_database import inspirehep_Field_1989uq as ipaper

    assert fpaper == ipaper


def test_find_isbn():
    fpaper = edb.find(eprint="978-0-201-50397-5")
    from equation_database import isbn_9780201503975 as ipaper

    assert fpaper == ipaper
