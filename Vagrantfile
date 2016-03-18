# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# Load External Preferences
require File.join(File.dirname(__FILE__), './', 'config/prefs.rb')

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Hostname Manager
  #config.hostmanager.enabled = true
  #config.hostmanager.manage_host = false
  #config.hostmanager.manage_guest = true
  #config.hostmanager.ignore_private_ip = false
  #config.hostmanager.include_offline = true


  # Digital Ocean Configuration
  config.vm.provider :digital_ocean do |provider, override|
    override.ssh.private_key_path = '~/.ssh/id_rsa'
    override.vm.box = 'digital_ocean'
    override.vm.box_url = "https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box"

    provider.token    = $do_token
    provider.region   = $do_region
    provider.image    = $do_image
    provider.size     = $do_size
    provider.ssh_key_name = $do_ssh_key_name
    provider.private_networking = true

  end

  config.vm.define :salt , primary: true do |srv|
    srv.vm.hostname = 'salt'
    srv.vm.provision :shell, :inline => "bash /vagrant/deploy/install-salt-master.sh salt"
    srv.vm.box = "dummy"

    srv.hostmanager.aliases = %w(salt)
  end
  
  config.vm.define :node1 do |srv|
    srv.vm.hostname = 'node1'
    srv.vm.provision :shell, :inline => "bash /vagrant/deploy/install-salt-minion.sh node1"
    srv.vm.box = "dummy"
  end

  config.vm.define :node2 do |srv|
    srv.vm.hostname = 'node2'
    srv.vm.provision :shell, :inline => "bash /vagrant/deploy/install-salt-minion.sh node2"
    srv.vm.box = "dummy"
  end

  config.vm.define :node3 do |srv|
    srv.vm.hostname = 'node3'
    srv.vm.provision :shell, :inline => "bash /vagrant/deploy/install-salt-minion.sh node3"
    srv.vm.box = "dummy"
  end

end
