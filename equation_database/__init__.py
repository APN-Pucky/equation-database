import importlib
import pkgutil
import bibtexparser


def find(title=None, doi=None, isbn=None, eprint=None, key=None):
    """
    Find a paper by an entry in the bibtex and return the imported module.
    """
    package_name = "equation_database"
    target_function_name = "bibtex"
    # Iterate through submodules of the package
    for module_info in pkgutil.iter_modules(
        importlib.import_module(package_name).__path__
    ):
        module_name = f"{package_name}.{module_info.name}"
        # Dynamically import the submodule
        submodule = importlib.import_module(module_name)

        # Check if the function exists in the submodule
        if hasattr(submodule, target_function_name):
            target_function = getattr(submodule, target_function_name)

            # Call the function and evaluate the condition
            r = target_function()
            for entry in bibtexparser.loads(r).entries:
                if entry.get("doi"):
                    if entry["doi"] == doi:
                        return submodule
                if entry.get("eprint"):
                    if entry["eprint"] == eprint:
                        return submodule
                if entry.get("title"):
                    if entry["title"] == title:
                        return submodule
                if entry.get("isbn"):
                    if entry["isbn"] == isbn:
                        return submodule
                if entry.get("ID"):
                    if entry["ID"] == key:
                        return submodule

    return None
