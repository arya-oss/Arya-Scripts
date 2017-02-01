## Set Up Linux VM in AWS Cloud and Access from NITW College Network

### Launch an EC2 Instance
1. [SignIn to AWS Console](https://aws.amazon.com/)
2. Click on Launch EC2 VMs.
3. Select Your favourite Operation Systems. I'll recommend Ubuntu 16.04
4. Select Free Tier instance and click on **Review and Launch**.
5. If you don't have existing Key-Pair for login create a new one. Keep this key secure, it is
the key to your VM.
6. Finalize and Launch
7. Goto Instance Page and check whether your VM is up or not.

`Get your Public IP Address from Instance Page` and default user is `ubuntu` in Ubuntu VMs (otherwise `ec2-user`)

**Since on our College N/W, SSH port 22 is blocked. So we need to bypass this.**
### Change SSH Port of EC2 Instance
1. Login into VMs from 3rd Party example [Cloud9](https://c9.i0/)
2. Launch a Simple Environment on Cloud9
3. Open a Terminal from `Windows` Tab after opening your Environment on Cloud9
4. Upload aws key file on Cloud9.
5. `ssh -i /path/to/aws_key.pem ubuntu@YOUR-PUBLIC-IP`
6. After login open `sudo nano /etc/ssh/sshd_config` Change `port 22` to `port 443`
7. Restart SSH service `sudo service ssh restart`

### Allow AWS to Login on port 443
*Since AWS Blocks port other than 22 to outside Networks* To change we need to Change
our security groups. On AWS Instance Page click on Security Groups (left side).
1. Click on any listed `Security Groups` and click on `Inbound` rule Below.
2. Edit Default Rule, select `Custom TCP Rule` and `port 443` and Save it.
3. Goto to Instance Page Right-Click on Instance and click on Security Group Change and select the security groups
we currently modified.
4. Check it from Cloud9 Terminal `ssh -p 443 -i /path/to/aws_key.pem ubuntu@YOUR-PUBLIC-IP`

### Login from our College Network (On your local system)
We will use SSH through HTTP proxies. For this we are going to use [Corkscrew](http://agroman.net/corkscrew/)
Corkscrew is a tool for tunneling SSH through HTTP proxies.
1. Download Corkscrew [corkscrew-2.0.tar.gz](http://agroman.net/corkscrew/corkscrew-2.0.tar.gz)
```bash
cd Downloads
tar -zxf corkscrew-2.0.tar.gz
cd corkscrew-2.0
./configure
make
sudo make install
```
2. Edit `~/.ssh/config/` file add `ProxyCommand corkscrew 172.30.0.7 3128 %h %p`
3. Now login into EC2 Instance `ssh -i /path/to/aws_key.pem -p 443 ubuntu@YOUR-PUBLIC-IP`

### Contact
For any doubts or issues.
mail: rajmani1995@gmail.com
