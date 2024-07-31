from subprocess import call
from subprocess import Popen, PIPE
import sys

def system_cmd(command):
    process = Popen(args=command, stdout=PIPE, stderr=PIPE, shell=True)
    out, err = process.communicate()
    retcode = process.poll()
    return retcode, out.decode("utf-8"), err..decode("utf-8")

class Guard():

    def againsNone(self, var, force_exit = True):
        if var == None:
            print("Supplied variable is None !")
            if force_exit:
                sys.exit(-1)

    def againstEmpty(self, var, force_exit = True):
        if isinstance(var, list):
            var_type = "list"
        elif isinstance(var, dict):
            var_type = "dict"
        elif isinstance(var, set):
            var_type = "set"
        elif isinstance(var, tuple):
            var_type = "tuple"
        else:
            var_type = None

        if var_type:
            is_empty = len(var) == 0
            if is_empty:
                print("Supplied variable of type ",var_type," is empty !")
                if force_exit:
                    sys.exit(-1)