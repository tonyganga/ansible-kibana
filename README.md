Kibana 5.x
=========

[![Build Status](https://travis-ci.org/tonyganga/ansible-kibana.svg?branch=master)](https://travis-ci.org/tonyganga/ansible-kibana)

This role will install and configure Kibana 5.x and plugins.

Supported Platforms
-------------------

This role has been tested on CentOS 7.

Requirements
------------

The role has been tested with the following on Mac and Linux.

* [Docker](https://www.docker.com/) >= 17.06.0-ce
* [Molecule](https://github.com/metacloud/molecule) >= 1.25.0
* [Ansible](https://www.ansible.com/) >= 2.3.1.0

Dependencies
------------

None

Role Variables
--------------

```yaml
kibana_version: 5.5.0
kibana_server_port: 5601
kibana_server_host: "0.0.0.0"
kibana_elasticsearch_url: "http://your_elasticsearch.io"
install_kibana_plugins: true
kibana_plugins: []
```

Listeners
---------

```yaml
---
- name: restart kibana service
  service:
    name: kibana
    state: restarted
  listen: restart kibana

- name: start kibana service
  systemd:
    name: kibana
    state: started
    enabled: yes
  listen: start kibana
```

Example Playbook
----------------

```yaml
- hosts: kibana
  roles:
    - kibana
  vars:
    kibana_version: 5.5.0
    kibana_server_port: 5601
    kibana_server_host: "0.0.0.0"
    kibana_elasticsearch_url: "elasticsearch.awesomedomain.com"
    kibana_plugins:
    - url: https://github.com/sivasamyk/logtrail/releases/download/v0.1.17/logtrail-5.5.0-0.1.17.zip
      name: logtrail
```

Tests
-----

Use molecule to run tests.

```bash
molecule test
```

License
-------

BSD
