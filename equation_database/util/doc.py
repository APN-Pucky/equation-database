import inspect
import warnings
import sympy
import bibtexparser

from dataclasses import dataclass
from typing import Optional


@dataclass
class Param:
    name: str
    description: str
    latex: Optional[str] = None  # Optional: nicer rendering


def add_latex(latex_str):
    def decorator(func):
        func.__doc__ = latex_str  # Optionally overwrite the docstring
        func.__latex__ = lambda: latex_str  # Add a __latex__ method
        return func

    return decorator


def equation(
    summary: str = None,
    latex=None,
    description: str = None,
    args: list[Param] = None,
    tags: list[str] = None,
    # TODO add warnings and other metadata?
):
    """

    Args:
        summary: Short summary of the equation
        latex: Optional LaTeX override
        description: Longer description of the equation
        args: List of parameters with their descriptions and optional LaTeX
        tags: List of tags for categorization

    """

    def wrapper(target):
        target.metadata = {
            "summary": summary,
            "description": description,
            "latex": latex,
            "args": args,
            "tags": tags,
        }
        # TODO be strict?
        # if target.__doc__ is not None:
        #    # Warning that this will overwrite existing docstring
        #    # Better put this information in the equation decorator metadata
        #    warnings.warn(
        #        f"Overwriting docstring of {target.__name__} in the future. "
        #        "If you want to keep the original docstring, "
        #        "use the `equation` decorator instead."
        #    )
        olddoc = target.__doc__
        target.__doc__ = ""
        if summary is not None:
            target.__doc__ += f"{summary}"
        if latex is not None:
            target.__doc__ += "$$" + latex + "$$\n"
            target.__latex__ = latex
        if description is not None:
            target.__doc__ += f"\n\n{description}\n"
        target.__doc__ += olddoc or ""
        if args is not None:
            dargs = {k.name: k for k in args}
            sig = inspect.signature(target)
            # missing = [k for k in sig.parameters if k not in (dargs or {})]
            # if missing:
            #    # TODO too strict?
            #    warnings.warn(f"Missing documentation for: {', '.join(missing)}")
            # Add Args section
            if not target.__doc__.endswith("\n"):
                target.__doc__ += "\n"
            target.__doc__ += "\n    Args:\n"

            for k, v in dargs.items():
                if k not in sig.parameters:
                    warnings.warn(f"Argument {k} not found in function signature")
                target.__doc__ += f"        {k}: {v.description}"
                if v.latex is not None:
                    target.__doc__ += f"(${v.latex}$)"
                target.__doc__ += "\n\n"

        if tags:
            if not target.__doc__.endswith("\n"):
                target.__doc__ += "\n"
            target.__doc__ += "\n\n    :keywords: " + ", ".join(tags) + "\n"

        r = target()
        # if array loop
        tex = ""
        if not isinstance(r, tuple):
            r = (r,)
        if isinstance(r, tuple):
            tex = tex + "\n\n    Returns:"
            for i in r:
                tex = tex + "\n        $" + sympy.latex(i) + "$,"
            # tex = tex + "\n\n    Example:"
            # for n, i in enumerate(r):
            #    tex += (
            #        "\n"
            #        + indent_string_twice(
            #            f">>> print(sympy.latex({target.__name__}()[{n}]))"
            #        )
            #        + "\n"
            #        + indent_string_twice(sympy.latex(i))
            #    )
            #    # tex += indent_string_twice(f">>> print(sympy.mathml({target.__name__}()))") + "\n" + indent_string_twice(sympy.mathml(r))
            tex = tex + "\n\n    .. tabs::"
            if latex is not None:
                tex += indent_string(
                    "\n\n    .. tab :: Original LaTeX\n\n"
                    + "        ::\n\n"
                    + indent_string(latex, 3)
                )
            tex += indent_string(
                "\n\n    .. tab :: LaTeX\n\n"
                + "        ::\n\n"
                + "\n\n".join([indent_string(sympy.latex(i), 3) for i in r])
            )
            tex += indent_string(
                "\n\n    .. tab :: MathML\n\n"
                + "        ::\n\n"
                + "\n\n".join([indent_string(sympy.mathml(i), 3) for i in r])
            )
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Sympy\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.sstr(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Octave\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.octave_code(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Mathematica\n\n"
                    + "        ::\n\n"
                    + "\n\n".join(
                        [indent_string(sympy.mathematica_code(i), 3) for i in r]
                    )
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Python\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.pycode(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: C\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.ccode(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: C++\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.cxxcode(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Fortran\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.fcode(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Rust\n\n"
                    + "        ::\n\n"
                    + "\n\n".join([indent_string(sympy.rust_code(i), 3) for i in r])
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: ASCII\n\n"
                    + "        ::\n\n"
                    + "\n\n".join(
                        [
                            indent_string(sympy.pretty(i, use_unicode=False), 3)
                            for i in r
                        ]
                    )
                )
            except Exception:
                # fails for some expressions
                pass
            try:
                tex += indent_string(
                    "\n\n    .. tab :: Unicode\n\n"
                    + "        ::\n\n"
                    + "\n\n".join(
                        [indent_string(sympy.pretty(i, use_unicode=True), 3) for i in r]
                    )
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
