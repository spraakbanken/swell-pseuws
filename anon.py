#! /usr/bin/env python

import json
from urllib.parse import parse_qs
from LR_project.src import source


def app(env, start_response):
    # Query string parameters.
    q = parse_qs(env['QUERY_STRING'])
    qd = dict((k, q.get(k)[0]) for k in q)

    # POST data parameters.
    p = parse_qs(env['wsgi.input'].read(int(env.get('CONTENT_LENGTH', 0))).decode())
    pd = dict((k, p.get(k)[0]) for k in p)

    # Combined (POST takes precedence).
    cd = qd.copy()
    cd.update(pd)

    if 'text' in cd:
        out = json.dumps(source.identify(cd['text']))
        body = [out, '']
    else:
        body = open('README.md', encoding="utf-8").readlines()

    status = '200 OK'
    response_headers = [
        ('Access-Control-Allow-Origin', '*'),
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(sum(len(s) for s in body))),
    ]
    start_response(status, response_headers)
    return (s.encode() for s in body)

