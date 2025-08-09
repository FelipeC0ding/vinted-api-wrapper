from vinted import vinted

proxy_settings  ={
    'username':'your_proxy_username',
    'password':'your_proxy_password',
    'host':'proxy_host',
    'port':'proxy_port'
}

proxy_url=f"https://{proxy_settings['username']}:{proxy_settings['password']}@{proxy_settings['host']}:{proxy_settings['port']}"
vinted = vinted(domain=".co.uk", pro
