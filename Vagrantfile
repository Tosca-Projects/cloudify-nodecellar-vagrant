load "./cloudify-config"

Vagrant.configure("2") do |config|
  config.vm.define "manager" do |node|
    node.vm.box = "boxcutter/centos72"
    node.vm.network :private_network, ip: "#{NETWORK}.100"
    node.vm.provider "virtualbox" do |v|
      v.name = "cloudify-manager"
      v.memory = 4500 # ElasticSearch needs a lot of RAM!
      v.cpus = 2 # Not necessary but won't hurt
    end
  end

  (1..HOST_COUNT).each do |i|
    config.vm.define "host#{i}" do |host|
      host.vm.box = "ubuntu/trusty64"

      # Why not Xenial?
      # 1) Its default sshd config doesn't support Cloudify 3.3.1's version of Paramiko, see: http://stackoverflow.com/a/32691055/849021
      # 2) Cloudify doesn't have an agent package for Xenial: http://10.10.2.100:53229/packages/agents/
      # 3) Vagrant box bug: https://github.com/mitchellh/vagrant/issues/7155
      #host.vm.box = "geerlingguy/ubuntu1604"

      host.vm.network :private_network, ip: "#{NETWORK}.#{100+i}"
      host.vm.provider "virtualbox" do |v|
        v.name = "cloudify-host#{i}"
      end
    end
  end
end
