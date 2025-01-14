# robotframework-jupyterlibrary

> A [Robot Framework][] library for automating (testing of) [Jupyter][] end-user
> applications and extensions

[robot framework]: http://robotframework.org
[jupyter]: https://jupyter.org

|          pip          |                 conda                 |          docs           |            demo             |             actions             |
| :-------------------: | :-----------------------------------: | :---------------------: | :-------------------------: | :-----------------------------: |
| [![pip-badge][]][pip] | [![conda-forge-badge][]][conda-forge] | [![docs-badge][]][docs] | [![binder-badge][]][binder] | [![workflow-badge][]][workflow] |

## Using

Write `.robot` files that use `JupyterLibrary` [keywords][]... or use [magics][]
in notebooks.

```robotframework
*** Settings ***
Library           JupyterLibrary
Suite Setup       Wait For New Jupyter Server To Be Ready
Test Teardown     Reset JupyterLab And Close
Suite Teardown    Terminate All Jupyter Servers

*** Test Cases ***
A Notebook in JupyterLab
    Open JupyterLab
    Launch A New JupyterLab Document
    Add And Run JupyterLab Code Cell
    Wait Until JupyterLab Kernel Is Idle
    Capture Page Screenshot
```

See the [acceptance tests][] for examples.

## Installation

```bash
pip install robotframework-jupyterlibrary
```

Or

```bash
conda install -c conda-forge robotframework-jupyterlibrary
```

Or see the [contributing guide][contributing] for a development install.

## Free Software

JupyterLibrary is Free Software under the [BSD-3-Clause License][license]. It
contains code from a number of other projects:

- [Jyve][] ([BSD-3-Clause][jyve-license])
  - Initial implementations of robot keywords

[license]:
  https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/blob/master/LICENSE
[acceptance tests]:
  https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/tree/master/atest
[miniforge]: https://github.com/conda-forge/miniforge/releases
[binder-badge]: https://mybinder.org/badge_logo.svg
[binder]:
  https://mybinder.org/v2/gh/robots-from-jupyter/robotframework-jupyterlibrary/master?urlpath=lab/tree/docs/MAGIC.ipynb
[workflow-badge]:
  https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/workflows/CI/badge.svg
[workflow]:
  https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/actions?query=workflow%3ACI+branch%3Amaster
[docs-badge]:
  https://readthedocs.org/projects/robotframework-jupyterlibrary/badge/?version=stable
[pip-badge]: https://img.shields.io/pypi/v/robotframework-jupyterlibrary.svg
[pip]: https://pypi.org/project/robotframework-jupyterlibrary
[conda-forge]:
  https://github.com/conda-forge/robotframework-jupyterlibrary-feedstock#installing-robotframework-jupyterlibrary
[conda-forge-badge]:
  https://img.shields.io/conda/vn/conda-forge/robotframework-jupyterlibrary.svg
[docs]: https://robotframework-jupyterlibrary.readthedocs.io
[jyve]: https://github.com/deathbeds/jyve
[jyve-license]: https://github.com/deathbeds/jyve/blob/master/LICENSE
[magics]:
  https://robotframework-jupyterlibrary.readthedocs.io/en/stable/MAGIC.html
[keywords]:
  https://robotframework-jupyterlibrary.readthedocs.io/en/stable/KEYWORDS.html
[contributing]:
  https://github.com/robots-from-jupyter/robotframework-jupyterlibrary/blob/master/CONTRIBUTING.md
