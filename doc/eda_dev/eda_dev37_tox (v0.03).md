#eda_dev37 (v0.03)
2021-06-10

>Note: No versions were specified in [`requirement.txt`](requirements%20(v0.03).txt)

`tox.ini` installation:
```shell
/home/cwm/git/git.c-w-m/sim_dev/.tox/sim_dev39/bin/python /opt/pycharm-community-2021.1/plugins/python-ce/helpers/pycharm/_jb_tox_runner.py
Testing started at 7:51 PM ...
eda_dev37 create: /home/cwm/git/git.c-w-m/eda_dev/.tox/eda_dev37
eda_dev37 installdeps: -rrequirements.txt
eda_dev37 installed: anyio==3.1.0,appdirs==1.4.4,argon2-cffi==20.1.0,async-generator==1.10,atomicwrites==1.4.0,attrs==21.2.0,Babel==2.9.1,backcall==0.2.0,beautifulsoup4==4.9.3,bleach==3.3.0,Brotli==1.0.9,brotlipy==0.7.0,certifi==2021.5.30,cffi==1.14.5,chardet==4.0.0,colorama==0.4.4,cramjam==2.3.2,cryptography==3.4.7,cycler==0.10.0,Cython==0.29.23,decorator==5.0.9,defusedxml==0.7.1,deprecation==2.1.0,distlib==0.3.2,entrypoints==0.3,et-xmlfile==1.1.0,fastparquet==0.6.3,filelock==3.0.12,fsspec==2021.6.0,greenlet==1.1.0,html5lib==1.1,icc-rt==2020.0.133,idna==2.10,importlib-metadata==4.5.0,importlib-resources==5.1.4,iniconfig==1.1.1,intel-openmp==2020.0.133,ipykernel==5.5.5,ipython==7.24.1,ipython-genutils==0.2.0,jdcal==1.4.1,jedi==0.18.0,Jinja2==3.0.1,json5==0.9.5,jsonschema==3.2.0,jupyter-client==6.1.12,jupyter-core==4.7.1,jupyter-packaging==0.10.2,jupyter-server==1.8.0,jupyterlab==3.0.16,jupyterlab-pygments==0.1.2,jupyterlab-server==2.6.0,kiwisolver==1.3.1,llvmlite==0.36.0,lml==0.1.0,lxml==4.6.3,MarkupSafe==2.0.1,matplotlib==3.4.2,matplotlib-inline==0.1.2,mistune==0.8.4,mock==4.0.3,more-itertools==8.8.0,nbclassic==0.3.1,nbclient==0.5.3,nbconvert==6.0.7,nbformat==5.1.3,nest-asyncio==1.5.1,notebook==6.4.0,numba==0.53.1,numexpr==2.7.3,numpy==1.20.3,odfpy==1.4.1,olefile==0.46,openpyxl==3.0.7,packaging==20.9,pandas==1.2.4,pandocfilters==1.4.3,parso==0.8.2,patsy==0.5.1,pexpect==4.8.0,pickleshare==0.7.5,Pillow==8.2.0,pluggy==0.13.1,prometheus-client==0.11.0,prompt-toolkit==3.0.18,psycopg2==2.8.6,ptyprocess==0.7.0,py==1.10.0,pyarrow==4.0.1,pycparser==2.20,pyexcel-ezodf==0.3.4,pyexcel-io==0.6.4,pyexcel-ods3==0.6.0,Pygments==2.9.0,PyMySQL==1.0.2,pyOpenSSL==20.0.1,pyparsing==2.4.7,pyreadstat==1.1.2,pyrsistent==0.17.3,PySocks==1.7.1,pytest==6.2.4,python-dateutil==2.8.1,pytz==2021.1,pyxlsb==1.0.8,pyzmq==22.1.0,requests==2.25.1,scipy==1.6.3,Send2Trash==1.5.0,six==1.16.0,sniffio==1.2.0,soupsieve==2.2.1,SQLAlchemy==1.4.18,statsmodels==0.12.2,terminado==0.10.1,testpath==0.5.0,thrift==0.13.0,toml==0.10.2,tomlkit==0.7.2,tornado==6.1,traitlets==5.0.5,typing-extensions==3.10.0.0,urllib3==1.26.5,wcwidth==0.2.5,webencodings==0.5.1,websocket-client==1.1.0,win-inet-pton==1.1.0,wincertstore==0.2,xlrd==2.0.1,XlsxWriter==1.4.3,xlwt==1.3.0,zipp==3.4.1,zstd==1.5.0.2
eda_dev37 run-test-pre: PYTHONHASHSEED='1750496607'
eda_dev37 run-test: commands[0] | python -m pip install --upgrade pip
Requirement already satisfied: pip in ./.tox/eda_dev37/lib/python3.7/site-packages (21.0.1)
Collecting pip
  Using cached pip-21.1.2-py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.0.1
    Uninstalling pip-21.0.1:
      Successfully uninstalled pip-21.0.1
Successfully installed pip-21.1.2
eda_dev37 run-test: commands[1] | python -c 'print((80*"~")+"\ntestenv: commands\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testenv: commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
eda_dev37 run-test: commands[2] | python -c 'print((80*"~")+"\n"+"pip list\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
eda_dev37 run-test: commands[3] | python -m pip list --format=columns
Package             Version
------------------- ----------
anyio               3.1.0
appdirs             1.4.4
argon2-cffi         20.1.0
async-generator     1.10
atomicwrites        1.4.0
attrs               21.2.0
Babel               2.9.1
backcall            0.2.0
beautifulsoup4      4.9.3
bleach              3.3.0
Brotli              1.0.9
brotlipy            0.7.0
certifi             2021.5.30
cffi                1.14.5
chardet             4.0.0
colorama            0.4.4
cramjam             2.3.2
cryptography        3.4.7
cycler              0.10.0
Cython              0.29.23
decorator           5.0.9
defusedxml          0.7.1
deprecation         2.1.0
distlib             0.3.2
entrypoints         0.3
et-xmlfile          1.1.0
fastparquet         0.6.3
filelock            3.0.12
fsspec              2021.6.0
greenlet            1.1.0
html5lib            1.1
icc-rt              2020.0.133
idna                2.10
importlib-metadata  4.5.0
importlib-resources 5.1.4
iniconfig           1.1.1
intel-openmp        2020.0.133
ipykernel           5.5.5
ipython             7.24.1
ipython-genutils    0.2.0
jdcal               1.4.1
jedi                0.18.0
Jinja2              3.0.1
json5               0.9.5
jsonschema          3.2.0
jupyter-client      6.1.12
jupyter-core        4.7.1
jupyter-packaging   0.10.2
jupyter-server      1.8.0
jupyterlab          3.0.16
jupyterlab-pygments 0.1.2
jupyterlab-server   2.6.0
kiwisolver          1.3.1
llvmlite            0.36.0
lml                 0.1.0
lxml                4.6.3
MarkupSafe          2.0.1
matplotlib          3.4.2
matplotlib-inline   0.1.2
mistune             0.8.4
mock                4.0.3
more-itertools      8.8.0
nbclassic           0.3.1
nbclient            0.5.3
nbconvert           6.0.7
nbformat            5.1.3
nest-asyncio        1.5.1
notebook            6.4.0
numba               0.53.1
numexpr             2.7.3
numpy               1.20.3
odfpy               1.4.1
olefile             0.46
openpyxl            3.0.7
packaging           20.9
pandas              1.2.4
pandocfilters       1.4.3
parso               0.8.2
patsy               0.5.1
pexpect             4.8.0
pickleshare         0.7.5
Pillow              8.2.0
pip                 21.1.2
pluggy              0.13.1
prometheus-client   0.11.0
prompt-toolkit      3.0.18
psycopg2            2.8.6
ptyprocess          0.7.0
py                  1.10.0
pyarrow             4.0.1
pycparser           2.20
pyexcel-ezodf       0.3.4
pyexcel-io          0.6.4
pyexcel-ods3        0.6.0
Pygments            2.9.0
PyMySQL             1.0.2
pyOpenSSL           20.0.1
pyparsing           2.4.7
pyreadstat          1.1.2
pyrsistent          0.17.3
PySocks             1.7.1
pytest              6.2.4
python-dateutil     2.8.1
pytz                2021.1
pyxlsb              1.0.8
pyzmq               22.1.0
requests            2.25.1
scipy               1.6.3
Send2Trash          1.5.0
setuptools          56.2.0
six                 1.16.0
sniffio             1.2.0
soupsieve           2.2.1
SQLAlchemy          1.4.18
statsmodels         0.12.2
terminado           0.10.1
testpath            0.5.0
thrift              0.13.0
toml                0.10.2
tomlkit             0.7.2
tornado             6.1
traitlets           5.0.5
typing-extensions   3.10.0.0
urllib3             1.26.5
wcwidth             0.2.5
webencodings        0.5.1
websocket-client    1.1.0
wheel               0.36.2
win-inet-pton       1.1.0
wincertstore        0.2
xlrd                2.0.1
XlsxWriter          1.4.3
xlwt                1.3.0
zipp                3.4.1
zstd                1.5.0.2
eda_dev37 run-test: commands[4] | python -c 'print((80*"~")+"\n"+"pip freeze\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip freeze
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
eda_dev37 run-test: commands[5] | pip freeze
anyio==3.1.0
appdirs==1.4.4
argon2-cffi==20.1.0
async-generator==1.10
atomicwrites==1.4.0
attrs==21.2.0
Babel==2.9.1
backcall==0.2.0
beautifulsoup4==4.9.3
bleach==3.3.0
Brotli==1.0.9
brotlipy==0.7.0
certifi==2021.5.30
cffi==1.14.5
chardet==4.0.0
colorama==0.4.4
cramjam==2.3.2
cryptography==3.4.7
cycler==0.10.0
Cython==0.29.23
decorator==5.0.9
defusedxml==0.7.1
deprecation==2.1.0
distlib==0.3.2
entrypoints==0.3
et-xmlfile==1.1.0
fastparquet==0.6.3
filelock==3.0.12
fsspec==2021.6.0
greenlet==1.1.0
html5lib==1.1
icc-rt==2020.0.133
idna==2.10
importlib-metadata==4.5.0
importlib-resources==5.1.4
iniconfig==1.1.1
intel-openmp==2020.0.133
ipykernel==5.5.5
ipython==7.24.1
ipython-genutils==0.2.0
jdcal==1.4.1
jedi==0.18.0
Jinja2==3.0.1
json5==0.9.5
jsonschema==3.2.0
jupyter-client==6.1.12
jupyter-core==4.7.1
jupyter-packaging==0.10.2
jupyter-server==1.8.0
jupyterlab==3.0.16
jupyterlab-pygments==0.1.2
jupyterlab-server==2.6.0
kiwisolver==1.3.1
llvmlite==0.36.0
lml==0.1.0
lxml==4.6.3
MarkupSafe==2.0.1
matplotlib==3.4.2
matplotlib-inline==0.1.2
mistune==0.8.4
mock==4.0.3
more-itertools==8.8.0
nbclassic==0.3.1
nbclient==0.5.3
nbconvert==6.0.7
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.4.0
numba==0.53.1
numexpr==2.7.3
numpy==1.20.3
odfpy==1.4.1
olefile==0.46
openpyxl==3.0.7
packaging==20.9
pandas==1.2.4
pandocfilters==1.4.3
parso==0.8.2
patsy==0.5.1
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.2.0
pluggy==0.13.1
prometheus-client==0.11.0
prompt-toolkit==3.0.18
psycopg2==2.8.6
ptyprocess==0.7.0
py==1.10.0
pyarrow==4.0.1
pycparser==2.20
pyexcel-ezodf==0.3.4
pyexcel-io==0.6.4
pyexcel-ods3==0.6.0
Pygments==2.9.0
PyMySQL==1.0.2
pyOpenSSL==20.0.1
pyparsing==2.4.7
pyreadstat==1.1.2
pyrsistent==0.17.3
PySocks==1.7.1
pytest==6.2.4
python-dateutil==2.8.1
pytz==2021.1
pyxlsb==1.0.8
pyzmq==22.1.0
requests==2.25.1
scipy==1.6.3
Send2Trash==1.5.0
six==1.16.0
sniffio==1.2.0
soupsieve==2.2.1
SQLAlchemy==1.4.18
statsmodels==0.12.2
terminado==0.10.1
testpath==0.5.0
thrift==0.13.0
toml==0.10.2
tomlkit==0.7.2
tornado==6.1
traitlets==5.0.5
typing-extensions==3.10.0.0
urllib3==1.26.5
wcwidth==0.2.5
webencodings==0.5.1
websocket-client==1.1.0
win-inet-pton==1.1.0
wincertstore==0.2
xlrd==2.0.1
XlsxWriter==1.4.3
xlwt==1.3.0
zipp==3.4.1
zstd==1.5.0.2
eda_dev37 run-test: commands[6] | python -c 'print((80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

___________________________________ summary ____________________________________
  eda_dev37: commands succeeded
  congratulations :)

Process finished with exit code 0

```