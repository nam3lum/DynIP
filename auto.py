#!/usr/bin/python3
import requests as r
from requests.exceptions import Timeout
import time as t
import sys as s
from rich.console import Console
c = Console()
try:
        while True:
                f = open("iplist.txt", "a+")
                f.seek(0)
                cnt = f.read()
                cnt_l = cnt.split("\n")
                e = '[white], [red]'.join(cnt_l)
                with c.status("[bold white]IP list: [red]"+e):
                        t.sleep(5)

                try:
                        ip = r.get("http://ipinfo.io", timeout=5).json()["ip"]
                        if ip in cnt_l:
                                with c.status("[bold white]Your IP([red]" + ip + "[white]) is in list already!"):
                                        f.close()
                                        t.sleep(10)
                        else:
                                with c.status("[bold white]Your IP([green]" + ip + "[white]) is not in the list, appending!"):
                                        f.write(ip + "\n")
                                        f.seek(0)
                                        cnt_l = f.read().split("\n")
                                        f.close()
                                        t.sleep(10)
                except:
                        with c.status("[bold orange]Request timeout, sleeping for 10 seconds"):
                                t.sleep(10)
except KeyboardInterrupt:
        c.print("[purple]See you!")
        s.exit(0)
