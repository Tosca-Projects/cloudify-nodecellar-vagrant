Node Cellar on Vagrant using Cloudify
=====================================

`cloudify-install` - pulls in all relevant Cloudify repositories from GitHub, creates a Python virtualenv and installs dependencies in it

`cloudify-checkout` - checks out a specific version of Cloudify from all repositories

`vagrant-install` - creates virtual machines for the Cloudify Manager and two additional nodes

`vagrant-bootstrap-manager` - bootstraps Cloudify Manager on its node

`vagrant-deploy-nodecellar` - uploads the blueprint, creates a deployment, runs "install" workflow

Access the Cloudify Manager at http://10.10.2.100/

Access Node Cellar at http://10.10.2.101:8080/
