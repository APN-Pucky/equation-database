import sympy


def equation():
    """

    Args:
        path: The path of the file to wrap
        field_storage: The :class:`FileStorage` instance to wrap
        temporary: Whether or not to delete the file when the File
           instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor

    """

    def wrapper(target):
        if target.__doc__ is None:
            target.__doc__ = ""
        r = target()
        # if array loop
        tex = ""
        if isinstance(r, tuple):
            tex = tex + "\n\n    Returns:"
            for i in r:
                tex = tex + "\n        $" + sympy.latex(i) + "$,"
            tex = tex + "\n\n    Example:"
            for n, i in enumerate(r):
                tex += (
                    "\n"
                    + indent_string_twice(
                        f">>> print(sympy.latex({target.__name__}()[{n}]))"
                    )
                    + "\n"
                    + indent_string_twice(sympy.latex(i))
                )
                # tex += indent_string_twice(f">>> print(sympy.mathml({target.__name__}()))") + "\n" + indent_string_twice(sympy.mathml(r))
        else:
            tex = tex + "\n\n    Returns:\n        $" + sympy.latex(r) + "$"
            tex = tex + "\n\n    .. tabs::\n\n"
            tex += indent_string(
                "    .. tab :: LaTeX\n\n"
                + "        ::\n\n    "
                + indent_string_twice(sympy.latex(r))
            )
            tex += indent_string(
                "\n\n    .. tab :: MathML\n\n"
                + "        ::\n\n    "
                + indent_string_twice(sympy.mathml(r))
            )
            tex += indent_string(
                "\n\n    .. tab :: Sympy\n\n"
                + "        ::\n\n    "
                + indent_string_twice(sympy.mathematica_code(r))
            )
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Octave\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.octave_code(r))
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Mathematica\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.mathematica_code(r))
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Python\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.pycode(r))
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: C\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.ccode(r))
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Fortran\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.fcode(r))
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Rust\n\n"
                    + "        ::\n\n    "
                    + indent_string_twice(sympy.rust_code(r))
                )
            except Exception:
                # fails for some expressions
                pass
        target.__doc__ = target.__doc__ + tex
        return target

    return wrapper


def indent_string_twice(string):
    return indent_string(string, 2)


def indent_string(string, n=1):
    indented_string = "\n".join("        " * n + line for line in string.splitlines())
    return indented_string


def bib():
    def wrapper(target):
        if target.__doc__ is None:
            target.__doc__ = ""
        r = target()
        ret = target.__doc__
        try:
            import bibtexparser

            for entry in bibtexparser.loads(r).entries:
                if entry.get("doi"):
                    ret += f"`DOI <https://doi.org/{entry['doi']}>`_, "
                if entry.get("eprint"):
                    ret += f"`arXiv <https://arxiv.org/abs/{entry['eprint']}>`_, "
                if entry.get("url"):
                    ret += f"`URL <{entry['url']}>`_, "
                if entry.get("title"):
                    t = f"{entry['title']}"
                    if t[0] == "{" and t[-1] == "}":
                        t = t[1:-1]
                    ret += t + " "
        except ImportError:
            pass
        ret += "\n:: \n" + indent_string_twice(r)
        target.__doc__ = ret
        return target

    return wrapper


def table():
    def wrapper(target):
        if target.__doc__ is None:
            target.__doc__ = ""
        r = target()
        # Loop through the table and add only the second column (the LaTeX expression) to the docstring
        for key, expression in r.items():
            latex_expr = sympy.latex(expression)
            target.__doc__ += (
                f"\n\n- {key}:\n\n    ${latex_expr}$"  # TODO latex expression?
            )

        return target

    return wrapper
