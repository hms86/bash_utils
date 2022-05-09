# shell_utils


## rm
Use this script to move files in a Recycle bin instead of directly deleting them. A schedule task is also created to delete the file in a later time. The script only handles the original `rm` options `-f` `-r` and `-i`. If the user gives any of the rest `rm` options, then the script passes all inputs into the original binary and does nothing else.
