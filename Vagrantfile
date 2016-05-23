# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "manager" do |node|
    node.vm.box = "boxcutter/centos71"
    node.vm.network :private_network, ip: "10.10.2.100"
    node.vm.provider "virtualbox" do |v|
      v.name = "cloudify-manager"
      v.memory = 4096
      v.cpus = 2
    end
  end

  (1..2).each do |i|
    config.vm.define "node#{i}" do |node|
      node.vm.box = "ubuntu/trusty64"
      # Xenial problems:
      # 1) Its default sshd config doesn't support Cloudify 3.3.1's version of Paramiko, see: http://stackoverflow.com/a/32691055/849021
      # 2) Cloudify 3.3.1 doesn't have an agent package for Xenial
      # 3) Vagrant box bug: https://github.com/mitchellh/vagrant/issues/7155
      #node.vm.box = "geerlingguy/ubuntu1604"
      node.vm.network :private_network, ip: "10.10.2.#{100+i}"
      node.vm.provider "virtualbox" do |v|
        v.name = "cloudify-node#{i}"
      end
    end
  end
end
