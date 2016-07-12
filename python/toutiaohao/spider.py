import requests
import json
import time
import sys
from random import randint

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

headers = {"User-agent":USER_AGENT}

TAG = ['funny']

now = int(time.time()*1000)

for tag in TAG:
    referer = "http://toutiao.com/%s/" % (tag)
    headers["referer"] = referer
    pages = randint(20, 30)
    behot = int(time.time())
    create = int(time.time())
    for i in xrange(pages):
        url = "http://toutiao.com/api/article/recent/?source=2&count=20&category=%s&max_behot_time=%d&utm_source=toutiao&offset=0&max_create_time=%d&_=%d" % (tag, behot, create, now)
        time.sleep(randint(3, 7))
        req = requests.get(url, headers = headers)
        data = json.loads(req.text)
        if data["message"] != "success":
            print "script be ban!"
            sys.exit(0)
            break
        if data["has_more"] == False:
            break
        behot = data["next"]["max_behot_time"]
        create = data["data"][-1]["create_time"]
        for d in data["data"]:
            try:
                print d["media_name"], d["media_url"], tag
            except Exception as e:
                pass

