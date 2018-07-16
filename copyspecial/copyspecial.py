#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
# copy_to(paths, dir) given a list of paths, copies those files into the given directory
# zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile

# +++your code here+++
# Write functions and modify main() to call them

## returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  special_paths = []
  filenames = os.listdir(dir)

  # pulls filenames xyz__hello__.txt from a dir and
  # prints their relative and absolute paths
  for filename in filenames:
    match = re.search(r'__(\w+)__', filename)
    if match:
      print os.path.join(dir, filename) # relative path
      print os.path.abspath(os.path.join(dir, filename)) # absolute path
      special_paths.append(os.path.abspath(os.path.join(dir, filename)))

  return special_paths

# given a list of paths, copies those files into the given directory
def copy_to(paths, todir):
  if not os.path.exists(todir):
    os.mkdir(todir)

  for path in paths:
    filename = os.path.basename(path)
    shutil.copy(path, os.path.join(todir, filename))

# given a list of paths, zip those files up into the given zipfile
def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print 'Excecuting command ' + cmd

  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  # +++your code here+++
  # Call your functions
  paths = []
  for dir in args:
    paths = get_special_paths(dir)

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print 'hello there'
  
if __name__ == "__main__":
  main()
