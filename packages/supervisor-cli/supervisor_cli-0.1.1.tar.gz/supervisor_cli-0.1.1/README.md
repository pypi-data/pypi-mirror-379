# 📦 Supervisor CLI

**Supervisor CLI** (`supercli`) is a lightweight, user-friendly command-line tool for managing [Supervisor](http://supervisord.org/) processes.  
It provides both an **interactive dashboard** and **scriptable commands**, so you can quickly check, start, stop, or restart services without remembering long `supervisorctl` commands.

---

## ✨ Features
- 🔹 **Interactive Mode**: Browse services, view status, and manage them from a simple menu.  
- 🔹 **Scripted Mode**: Use flags for automation, scripting, or CI/CD pipelines.  
- 🔹 **Supervisor Wrapper**: Friendly interface around `supervisorctl`.  
- 🔹 **Logs Support**: Tail logs of any service directly from the CLI.  

---

## 🚀 Usage

### Interactive Mode
```bash
supercli

Supervisor Services
========================================
1) webapp              RUNNING
2) celery_worker       STOPPED
3) redis               RUNNING
0) Exit

### Scripted Mode

Run direct commands without entering the menu:

# List services
supercli --list

# Restart a service
supercli --restart webapp

# Start a service
supercli --start celery_worker

# Stop a service
supercli --stop redis

# Tail logs
supercli --logs webapp


###🛠️ Installation
pip install supervisor-cli
