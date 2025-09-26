'''modx.py: A module whose functions have to do with other modules.
For example: importall(), a function used to import every single module
in Python that is supported on most devices without printing an
error message, does not print out dialog nor pop up a link when
imported, and not required to be downloaded
separately with Python (such as Pygame, downloaded in Terminal).

Modules ios_support, pty, this, sre_compile, sre_parse,
sre_constants, tty, idle and antigravity are left out of import_all().
Reason: ios_support not supporting computers,
pty and tty importing a non-existing module (termios),
sre_compile, sre_constants and sre_parse printing warnings,
this printing out "The Zen of Python" poem, idle
opening up Python Shell window, and
antigravity popping out a web browser link
(There are more modules left out but the full list is way too long).

Permission to use this module is granted to anyone wanting to use it,
under the following conditions: 1.) Any copies of this module must be clearly
marked as so. 2.) The original of this module must not be misrepresented;
you cannot claim this module is yours.

Note: for imported(), module idlelib will not show up as it is pre-imported
as soon as this module is run, leading to problems and bugs, thus idlelib
is not shown in imported().

Created by: Austin Wang. Created at: September 19, 2025. Version: 1.3.1'''

import sys, importlib, pkgutil, random

# Record what modules were loaded at the time modx itself was imported
_initial_modules = set(sys.modules.keys())
import builtins

# Capture original __import__ BEFORE overriding
_original_import = builtins.__import__

# Track modules imported manually by the user after ModX loaded
_user_imports = set()

def _tracking_import(name, globals=None, locals=None, fromlist=(), level=0):
    """
    Non-public function: wrapper around Python's import to record user imports,
    even if the module was already loaded.
    """
    # Use the *original* import function to avoid recursion
    mod = _original_import(name, globals, locals, fromlist, level)
    top_name = name.split('.')[0]
    if not name.startswith('idlelib'):
        _user_imports.add(top_name)
    return mod

# Install the hook immediately when ModX is imported
builtins.__import__ = _tracking_import

_imported_by_modx = set()
# Track modules at the last imported() call
_last_imported_snapshot = set(_initial_modules)


modules = [
        'collections', 'sys', 'asyncio', 'concurrent', 'ctypes', 'dbm', 'email',
        'encodings', 'ensurepip', 'html', 'http', 'idlelib', 'importlib', 'json', 'logging',
        'multiprocessing', 'pathlib', 'pydoc_data', 're', 'sqlite3',
        'sysconfig', 'test', 'tkinter', 'tomllib', 'turtledemo', 'unittest', 'urllib',
        'venv', 'wsgiref', 'xml', 'xmlrpc', 'zipfile', 'zoneinfo',
        '_pyrepl', '_collections_abc', '_colorize',
        '_compat_pickle', '_compression', '_markupbase', '_opcode_metadata',
        '_py_abc', '_pydatetime', '_pydecimal', '_pyio', '_pylong', '_sitebuiltins', '_strptime',
        '_threading_local', '_weakrefset', 'abc', 'argparse', 'ast', 'base64', 'bdb',
        'bisect', 'bz2', 'calendar', 'cmd', 'codecs', 'codeop', 'colorsys', 'compileall', 'configparser',
        'contextlib', 'contextvars', 'copy', 'copyreg', 'cProfile', 'csv', 'dataclasses', 'datetime',
        'decimal', 'difflib', 'dis', 'doctest', 'enum', 'filecmp', 'fileinput', 'fnmatch', 'fractions',
        'ftplib', 'functools', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib',
        'gzip', 'hashlib', 'heapq', 'hmac', 'imaplib', 'inspect', 'io', 'ipaddress', 'keyword', 'linecache',
        'locale', 'lzma', 'math', 'mailbox', 'mimetypes', 'modulefinder', 'netrc',
        'opcode', 'optparse', 'os', 'pdb', 'pickle', 'pickletools', 'pkgutil',
        'platform', 'plistlib', 'poplib', 'pprint', 'profile', 'pstats', 'py_compile',
        'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 'reprlib', 'runpy', 'sched', 'secrets',
        'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtplib', 'socket', 'socketserver',
        'ssl', 'stat', 'statistics', 'string', 'stringprep',
        'struct', 'subprocess', 'symtable', 'tabnanny', 'tarfile', 'tempfile', 'textwrap',
        'threading', 'timeit', 'token', 'tokenize', 'trace', 'traceback', 'tracemalloc', 'turtle',
        'types', 'typing', 'uuid', 'warnings', 'wave', 'weakref', 'webbrowser', 'zipapp', 'zipimport',
        '__future__', '__hello__', '__phello__', "atexit", "mmap",
        'autocomplete','autocomplete_w','autoexpand','browser','build',
        'calltip','calltip_w','codecontext','colorizer',
        'config','config_key','configdialog','debugger','debugger_r',
        'debugobj','debugobj_r','delegator','direct','dynoption','editor',
        'filelist','format','grep','help','help_about','history','hyperparser',
        'id','idle_test','iomenu','keyring','mainmenu','more_itertools',
        'multicall','outwin','parenmatch','pathbrowser','percolator','pyparse',
        'pyshell','query','redirector','replace','rpc','run',
        'runscript','screeninfo','scrolledlist','search','searchbase','searchengine',
        'sidebar','squeezer','stackviewer','statusbar','textview','tooltip',
        'tree','undo','util','window','zoomheight','zzdummy', 'builtins', 'itertools',
        'operator', 'collections.abc', 'errno', 'msvcrt', 'array', 'marshal', 'readline',
        'rlcompleter', 'urllib.request', 'urllib.response', 'urllib.parse', 'urllib.error', 
        'urllib.robotparser', 'http.client', 'http.server', 'nntplib', 'telnetlib',
        'smtpd', 'xml.etree.ElementTree', 'xml.parsers.expat', 'audioop', 'aifc', 'sunau', 'chunk',
        'imghdr', 'lib2to3', '_thread', '_weakref', '_collections', '_ast', '_bisect',
        '_heapq', '_io', '_functools', '_operator', '_signal', '_socket', '_ssl',
        '_stat', '_struct', '_datetime', '_random', '_hashlib', '_md5', '_sha1',
        '_blake2', '_pickle', '_json', '_zoneinfo', '_opcode', 'cmath', 'numbers',
        ]


