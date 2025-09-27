Contributing
============

Thank you for your interest in contributing to the WTF Transcript Converter! This document provides guidelines and information for contributors.

Code of Conduct
---------------

This project follows the `Contributor Covenant Code of Conduct <https://www.contributor-covenant.org/version/2/1/code_of_conduct.html>`_. By participating, you are expected to uphold this code.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

* Python 3.10+ (3.12 recommended)
* `uv <https://github.com/astral-sh/uv>`_ package manager
* Git

Fork and Clone
~~~~~~~~~~~~~~

1. Fork the repository on GitHub
2. Clone your fork locally:

.. code-block:: bash

   git clone https://github.com/your-username/wtf-transcript-converter.git
   cd wtf-transcript-converter

Development Setup
-----------------

Quick Setup
~~~~~~~~~~~

.. code-block:: bash

   # Install development dependencies
   make setup-dev
   
   # Or manually:
   uv sync --dev
   uv run pre-commit install

Verify Installation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run tests to verify everything works
   make test
   
   # Run cross-provider tests
   make cross-provider-all

Contributing Guidelines
-----------------------

Types of Contributions
~~~~~~~~~~~~~~~~~~~~~~

We welcome several types of contributions:

1. **Bug Fixes**: Fix issues in existing code
2. **New Features**: Add new functionality
3. **Provider Integrations**: Add support for new transcription providers
4. **Documentation**: Improve documentation and examples
5. **Testing**: Add or improve tests
6. **Performance**: Optimize existing code

Development Workflow
~~~~~~~~~~~~~~~~~~~~

1. **Create a branch**:

.. code-block:: bash

   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number

2. **Make your changes**:
   * Write code following our style guidelines
   * Add tests for new functionality
   * Update documentation as needed

3. **Test your changes**:

.. code-block:: bash

   make check          # Run linting, type checking, security
   make test-all       # Run all tests
   make cross-provider-all  # Run cross-provider tests

4. **Commit your changes**:

.. code-block:: bash

   git add .
   git commit -m "feat: add new provider integration"

5. **Push and create PR**:

.. code-block:: bash

   git push origin feature/your-feature-name

Provider Integration
--------------------

Adding a New Provider
~~~~~~~~~~~~~~~~~~~~~

To add support for a new transcription provider:

1. **Create the converter**:

.. code-block:: bash

   # Create new provider file
   touch src/wtf_transcript_converter/providers/new_provider.py

2. **Implement the converter**:

.. code-block:: python

   from wtf_transcript_converter.providers.base import BaseProviderConverter
   from wtf_transcript_converter.core.models import WTFDocument
   
   class NewProviderConverter(BaseProviderConverter):
       provider_name: str = "new_provider"
       description: str = "New Provider Description"
       status: str = "Implemented"
       
       def __init__(self, provider_name: str = "new_provider"):
           super().__init__(provider_name)
       
       def convert_to_wtf(self, data: Dict[str, Any]) -> WTFDocument:
           # Implementation here
           pass
       
       def convert_from_wtf(self, wtf_doc: WTFDocument) -> Dict[str, Any]:
           # Implementation here
           pass

3. **Add to providers module**:

.. code-block:: python

   # Update src/wtf_transcript_converter/providers/__init__.py
   from .new_provider import NewProviderConverter
   
   __all__ = [
       # ... existing providers
       "NewProviderConverter",
   ]

4. **Update CLI**:

.. code-block:: python

   # Update src/wtf_transcript_converter/cli/main.py
   from ..providers.new_provider import NewProviderConverter
   
   def _get_converter(provider: str):
       # ... existing providers
       elif provider == "new-provider":
           return NewProviderConverter()

5. **Add tests**:

.. code-block:: bash

   # Create test file
   touch tests/test_providers/test_new_provider.py

6. **Update documentation**:
   * Update README.md with new provider
   * Add usage examples
   * Update provider list in CLI

Provider Testing Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each provider must have:

* [ ] Unit tests for `convert_to_wtf()`
* [ ] Unit tests for `convert_from_wtf()`
* [ ] Integration tests (if API available)
* [ ] Cross-provider consistency tests
* [ ] Error handling tests
* [ ] Sample data fixtures

Testing
-------

Test Structure
~~~~~~~~~~~~~~

