# Vagrant Cloud Project Template

A template for creating vagrant based projects that provision in the cloud. This is 
mostly for my projects where I'm learning how to setup clusters of servers and want
to quickly tear down the project inbetween coding sessions.

## Prerequisites 

You will need the following:

- Vagrant 1.8.1+ - [download](https://www.vagrantup.com/downloads.html)
- Vagrant DigitalOcean provider - [repo](https://github.com/devopsgroup-io/vagrant-digitalocean)

You can install the DigitalOcean provider by running the command:

```
vagrant plugin install vagrant-digitalocean
```

## Setup

### Step 1: Clone the repository

Go ahead and clone this repository somewhere (feel free to fork it!):

```bash
git clone git@github.com:JustinCarmony/vagrant-cloud-project.git
```

Once you've cloned it, you will need to copy ``config/prefs.example.rb`` 
to ``config/prefs.rb`` and change the values inside the example config.

```ruby
# Copy this file to `config/prefs.rb`

## Digital Ocean Settings ##

# Your API Token
$do_token       = 'abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789'
# Region Name
$do_region      = 'nyc2'
# Which image
$do_image       = 'ubuntu-14-04-x64'
# Image Size
$do_size        = '1gb'
# The name of your ssh key in Digital Ocean
$do_ssh_key_name = 'Vagrant'
```



