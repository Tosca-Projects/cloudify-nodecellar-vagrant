from cosmo_tester.test_suites.test_simple_manager_blueprint.nodecellar_singlehost_test import NodecellarSingleHostTest

from cosmo_tester.framework.testenv import initialize_without_bootstrap, clear_environment

def setUp():
    initialize_without_bootstrap()

def tearDown():
    clear_environment()

class NodecellarSingleHostTest2(NodecellarSingleHostTest):
    def __init__(self, *args, **kwargs):
	super(NodecellarSingleHostTest2, self).__init__(*args, **kwargs)
	self.public_ip_address = '10.10.2.101'
        self.private_ip_address = '10.10.2.101'
        self.remote_manager_key_path = '/home/vagrant/.ssh/rsa'

    def setup_simple_manager_env(self):
        return

    def bootstrap_simple_manager_blueprint(self, override_inputs=None):
        return

