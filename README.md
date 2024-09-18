# equation-database


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
