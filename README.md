# grigode-env-2

grigode-env-2 is a library for reading and managing key-value pairs from .env files in your projects.

- [Installation](#installation)
- [The syntax of the `.env` file](#the-syntax-of-the-env-file)
- [Available data types](#available-data-types)

## Installation

```bash
pip install grigode-env-2
```

If you need to use system environment variables and want to add more environment variables without having to configure them manually or modify the system variables, you can choose to add grigode_env to your application to load the configuration from one or more .env files:

```python
from grigodeenv2 import datetime, Env, read_environ

read_environ('.env')

env = Env(
    EMAIL_PORT=(int, 45),
    ANY_DATETIME=(datetime, None, {"format": '%d/%m/%y %H:%M:%S'})
)

SECRET_KEY = env('SECRET_KEY')  # str
DEBUG = env.bool('DEBUG')  # bool
SERVER_PORT = env.int('SERVER_PORT')  #int
EMAIL_PORT = env('EMAIL_PORT')  #int
HOSTS = env.list('HOSTS')  # list
ANY_DATETIME = env('ANY_DATETIME')  # datetime

```

## The syntax of the `.env` file

```
# App Config
SECRET_KEY=mi_clave_secreta
DEBUG=true

# Server Config
SERVER_PORT=3000
HOSTS=["localhost"]

# Configuración de correo electrónico
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=usuario@example.com
EMAIL_PASSWORD=mi_password_secreto

# Other
ANY_DATETIME=15/03/24 13:55:26
```

## Available data types

```python
STRING = env.str('STRING')  # str
BYTES = env.bytes('BYTES')  # bytes
BOOLEAN = env.bool('BOOLEAN')  # bool
INTEGER = env.int('INTEGER')  # int
FLOAT = env.float('FLOAT')  # float
JSON = env.json('JSON')  # dict
LIST = env.list('LIST')  # list
TUPLE = env.tuple('TUPLE')  # tuple
DICTIONARY = env.dict('DICTIONARY')  # dict
DATETIME = env.datetime('DATETIME')  # datetime.datetime
```
