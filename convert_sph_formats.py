# Written 18/8/16 by Duncan Forgan

# Simple script to wrap conversion of one SPH file type to another
# using SPLASH - see website for system requirements

# http://users.monash.edu.au/~dprice/splash/

# This script requires that SPLASH be fully installed locally
 
import subprocess as sub
from io_format import filetypes,ntypes,exec_dict

# Read in the input filename
inputfile = raw_input('What is the input SPH filename? ')

# Enter the format of the input file
for i in range(ntypes):
    print '(',i+1,') ', filetypes[i]

inputnumber = input('Select input file format: ')
inputtype = filetypes[inputnumber-1]

for i in range(len(filetypes)):
    if(i==inputnumber): 
        continue
    print '(',i+1,') ', filetypes[i]
    
outputnumber = input('Select output file format: ')
outputtype = filetypes[outputnumber-1]

# construct command to run
command = exec_dict[inputtype] + ' to '+outputtype+ ' '+inputfile

print command
print 'Converting ',inputfile, ' to ', outputtype, ' format'
print 'Be patient! This may take some time'

p = sub.Popen([command],stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
output, errors = p.communicate()
print output

