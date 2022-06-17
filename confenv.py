# -*- coding：utf-8 -*-
# time ：2022/5/29 10:44
# author: Max Mei

import os
import sys
import argparse
from pathlib import Path
from configparser import ConfigParser
from subprocess import PIPE, Popen

env_file = ".envrc.ini"
parser = argparse.ArgumentParser("confenv",
                                 description="To wrap a command and setup environment variables automatically through config file `.envrc.ini` at execution dir.",
                                 epilog="""
    The example of configuration .envrc.ini:
        [dev]
        PULUMI_CONFIG_PASSPHRASE=
        AZURE_STORAGE_DOMAIN=
        AZURE_STORAGE_ACCOUNT=
        AZURE_STORAGE_KEY=

        [test]
        ...
        [prod]
        ...
     """)
parser.add_argument(
    "env", help="the section name of file .envrc.ini, it should be corresponed to pulumi's stack name.")
args, unknownargs = parser.parse_known_args()
env_str = args.env

def get_config_dirs():
    return [os.getcwd(), Path.home()]

def init_environment(env_str):
    config = ConfigParser()
    config_dirs = get_config_dirs()
    configured = False
    for conf_dir in config_dirs:
        config_path = os.path.join(conf_dir, env_file)
        if not os.path.exists(config_path):
            continue
        
        print(f"Load environment {env_str} from config: {config_path}")
        config.read(config_path, encoding='UTF-8')
        if env_str not in config:
            print(f"Environment {env_str} is not configured.")
            sys.exit("Exit Error.")

        envs = config[env_str]
        for key in envs.keys():
            os.environ[key] = envs.get(key)
        configured = True
        break
    
    if not configured:
        print(f"Please makesure config file '{env_file}' can be found at dirs: %s" % ", ".join(config_dirs))
        sys.exit("Exit NotFound.")

def execute_command(command_str):
    print("exec:", command_str)
    env = os.environ.copy()
    p = Popen(command_str, shell=True, env=env)
    p.wait()


init_environment(env_str)
command_str = ' '.join(unknownargs)
if not command_str:
    print("Usage: confenv [env] -- [command] [args]")
    sys.exit("Exit NotFound.")

execute_command(' '.join(unknownargs))
sys.exit("Exit Done.")
