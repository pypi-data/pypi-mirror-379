# Contributing

Welcome to `cts-chamber` contributor\'s guide.

This document focuses on getting any potential contributor familiarized
with the development processes, but [other kinds of
contributions](https://opensource.guide/how-to-contribute) are also
appreciated.

If you are new to using [git](https://git-scm.com) or have never
collaborated in a project previously, please have a look at
[contribution-guide.org](https://www.contribution-guide.org/). Other
resources are also listed in the excellent [guide created by
FreeCodeCamp](https://github.com/FreeCodeCamp/how-to-contribute-to-open-source)[^1].

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt, [Python
Software Foundation\'s Code of
Conduct](https://www.python.org/psf/conduct/) is a good reference in
terms of behavior guidelines.

## Issue Reports

If you experience bugs or general issues with `cts-chamber`,
please have a look on the
[issue tracker](https://gitlab.desy.de/leandro.lanzieri/cts-chamber/-/issues).
If you don\'t see anything useful there, please feel free to fire an
issue report or write email (check pypi.org or sources for the address).

Please don\'t forget to include the closed issues in your search.
Sometimes a solution was already reported, and the problem is considered
**solved**.

New issue reports should include information about your programming
environment (e.g., operating system, Python version) and steps to
reproduce the problem. Please try also to simplify the reproduction
steps to a very minimal example that still illustrates the problem you
are facing. By removing other factors, you help us to identify the root
cause of the issue.

You will need an account for this. Check
[this section](#getting-an-account-on-this-gitlab-instance).

## Documentation Improvements

You can help improve `cts-chamber` docs by making them more
readable and coherent, or by adding missing information and correcting
mistakes.

`cts-chamber` documentation uses
[Sphinx](https://www.sphinx-doc.org/en/master/) as its main
documentation compiler. This means that the docs are kept in the same
repository as the project code, and that any documentation update is
done in the same way was a code contribution.

We are using [CommonMark](https://commonmark.org/) format.

When working on documentation changes in your local machine, you can
compile them using `uv`:

    $ uv run poe docs


and use Python\'s built-in web server for a preview in your web browser
(`http://localhost:8000`):


    $ python3 -m http.server --directory 'docs/_build/html'


## Code Contributions

### Submit an issue

Before you work on any non-trivial code contribution it\'s best to first
create a report in the [issue
tracker](https://gitlab.desy.de/leandro.lanzieri/cts-chamber/-/issues)
to start a discussion on the subject. This often provides additional
considerations and avoids unnecessary work.

You will need an account for this. Check
[this section](#getting-an-account-on-this-gitlab-instance).

### Create an environment

Before you start coding, we recommend creating an isolated [virtual
environment](https://realpython.com/python-virtual-environments-a-primer/)
to avoid any problems with your installed Python packages. This project
uses [uv](https://docs.astral.sh/uv/) for dependency management, which
will automatically create and manage a virtual environment for you.

### Clone the repository

1.  Clone this copy to your local disk:

        $ git clone git@gitlab.desy.de:leandro.lanzieri/cts-chamber.git
        $ cd cts-chamber

2.  Install the project and its dependencies using `uv`:

        $ uv sync --all-extras

    This will create a virtual environment, install all dependencies
    (including development dependencies), and make the package available
    for import in editable mode.

3.  Install `pre-commit`:

        $ uv run pre-commit install

    `cts-chamber` comes with a lot of hooks configured to
    automatically help the developer to check the code being written.

### Implement your changes

1.  Create a branch to hold your changes:

        $ git checkout -b my-feature

    and start making changes. Never work on the main branch!

2.  Start your work on this branch. Don\'t forget to add
    [docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
    to new functions, modules and classes, especially if they are part
    of public APIs.

    The project configuration is centralized in `pyproject.toml`, which
    contains all the metadata, dependencies, and tool configurations.

3.  Add yourself to the list of contributors in `AUTHORS.md`.

4.  When you're done editing, record your changes in [git](https://git-scm.com) by running:

        $ git add <MODIFIED FILES>
        $ git commit

    Please make sure to see the validation messages from `pre-commit`
    and fix any eventual issues. This should automatically use
    [ruff](https://docs.astral.sh/ruff/) to check/fix the code style
    in a way that is compatible with the project.

    **Important**: Don\'t forget to add unit tests and documentation in case your
    contribution adds an additional feature and is not just a bugfix.

    Moreover, writing a [descriptive commit
    message](https://chris.beams.io/posts/git-commit) is highly
    recommended. In case of doubt, you can check the commit history
    with:

        $ git log --graph --decorate --pretty=oneline --abbrev-commit --all

    to look for recurring communication patterns.


5.  Please check that your changes don\'t break any unit tests with:

        $ uv run poe test

    You can also run other development tasks using the available poe commands:

    - `uv run poe test` - Run unit tests with coverage
    - `uv run poe test_hil` - Run hardware-in-the-loop tests
    - `uv run poe docs` - Build documentation
    - `uv run poe pre_commit` - Run pre-commit hooks on all files

### Submit your contribution

1.  If everything works fine, push your local branch to GitLab with:

        $ git push -u origin my-feature


2.  Go to the web page of your fork and click \"Create merge request\" to
    send your changes for review.

You will need an account for this. Check
[this section](#getting-an-account-on-this-gitlab-instance).

### Troubleshooting

The following tips can be used when facing problems to build or test the
package:

1.  Sometimes `uv` might have issues with cached dependencies. If you find
    any problems with missing dependencies or version conflicts, try to
    recreate the virtual environment:

        uv sync --reinstall

    This will reinstall all dependencies from scratch.

2.  Make sure to have a reliable `uv` installation. When in doubt you can run:

        uv --version

    If you have trouble with `uv`, you can try installing it fresh:

        curl -LsSf https://astral.sh/uv/install.sh | sh

3.  [Pytest can drop
    you](https://docs.pytest.org/en/stable/how-to/failures.html#using-python-library-pdb-with-pytest)
    in an interactive session in the case an error occurs. In order to
    do that you need to pass a `--pdb` option (for example by running
    `uv run pytest -k <NAME OF THE FALLING TEST> --pdb`). You can also setup
    breakpoints manually instead of using the `--pdb` option.


[^1]: Even though, these resources focus on open source projects and
    communities, the general ideas behind collaborating with other
    developers to collectively create software are general and can be
    applied to all sorts of environments, including private companies
    and proprietary code bases.

## Getting an Account on this GitLab Instance

To file issues and merge requests you'll need an account with `https://gitlab.desy.de`.
If you happen to have a DESY account you can directly sign in.
In case you don't have a DESY account, browse to the
[sign in page](https://gitlab.desy.de/users/sign_in), and click on `Helmholtz AAI`.
There, you can choose different identity providers, including Google and GitHub.
