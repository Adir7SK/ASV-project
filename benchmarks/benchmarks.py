# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import time
from timeit import default_timer as timer
import sys
#sys.path.append('/users/adir saly kaufmann/anaconda3/lib/site-packages/asv/template/ASV-project')
sys.path.append('/users/adir saly kaufmann/Desktop/BeginnerGit/ASV-project') #import Experimental as e
"""
Note: Functions and classes can only be called by particulary names
depending on their perpose, i.e. you want the benchmark to measure time, the
you'll start its name with time.
When running; the compiler go through all the non-functions(not def) first,
and if there's something to remember, as timeout, the last command
will be the timeout fx the code will use. Afterwards it will start with the
functions
"""
import Experimental as e

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
   
    timeout = 120.0     #Increases the timeout to 120 sec, instead of the default option - 60 sec.
    def setup(self):
        self.d = {}
        self.len = 50
        for x in range(self.len):
            self.d[x] = None

    #Measures the time to run through the list of keys
    def time_keys(self):
        for key in list(self.d.keys()):
            pass

    def time_experimental(self):
        e.wait()

    def mem_experimental(self):
        print (e.alphabetic_order("badc gefh"))
        #print (e.unique_chars("Adir"))
        print (e.longest_word("when you are going to some place and notice Somthing"))
"""
    #Letting a function to run slower than the default defines (Should work because we re-defined the timeout)
    #Prints also the time it takes, to make sure there is an agreement
    def time_more_than_default (self):
        start = timer()
        for key in self.d.keys():
            pass
        time.sleep(70)
        elapsed_time = timer() - start
        print (elapsed_time)

    #Measures the run time of a normal for loop
    def time_range(self):
        start = timer()
        for i in range(300000000):
            x=5
            y=x*2
        ell = timer() - start
        print (ell)
        d = self.d
        for key in list(range(self.len)):
            x = d[key]

    #A function that takes more than 120 sec to run, which means that it will fail and print:
    #asv: benchmark timed out (timeout 120.0s).
    def time_destind_to_fail(self):
        time.sleep(200)


class MemSuite:
    #Memory benchmarks, measures the memory
    def mem_list(self):
        return [0] * 256

    def peakmem_list(self):
        time.sleep(200)
        [0] * 165536


class TimeExperiment(TimeSuite):

    def time_range(self):
         time.sleep(10)
    def time_destind_to_fail(self):
        start = timer()
        for i in range(300000000):
            x=5
            y=x*2
        ell = timer() - start
        print (ell)
    def time_new(self):
        time.sleep(17.5)

     
        
    timeout = 120.0
"""
