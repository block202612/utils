import os
import sys

path=sys.argv[1]
license_to_replace="Copyright (c) 2017, edollar project"# (fork from Monero)"
license_line1=           "// Copyright (c) 2014-2017, The Monero Project\n"
license_line2=           "// Copyright (c) 2017-2018, The Monero Project\n"

counter=0

files_container=[]
for root, directories, filenames in os.walk(path):
        for filename in filenames:
                  files_container.append(os.path.join(root,filename))

for filename in files_container:
        rstream=open(filename,"r")
        lines=rstream.readlines()
        tmp_source_lines=[]
        flag=False 
        for line in lines:
             if license_to_replace in line:
                  flag=True
                  counter+=1
                  tmp_source_lines.append(license_line1)
                  tmp_source_lines.append(license_line2)
             else:
                  tmp_source_lines.append(line)
        if flag==True:
             tmp_filename=filename+".xxxxx"
             wstream=open(tmp_filename,"w")
             for line in tmp_source_lines:
                  newline=line#[:-1]
                  wstream.write("%s" % newline)
