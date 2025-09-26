"""Installer for the rer.ufficiostampa package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="rer.ufficiostampa",
    version="3.0.4",
    description="Policy for Ufficio Stampa",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="RedTurtle Technology",
    author_email="sviluppo@redturtle.it",
    url="https://github.com/RegioneER/rer.ufficiostampa",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/rer.ufficiostampa",
        "Source": "https://github.com/RegioneER/rer.ufficiostampa",
        "Tracker": "https://github.com/RegioneER/rer.ufficiostampa/issues",
        # 'Documentation': 'https://rer.ufficiostampa.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["rer"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "itsdangerous>=1.1.0",
        "plone.base",
        "premailer",
        "requests",
        "souper.plone",
        "defusedcsv",
        "rer.blocks2html",
        "collective.volto.blocksfield",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.iterate",
            "plone.app.robotframework",
            "collective.MockMailHost",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = rer.ufficiostampa.locales.update:update_locale
    """,
)
