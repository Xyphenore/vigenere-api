# Production :

## Install the API :

### Requirements :

<b> Python 3.9 </b>

Upper versions are not tested, but we think the package can work.<br>
If an issue has occurred, open a ticket to: https://etulab.univ-amu.fr/d19006523/vigenere-api/-/issues

### Update pip :

```shell
pip install --upgrade pip
```

### Create a virtual environment :

#### Install the virtual environment package :

Install the virtual environment, the one you want.<br>
We recommend installing the 'venv' package.<br>
In the next steps, we use the package 'venv'.

```shell
pip install venv
```

#### Create the environment :

```shell
python3 -m venv .venv
```

#### Load the environment :

##### Linux / MacOS :

```shell
source .venv/bin/activate
```

##### Windows :

###### CMD :

```shell
.venv\Scripts\activate.bat
```

###### PowerShell :

```shell
.venv\Scripts\Activate.ps1
```

### Install dependencies :

```shell
pip install vigenere-api --index-url https://etulab.univ-amu.fr/api/v4/projects/8004/packages/pypi/simple
```

## Run the API :

```shell
python3 -m vigenere_api
```

# Development :

### Requirements :

<b> Python 3.9 </b>

Upper versions are not tested, but we think the package can work.<br>
If an issue has occurred, open a ticket to: https://etulab.univ-amu.fr/d19006523/vigenere-api/-/issues

## Install requirements :

### Last version of pip :

```shell
pip install --upgrade pip
```

### Poetry :

To execute tests or improve the package, you need Poetry.<br>
Go to: https://python-poetry.org/docs/#installing-with-the-official-installer

You can install poetry with the official installer or pipx.

## Create a virtual environment :

### Install the virtual environment package :

Install the virtual environment, the one you want.<br>
We recommend installing the 'venv' package.<br>
In the next steps, we use the package 'venv'.

```shell
pip install venv
```

### Create the environment :

```shell
python3 -m venv .venv
```

### Load the environment :

#### Linux / MacOS :

```shell
source .venv/bin/activate
```

#### Windows :

##### CMD :

```shell
.venv\Scripts\activate.bat
```

##### PowerShell :

```shell
.venv\Scripts\Activate.ps1
```

## Install dependencies :

### Main dependencies like the production :

```shell
poetry install --only main
```

### Dependencies for development :

```shell
poetry install
```

## (Optional) Update dependencies :

```shell
poetry update
```

## Run the API :

```shell
python -m vigenere_api
```

## Execute tests :

```shell
PYTHONPATH=./src pytest
```

## Execute coverage :

```shell
PYTHONPATH=./src pytest --cov=src --cov=tests --cov=src --cov=tests --junit-xml=coverage.xml --cov-report=html:coverage_html
```

## Execute integration tests :

```shell
PYTHONPATH=./src pytest --with-integration
```

## Build the API package :

```shell
poetry build
```
