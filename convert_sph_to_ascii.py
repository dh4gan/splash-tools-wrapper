# Written 18/8/16 by Duncan Forgan

# Simple script to wrap conversion of any SPH file type to ASCII
# using SPLASH - see website for system requirements

# http://users.monash.edu.au/~dprice/splash/

# This script requires that SPLASH be fully installed locally
 
import subprocess as sub
from io_format import filetypes, ntypes, exec_dict

# Read in the input filename
inputfile = raw_input('What is the input SPH filename? ')

# Enter the format of the input file
for i in range(ntypes):
    print '(',i+1,') ', filetypes[i]

inputnumber = input('Select input file format: ')
inputtype = filetypes[inputnumber-1]

# For now, output in ascii format only
outputformat = 'ascii'

# construct command to run
command = exec_dict[inputtype] + ' to '+outputformat+ ' '+inputfile

print 'Converting ',inputfile, ' to ', outputformat, ' format'
print 'Be patient! This may take some time'

p = sub.Popen([command],stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
output, errors = p.communicate()
print output

