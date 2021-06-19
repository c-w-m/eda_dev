# Conda Installation

Ubuntu 16.04 Issues:

**Fix: add channels**

```shell
(base) cwm@flxsa02:~/git/git.c-w-m/eda_dev$ conda install --force-reinstall -y -q --name eda_dev39 -c conda-forge --file requirements.txt
Collecting package metadata (current_repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.

PackagesNotFoundError: The following packages are not available from current channels:

  - jupyterlab-pygments==0.1.2
  - importlib-resources==5.1.0
  - jupyterlab-widgets==1.0.0
  - tables==3.6.1
  - pyexcel-ods3==0.6.0
  - mypy-extensions==0.4.3
  - et-xmlfile==1.1.0
  - cramjam==2.3.2
  - desmod==0.6.1
  - jupyter-client==6.1.12
  - jupyter-core==4.7.1
  - ipython-genutils==0.2.0
  - jupyterlab-server==2.6.0
  - websocket-client==1.0.1
  - async-generator==1.10
  - jupyter-server==1.8.0
  - prometheus-client==0.11.0

Current channels:

  - https://conda.anaconda.org/conda-forge/linux-64
  - https://conda.anaconda.org/conda-forge/noarch
  - https://repo.anaconda.com/pkgs/main/linux-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/linux-64
  - https://repo.anaconda.com/pkgs/r/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


(base) cwm@flxsa02:~/git/git.c-w-m/eda_dev$ 

```

pip install <missing packages>
``shell
    - jupyterlab
      - async-generator
      - ipython-genutils
      - jupyter-client
      - jupyter-core
      - jupyter-server
      - jupyterlab-pygments
      - jupyterlab-server
      - prometheus-client

    - desmod
    - importlib-resources
    - jupyterlab-widgets
    - mypy-extensions
    - tables
```