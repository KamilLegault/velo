#!/usr/bin/env python
import setuptools

if not getattr(setuptools, "_distribute", False):
    raise SystemExit("""Setuptools is not supported. Please use Distribute""")

setup_requires = [
    # d2to1 bootstrap
    'd2to1',
    ]

tests_require = [
    # Testing dependencies (the application doesn't need them to *run*)
    'nose',
    'nosexcover',
    'coverage',
    'mock',
    'webtest',
    'yanc',
    'Sphinx',
    ]

setuptools.setup(
    setup_requires=setup_requires + tests_require,
    tests_require=tests_require,
    d2to1=True,
    test_suite='nose.collector',
    package_data={"velo": [
        "templates/*.*",
        "templates/*/*.*",
        "static/*.*",
        "static/*/*.*",
        "static/*/*/*.*",
    ]},
    entry_points="""\
        [paste.app_factory]
            main = velo:main
    """
    )
