(contributing)=
# Contributing to HVL CCB

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given. You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at [Repository issues](https://gitlab.com/ethz_hvl/hvl_ccb/issues).

If you are reporting a bug, please include:

* Your operating system name, Python version, and HVL CCB version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the [GitLab issues](https://gitlab.com/ethz_hvl/hvl_ccb/issues) for bugs. Anything tagged with "Bug" is open to whoever wants to fix it.

### Implement New Device

Look through the [GitLab issues](https://gitlab.com/ethz_hvl/hvl_ccb/issues): anything tagged with "New device" is open to whoever wants to implement it.

### Write Documentation

HVL CCB always welcomes more documentation, whether as part of the official HVL CCB docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at [GitLab  issues](https://gitlab.com/ethz_hvl/hvl_ccb/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started for Contribution to HVL CCB

Ready to contribute? Here's how to set up `hvl_ccb` for local development.

1. Clone `hvl_ccb` repo from GitLab:

    ```console
    git clone https://gitlab.com/ethz_hvl/hvl_ccb.git
    ```

    Go into the cloned folder (`cd` or `dir` in Terminal). It is recommended to use Git Bash or Unix-based terminal and Visual Studio Code for development.

1. We recommend using [uv](https://docs.astral.sh/uv/) for creating the virtual environment and managing dependencies. The tool `uv` is used to manage project dependencies and virtual environments. First we need to install `uv`:

   Follow the installation instructions on [uv website - Installation](https://docs.astral.sh/uv/#installation).
  
   You need to re-start Visual Studio Code or any IDE after installation and type `uv` in terminal to check if the installation is successful.

1. Then create the virtual environment with all dependencies using the following command with Python version 3.xx (xx is the version number, 3.13 for example, check the `hvl_ccb` support Python versions):

    ```console
    uv sync --all-extras --python=3.xx
    ```

    This command creates a virtual environment with a default name `.venv` and install the HVL CCB with its dependencies as well as the dependencies for development (`--all-extras`).

    The command above install `hvl_ccb` in editable mode, meaning any changes made to the source code will immediately take effect without needing to reinstall the package. This is useful for development.

    If you want to learn more: check [uv website - Python environments](https://docs.astral.sh/uv/pip/environments/) and [uv website - Syncing the environment](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-the-environment) for more details.

1. It is recommended to install the Git hook script shipped within the repository. These pre-commit hook perform basic code review automatically the committed code:

    ```console
    pre-commit install
    ```

1. Creating an [Issue](https://gitlab.com/ethz_hvl/hvl_ccb/-/issues) and discuss with maintainer(s) if the issue is needed to be addressed. If so, then create a [Merge Request](https://gitlab.com/ethz_hvl/hvl_ccb/-/merge_requests) on GitLab (by pressing "Create merge request" in the issue page), you can switch to the development branch you created:

    ```console
    git fetch
    git switch xxx-branch-name-of-your-bugfix-or-feature
    ```

    For example: `git switch 374-drop-support-for-python-3-9`, you can type the number and tab, the branch name should be auto-completed (in Git Bash for example, if the branch exists). If the new branch does not show up, you might need to do `git pull` again to retrieve update information.

    Now you can make your changes locally by first activating the virtual environment (Linux-based command):

    ```console
    . .venv/Scripts/activate
    ```

    You should see parenthesis of the virtual environment in the terminal, e.g. (hvl_ccb) or (.venv).

1. When you're done making changes, we have to make sure that the changes fulfill the style, typing, and sorting requirements, see . To do this, we recommend to use [ruff](https://docs.astral.sh/ruff/) (previously: flake8, black, and isort), which should already be installed from the previous step. The [guideline on the coding style of HVL CCB](#coding-style) can be found below in this document. To use `ruff` for checking:

    ```console
    ruff check --fix src/ tests/ examples/ docs/ # Lint all files 
    ```

    ```console
    ruff format src/ tests/ examples/ docs/ # Format all files 
    ```

    Then, `mypy` is used for type checking

    ```console
    mypy --show-error-codes src/hvl_ccb
    ```

    The tests, including testing other Python versions with tox:

    ```console
    py.test
    tox
    ```
  
    You can also use the provided make-like shell script to run ruff and tests:

    ```console
    ./make.sh ruff
    ./make.sh type
    ./make.sh test
    ```

1. As we want to maintain a high quality of coding style we use `mypy` and `ruff`. This style is checked with the [pipelines on GitLab](https://gitlab.com/ethz_hvl/hvl_ccb/-/pipelines). Ensure that your commits include only properly formatted code. One way to comply is to install and use `pre-commit`. This package includes the necessary configuration.

1. Commit your changes and push them to GitLab, for committing all changes:
  
    ```console
    git add .
    ```

    Or committing only a file:

    ```console
    git add path_to_file/file_name
    ```

    Add commit message: make sure that the commit message is clear and readable, not just "bug fix" or something ambiguous, then push the commit.

    ```console
    git commit -m "Your detailed description of your changes."
    git push
    ```

1. Request a review of your merge request through the [GitLab website](https://gitlab.com/ethz_hvl/hvl_ccb/-/merge_requests). One of the maintainers should review the change and approve before it can be merged.

Before you request a review from a maintainer(s), check that it meets these guidelines:

1. The merge request should include [tests](#test-guidelines).
1. If the merge request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in `README.md`.
1. The merge request should work for all supporting Python versions. Check [Merge Request](https://gitlab.com/ethz_hvl/hvl_ccb/merge_requests) and make sure that the tests pass for all supported Python versions ([Pipeline](https://gitlab.com/ethz_hvl/hvl_ccb/-/pipelines) should pass).

### Test Guidelines

To ensure code quality, we need to run tests that execute every newly written line, making sure that the test coverage is (close to) 100%. Tests should verify correctness, edge cases, and expected failure modes to guarantee robustness and maintainability of the code.

We use [pytest](https://docs.pytest.org/en/stable/) for testing and generating coverage report. Test file for a newly implemented device should be named `test_dev_{device_name}` in directory `tests/`. Examples of tests can be found in the directory. To run tests for the new file:

  ```console
  py.test tests/test_dev_{device_name}.py
  ```

To generate coverage report (in terminal), so that you know which line is missing in the test:

  ```console
  coverage report -m
  ```

  or in an HTML file

  ```console
  coverage html
  ```

The coverage should be (close to) 100% for the newly added file, meaning that every line should be executed. This can be checked from the coverage report.

### Tips

Here are some tips to help with contributing:

* To run tests from a single file:

    ```console
    py.test tests/test_hvl_ccb.py
    ```
  
  or a single test function:

    ```console
    py.test tests/test_hvl_ccb.py::test_command_line_interface
    ```

* If your tests are slow, profile them using the pytest-profiling plugin:

    ```console
    py.test tests/test_hvl_ccb.py --profile
    ```

  or for a graphical overview (you need a SVG image viewer):

    ```console
    py.test tests/test_hvl_ccb.py --profile-svg
    open prof/combined.svg
    ```

* To add dependency for development

    ```console
    uv add --dev dependency_name
    ```

* To generate a PDF version of the Sphinx documentation instead of HTML use:

    ```console
      rm -rf docs/hvl_ccb.rst docs/modules.rst docs/_build && sphinx-apidoc -o docs/hvl_ccb && python -msphinx -M latexpdf docs/ docs/_build
    ```

  This command can also be run through the make-like shell script:

    ```console
    ./make.sh docs-pdf
    ```

  This requires a local installation of a LaTeX distribution, e.g. MikTeX.

## Deploying and Release New Version (For Maintainer)

This section is a reminder for the maintainers on how to deploy and release a new version. Typically a [Milestone](https://gitlab.com/ethz_hvl/hvl_ccb/-/milestones) is created for tracking the issues and merge requests.

Make sure all your changes are committed and that all relevant merge requests within the milestone are merged. Then switch to `devel`, update it (git pull), and create `release-N.M.K` branch:

  ```console
  git switch devel
  git pull
  git switch -c release-N.M.K
  ```

* Update copyright (year) information (if necessary) in `docs/conf.py` and `README.md`
* Update or create entry in `HISTORY.md` (commit message: Update HISTORY.md: release N.M.K).
* Update, if applicable, `AUTHORS.md` (commit message: Update AUTHORS.md: release N.M.K)
* Update features tables in `README.md` file (commit message: Update README.md: release N.M.K)
* Update API docs (commit message: Update API-docs: release N.M.K):

  ```console
  ./make.sh docs  # Windows
  make docs  # Unix-based
  ```

Commit all of the above, except for

* `docs/hvl_ccb.dev.picotech_pt104.rst`.

Before you continue revert the changes in this file.

Then run to bump the version to the new one:

  ```console
  bumpver update --patch # possible: major / minor / patch
  git push --set-upstream origin release-N.M.K
  git push --tags
  ```

Go to [readthedocs](https://readthedocs.org/projects/hvl-ccb/builds/) and check if docs build for the pushed tag passed.

Wait for the CI pipeline to finish successfully.

The two following commands are best executed in a WSL or Unix based OS. Run a release check:

  ```console
  make release-check
  ```

Finally, prepare and push a release:

  ```console
  make release
  ```

Merge the release branch into master and `devel` branches with `--no-ff` flag and delete the release branch:

  ```console
  git switch master
  git pull
  git merge --no-ff release-N.M.K
  git push
  git switch devel
  git merge --no-ff release-N.M.K
  git push
  git push --delete origin release-N.M.K
  git branch --delete release-N.M.K
  ```

After this you can/should clean your folder (with WSL/Unix command):

  ```console
  make clean
  ```

Finally, prepare GitLab release and cleanup the corresponding milestone:

1. [Tags](https://gitlab.com/ethz_hvl/hvl_ccb/-/tags/)
   * Go to [Tags](https://gitlab.com/ethz_hvl/hvl_ccb/-/tags/), select the latest release tag
   * Press "Edit release notes" and add the release notes (copy a corresponding entry from `HISTORY.md` file)
   * Press "Save changes"

1. [Releases](https://gitlab.com/ethz_hvl/hvl_ccb/-/releases)
   * Go to [Releases](https://gitlab.com/ethz_hvl/hvl_ccb/-/releases), select the latest release
   * Press "Edit this release" and under "Milestones" select the corresponding milestone
   * Press "Save changes"

1. [Milestones](https://gitlab.com/ethz_hvl/hvl_ccb/-/milestones)
   * Go to [Milestones](https://gitlab.com/ethz_hvl/hvl_ccb/-/milestones), make sure that it is 100% complete (otherwise, create a next patch-level milestone and assign it to the ongoing Issues and Merge Requests therein)
   * Press "Close Milestone"

## Coding Style

We follow primarily [PEP 8 (Python Enhancement Proposal 8)](https://peps.python.org/pep-0008/), the official style guide for Python code. The purpose is that the code should be clean and maintainable. Some frequently used guidelines for HVL CCB are outlined here:

### Naming Conventions

* Use descriptive names: Choose meaningful names for variables, functions, classes, and modules to clearly convey their purpose. For example: `serial_number` is better than `s_num`.
* Variables and functions: Use `snake_case` (lowercase with underscores) for variable and function names. For example: `serial_number` not `SerialNumber`.
* Classes: Use `CamelCase` for class names. For example: `MeasurementFunction`.
* Constants: Use `UPPER_SNAKE_CASE` for constants. For example: `N_CHANNELS = 2`.

### Code Comments

* Write clear, concise comments to explain more "why" something is done, not "what".
* Use docstrings for functions, classes, and modules to describe their purpose.

### PEP 20 - The Zen of Python

* Explicit is Better Than Implicit: Write code that is clear and unambiguous. Avoid relying on implicit behavior that might confuse users.
* Simple is better than complex: We don't need fancy one-liners but we want readability.
* Please find more details about [PEP 20](https://peps.python.org/pep-0020/). Or try `import this`.

### Others

* Use 4 spaces per indentation level (instead of tabs).
* Maximum line length: 88 characters for better readability
* Error handling is important to make code robust and clear.
* Use type hints [PEP 484](https://peps.python.org/pep-0484/)
* When in doubt, check the existing code, or ask maintainer(s)