.. code-block::

   tests/
   ├── test_providers/          # Provider-specific tests
   ├── test_cross_provider/     # Cross-provider testing
   ├── test_integration/        # Integration tests
   ├── test_cli/               # CLI tests
   ├── fixtures/               # Test data
   └── conftest.py            # Test configuration

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   make test-all
   
   # Run specific test categories
   make test                    # Unit tests
   make test-integration        # Integration tests
   make test-cross-provider     # Cross-provider tests
   
   # Run with coverage
   make test-cov
   
   # Run specific test file
   uv run pytest tests/test_providers/test_whisper.py -v

Writing Tests
~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from wtf_transcript_converter.providers.whisper import WhisperConverter
   
   class TestWhisperConverter:
       def test_convert_to_wtf(self, sample_whisper_data):
           converter = WhisperConverter()
           wtf_doc = converter.convert_to_wtf(sample_whisper_data)
           
           assert wtf_doc.transcript.text == "expected text"
           assert wtf_doc.transcript.language == "en"
           assert len(wtf_doc.segments) > 0

Code Style
----------

Python Style
~~~~~~~~~~~~

We use several tools to maintain code quality:

* **Black**: Code formatting
* **isort**: Import sorting
* **flake8**: Linting
* **mypy**: Type checking
* **bandit**: Security scanning

Running Style Checks
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run all style checks
   make check
   
   # Individual checks
   make lint          # flake8, black, isort
   make type-check    # mypy
   make security      # bandit, safety

Pre-commit Hooks
~~~~~~~~~~~~~~~~

Pre-commit hooks run automatically on commit:

.. code-block:: bash

   # Install hooks
   make pre-commit-install
   
   # Run manually
   make pre-commit

Code Style Guidelines
~~~~~~~~~~~~~~~~~~~~~

1. **Line length**: 99 characters
2. **Import order**: isort with black profile
3. **Type hints**: Required for all public functions
4. **Docstrings**: Google style for all public functions
5. **Error handling**: Use specific exceptions, not bare `except:`

Pull Request Process
--------------------

Before Submitting
~~~~~~~~~~~~~~~~~

1. **Ensure tests pass**:

.. code-block:: bash

   make test-all
   make check

2. **Update documentation** if needed

3. **Add changelog entry** if applicable

PR Requirements
~~~~~~~~~~~~~~~

* [ ] All tests pass
* [ ] Code follows style guidelines
* [ ] Documentation updated
* [ ] No security issues
* [ ] Cross-provider tests pass (for provider changes)

PR Template
~~~~~~~~~~~

Use the provided PR template and fill out all relevant sections.

Release Process
---------------

Version Bumping
~~~~~~~~~~~~~~~

We use semantic versioning (MAJOR.MINOR.PATCH):

* **MAJOR**: Breaking changes
* **MINOR**: New features, backward compatible
* **PATCH**: Bug fixes, backward compatible

Release Checklist
~~~~~~~~~~~~~~~~~

* [ ] All tests pass
* [ ] Documentation updated
* [ ] Changelog updated
* [ ] Version bumped in `pyproject.toml`
* [ ] Release notes prepared

Creating a Release
~~~~~~~~~~~~~~~~~~

1. **Update version** in `pyproject.toml`
2. **Update changelog**
3. **Create release** on GitHub
4. **CI/CD** will automatically publish to PyPI

Documentation
-------------

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   docs/
   ├── index.rst              # Main documentation page
   ├── installation.rst       # Installation guide
   ├── quickstart.rst         # Quick start guide
   ├── user_guide.rst         # Comprehensive user guide
   ├── api_reference.rst      # API documentation
   ├── providers.rst          # Provider documentation
   ├── cross_provider_testing.rst  # Cross-provider testing
   ├── examples.rst           # Examples and use cases
   ├── contributing.rst       # Contributing guide
   └── changelog.rst          # Changelog

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build documentation
   make docs
   
   # Or manually
   cd docs
   make html

Documentation Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Use reStructuredText** for documentation
2. **Include code examples** for all features
3. **Update API docs** when code changes
4. **Test all examples** before committing
5. **Use consistent formatting**

Getting Help
------------

If you encounter issues during development:

1. Check the `GitHub Issues <https://github.com/vcon-dev/wtf-transcript-converter/issues>`_
2. Review the `troubleshooting section <troubleshooting.html>`_
3. Join our `Discord community <https://discord.gg/vcon>`_
4. Contact the development team at `vcon@ietf.org <mailto:vcon@ietf.org>`_

Recognition
-----------

Contributors will be recognized in:

* CONTRIBUTORS.md file
* Release notes
* Project documentation

Thank you for contributing to WTF Transcript Converter! 🎉
