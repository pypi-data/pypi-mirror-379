==============
Contributing
==============

We welcome contributions to the sphinx-linkfix project! This guide will help you get started with contributing to the project.

📋 **Table of Contents**
========================

1. `Getting Started`_
2. `Development Setup`_
3. `Development Workflow`_
4. `Branching Model and Workflow`_
5. `Code Standards`_
6. `Testing`_
7. `Documentation`_
8. `Submitting Changes`_
9. `Issue Reporting`_
10. `Project Structure`_

Getting Started
===============

Prerequisites
-------------

- Python 3.9
- Git
- Docker (optional, for containerized development)
- Conda or similar environment manager (recommended)

Fork and Clone
--------------

1. Fork the repository on GitHub
2. Clone your fork locally:

.. code-block:: bash

    git clone https://github.com/j-moralejo-pinas/sphinx-linkfix.git
    cd sphinx-linkfix

Development Setup
=================

Environment Setup
-----------------

1. Create a conda environment (recommended):

.. code-block:: bash

    conda create -n sphinx-linkfix python=3.9
    conda activate sphinx-linkfix

2. Install the package in development mode:

.. code-block:: bash

    pip install -e .[dev,docs]

This will install:

- All runtime dependencies
- Development tools (pytest, ruff, pre-commit, etc.)
- Documentation tools (sphinx, sphinx-autoapi)

Pre-commit Hooks
----------------

Set up pre-commit hooks to ensure code quality:

.. code-block:: bash

    pre-commit install

This will automatically run code formatting and linting before each commit.

Development Workflow
====================

Creating a Feature Branch
--------------------------

1. Make sure you're on the dev branch and it's up to date:

.. code-block:: bash

    git checkout dev
    git pull

2. Create a new feature branch:

.. code-block:: bash

    git checkout -b feature/your-feature-name

Making Changes
--------------

1. Make your changes in the appropriate files
2. Add tests for new functionality
3. Update documentation if needed
4. Run the test suite to ensure everything works

Running During Development
--------------------------

When running code during development, use:

.. code-block:: bash

    PYTHONPATH='/path/to/sphinx-linkfix/src' python your_script.py

Branching Model and Workflow
============================

This project follows a structured Gitflow branching model to maintain code quality and enable collaborative development.

Branch Types
------------

**main**
~~~~~~~~
- The production-ready branch
- Contains stable, tested code
- Protected branch requiring pull request reviews
- Only accepts merges from ``dev`` or ``hotfix`` branches

**dev**
~~~~~~~
- The integration branch for ongoing development
- Contains the latest development features
- All feature and bugfix branches merge here first
- Regularly merged into ``main`` when stable

