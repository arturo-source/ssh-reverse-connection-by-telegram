# SSH Reverse connection by telegram
This is my first contribution to the open source, it's a very simple script made in Python language.
I had one problem few days ago, it was that I cannot connect to my Raspberry Pi out from my home but I have access to external server with associated Domain Name. So I decided to make a SSH reverse conection, then I could do it.

## How to execute manually
You only have to execute as a python script:
```python ssh_conection.py```

## How to start the script working always
I could use a **for** statement so the telegram bot would be listening all the time, but the Raspberry Pi has low specifications and it's not necessary to be listening all the time, so you can init a cron job using ```crontab -e```. Then, you should add the following line:
```
# m h  dom mon dow   command
* * * * * python3 /path/to/script/ssh_connect.py
```
