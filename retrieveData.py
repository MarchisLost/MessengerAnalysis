import json
import os


def retrieveData():
    PATH = "E:\\Downloads\\facebook-davidmarch15\\messages\\inbox\\joanaribeiro_oszc0ittog"

    # TODO fix the bug of having several dicts inside and only reads the first
    # Gets all the files names ended in json
    files = [pos_json for pos_json in os.listdir(PATH) if pos_json.endswith('.json')]

    # Searches all the files found above and loads the data from them
    jsonData = {}
    for i, js in enumerate(files):
        with open(os.path.join(PATH, js)) as json_file:
            jsonData[files[i]] = json.load(json_file)['messages']

    return jsonData
