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
