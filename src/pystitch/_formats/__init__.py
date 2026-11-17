import importlib
import pkgutil

# Load all formats
for _loader, module_name, _is_pkg in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f".{module_name}", __name__)
