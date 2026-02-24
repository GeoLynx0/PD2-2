partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5t000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mn/win;100000;90",
"Recovery;/recovery;2000;98"
]
partitions = [str(e) for e in partitions]
for str1 in partitions:
    x = str1.split(";")[0]
    print(x)