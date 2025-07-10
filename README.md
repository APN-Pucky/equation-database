# equation-database

[![Documentation Status](https://readthedocs.org/projects/equation-database/badge/?version=latest)](https://equation-database.readthedocs.io/en/latest/?badge=latest)

## Description

This project is a database of equations that can be used in various fields of science and engineering.
- Equations are uniquely identified by their publication (doi, isbn, arxiv, inspirehep, etc.) with invalid python module characters replaced by underscores.
- Every equation must be the exact copy of the original publication.
- All ingredients of the equations should at least be labelled.


## FAQ

- Why?
    - Coming from HEP experimental papers often come with data on hepdata. Similarly to the data, the equations should be stored in a database.
- Why sympy?
    - Since sympy has the best conversion to LaTeX, MathML and other programming languages.

## Contributing

The minimum requirement for a contribution is:

```python
@bib()
def bibtex():
    bibtex: str = r"""
    ORIGINAL SOURCE AS BIBTEX ENTRY
"""
    return bibtex

@equation(
    latex="...",
)
def equation_X_Y_Z():
    raise NotImplementedError("This equation is not implemented in sympy yet.")

```

The ideal contribution however adds more information:

```python
@bib()
def bibtex():
    # SRC: https://where-to-download-if-not-given-in-bibtex
    bibtex: str = r"""
    ORIGINAL SOURCE AS BIBTEX ENTRY
"""

@equation(
    summary="...",
    latex="...",
    description="""
    ...
    See-also ...
    Ref ...
    ..warn ...
    ..note ...
    """,
    args = [
        Param("name", "description", "latex_name"),
        ...
    ],
    tags=["tag1", "tag2"],
)
def equation_X_Y_Z(
    name=sympy.Symbol("name"),
    ...
):
    return sympy.Eq(name, name)
```
