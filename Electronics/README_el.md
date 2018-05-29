This folder is the next step toward working with electronic devices.
In particulary, in the explanation there will be usage of QCoDes: https://github.com/QCoDeS/Qcodes

Assuming asv is installed in the cloned QCoDes folder, and using the QCoDes environment (qcodes), then firstly will the configuration file (asv.conf.json) look like this:
```
{
  "version": 1,
  "project": "qcodes",
  "project_url": "https://github.com/QCoDeS/Qcodes",
  "repo": ".",
  "show_commit_url": "https://github.com/QCoDeS/Qcodes/commit/",
  "branches": ["master"], 
  "environment_type": "conda"
}
```
Note that our example is using KEYSIGHT34465A.
Copy the file benchmark_el.py into the folder benchmarks.
Now type ```asv run```, and you'll notice the change in the KEYSIGHT34465A. In addition you will have a result for benchmarking the time of the functions time_keyEl.
