#!/bin/bash
yum -y install epel-release
yum -y update
yum -y install ansible
mkdir -p /home/alineuser/share/docker/mount_dir/builds/
mkdir -p /home/alineuser/share/docker/mount_dir/elastic_env/

cat <<EOF >/home/alineuser/share/docker/mount_dir/elastic_env/env.txt
TOKEN_EXPIRATION=55
TOKEN_SECRET=Aline-secret-key
LOG_INFO_TIME=1
LOG_ENABLE=true
FILE_EXT=/tab/csv/xlsx
TEMP_PATH=C:\Users\vinay\Downloads
APP_PORT=8082
ENV_MGMT_URL=http://localhost
ENV_MGMT_PORT=9000
BINARY_URL=http://localhost:8080/hoster/envmgmt
EOF

ip=`hostname -I`

for i in $ip; 
do 
echo -n "do you want to use $i as master ip? (y/n) : "
read varname
if [ "$varname" == "y" ]; then
    sed -i "s/localhost/$i/g" /home/alineuser/share/docker/mount_dir/elastic_env/env.txt
    sed -i "s/localhost/$i/g" ./3_depend.yml
    sed -i "s/localhost/$i/g" ./5_startcontaines.yml

               break
fi
done

echo -n "enter registry ip:"
read regip
sed -i "s/registryip/$regip/g" ./3_depend.yml


echo -n "enter registry name:"
read regname
sed -i "s/registryname/$regname/g" ./3_depend.yml
sed -i "s/registryname/$regname/g" ./5_startcontaines.yml

