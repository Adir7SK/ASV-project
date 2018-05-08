#Before starting, if any problem occures at any time, you'll presumeably find the answer in the README file.
*Firstly make sure you are in the file where you want the airspeed velocity.

Step 1: Install
Airspeed velocity is a standard Python package, and the latest version may be installed with ```pip install asv```. The project uses ```setuptools```, and can also be installed by cloning the repository and using: ```python setup.py install```.
For more information: https://asv.readthedocs.io/en/latest/installing.html

Step 2:
Type ```asv quickstart```. Now you have ```asv.conf.json``` file. In the README file, you can see what should be written there.
Now run it for the first time by typing ```asv run```. Afterwards type ```asv machine```, and just press Enter for all the arguments.

Step 3:
Let's try with our benchmarks files. Create a new Python file (dosn't matter where) called Experimental.py, and paste the code from the Experimental.py we have here (and obviously make sure that it runs).
In the file where you downloaded asv, go in to the the folder named benchmarks, and then open the Python file named benchmarks. Paste the code from benchmarks1.py we have here (and obviously make sure that it runs). *Note that you have to change there, the path to the place where Experimental.py located, up in sys.path.append('Insert the location of Experimental.py')

Step 4:
Type ```asv run```, see that you don't get any errors or failures. Then commit it to git (```git add benchmarks/benchmarks.py``` and ```git commit```).
Now type ```asv publish``` and then ```asv preview```. First time you'll do it, you'll get one point on each graph (since there's only 3 functions, not including setup, there will only be 3 graphs).

Step 5:
Open again benchmarks.py and copy into it benchmarks2.py, and go back to Step 4. Then do the same with benchmarks3.py and benchmarks4.py.
Now you should have 3 graphs that looks like this:
![capture1](https://user-images.githubusercontent.com/31063975/39300734-fe309e58-494c-11e8-9d15-98d1fbff51e7.PNG)

You can press on each graph in order to see its details. If you choose to open time_experimental (which is the only one we changed), it should look like this:
![capture](https://user-images.githubusercontent.com/31063975/39300791-2cdc2272-494d-11e8-811a-0b18411cdb8b.PNG)
