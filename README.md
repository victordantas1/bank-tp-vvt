# bank-tp-vvt
Bank System to  apply Mutation Tests

## Classes Diagram
![Classes Diagram](assets/diagrama-de-classes.png)
[Link to Diagram](https://drive.google.com/file/d/1xOfx8NG1MYgtKMKggUXQLsjS_ahc-RpQ/view?usp=sharing)

## Pre-requisites
- Python 3.10.x

## Create Virtual Enviroment
```
python3 -m venv .venv
```

## Install Dependencies
```
.venv/Scripts/activate
pip install -r requirements.txt
```

## How run tests
```
pytest
```
To see coverage:
```
pytest --cov=src
```

## Setup and Run Cosmic Ray
```
# Create config to mutation test
cosmic-ray new-config bank-vvt.toml

# Init mutations and .sqlite
cosmic-ray init bank-vvt.toml bank-vvt.sqlite

# Execute a baseline tests (without mutations)
cosmic-ray --verbosity=INFO baseline bank-vvt.toml

# To see mutations report 
cr-report bank-vvt.sqlite --show-pending

# Execute mutation tests
cosmic-ray exec bank-vvt.toml bank-vvt.sqlite

# To see report in html
cr-html bank-vvt.sqlite > report.html

```