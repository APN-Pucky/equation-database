import sympy

def equation():
    def wrapper(target):
        if target.__doc__ is None:
            target.__doc__ = ""
        r = target()
        # if array loop
        if isinstance(r, tuple):
            for i in r:
                target.__doc__ = target.__doc__ + "\n\n$" + sympy.latex(i) +"$" + "\n:: \n"+ indent_string_twice(sympy.latex(i))
        else:
            target.__doc__ = target.__doc__ +"\n\n$" + sympy.latex(r) +"$" + "\n:: \n" + indent_string_twice(sympy.latex(r))
        return target
    return wrapper

def indent_string_twice(string):
    indented_string = '\n'.join('        ' + line for line in string.splitlines())
    return indented_string

def bib():
    def wrapper(target):
        if target.__doc__ is None:
            target.__doc__ = ""
        r = target()
        # if array loop
        if isinstance(r, tuple):
            for i in r:
                #target.__doc__ = target.__doc__ +"\n.. code-block:: bibtex\n" + indent_string_twice(i)
                target.__doc__ = target.__doc__ +"\n:: \n" + indent_string_twice(i)
        else:
            #target.__doc__ = target.__doc__ +"\n.. code-block:: bibtex\n"+ indent_string_twice(r)
            target.__doc__ = target.__doc__ +"\n:: \n"+ indent_string_twice(r)
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
            target.__doc__ += f"\n\n- {key}:\n\n    ${latex_expr}$" # TODO latex expression?
        
        return target
    return wrapper