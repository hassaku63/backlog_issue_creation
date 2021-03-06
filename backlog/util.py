# coding: utf-8

import os
from yaml import load as yaml_load


CONFIG_SKELTON_YAML = """
backlog:
  default_project: default_project_key
  user: alice
  api_key: api_key
"""


def load_conf(filename="./conf.yml"):
  with open(filename) as f:
    return yaml_load(f)


def generate_default_config():
    return CONFIG_SKELTON_YAML


