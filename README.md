# preliminary steps to make the project functional

1. setup Onion:

* install Onion2 in an onion Docker that accepts an Expansion.
* [install OLED display](https://docs.onion.io/omega2-docs/oled-expansion.html).
* connect to onion using it's local wifi, and configure it to connect it to your wifi.
(see [Onion first time setup instructions](https://docs.onion.io/omega2-docs/first-time-setup-command-line.html) for instructions.)


2. install pip on the onion Omega2+

```bash
opkg update
opkg install python-pip
```

2. install Coinmarketcap python wrapper using pip on the onion Omega2+:

```bash
pip install coinmarketcap
```

3. install python-light and pyOledExp libraries to use the OLED Expansion on the onion Omega2+:

```bash
opkg update
opkg install python-light pyOledExp
```





5. execute script on the Onion Omega2+:

```bash
python3 coinmarketcapMain.py
```

# additional project ideas:

* use Steem API to display voting power, exchange ratio Steem<->SBD
* Use data from altcoins according to [this tutorial]() to analyze altcoins and decide on investment possibilities.
* Create an "altcoin discoveror" function set that can search coinmarketcap for unknown coins with certain criteria.