**feature/***
~~~~~~~~~~~~~
- Created for new features or enhancements
- Branched from ``dev``
- Naming convention: ``feature/feature-name`` or ``feature/issue-number-description``
- Merged back into ``dev`` via pull request

**release/***
~~~~~~~~~~~~~
- Created for preparing a new production release
- Branched from ``dev``
- Naming convention: ``release/version-number``
- Used for final testing and bug fixes before merging into ``main``

**bugfix/***
~~~~~~~~~~~~
- Created for non-urgent bug fixes
- Branched from ``dev``
- Naming convention: ``bugfix/bug-description`` or ``bugfix/issue-number-description``
- Merged back into ``dev`` via pull request

**hotfix/***
~~~~~~~~~~~~
- Created for urgent production fixes
- Branched from ``main``
- Naming convention: ``hotfix/critical-issue-description``
- Merged directly into ``main`` and then back-merged into ``dev``

**meta/***
~~~~~~~~~~~~
- Created for non-code changes (documentation, CI/CD, etc.)
- Branched from ``main``
- Naming convention: ``meta/change-description``
- Merged back into ``main`` via pull request

Merge Workflows
---------------

**Feature/Bugfix → Dev**
~~~~~~~~~~~~~~~~~~~~~~~~

1. Rebase ``dev`` into your feature/bugfix branch:

.. code-block:: bash

    git checkout feature/your-feature
    git fetch origin
    git rebase origin/dev

2. Create a pull request from ``feature/your-feature`` to ``dev``
3. Use **squash commit** or **squash and merge** to maintain clean commit history
4. Delete the feature branch after successful merge

**Dev → Release → Main**
~~~~~~~~~~~~~~~~~~~~~~~~

1. When ready for a release, create a release branch from ``dev``:

.. code-block:: bash

    git checkout dev
    git pull origin dev
    git checkout -b release/x.y.z
    git push origin release/x.y.z

2. Perform final testing and bug fixes on the release branch
3. Create a pull request from ``release/x.y.z`` to ``main``
4. Use **squash commit** for a clean release commit
5. After merge, CI pipeline will tag the release, publish packages, deploy documentation and merge ``main`` back into ``dev`` to keep branches synchronized

**Hotfix → Main**
~~~~~~~~~~~~~~~~~

1. Rebase ``main`` into your hotfix branch:

.. code-block:: bash

    git checkout hotfix/critical-fix
    git fetch origin
    git rebase origin/main

2. Create a pull request from ``hotfix/critical-fix`` to ``main``
3. Use **squash and merge** for clean hotfix commits
4. After merge, CI pipeline will tag the hotfix release, publish packages, deploy documentation and merge ``main`` back into ``dev`` to keep branches synchronized

**Meta → Main**
~~~~~~~~~~~~~~~

1. Rebase ``main`` into your meta branch:

.. code-block:: bash

    git checkout meta/your-meta-change
    git fetch origin
    git rebase origin/main

2. Create a pull request from ``meta/your-meta-change`` to ``main``
3. Use **squash and merge** for clean meta commits
4. After merge, CI pipeline will deploy documentation and merge ``main`` back into ``dev`` to keep branches synchronized

Branch Protection Rules
-----------------------

- **main**: Requires pull request reviews, status checks must pass
- **dev**: Requires pull request reviews, status checks must pass
- Direct pushes to ``main`` and ``dev`` are prohibited
- All branches must be up-to-date before merging

Workflow Examples
-----------------

**Creating a Feature**

.. code-block:: bash

    # Start from dev
    git checkout dev
    git pull origin dev

    # Create feature branch
    git checkout -b feature/user-authentication

    # Make changes and commit
    git add .
    git commit -m "feat: implement user authentication system"

    # Push and create PR
    git push origin feature/user-authentication

**Preparing for Merge**

.. code-block:: bash

    # Before creating PR, rebase on latest dev
    git fetch origin
    git rebase origin/dev

    # Resolve conflicts if any, then force push
    git push --force-with-lease origin feature/user-authentication

Code Standards
==============

This project follows modern Python development practices:

Code Modernization with Pyupgrade
----------------------------------

We use **pyupgrade** to automatically upgrade Python syntax to use modern features:

.. code-block:: bash

    # Upgrade Python syntax for Python 3.12+
    pyupgrade --py312-plus src/**/*.py

    # Upgrade specific files
    pyupgrade --py312-plus src/sphinx_linkfix/specific_module.py

    # Upgrade all Python files recursively
    find src -name "*.py" -exec pyupgrade --py312-plus {} +

Pyupgrade automatically modernizes code by:

- Converting old string formatting to f-strings
- Updating type annotations to use modern syntax
- Replacing outdated syntax with newer equivalents
- Removing unnecessary imports and comprehensions

Docstring Formatting
---------------------

We use **docformatter** to automatically format docstrings:

.. code-block:: bash

    # Format docstrings in place
    docformatter --in-place src/**/*.py

    # Check docstring formatting without making changes
    docformatter --check src/**/*.py

    # Format specific files
    docformatter --in-place src/sphinx_linkfix/specific_module.py

Docformatter ensures:

