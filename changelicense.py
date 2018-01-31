import os
import sys

path=sys.argv[1]
license_to_replace="// Copyright (c) 2014-2017, The Monero Project"
license=           "// Copyright (c) 2014-2017, The Monero Project\n// Copyright (c) 2017-2018, The Monero Project\n"

counter=0

path_files_container=[]
for root, directories, filenames in os.walk(path):
        for filename in filenames:
                  path_files_container.append(os.path.join(root,filename))

for item in path_files_container:
        rstream=open(item,"r")
        source=rstream.read()
        if license_to_replace in source:
               counter+=1
               source=source.replace(license_to_replace,license)
               tmp_filename=item+".xxxxx"
               wstream=open(tmp_filename,"w")
               wstream.write(source)
               os.remove(item)
               filename=tmp_filename.replace(".xxxxx","")
               os.rename(tmp_filename,filename)

               

                  
            
