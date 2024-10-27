# Server Monitoring Tool

This **Server Monitoring Tool** is designed to monitor file activities on a server, detecting unauthorized file modifications or suspicious uploads like webshells. The tool runs in real-time and monitors file creation, modification, deletion, and updates. It also uses **Yara** rules to detect potentially malicious files, such as webshells or unauthorized scripts.

## Features
- **Real-time file monitoring**: Monitors directories for new, modified, or deleted files.
- **Malicious file detection**: Uses Yara rules to scan and detect suspicious files such as webshells.
- **Configurable directories**: Customize the directories to monitor by updating the configuration file.
- **Log and alert system**: Logs all file activities and alerts on suspicious file detections.

## ## Installation

1. Clone the repository:
```bash
   git clone https://github.com/lamcodeofpwnosec/server-monitoring.git
   cd server-monitoring
```
2. Install required dependencies:
```
sudo apt-get install python3 python3-pip libyara3 yara
pip install inotify-simple yara-python paramiko
```
3. Set up your directories to monitor by editing the `config.py` file in the `/src/` directory.
4. Start the file monitoring tool:
```
python3 src/monitor.py
```

## Usage
 * Modify `config.py` to include the directories you want to monitor.
 * Define your custom Yara rules in the `yara_rules/malicious_rules.yar` file.
 * Run `monitor.py` to start the monitoring process. It will scan all detected file changes and log potential threats.

   
> [!NOTE]
> Copyright [©lamcodeofpwnosec](https://github.com/lamcodeofpwnosec/)