def import_all():
    """Import about every module in Python that is given when downloading Python."""
    import builtins
    # Temporarily disable tracking hook to avoid recursion
    builtins.__import__ = _original_import
    try:
        # In import_all() and similar functions, pre-compile the split
        for m in modules:
            try:
                globals()[m] = importlib.import_module(m)
                _imported_by_modx.add(m.partition('.')[0])  # Slightly faster than split('.')[0]
            except Exception:
                pass
    finally:
        # Restore tracking hook
        builtins.__import__ = _tracking_import

def list_importall():
    """Return the list of modules that import_all() would import"""
    return modules

def modules_loaded():
    """Shows how many modules are currently loaded in sys.modules."""
    return len(sys.modules)

def import_random(n):
    """Import n random stdlib modules and track them."""
    import builtins
    chosen = random.sample(modules, min(n, len(modules)))
    builtins.__import__ = _original_import
    try:
        for m in chosen:
            try:
                globals()[m] = importlib.import_module(m)
                _imported_by_modx.add(m.partition('.')[0])  # Slightly faster than split('.')[0]
            except Exception:
                pass
    finally:
        builtins.__import__ = _tracking_import
    return chosen

def import_external():
    """Import all installed third-party modules (anything not in stdlib list).
Does NOT show user defined modules."""
    import builtins
    stdlib_set = set(modules) | set(sys.builtin_module_names)
    builtins.__import__ = _original_import
    try:
        for finder, name, ispkg in pkgutil.iter_modules():
            if name not in stdlib_set:
                try:
                    globals()[name] = importlib.import_module(name)  # Fixed: m -> name
                    _imported_by_modx.add(name.partition('.')[0])    # Fixed: m -> name
                except Exception:
                    pass
    finally:
        builtins.__import__ = _tracking_import

def import_screen():
    """Import common screen/GUI/game modules if available."""
    import builtins
    screen_modules = ['pygame', 'pyglet', 'arcade', 'tkinter', 'turtle']
    builtins.__import__ = _original_import
    try:
        for m in modules:
            try:
                globals()[m] = importlib.import_module(m)
                _imported_by_modx.add(m.partition('.')[0])  # Slightly faster than split('.')[0]
            except ImportError:
                pass
    finally:
        builtins.__import__ = _tracking_import

def imported():
    """
    Show all modules imported since ModX loaded:
    Whether by user, ModX or dependencies.
    This counts imports that were already imported
    before ModX started. Modules that ModX import at
    the start (sys, importlib, pkgutil, random)
    won't show up.
    """
    # Union of user imports and ModX imports
    all_new = _user_imports | _imported_by_modx

    all_new_sorted = sorted(all_new)
    print("Modules imported after ModX load (user, ModX and dependencies):")
    for name in all_new_sorted:
        print("-", name)
    print(f"\nTotal modules imported after ModX load: {len(all_new_sorted)}")

