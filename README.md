# ASV-project

Benchmark suite intended to run with Airspeed-velocity:
http://asv.readthedocs.io/en/latest/
To run the benchmark, type:
asv run
in the command prompt.

About benchmarking:

Each class and function have to have a particular name, depending on its perposes.
If you fx start the benchmarks name with time, then the benchmark will measure the time. 
asv understands how to handle the prefix in either CamelCase or lowercase with underscores.
See more in the following link, under "Benchmark types": https://asv.readthedocs.io/en/latest/writing_benchmarks.html#writing-benchmarks

The default timeout for each function is 60s, which can be sometimes problematic.
In order to change it, you'll need to write in the class but not in a function; timeout = x, where x is a float variale, and is in seconds, i.e. timeout = 72.33 means that you've changed the timeout to be 72.33 seconds.

Creating a new class, with an existing class name in the following brackets, means that the new class wil inherit all the functions from the class in the brackets. It's also possible to add other functions. Short example:

```
class TimeSuit():
    def time_range(self):
        code...
    def time_upper(self):
        code...
class TimeNew(TimeSuit):
    def time_upper(self):
        code...
    def time_other(self):
        code...
```        
        
The result will be that it runs the function time_range twice normally (once through TimeSuit and once through TimeNew). The function time_upper will run ones with the code in TimeSuite class, and ones with the code in TimeNew. The function time_other will run just ones.

Files in this project:
1. Dummy_benchmarking.py
