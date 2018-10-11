# Server Monitoring Script

[![GitHub license](https://img.shields.io/github/license/mfappsandweb/Server-Monitoring-Script.svg)](https://github.com/mfappsandweb/Server-Monitoring-Script/blob/master/LICENSE.md) [![Build Status](https://travis-ci.com/mfappsandweb/Server-Monitoring-Script.svg?branch=master)](https://travis-ci.com/mfappsandweb/Server-Monitoring-Script)
[![Code Coverage](https://codecov.io/gh/mfappsandweb/Server-Monitoring-Script/branch/master/graphs/badge.svg)](https://codecov.io/gh/mfappsandweb/Server-Monitoring-Script) ![GitHub Size](https://img.shields.io/github/repo-size/mfappsandweb/Server-Monitoring-Script.svg)

## Purpose

The Python script is designed to be run as a cronjob on every boot to run in the background.
The script will gather information:

- CPU
- Memory
- Network
- Hard Drives
- System OS
- Current UTC Timestamp

The script will produce a JSON output at 5 second intervals for use with any software or server accepting a JSON input.
Example:

```json
{
    "hostname": "HOME-LAPTOP1",
    "system": {
        "name": "Windows",
        "version": "10"
    },
    "cpu_count": 4,
    "cpu_usage": 17.9,
    "memory_total": 8440942592,
    "memory_used": 6244225024,
    "memory_used_percent": 74.0,
    "drives": [
        {
            "name": "C:\\",
            "mount_point": "C:\\",
            "type": "NTFS",
            "total_size": 536224985088,
            "used_size": 167306108928,
            "percent_used": 31.2
        },
        {
            "name": "D:\\",
            "mount_point": "D:\\",
            "type": "NTFS",
            "total_size": 463332921344,
            "used_size": 49498419200,
            "percent_used": 10.7
        }
    ],
    "network_up": 54,
    "network_down": 4150,
    "timestamp" : "2018-10-10 01:41:21"
}
```

The script includes a function to send JSON to a remote server.

This script can be installed on several machines that report to a central monitoring server.

## Usage

Clone the script with `git clone`.

Install Python.

If any library is missing do `pip install` *library*.

To test the script output run with `python3 monitor.py`.

### Linux Autostart

Create a cron job to run the script on every boot.

Edit cron with `crontab -e`.

Add the script at the bottom of the cron list as `@reboot python3 /path/to/script/monitor.py &`.

### Windows Autostart

`Windows/monitor.bat` and `Windows/monitor.vbs` scripts are included.

`monitor.bat` will call python to launch `monitor.py`.

`monitor.vbs` silently calls `monitor.bat` to run in the background.

To create an autostart for Windows open the startup folder with keyboard `Windows + R`, enter `shell:startup` and create a shortcut here to `monitor.vbs`. 

This will run the script in the background on every boot.

## Author

MF Softworks <mf@nygmarosebeauty.com>

mf.nygmarosebeauty.com