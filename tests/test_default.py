import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_kibana_config_file_exists(File):
    config = File('/etc/kibana/kibana.yml')
    assert config.exists
    assert config.is_file


def test_kibana_binary_exist(File):
    bin = File('/usr/share/kibana/bin/kibana')
    assert bin.exists
    assert bin.is_file


def test_kibana_service_is_running_and_enabled(Service):
    service = Service("kibana")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("port", [
    ("5601")
])
def test_kibana_listen_on_port_5601(Socket, port):
    port = Socket("tcp://0.0.0.0:" + port)
    assert port.is_listening


@pytest.mark.parametrize("version", [
    ("5.5.0")
])
def test_kibana_package_version_is_550(Package, version):
    package = Package("kibana")
    assert package.is_installed
    assert version == package.version


@pytest.mark.parametrize("plugin", [
    ("logtrail")
])
def test_kibana_plugins_installed(File, Command, plugin):
    if "centos-7-kibana-plugins" in Command("hostname").stdout:
        directory = File("/usr/share/kibana/plugins/" + plugin)
        assert directory.exists
        assert directory.is_directory
