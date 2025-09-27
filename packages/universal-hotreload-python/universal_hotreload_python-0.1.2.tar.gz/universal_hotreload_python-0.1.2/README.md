# HotReload

Ein einfaches HotReload-System für Python-Dateien / A simple HotReload system for Python files.

---

## Deutsch

HotReload erlaubt es, eine Python-Datei oder Funktion automatisch neu zu starten, sobald sich der Code ändert.  
Es prüft die Syntax der Datei vor dem Neustart und nutzt `multiprocessing` sowie `watchdog`.

### Installation
```bash
pip install universal-hotreload-python
```

### Nutzung

```bash
hotreload <file.py>
```

- `<file.py>`: Die Python-Datei, die überwacht und neu gestartet werden soll.

### Features

- Überwacht die angegebene Datei  
- Syntaxprüfung vor jedem Neustart  
- Cross-platform (Windows/Linux/macOS)
- CLI über `hotreload` Befehl

---

## English

HotReload allows you to automatically restart a Python file or function whenever the code changes.  
It checks the syntax before restarting and uses `multiprocessing` and `watchdog`.

### Installation

```bash
pip install hotreloading
```

### Usage

```bash
hotreload <file.py>
```

- `<file.py>`: The Python file to watch and automatically restart.

### Features

- Watches only the specified file  
- Syntax check before each restart  
- Cross-platform (Windows/Linux/macOS)  
- Logging with timestamp  
- CLI via `hotreload` command
