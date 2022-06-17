# confenv
Confenv is an environment variable setup tool for windows User. It's similar to "direnv" tool on the unix/linux OS.

## Installation
- Requirements
  ```
  python>=3.4

  pip install configparser, pyinstaller
  ```

- Package & Install
  ```bash
  # Package
  pyinstaller.exe --hidden-import ConfigParser -F -p [your python libary path] .\confenv.py
  
  # Install
  cp .\dist\confenv.exe [your private bin path in $PATH]
  ```

## How to Use it?
```bash
confenv [env_name] -- [command] [args] [options]

For instance:
confenv cn-dev -- pulumi up -s dev
```
```ini
And the config file '.envrc.ini' you need to setup is like:
[cn-dev]
PULUMI_CONFIG_PASSPHRASE=xxx
AZURE_STORAGE_DOMAIN=xxx
AZURE_STORAGE_ACCOUNT=xxx
AZURE_STORAGE_KEY=xxx

[cn-dev]
...
[cn-dev]
...

```