# WIFI users scanner

#### How to run it?
* clone this repository

    ```git clone https://github.com/irezwi/wifi-users.git```
* install arp-scan

    ```sudo apt-get install arp-scan```
* complete persons dictionary in app.py script with your MAC addresses and names e.g.
    ```python
    persons = {
        'AA:BB:CC:DD:EE:FF': 'John Doe',
    }
    ```
* run app.py file with python3 e.g.

    ```python3 ~/username/wifi-users/app.py```
