# Purpose

An attempt to reproduce scenario where Uvicorn hot reloading gets stuck.

# Installation

```sh
git clone https://github.com/desprit/uvicorn_reload_test.git
cd uvicorn_reload_test
virtualenv --no-site-packages -p python3.8 venv
pip install -r requirements.txt
```

# Running

```sh
cd src
# Run webserver
uvicorn main:app --reload
```

# Reproducing error

1. Try to override any existing python file and make sure Uvicorn gets automatically restarted
2. Send request `curl 127.0.0.1:8000/ping`
3. Override any python file again to make sure Uvicorn gets reloaded successfully
4. Send request `curl 127.0.0.1:8000/run`
5. Override any python file again and see that Uvicorn is stuck with the following message:

```sh
WARNING:  Detected file change in 'runner.py'. Reloading...
```

6. Try `ctrl+c` to stop the server, shouldn't work
7. `ps aux` to locate the following process:

```sh
venv/bin/python3.8 -c from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=5, pipe_handle=7)
```

8. Kill it: `kill -9 PID`

Uvicorn is unstuck, `ctrl+c` will work now but reloading won't until restarted manually
