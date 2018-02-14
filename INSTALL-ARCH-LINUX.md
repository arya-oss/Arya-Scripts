## Install Arch Linux
1. Download Arch Linux Iso [Link](https://www.archlinux.org/download/)
2. Create Bootable Pen Drive With **Universal USB Installer** or **Rufus**
3. Plugin into Laptop and Boot
5. After this step you'll get root terminal `root@archiso ~ # `
6. Must have internet access, check ip address with `ip addr` command
7. Check internet with ping `ping -c 3 google.com`

## Step to install Arch

1. Check disk with `fdisk -l`
2. Create disks with **cfdisk** `cfdisk /dev/sda` and select partition type `dos` or `gpt`
3. Create three partitions - Bootable, Swap and Linux

| Device        | Boot     | Start  | End | Sectors | Size | Id | Type      |
| ------------- |:--------:| ------:| ---:| -------:| ----:| --:| ---------:|
| /dev/sda1     | *        | 2048   |  _  |    _    |  1G  | 83 | Linux     |
| /dev/sda2     |          |    _   |  _  |    _    |  4G  | 82 | Linux Swap|
| /dev/sda3     |          |    _   |  _  |    _    |  60G | 83 | Linux     |

4. Create `/dev/sda1` to filesystem of type `ext4` using command `mkfs.ext4 /dev/sda1`
5. Create `/dev/sda3` to filesystem of type `ext4` using command `mkfs.ext4 /dev/sda3`
6. Create `/dev/sda1` to filesystem of type `swap` using command `mkswap /dev/sda2`
7. Enable Swap `swapon /dev/sda2`
8. `mount /dev/sda3 /mnt`
9. Create Folders `mkdir /mnt/boot /mnt/var /mnt/home`
10. Mount Boot `mount /dev/sda1 /mnt/boot`
11. Install base and development packages `pacstrap /mnt base base-devel`
12. Update packages `pacman -Syu`
13. Install GRUB BIOS `pacstrap /mnt grub-bios`
14. `genfstab -p /mnt >> /mnt/etc/fstab`
15. `arch-chroot /mnt /bin/bash`
16. Add locale `nano /etc/locale.gen` uncomment `#en_US.UTF-8 UTF-8` and Save it
17. `local-gen` it will generate locales.
18. `echo LANG=en_US.UTF-8 > /etc/locale.conf`
19. `export LANG=en_US.UTF-8`
20. set local time and zone `rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime`
21. `hwclock --systohc --utc`
22. Add hostname `echo YOURPCNAME > /etc/hostname`
23. Enable DHCPCD `systemctl enable dhcpcd.service`
24. Install SSH `pacman -Sy openssh` and enable it `systemctl enable sshd.service`
25. Change root password `passwd`
26. Add user `useradd -m -g users -s /bin/bash <USERNAME>`
27. `grub-install /dev/sda`
28. `grub-mkconfig -o /boot/grub/grub.cfg`
29. `mkinitcpio -p linux`
30. `exit` twice, you'll get `root@archiso ~ #` prompt
31. Unmount mounted dirs `umount /mnt/boot` and `umount /mnt`
32. Restart and login again `reboot`
33. Install Xorg `pacman -Sy xorg xorg-xinit` install with default selections
34. Update and Install Sound Driver `pacman -Syu` and `pacman -S alsa-utils`
35. Install Gnome `pacman -S gnome` install with default selections.
36. Install fonts dejavu `pacman -S ttf-dejavu`
37. Enable GDM `systemctl enable gdm.service`
38. Options packages `pacman -S archlinux-wallpapers`, if on virtualbox `pacman -S virtualbox-guest-utils` with 2nd Option `systemctl enable vboxadd.service`
39. To use GDM to use Xorg for welcome screen, uncomment `#WaylandEnable=false` in `/etc/gdm/custom.conf`

40. Install Your Favourite packages `pacman -S firefox libreoffice`

## Note
#### While installing packages if you are getting less network speed then rerank mirrors.
1. backup current mirrors (root user) `cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bkp`
2. rank mirrors `rankmirrors -n 5 /etc/pacman.d/mirrorlist.bkp > /etc/pacman.d/mirrorlist`
3. update packages `pacman -Syuu`
