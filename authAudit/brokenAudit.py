import os
from datetime import datetime  
import json

OutputFile = "stage0_output.txt"
TEAMname = "AuthTeam"

def doStuff():
    print("hello welcome to the audit thing")

    users = ["user-100", "user-200", "user-300"]
    attempts = [
        ("user-100", True),
        ("user-200", False),
        ("user-100", False),
        ("user-999", True),
    ]

    header = "EVENTS FOR SYSTEM"
    print(header, TEAMname)
    print(header, TEAMname)

    ts = datetime.now()

    f = open(OutputFile, "w", encoding="utf-8")  

    for a in attempts:
        u = a[0]
        ok = a[1]

        outcome = "OK" if ok else "NOT_OK"

        line = "time=" + repr(ts) + " user=" + u + " result=" + outcome

        if ok == True:
            print("SUCCESS happened for", u)
        else:
            print("fail happened for", u)

        f.write(line)
        # f.write("\n")

    print("done. output file maybe created:", OutputFile)

doStuff()
