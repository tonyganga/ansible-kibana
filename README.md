Kibana 5.x
=========

This role will install and configure Kibana 5.x

Supported Platforms
-------------------

This role has been tested on CentOS 7.

Requirements
------------
The role has been tested with the following on Mac and Linux.

* [Docker](https://www.docker.com/) >= 17.06.0-ce
* [Molecule](https://github.com/metacloud/molecule) >= 1.25.0
* [Ansible](https://www.ansible.com/) >= 2.3.1.0

Role Variables
--------------

```
kibana_version: 5.5.0
kibana_server_port: 5601
kibana_server_host: "0.0.0.0"
kibana_elasticsearch_url: "http://your_elasticsearch.io"
install_kibana_plugins: true
kibana_plugins: []
#- url: https://github.com/sivasamyk/logtrail/releases/download/v0.1.17/logtrail-5.5.0-0.1.17.zip
#  name: logtrail

```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: kibana
      roles:
         - kibana
      vars:
        kibana_version: 5.5.0
        kibana_server_port: 5601
        kibana_server_host: "0.0.0.0"
        kibana_elasticsearch_url: "elasticsearch.awesomedomain.com"


Tests
-----
Use molecule to run tests, you should see something similiar to the below output.

```
$ molecule test

--> Idempotence test in progress (can take a few minutes)...
--> Starting Ansible Run...
Idempotence test passed.
--> Executing ansible-lint...
--> Executing flake8 on *.py files found in tests/...
--> Executing testinfra tests found in tests/...
============================= test session starts ==============================
platform darwin -- Python 2.7.13, pytest-3.1.1, py-1.4.34, pluggy-0.4.0 -- /usr/local/opt/python/bin/python2.7
cachedir: .cache
rootdir: /Users/anthonyganga/projects/logging/roles/kibana, inifile:
plugins: testinfra-1.5.5, xdist-1.18.0
collected 10 itemss

tests/test_default.py::test_kibana_config_file_exists[docker://kibana] PASSED
tests/test_default.py::test_kibana_binary_exist[docker://kibana] PASSED
tests/test_default.py::test_kibana_service_is_running_and_enabled[docker://kibana] PASSED
tests/test_default.py::test_kibana_listen_on_port_5601[docker://kibana] PASSED
tests/test_default.py::test_kibana_package_version_is_550[docker://kibana] PASSED

=============================== warnings summary ===============================
None
  Module already imported so can not be re-written: testinfra

-- Docs: http://doc.pytest.org/en/latest/warnings.html
==================== 5 passed, 0 warnings in 1.12 seconds =====================
--> Destroying instances...
Stopping container kibana...
Removed container kibana.
```

License
-------

BSD