- Consistent docstring formatting
- Proper line wrapping at the configured length
- Standardized spacing and structure
- Removal of unnecessary blank lines in docstrings

Code Formatting and Linting
----------------------------

We use **Ruff** for both linting and formatting:

.. code-block:: bash

    # Format code
    ruff format .

    # Run linting
    ruff check .

    # Fix auto-fixable issues
    ruff check --fix .

Docstring Linting
-----------------

We use **pydoclint** to ensure docstring quality and consistency:

.. code-block:: bash

    # Check docstring compliance
    pydoclint src/

    # Check specific files
    pydoclint src/sphinx_linkfix/specific_module.py

Pydoclint helps ensure that:

- All public functions and classes have docstrings
- Docstrings follow the NumPy format consistently
- Function signatures match their docstring parameters
- Return values are properly documented

Type Checking
-------------

We use **Pyright** for static type checking:

.. code-block:: bash

    # Run type checking
    pyright

    # Check specific files
    pyright src/sphinx_linkfix/specific_module.py

Pyright is configured in ``pyrightconfig.json`` and helps catch type-related errors before runtime.

**Important**: You should link your conda environment path in ``pyrightconfig.local.json`` for proper type checking. Create this file if it doesn't exist:

.. code-block:: json

    {
        "venvPath": "/path/to/your/conda/envs",
        "venv": "sphinx-linkfix"
    }

Replace ``/path/to/your/conda/envs`` with your actual conda environments path (e.g., ``/home/username/miniconda3/envs`` or ``/home/username/micromamba/envs``).

Make sure your code passes type checking before submitting a pull request.

Pre-commit Hooks
----------------

We use **pre-commit** to automatically run all code quality checks before each commit:

.. code-block:: bash

    # Install pre-commit hooks (run once after cloning)
    pre-commit install

    # Run pre-commit on all files manually
    pre-commit run --all-files

    # Run pre-commit on staged files only
    pre-commit run

    # Update pre-commit hooks to latest versions
    pre-commit autoupdate

Pre-commit automatically runs the following tools on your code:

- **pyupgrade**: Modernizes Python syntax
- **docformatter**: Formats docstrings consistently
- **ruff**: Lints and formats code
- **pydoclint**: Checks docstring quality
- **pyright**: Performs type checking

**Configuration**: You can customize which tools run by editing ``.pre-commit-config.yaml``:

- **Comment out tools** to make pre-commit less restrictive (e.g., comment out pyright for faster commits)
- **Uncomment additional hooks** for more thorough checking
- **Adjust tool arguments** to match your preferences

**Note**: Even if you skip certain pre-commit checks locally, all tools will still be enforced in the CI/CD pipeline via GitHub Actions. This ensures code quality while allowing flexibility during development.

Code Style Guidelines
---------------------

- **Line length**: 100 characters maximum
- **Docstring style**: NumPy format
- **Import sorting**: Follow the black profile
- **Type hints**: Use type hints for function signatures
- **Variable naming**: Use descriptive names in snake_case

Example of well-formatted code:

.. code-block:: python

    from typing import Any, Dict, List, Optional

    import numpy as np
    import pandas as pd

    from sphinx_linkfix import fun

    def calculate_statistics(data: List[float]) -> Dict[str, float]:
        """Calculate basic statistics for a list of numbers.

        Parameters
        ----------
        data : List[float]
            List of numerical values.

        Returns
        -------
        Dict[str, float]
            Dictionary containing mean, median, and standard deviation.
        """
        if not data:
            return {"mean": 0.0, "median": 0.0, "std_dev": 0.0}

        mean = np.mean(data)
        median = np.median(data)
        std_dev = np.std(data)

        return {"mean": mean, "median": median, "std_dev": std_dev}

Testing
=======

We use **pytest** for testing. Tests are located in the ``tests/`` directory.

Running Tests
-------------

