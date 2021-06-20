import requests
import os

save_path = '/Users/jose.souza/repos_personal/requests_python/download'
download_url = 'https://binaries.templates.cdn.office.net/support/templates/en-us/tf16402488_win32.dotx'

req = requests.get(download_url)

filename = req.url[download_url.rfind('/')+1:]
complete_path = os.path.join(save_path, filename)

open(f'{complete_path}', 'wb').write(req.content)

print(complete_path)
