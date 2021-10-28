Vagrant.configure("2") do |config|
  config.vm.box = "centos8"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision "shell", inline: <<-shell
    if [ ! -f "/var/log/first.log" ]; then
        sed -i '/^SELINUX=/s/enforcing/disabled/' /etc/selinux/config
        timedatectl set-timezone Asia/Shanghai
        systemctl stop firewalld
        systemctl disable firewalld
        yum install -y yum-utils device-mapper-persistent-data lvm2
        yum-config-manager --add-repo http://mirrors.aliyun.com/repo/Centos-8.repo
        yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
        yum clean all && yum makecache
        yum -y upgrade && yum -y update
        yum remove -y docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
        yum install -y docker-ce docker-ce-cli containerd.io
        systemctl start docker
        systemctl enable docker
        echo $(date) > /var/log/first.log
    fi
  shell
end