.. code-block:: bash

    # Run all tests
    pytest

    # Run tests with coverage
    pytest --cov=src

    # Run specific test file
    pytest tests/sphinx_linkfix/test_specific_module.py

    # Run tests matching a pattern
    pytest -k "test_pattern"

Writing Tests
-------------

- Place tests in the ``tests/`` directory, mirroring the ``src/`` structure
- Test file names should start with ``test_``
- Test function names should start with ``test_``
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases
- Mock external dependencies when appropriate

Example test:

.. code-block:: python

    import pytest
    import numpy as np

    from sphinx_linkfix import fun


    class TestFeature:
        """Test suite for new feature."""

        def test_feature_initialization(self):
            """Test that the feature initializes with correct default values."""
            assert fun()


Documentation
=============

We use **Sphinx** with **autoapi** for documentation generation.

Building Documentation
----------------------

.. code-block:: bash

    cd docs
    make html

The built documentation will be in ``docs/_build/html/``.

Writing Documentation
---------------------

- Use NumPy-style docstrings for all public functions and classes
- Update relevant ``.rst`` files in the ``docs/`` directory
- Include examples in docstrings when helpful
- Keep documentation up to date with code changes
- Documentation links should be relative and use the GitHub format (e.g., `Name <NAME.rst>`_)

Submitting Changes
==================

Pull Request Process
--------------------

1. Rebase your feature branch on the latest dev branch:

.. code-block:: bash

    # Fetch the latest changes from upstream
    git fetch origin

    # Rebase your feature branch on dev
    git rebase origin/dev

    # If there are conflicts, resolve them and continue
    git add .
    git rebase --continue

2. Ensure your code passes all tests and linting:

.. code-block:: bash

    # Run the full test suite
    pytest

    # Run all pre-commit hooks (formatting, linting, type checking, etc.)
    pre-commit run --all-files

3. Commit your changes with descriptive commit messages:

.. code-block:: bash

    git add .
    git commit -m "feat: add new feature

    - Implement new feature
    - Add comprehensive tests for edge cases
    - Update documentation with usage examples"

4. Push to your fork:

.. code-block:: bash

    git push origin feature/your-feature-name

5. Create a pull request to dev on GitHub with:

