from PIL import Image

import os
import sys
import shutil

num_key_frames = 8
parent_dir = "C:/Users/user/Desktop/ai/hatchy training/Gif Spliter/"

cwd = os.getcwd()
pwd = os.getcwd() 

pwdstring = str(pwd)


#print(cwd)


#print("Current working directory: {0}".format(cwd))

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".gif"):
             #print(os.path.join(root, file))
             #print(file)
             #filename = file
             
             orginal_name = file
             prefix = orginal_name.rsplit('.')[0]
             fileout = prefix + '_Split'
             
             #print(fileout)
             
             directory = fileout
             path = os.path.join(cwd, directory)
             os.mkdir(path)
             #print(file)
            # shutil.move((pwd + file), (fileout + file))
             #dst_path = pwd + \ + fileout
             #print(dst_path)
             
             filestring = str(file)
             targetstring = str(fileout)
             
             original = pwdstring + "\\" + filestring
             print(original)
             target = pwdstring + "\\" + targetstring + "\\" + filestring
             print(target)

             shutil.copyfile(original, target)
             
             os.chdir(fileout)
             
             with Image.open(file) as im:
                for i in range(num_key_frames):
                    im.seek(im.n_frames // num_key_frames * i)
                   
                    im.save('{}.png'.format(i))
             os.chdir(pwd)
