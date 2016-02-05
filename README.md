# shell-scripts

# java.sh
### Use
```bash
sh java.sh email@address
```
or to set up as a cron
```bash
0 7 * * * /bin/bash /home/user/editme/java.sh email@address >/dev/null 2>&1
```
You can also edit the script to hard-code an email address in. You won't have to pass it in, then.
### Description
java.sh will check against java's website to see if there is a new version available. If there is, it will email you or someone you specify. Meant for use in an enterprise environment.

---

#remindme

##Dependencies
```Python```, ```PyMsgBox```, and ```Sox```

Install from scratch instructions:

$```pacman -S python sox python-pip```

$```sudo pip install pymsgbox```

##Syntax

```remindme``` | Time | Message | Format | Send To 
--- | --- | --- | --- | ---
 | 2:30pm | "Or AM, if you're a morning person" | | 
 | 14:30 | "Utilizes 24h | |
 | 1h | "Check your email" | email | your@email.com 
 | 10m | | |
 | 75s | | |
 | 1h10m4s | "H/M/S can be combined, S optional, M/S also works" | |
 | tomorrow | "Capitalization doesn't matter" | |
 | monday | | |
 | mon | "Any three letter weekday (tue, wed, etc)" | |

##Examples

```Mod```+```d``` to open dmenu (or open your launcher of choice), or open a command line and then:

```remindme 2:30PM "Bomgar AR-3QQ7XXX"```

```remindme 14:30 "Bomgar AR-3QQ7XXX"```

```remindme 10m "Drink your ovaltime"```

```remindme 1h "Did you forget to drink your ovaltine?"```

```remindme 1h50m "Scam kids with decoder rings"```

```remindme 1234s "5678"```

```remindme tomorrow "Breakfast at Tiffany's"```

```remindme friday "Turn down"```

To put this process into the background, end the command with ```&```

##Disclaimer
This is a work in progress. Currently it only functions for current day scheduled tasks. If you call it in a terminal, it'll lock it up until the process finishes unless you send it to background.
