Flute
=========


Jenkins [![Build Status](https://ci.corchestra.ru/buildStatus/icon?job=fluteansible/master)](https://ci.corchestra.ru/job/fluteansible/job/master/)

Travis [![Build Status](https://travis-ci.org/CourseOrchestra/fluteansible.svg?branch=master)](https://travis-ci.org/CourseOrchestra/fluteansible)

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-CourseOrchestra.flute-blue.svg)](https://galaxy.ansible.com/CourseOrchestra/flute/)

Installation of [Course Orchestra Flute](https://github.com/CourseOrchestra/flute) (https://corchestra.ru/wiki/index.php?title=Flute)

Requirements
------------

Java 8 (Oracle)

Role Variables
--------------

* flute_build: flute build number
* flute_group: the group for flute service user (default valute is flute)
* flute_dir: where to intall flute (default value is /opt/flute)
* flute_log_dir directory for logs output (default is /var/log/flute)
* flute_user  user for flute service (default is flute3)


Example Playbook
----------------

    - hosts: servers
      vars:
         oracle_java_version: 8
         oracle_java_version_update: 131
      roles:
         - role: ansiblebit.oracle-java
         - role: CourseOrchestra.flute

License
-------

MIT

Author Information
------------------

https://corchestra.ru/en
