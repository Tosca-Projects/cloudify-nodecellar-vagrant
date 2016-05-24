Node Cellar on Vagrant using Cloudify
=====================================

`cloudify-reset` - start from scratch with Cloudify

`cloudify-install` - pulls in all relevant Cloudify repositories from GitHub, checks out the right tag/branch, creates a Python virtualenv and installs dependencies in it

`vagrant-reset` - start from scratch with Vagrant

`vagrant-install` - creates virtual machines for the Cloudify Manager and additional nodes

`vagrant-bootstrap-manager` - bootstraps Cloudify Manager on its node

`vagrant-deploy-nodecellar` - uploads the blueprint, creates a deployment, runs "install" workflow

Access the Cloudify Manager at http://10.10.2.100/

Access Node Cellar at http://10.10.2.101:8080/
