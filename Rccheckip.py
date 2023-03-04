import rc, sys

# to deal with the arguments

i=1
for argv in sys.argv:
    if argv=="-o":
        try:
            of_name=sys.argv[i+1]
        except:
            print("There is something wrong. See if you have pointed the name of the output file.")
            exit(1)
    else: # in this case it can only be the input file.
        if_name=sys.argv[i]
    i=i+1
# obviously, if multiple arguments exist, the final one would be used.

# to open files
i_file=open(if_name,'r')
o_file=open(of_name,'w')

# read from the input file and define the rc rule
input_all=i_file.read()
i_lines=input_all.splitlines()
cker=rc.compile("\d+:\d+:\d+:\d+")
print("Reading completed. Now dealing process has started.")

# check the 
for i_line in i_lines:
    IP=cker.check(i_line)
    if IP:
        o_file.write(IP)
        num=num+1
        
print("All works done. ",num,"results in total.")