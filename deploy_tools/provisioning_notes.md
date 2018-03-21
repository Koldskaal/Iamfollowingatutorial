Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

* Generate nginx file
cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/live.denpizza.dk/g" \
    | sudo tee /etc/nginx/sites-available/live.denpizza.dk

* Creating a symlink
sudo ln -s /etc/nginx/sites-available/live.denpizza.dk \
    /etc/nginx/sites-enabled/live.denpizza.dk

* Same for gunicorn
cat ./deploy_tools/gunicorn-systemd.template.conf \
    | sed "s/DOMAIN/live.denpizza.dk/g" \
    | sudo tee /etc/systemd/system/gunicorn-live.denpizza.dk.service

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
