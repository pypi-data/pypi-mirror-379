==============
sphinx-linkfix
==============

.. image:: https://img.shields.io/badge/python-3.9+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python Version

.. image:: https://img.shields.io/badge/license-MIT-green.svg
    :alt: License

Sphinx extension that rewrites GitHub-style links into proper Sphinx references.

🎯 **Project Description**
--------------------------

I like to have links in the README that point to other sections of the documentation,
so you can navigate the docs easily from the GitHub repo itself. However, Sphinx does not
understand GitHub-style links (e.g., \`reference <docs/reference.rst>\`_), so links break
when building the docs. If you write links using Sphinx syntax instead, they work in the built docs but
not on GitHub.

This extension solves this problem by rewriting GitHub-style links into proper Sphinx references
during the Sphinx build process. It scans the document for links that point to local files
and rewrites them to use Sphinx's internal referencing system.

You can combine this with a script to removes all of the links in the README during CI before publishing
to pypi, so that the README on PyPI does not contain broken links, and keep a single README file for GitHub, Sphinx and PyPI.


🚀 **Key Features**
-------------------

- **Transform GitHub-style links**: Automatically rewrite links in the documentation to use Sphinx's internal referencing system.
- **Ignores external links**: Only processes local file links, leaving external URLs untouched.
- **Configurable prefixes**: Specify path prefixes to strip from links for cleaner references.
- **Support for multiple file extensions**: Configure which file extensions to process (e.g., ``.rst``, ``.md``).
- **Easy integration**: Simple setup and configuration in ``conf.py``.


🚀 **Quick Start Guide**
------------------------

1. Install the extension using pip:

.. code-block:: bash

    pip install sphinx-linkfix

2. Add the extension to your Sphinx ``conf.py`` file:

.. code-block:: python

    extensions = [
        ...,
        'sphinx_linkfix',
    ]

3. (Optional) Configure the extension in ``conf.py``:

.. code-block:: python

    # List of path prefixes to strip from links
    sphinx_linkfix_strip_prefixes = ('docs/', 'source/')

    # List of file extensions to process
    sphinx_linkfix_file_extensions = ('.rst', '.md')

4. Write links in your documentation using GitHub-style syntax, e.g., \`Reference <REFERENCE.rst>\`_. (You can use the repository README.rst as an examples)

5. Create files in your sphinx directory with the same names that you used in the links, that include the original file. E.g., docs/REFERENCE.rst with

.. code-block:: rst

    .. include:: ../REFERENCE.rst

6. During the Sphinx build process, the extension scans the documents for links that point to local files and rewrites them to use Sphinx's internal referencing system.


📚 **Documentation**
--------------------

**Essential Guides:**

- 📦 `Installation Guide <docs/installation.rst>`_ - Setup instructions and requirements
- 🤝 `Contributing Guidelines <CONTRIBUTING.rst>`_ - Development standards and contribution process
- 📄 `License <LICENSE.txt>`_ - License terms and usage rights
- 👥 `Authors <AUTHORS.rst>`_ - Project contributors and maintainers
- 📜 `Changelog <CHANGELOG.rst>`_ - Project history and version changes
- 📜 `Code of Conduct <CODE_OF_CONDUCT.rst>`_ - Guidelines for participation and conduct
