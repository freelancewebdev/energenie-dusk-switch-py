#Energenie Dusk Switch
#Introduction
[Energenie](https://energenie4u.co.uk/) provide the [Pi-mate addon board](https://energenie4u.co.uk/index.php/catalogue/product/ENER314) which allows Raspberry Pi owners to safely and easily control electrical devices without the need to hook up a relay to the GPIO pins of the Pi.

This is a simple script which turns a trained Energenie socket to the on position at dusk each day (to control a light for example) using the [Astral module](https://pypi.python.org/pypi/astral) for Python to calculate the time of dusk for a given location. 

# Usage
## Dependencies
You will need the following Python modules installed:

pytz
RPi.GPIO
Astral

#Setup
The script assumes that you have 'trained' your Energenie socket and also that you are using socket 1.  Please see the [Energenie Pi-Mate Documentation PDF](https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf) for details on doing this.

The script can be called from a cron job run at the earliest time for sunset in the year at your location.  In Dublin Ireland for example, this is 16:08 on December 21st.  

A sample crontab entry to achieve this would look like:

```
8 16 * * * sudo /home/pi/path/to/script/timer.py
```

You can create this entry using the following command on your Raspberry Pi command line:

```
crontab -e
```

You should also change the 'city' variable in the timer.py script to 
your closest city for correct calculation of dusk - see the Astral docs for further information about the location related dependencies of the script.

Cron should then call the script at the appropriate time (earliest possible sunset) and wait until dusk as determined by Astral before switching on the socket.

## Extras
The script switch.py allows you to switch on and off the socket.  

To switch on the socket call 

```
sudo python /path/to/script/switch.py 1
```

and to turn off the socket call

```
sudo python /path/to/script/switch.py 0
```