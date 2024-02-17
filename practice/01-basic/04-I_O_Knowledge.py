# f = open( “file_name”, “mode”)
# r : read mode
# w : write mode
# data = f.read( )
# f.close( )

'''
# Meaning of some popular Character
'r' => open for reading(default)
'w' => open for writing, truncating the file first
'x' => create a new file and open it for writing
'a' => open for writing, appending to the end of the file if it exists
'b' => binary mode
't' => text mode (default)
'+' => open a disk file for updating (reading and writing) 
'r+' => reding + overwriting (pointer in start) [no truncate]
'w+' => reding + overwriting (pointer in start) [truncate]
'a+' => reding + append (pointer in LAST) [no truncate]
'''

# data = f.readline( ) #reads one line at a time

# '''f = open( “demo.txt”, “w”)
# f.write( “this is a new line“ )
# #overwrites the entire file'''

# f = open( “demo.txt”, “a”)
# f.write( “this is a new line“ ) #adds to the file

# import os
# os.remove( filename ) #delete a file
