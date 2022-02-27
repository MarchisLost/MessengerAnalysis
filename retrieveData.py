import json
import os
import re
from dotenv import load_dotenv

load_dotenv()
DATAPATH = os.getenv('DATAPATH')


def retrieveData():
    # Gets all the files names ended in json, then gets just the number on the file name into a sorted list
    files = [pos_json for pos_json in os.listdir(DATAPATH) if pos_json.endswith('.json')]
    fileNumber = {}
    for name in files:
        fileNumber[name] = int([re.findall(r'(\w+?)(\d+)', name)[0]][0][1])

    # Searches all the files found above and loads the data from them
    jsonData = {}
    for js in files:
        with open(os.path.join(DATAPATH, js)) as json_file:
            jsonData[fileNumber[js]] = json.load(json_file)['messages']
    return jsonData, files
