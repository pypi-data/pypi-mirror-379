# NetBox Account Management

[Netbox](https://github.com/adestis/netbox-account-management) plugin for managing the ownership of accounts.

## Features

This plugin provide following Models:

* Systems
* Login Credentials
* SSH Keys

## Compatibility

|              |       |
| ------------ | ----- |
| NetBox 4.2.x | 1.9.x |

## Installation

The plugin is available as a Python package in pypi and can be installed with pip  

```bash
pip install adestis-netbox-plugin-account-management
```

Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:

```python
PLUGINS = ['adestis_netbox_plugin_account_management']
```

Restart NetBox and add `adestis-netbox-plugin-account-management` to your local_requirements.txt

See [NetBox Documentation](https://docs.netbox.dev/en/stable/plugins/#installing-plugins) for details

## Configuration

The following options are available:

* `top_level_menu`: Bool (default False) Enable top level section navigation menu for the plugin.

## Screenshots

![Systems](docs/img/systems.png)

![SSH Keys](docs/img/ssh_keys.png)

![Login Credentials](docs/img/login_credentials.png)

![Login Credentials - SSH Key](docs/img/login_credentials_ssh_key.png)
