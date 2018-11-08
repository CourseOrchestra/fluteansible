import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_executable_file(host):
    flute = host.file('/opt/flute/flute.jar')
    assert flute.exists


def test_jython_installed(host):
    cmd = host.run('jython --version')
    assert cmd.rc == 0
    assert cmd.stderr.find(u'Jython 2') > -1

def test_log_files(host):
    stdout = host.file('/var/log/flute/std.out')
    stderr = host.file('/var/log/flute/std.err')
    assert stdout.exists
    assert stderr.exists
