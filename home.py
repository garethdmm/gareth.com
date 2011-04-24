from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class HomeHandler(webapp.RequestHandler):
  def get(self):
    f = open('index.html')
    index = f.read()
    f.close()
    self.response.out.write(index)

appRoute = webapp.WSGIApplication( [
  ('/', HomeHandler)
], debug=True)

def main():
  run_wsgi_app(appRoute)

if __name__ == '__main__':
  main()
