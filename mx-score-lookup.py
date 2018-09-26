#!/usr/bin/env python
import requests
import sys

ip_addr = sys.argv[1]

sess = requests.session()
r = sess.get('https://talosintelligence.com/sb_api/query_lookup',
            headers = {'referer' : 'https://talosintelligence.com/reputation_center/lookup?search=%s' % ip_addr},
            params = {'query' : '/api/v2/details/ip/', 'query_entry' : ip_addr}
            )
if r.status_code == 200 or r.status_code == 201:
    data = r.json()
    score = data['email_score_name']
    print(score)