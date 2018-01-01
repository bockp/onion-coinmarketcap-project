# preliminary steps to make the project functional

1. install pip

```bash
opkg update
opkg install python-pip
```

2. install Coinmarketcap python wrapper using pip

```bash
pip install coinmarketcap
```

3. setup Onion:

* install Onion2 in onion Docker
* connect to onion using it's local wifi, and configure it to connect it to your wifi.
(see [Onion first time setup instructions](https://docs.onion.io/omega2-docs/first-time-setup-command-line.html) for instructions.)

* [install OLED display](https://docs.onion.io/omega2-docs/oled-expansion.html).
