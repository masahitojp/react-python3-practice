#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic()
jinja = SanicJinja2(app)

def test(a: str) -> int:
    b: int = a + " hoge"
    return b


@app.route('/')
async def index(request):
    return jinja.render('index.html', request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
