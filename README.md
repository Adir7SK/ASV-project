# ASV-project 

Before started, make sure you are in a git repository and in an enviroment.
Benchmark suite intended to run with Airspeed-velocity:
http://asv.readthedocs.io/en/latest/
To run the benchmark, type:
```asv run```
in the command prompt.

Put everything in place - in Example.md (https://github.com/Adir7SK/ASV-project/blob/master/Example.md) follow only step 1 and 2, for installing and adding all the proper files.

About benchmarking:

Each class and function have to have a particular name, depending on its perposes.
If you fx start the functions name with time, then it will be a time benchmarking. 
asv understands how to handle the prefix in either CamelCase or lowercase with underscores (fx def time_measure and def TimeMeasure).
See more in the following link: https://asv.readthedocs.io/en/latest/writing_benchmarks.html#benchmark-types

The default timeout for each function is 60s, which can be sometimes problematic.
In order to change it, you'll need to write in the class but not in a function; timeout = x, where x is a float variale, and is in seconds, i.e. timeout = 72.33 means that you've changed the timeout to be 72.33 seconds.

Creating a new class, with an existing class name in the following brackets, means (as in every python program) that the new class will inherit all the functions from the class in the brackets. It's also possible to add other functions. Short example:

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

Useful options for ```asv run``` is adding ```--show-stderr``` to see the results (if a function have outputs) and full explanation of errors/possible errors. Another one is adding ```--python=python``` if you don't want the program to reinstall everything every time you run it, so you won't need to wait to long. See more here: https://asv.readthedocs.io/en/latest/writing_benchmarks.html#running-benchmarks-during-development

In each benchmark you can measure a function from another place, by importing as in every python file.
The configuration file (asv.conf.json) should only have this code:
```
{
  "version": 1,
  "project": "project",
  "project_url": "https://github.com/Whichever_url",
  "repo": ".",
  "show_commit_url": "https://github.com/Same_url/commit/",
  "branches": ["master"], 
  "environment_type": "conda"
}
```
*Note that there have to be a setup file in the url.

After commiting your python files, write in the Bash: ```asv run``` then: ```asv publish```
And in order to see the graph, type: ```asv preview```, and then paste the http you get.
Sometimes problems with ```asv publish``` might accure. In this case you should check the hash of the commit in the error. If the hash isn't amoung those you get in the command ```git log```, but is in the results -> DESKTOP-53K0ASV file, then delete it from results -> DESKTOP-53K0ASV, and you are good to go.
If there's problems with ```asv preview``` then you'll probably have to change the port. Do that by typing ```asv preview --port 8081```, which will change the port to port number 8081, instead of the default, which is normally 8080.

In order to remove some commits from the graph before its running (asv run) and drawing, enter the file where you saved the benchmark project (but not the file named benchmarks) -> results -> DESKTOP-53K0ASV  then delete whichever commit you want (each commit will be assigned with its first 8 letters).

Working with environments:
If you want to work with special environment, you should have your asv project with a modified configuration file (asv.conf.json), in the project with all the modules you want to use(normally you'll have to change in the configuration file the "project_url" and "show_commit_url"). The reason for that is that asv builds, each time you run it, a new environment.
In the folder Benchmarks, you can add as many Python files as you want, and if you want the Airspeed Velocity (asv) program to measure them, you should start their names with "benchmark".
If performing a measurements on electronic devices, such as Keysight 34465A, in addition to defining connection under setup, you should also remember to have a teardown function.

*Precis measurements: Basically, in order to have the most accurate measurements, try to put as much as possible in the ```setup``` and ```teardown``` functions, and less in the functions you want to benchmark.You'll find a complete explanation for every type of function in here: https://asv.readthedocs.io/en/stable/writing_benchmarks.html#timing

If you have any problem not explained here, please message me on: adir7saly@gmail.com , or see if you can find an answer here (if not, create a new issue): https://github.com/airspeed-velocity/asv/issues

Files in this project:
1. Example.md - how to use asv step by step 
2. Used in Example.md: experimental.py and benchmarks1-4.
3. benchmark_el.py in Electronics folder - using asv on electronic devices.
