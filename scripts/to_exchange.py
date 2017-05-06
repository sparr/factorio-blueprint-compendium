#!/usr/bin/env python3

import os
import sys
import json

from python_factorio.blueprints import *

# accept input from command line parameter(s) or stdin
if len(sys.argv) == 1:
  input = sys.stdin.read()
else:
  input = "".join(sys.argv[1:])

if os.path.isfile(input): # filename
    if input[-5:]==".json":
        blob = EncodedBlob.from_json_file(input)
    else:
        blob = EncodedBlob.from_exchange_file(input)
else:
    if input[0] == "{": # JSON
        blob = EncodedBlob.from_json_string(input)
    else:
        blob = EncodedBlob.from_exchange_string(input)

if blob.data_type == "blueprint":
    blob.__class__ = Blueprint
    blob.replace_entity_numbers()
elif blob.data_type == "blueprint_book":
    blob.__class__ = BlueprintBook
    blob.replace_indexes()
else:
    raise TypeError

print(blob.to_exchange_string())