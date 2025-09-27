# Gancho takes websocket payload and perform actions

## Usage:

On github set websocket for the desired events,
recommended **Tag Creation**.

## Deployment on VM

#### Set dir and user

```bash
mkdir /opt/gancho
sudo useradd -r -s /usr/sbin/nologin -d /opt/gancho -M gancho

# This gives permission to manipulate /var/www, adjust for your needs
sudo chown -R gancho:www-data /opt/gancho
```




