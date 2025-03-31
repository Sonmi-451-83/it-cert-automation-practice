#!/usr/bin/env python3

import os
import requests


def processfiles(dir):

    files = os.listdir(dir)
    feedbacks = []

    for filename in files:
        if filename.endswith('.txt'):
            with open(os.path.join(dir, filename), "r") as file:

                lines = file.readlines()
                if len(lines) == 4:
                    feedbacks.append({"title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3]})
    
    return feedbacks



def post_feedbacks(fb, url):

    for feed in fb:
        response = requests.post(url, json=feed)
        print(response.status_code)



if __name__ == "__main__":
    directory = "/data/feedback"
    url = "http://34.148.250.90/feedback/"
    feedbacks = processfiles(directory)
    post_feedbacks(feedbacks, url)
