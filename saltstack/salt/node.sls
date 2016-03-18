include:
  - common

## Install the siege command
siege:
  pkg.installed:
    - require:
      - sls: common