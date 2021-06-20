import requests
import os

save_path = f'{os.getcwd()}/download'
download_url = 'https://binaries.templates.cdn.office.net/support/templates/en-us/tf16402488_win32.dotx'

req = requests.get(download_url)

filename = req.url[download_url.rfind('/')+1:]
file_path = os.path.join(save_path, filename)

open(f'{file_path}', 'wb').write(req.content)

print(file_path)
