#!/usr/bin/env python

import web
render = web.template.render('.')

urls = (
  '/', 'index',
  '/payoff', 'payoff'
)

app = web.application(urls, globals())

class index:
  def GET(self):
    return render.index()

class payoff:
  def GET(self):
    data = web.input()

    return render.payoff(data)

if __name__ == "__main__": app.run()


