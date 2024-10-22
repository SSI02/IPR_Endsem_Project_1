import urllib.request
import os
import tarfile

download = 1

def show_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    print(f"\rProgress: {percent}% ", end='')


if download == 1:
    if not os.path.exists('../2_data'):
        os.makedirs('../2_data')
    for i in range(3,17):
        url = 'https://zenodo.org/records/4004271/files/S{}.mat?download=1'.format(i)
        filename = '../2_data/S{}.mat'.format(i)
        print('Downloading {}...'.format(filename))
        urllib.request.urlretrieve(url, filename, show_progress)
        print()


print('Done.')
