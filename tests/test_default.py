import testinfra.utils.ansible_runner


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


def test_kibana_listen_on_port_5601(Socket):
    port = Socket("tcp://0.0.0.0:5601")
    assert port.is_listening


def test_kibana_package_version_is_550(Package):
    package = Package("kibana")
    assert package.is_installed
    assert '5.5.0' == package.version


def test_kibana_plugins_directory_exists(File):
    plugins = File('/usr/share/kibana/plugins/logtrail')
    assert plugins.exists
    assert plugins.is_directory
