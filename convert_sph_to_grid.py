# Written 18/8/16 by Duncan Forgan

# Simple script to wrap conversion of one SPH file type to ASCII grid
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
outputformat = 'gridascii'

# Do you want to interpolate everything to the grid?
interpolate_all = raw_input('Do you want to:\n1) interpolate everything to the grid, or \n2) Just density, (velocity, B-field if present)?\nEnter your choice:')
interpolate_command = 'to'

if(interpolate_all=='1'): 
    print 'Interpolating everything'
    interpolate_command = 'allto'
else:
    print 'Only interpolating density (plus v and B fields if present)'

onefile = raw_input('Do you want all the variables in one file? (y/n)')

if(onefile=='y' or onefile=='Y'):
    outputformat = 'gridascii2'

# construct command to run
command = exec_dict[inputtype] + ' '+interpolate_command +' '+outputformat+ ' '+inputfile

print command
print exec_dict
print 'Converting ',inputfile, ' to grid format'

if(onefile=='y' or onefile=='Y'):
    print 'The grid will be written to a single file'
else:
    print 'Each variable will be written to a separate file'
    
print 'Be patient! This may take some time'

p = sub.Popen([command],stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
output, errors = p.communicate()
print output