def modximported():
    """
    Show only the modules imported via ModX functions
    (import_all, import_random, import_external, import_screen),
    plus a total count.
    """
    top_level_sorted = sorted(_imported_by_modx)
    print("Modules imported via ModX:")
    for name in top_level_sorted:
        print("-", name)
    print(f"\nTotal modules imported via ModX: {len(top_level_sorted)}")

def import_letter(letter):
    """
    Import every standard library module from the ModX 'modules' list
    whose name starts with the given letter (case-insensitive).
    
    Example:
        import_letter('t')  # imports turtle, tkinter, tarfile, etc.
    """
    letter = letter.lower()
    imported_list = []

    for m in modules:
        if m.lower().startswith(letter):
            try:
                globals()[m] = importlib.import_module(m)
                _imported_by_modx.add(m.partition('.')[0])  # Slightly faster than split('.')[0]
                imported_list.append(m)
            except Exception:
                pass  # skip modules that can't be imported

    return imported_list

def search_modules(keyword):
    """
    Search for modules whose names contain the keyword.
    """
    keyword = keyword.lower()
    matches = []
    for m in modules:
        if keyword in m.lower():
            matches.append(m)
    return matches


def info(module_name):
    """
    Show basic info about typed module: file path, built-in status, docstring.
    """
    import sys, inspect
    if module_name in sys.modules:
        mod = sys.modules[module_name]
    else:
        try:
            mod = importlib.import_module(module_name)
        except ImportError:
            print(f"Module '{module_name}' not found.")
            return
    path = getattr(mod, '__file__', '(built-in)')
    doc = (inspect.getdoc(mod) or '').splitlines()[0:3]
    print(f"Module: {module_name}")
    print(f"Path: {path}")
    print("Docstring:")
    for line in doc:
        print(line)

def nonimported():
    """
    Returns a list of standard library modules that have NOT been imported yet.

    Ignores:
      - Third-party packages (site-packages)
      - Any user-defined modules (any path outside the stdlib or built-ins)
    """
    import os
    import sys
    import importlib
    import pkgutil
    from pathlib import Path

    unimported_list = []

    # Get stdlib directory (…/lib/pythonX.Y)
    stdlib_dir = Path(os.__file__).parent.resolve()
    builtins_set = set(sys.builtin_module_names)

    for module_info in pkgutil.iter_modules():
        name = module_info.name

        # Skip already-loaded modules
        if name in sys.modules:
            continue

        try:
            spec = importlib.util.find_spec(name)
            if not spec:
                continue

            # Built-ins have no origin but should be included
            if name in builtins_set:
                unimported_list.append(name)
                continue

            origin = spec.origin
            if not origin:
                continue

            origin_path = Path(origin).resolve()

            # Must live inside stdlib_dir to count as stdlib
            if stdlib_dir in origin_path.parents:
                unimported_list.append(name)

        except Exception:
            continue

    return sorted(set(unimported_list))

def modxhelp():
    """
    Show full ModX help including all functions and example usage.
    """
    help_text = """
ModX — The Python Module Universe
=================================

Functions:
----------

import_all()
    Import almost every standard library module at once.
    Example: modx.import_all()

import_external()
    Import all installed third-party modules.
    Example: modx.import_external()

import_screen()
    Import common screen/GUI/game modules if available (pygame, turtle, tkinter, etc.).
    Example: modx.import_screen()

import_letter(letter)
    Import every standard library module starting with a given letter.
    Example: modx.import_letter('t')

import_random(n)
    Import n random standard library modules.
    Example: modx.import_random(5)

list_importall()
    Return a list of modules that import_all() would load.
    Example: modx.list_importall()

modules_loaded()
    Show how many top-level modules are currently loaded.
    Example: modx.modules_loaded()

imported()
    Show ALL modules currently loaded in Python (top-level only).
    Example: modx.imported()

modximported()
    Show only the modules imported via ModX functions.
    Example: modx.modximported()

info(module_name)
    Show information (path + docstring snippet) about a module.
    Example: modx.info('random')

search_modules(keyword)
    Search the stdlib modules list for names or docstrings containing a keyword.
    Example: modx.search_modules('html')

modxhelp()
    Show this help screen.
    Example: modx.modxhelp()
    
Tips:
-----
- Use imported() to see *everything* loaded after Python started.
- Use modximported() to see only what ModX loaded.
- You can combine functions, e.g. modx.import_all() then modx.imported().
"""
    print(help_text)

def isimported(module_name: str):
    """Check if a module is imported in caller's globals."""
    import importlib.util
    import inspect
    
    try:
        frame = inspect.currentframe().f_back
        caller_globals = frame.f_globals
        
        if module_name in caller_globals:
            return True
            
        spec = importlib.util.find_spec(module_name)
        return False if spec else f"Module '{module_name}' doesn't exist."
        
    except Exception:
        return "Error checking module status."