- Reference to any related issues
- Screenshots or examples if applicable
- Clear description of changes in the PR body in the following format [#format]_:

.. code-block:: bash

    - Added: New features or modules
    - Changed: Modifications to existing functionality
    - Fixed: Bug fixes

.. [#format] PR body format is important for automatic changelog generation.

Commit Message Format
---------------------

Use conventional commit format:

- ``feat:``: New features
- ``fix:``: Bug fixes
- ``docs:``: Documentation changes
- ``style:``: Code style changes (formatting, etc.)
- ``refactor:``: Code refactoring
- ``test:``: Adding or updating tests
- ``chore:``: Maintenance tasks

Project Structure
=================

Understanding the codebase structure will help you contribute effectively:

.. code-block::

    sphinx-linkfix/
    ├── src/                        # Source code
    │   ├── sphinx_linkfix/           # Main package
    │   └── other_package/          # Additional package
    ├── tests/                      # Test suite
    ├── docs/                       # Documentation
    └── pyproject.toml              # Project configuration

Getting Help
============

If you have questions or need help:

1. Check the documentation in ``docs/``
2. Look for similar issues in the GitHub issue tracker
3. Create a new issue using the appropriate template from the `Issue Reporting`_ section
4. Join discussions in existing issues or pull requests

For detailed guidance on reporting issues, please see the `Issue Reporting`_ section above.

Code of Conduct
===============

All contributors are expected to adhere to our `Code of Conduct <CODE_OF_CONDUCT.rst>`_.

Thank you for contributing to the sphinx-linkfix project! 🚀

Issue Reporting
===============

When reporting issues, please help us help you by providing detailed information. Use the appropriate template below based on your issue type.

Bug Reports
-----------

Use this template for any functional issues, including performance problems, crashes, unexpected behavior, or errors.

**Bug Report Template:**

.. code-block:: text

    ## Bug Description
    A clear and concise description of what the bug is.

    ## Environment
    - **OS**: [e.g., Ubuntu 22.04, Windows 11, macOS 13.0]
    - **Python Version**: [e.g., 3.9.y]
    - **Project Version**: [e.g., 1.0.0 or commit hash if using dev]
    - **Conda Environment**: [e.g., sphinx-linkfix]
    - **Hardware** (for performance issues): [CPU, RAM, relevant specs]

    ## Steps to Reproduce
    1. Go to '...'
    2. Click on '....'
    3. Run command '....'
    4. See error

    ## Expected Behavior
    A clear and concise description of what you expected to happen.

    ## Actual Behavior
    A clear and concise description of what actually happened.

    ## Error Messages/Stack Trace
    ```
    Paste the complete error message and stack trace here
    ```

    ## Code Sample
    Provide a minimal code example that reproduces the issue:

    ```python
    # Your code here
    ```

    ## Configuration Files
    If relevant, include relevant parts of your configuration files:

    ```json
    {
        "your": "config",
        "here": "..."
    }
    ```

    ## Performance Information (if applicable)
    For performance-related issues:
    - **Execution Time**: [e.g., 45 minutes]
    - **Memory Usage**: [e.g., 8GB RAM]
    - **Profiling Output**: [if available]

    ## Additional Context
    Add any other context about the problem here, such as:
    - Screenshots (if applicable)
    - Related issues or PRs
    - Workarounds you've tried
    - When the issue started occurring

Feature Requests
----------------

Use this template when proposing new functionality or enhancements.

**Feature Request Template:**

.. code-block:: text

    ## Feature Summary
    A clear and concise description of the feature you'd like to see.

    ## Problem Statement
    Describe the problem this feature would solve. What use case does it address?

    ## Proposed Solution
    Describe the solution you'd like to see implemented.

    ## Alternative Solutions
    Describe any alternative solutions or features you've considered.

    ## Use Cases
    Provide specific examples of how this feature would be used:

    1. **Use Case 1**: Description of first use case
    2. **Use Case 2**: Description of second use case

    ## Implementation Considerations
    If you have thoughts on implementation:

    - API design considerations
    - Performance implications
    - Backward compatibility concerns
    - Dependencies that might be needed

    ## Additional Context
    Add any other context, mockups, or examples about the feature request here.

Documentation Issues
--------------------

Use this template for reporting problems with documentation.

**Documentation Issue Template:**

.. code-block:: text

    ## Documentation Issue
    Describe what's wrong with the current documentation.

    ## Location
    - **File/Page**: [e.g., docs/simulation_guide.rst, README.rst]
    - **Section**: [specific section if applicable]
    - **URL**: [if reporting web documentation issue]

    ## Issue Type
    - [ ] Outdated information
    - [ ] Missing information
    - [ ] Unclear explanation
    - [ ] Broken links
    - [ ] Code examples don't work
    - [ ] Typos/grammar
    - [ ] Other: _______________

    ## Current Content
    Quote or describe the current problematic content.

    ## Suggested Improvement
    Describe how the documentation could be improved.

    ## Additional Context
    Any other relevant information.

Issue Labels
------------

To help us categorize and prioritize issues, please suggest appropriate labels:

**Type Labels:**

- ``bug``: Something isn't working (includes performance issues)
- ``enhancement``: New feature or request
- ``documentation``: Improvements or additions to documentation
- ``question``: Further information is requested (use GitHub Discussions for general questions)

**Priority Labels:**

- ``critical``: Blocking issue that affects core functionality
- ``high``: Important issue that should be addressed soon
- ``medium``: Standard priority
- ``low``: Nice to have, can be addressed when time permits

**Component Labels:**

- ``documentation``: Issues related to docs
- ``ci/cd``: Issues related to continuous integration/deployment
