import requests
import tarfile
import os
import json


def download_pkg(pkg):
    url = "https://pypi.org/pypi/%s/json" % pkg
    meta_data = requests.get(url).json()
    link = meta_data['urls'][0]['url']
    pkg_name = link.split('/')[-1]
    zipped_pkg = requests.get(link)

    with open(pkg_name, 'wb') as f:
        f.write(zipped_pkg.content)

    return pkg_name


def unzip_pkg(pkg):
    t = tarfile.open(pkg)
    t.extractall()
    for i in os.listdir(pkg.replace('.tar.gz', '')):
        if not i.endswith('.py'):
            os.remove('%s/%s' % (pkg.replace('.tar.gz', ''), i))

    os.remove('%s/%s' % (pkg.replace('.tar.gz', ''), 'setup.py'))


def remove_trash(pkg):
    os.system('rm %s' % pkg)
    os.system('rm -rf %s' % pkg.replace('.tar.gz', ''))


if __name__ == '__main__':
    # pkg_name = download_pkg('emp-ext')
    # unzip_pkg(pkg_name)
    pkg_name = 'emp-ext-1.13.tar.gz'
    remove_trash(pkg_name)
