Role Name
=========

This role installs Kibana 5.x

Requirements
------------

* Docker >= 17.06.0-ce, build 02c1d87
* Molecule >= 1.25.0
* Ansible >= 2.3.1.0

Role Variables
--------------

```
kibana_version: 5.5.0
kibana_server_port: 5601
kibana_server_host: "0.0.0.0"
kibana_elasticsearch_url: "http://your_elasticsearch.io"
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: kibana
      roles:
         - kibana
      vars:
        kibana_version: 5.5.0
        kibana_server_port: 5601
        kibana_server_host: "0.0.0.0"
        kibana_elasticsearch_url: "elasticsearch.awesomedomain.com"

License
-------

BSD
