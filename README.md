# ![mdf-logo](doc/img/mdf-logo100x100.gif)  EDA Development

---

## Goal

This project is a collection of open source tools used for Exploratory Data Analysis (EDA).

## Setup

`tox` is the preferred virtual environment management tool when not behind a proxy.  When working 
behind a `proxy` it may be more convenient to use Anaconda to setup the virtual environments.

### Run the `tox.ini`

This is the fastest way to get setup.  Steps to follow:

1. Install `tox`
2. from a terminal window, go to the directory that contains the `tox.ini` file
3. run     : `$ tox > doc/eda_dev/tox-eda_dev.md`  # capture results ana analyze for failures/errors
4. activate: `$ source .tox/eda_dev{38,39}/bin/activate`
5. confirm: `(eda_dev{38,39})$ `

### Download the Project Code

Use `clone -- recursive` to get the submodule code.
```shell
$ git clone --recurse-submodules https://github.com/c-w-m/eda_dev.git  ## https or
$ git clone --recurse-submodules git@github.com:c-w-m/eda_dev.git      ## ssh
```

---

## Directory Layout

| Directory      | Description               |
|----------------|---------------------------|
| 3p/*           | 3rd party projects        |
| doc/*          | links and notes           |
| ipynb/*        | sandbox/demo notebooks    |
| src/*          | submodules                |
| src/demo       | sandbox/demo code         |
|----------------|---------------------------|

### Third Party Projects

These are in `3p/`

| Directory  | Description            |
|------------|------------------------|
| matplotlib | plotting               |
| pandas     | data analysis          |
|------------|------------------------|

### Forked Projects

These are in `src/`

| Directory  | Description            |
|------------|------------------------|
| demo       | see next section       |
| pyGeometry | geometry               |
| Spirograph | Turtle drawing         |
|------------|------------------------|

### Demo

Example projects that demonstrate visualization code snippets.

These are in `src/demo/`

| Directory      | URL                          |
|----------------|------------------------------|
| altair-examples | https://github.com/madewitt/altair-examples.git |
| Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project | https://github.com/micgonzalez/Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project |
| data_viz_python_tutorial | https://github.com/micgonzalez/Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project.git |
| EDA-with-Seaborn | https://github.com/Devesh1997Yadav/EDA-with-Seaborn.git |
| file_IO | |
| handy_data_viz_functions | https://github.com/manukalia/handy_data_viz_functions.git |
| matplotlib-challenge | https://github.com/malvika/matplotlib-challenge.git |
| python-data-exploration | https://github.com/MartinSeeler/python-data-exploration.git |
| Seaborn-Basics | https://github.com/ashish-mehta-mlp/Seaborn-Basics.git |
| Understanding-Seaborn | https://github.com/kb22/Understanding-Seaborn.git |
|----------------|------------------------------|

## Submodules

The following projects were added under the `src/` directory.

### 3p/

```shell
cd src
git submodule add https://github.com/matplotlib/matplotlib.git
git submodule add https://github.com/pandas-dev/pandas.git
```

### src/

```shell
cd src
git submodule add https://github.com/c-w-m/pbpython.git
git submodule add https://github.com/c-w-m/pyGeometry.git
git submodule add https://github.com/c-w-m/Spirograph.git
git submodule add https://flxsa@bitbucket.org/flxsa/tpq_dev.git
```

### Recursive Update Submodules

```shell
$ cd src
/src$ git submodule update --init --recursive
/src$ git submodule foreach --recursive git fetch
/src$ git submodule foreach git merge origin master
```

### Removing Submodules

```shell
$ git submodule deinit -f src/yloader
$ rm -rf .git/modules/src/yloader
$ git rm -f src/yloader
```

```shell
git submodule deinit -f demo/tpq_dev
rm -rf .git/modules/demo/tpq_dev
git rm -f demo/tpq_dev
```

Here is a more verbose example.

```shell
# Remove the submodule entry from .git/config
git submodule deinit -f src/<submodule_name>

# Remove the submodule directory from the super-project's .git/modules 
directory
rm -rf .git/modules/src/<submodule_name>     #nix
rd /s /q '.git\modules\src\<submodule_name>' #win

# Remove the entry in .gitmodules and remove the submodule directory located at path/to/submodule
git rm -f src/<submodule_name>

# optional last two steps
git rm -r --cached src/<submodule_name>
git commit -m "removing <submodule_name>"
```

---

## Feature Branches

### `lint`

Get the code to pass  `pylint` from PyCharm IDE and `tox -e check`.

```shell
(ibaio_dev36) $ git fetch && git checkout dev/lint

Branch 'dev/lint' set up to track remote branch 'dev/lint' from 'origin'.
Switched to a new branch 'dev/lint'
(ibaio_dev36) $ 
```

---

## PIP Installations

### Install

```shell
(ibaio_dev{38,39})$ pip install <package-name>
```

### Uninstall

```shell
(ibaio_dev{38,39})$ pip uninstall <package-name>
```

---

## Develop Installations

### Install

```shell
<package-dir>(ibaio_dev{38,39})$ python setup.py develop
```

### Uninstall

```shell
<package-dir>(ibaio_dev{38,39})$ python setup.py develop --uninstall
```

or, in case the install was not using develop

```shell
python setup.py install --record files.txt
# followed by
xargs rm -rf < files.txt
```

you'll need to delete the directories in the project as well

develop creates an .egg-link file in the site-packages directory, which points back to the
location of the project files. The same path is also added to the easy-install.pth file in
the same location. Uninstalling with setup.py develop -u removes that link file again.

Do note that any install_requires dependencies not yet present are also installed, as
regular eggs (they are easy_install-ed). Those dependencies are not uninstalled when
uninstalling the development egg.

---
## Jupyter Notebooks

Remember to use `ipykernel` to expose your python environment in Jupyterlab.

```shell
$ conda activate eda_dev39
(ibaio_dev{38,39})$ python -m ipykernel install --user --name=ibaio_dev{38,39}
(ibaio_dev{38,39})$ jupyter lab
```

#### List All Kernels

```shell
$ jupyter kernelspec list
```

#### Remove a Kernel

```shell
$ jupyter kernelspec uninstall <kernel_name>
```

---
## Anaconda Environment

### Using Conda

Using the channel conda-forge and the [requirements.ubnt1604.txt](requirements.ubnt1604.txt) or [requirements.win10.txt](requirements.win10.txt) list of packages:

```shell
# activate conda base
$ conda activate base
(base)$ conda create -y --name eda_dev39 python={38,39}
(base)$ conda install --force-reinstall -y -q --name eda_dev39 -c anaconda -c conda-forge -c defaults --file requirements.txt
(base)$ conda activate eda_dev{38,39}
(eda_dev{38,39})$ conda install <any missing packages>
...
(eda_dev39)$ deactivate
(base)$
```

Additional commands can be found in the [cheet-sheets.pdf](doc/conda/conda-cheatsheet.pdf).

### Create and Load Conda Environment From `yml` File

>Note: The `<os>` designation is either `ubnt1604` (for Ubuntu 16.04) or `win10` (for Windows 10).

```shell
(base)$ conda env create -f ibaio_dev{38,39}.<os>.yml
(base)$ conda activate eda_dev39 
(ibaio_dev{38,39})$ cd ipynb
(ibaio_dev{38,39})$ jupyter lab
```

### Install New Conda Environment Packages

```shell
(ibaio_dev{38,39}) $ conda install <package name>
```

### Update Conda Environment Packages

```shell
(ibaio_dev{38,39}) $ conda update <package name>
```

### Export Conda Environment

```shell
(ibaio_dev{38,39}) $ conda env export > ibaio_dev{38,39}.<os>.yml
```

### Get Conda Environment

```shell
(ibaio_dev{38,39}) $ conda info -e
```

### Remove Conda Environment

```shell
(ibaio_dev{38,39}) $ conda remove -n <env_name> -all
```

---

## References

* []()
* []()
* []()
* []()
* []()