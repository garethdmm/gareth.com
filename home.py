import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def showPage(handler, page):
  template_file = open("template.html")
  template = template_file.read()
  template_file.close()

  f = open(page + '.html')
  content = f.read()
  f.close()

  page = template % (content)
  handler.response.out.write(page)

class HomeHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "index")

class ProjectsHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "projects")

class WorkHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "work")

class ContactHandler(webapp.RequestHandler):
  def get(self):
    showPage(self, "contact")

class ResumeHandler(webapp.RequestHandler):
  def get(self):
    f = open('resume.html')
    html = f.read()
    self.response.out.write(html)

applications = {
  'www.garethmacleod.com': webapp.WSGIApplication( [
    ('/', HomeHandler),
    ('/projects', ProjectsHandler),
    ('/work', WorkHandler),
    ('/contact', ContactHandler),
    ('/resume', ResumeHandler),
  ], debug=True),
  'resume.garethmacleod.com': webapp.WSGIApplication( [
    ('/', ResumeHandler),
  ], debug=True),
  'localhost:8080': webapp.WSGIApplication( [
    ('/', HomeHandler),
    ('/projects', ProjectsHandler),
    ('/work', WorkHandler),
    ('/contact', ContactHandler),
    ('/resume', ResumeHandler),
  ], debug=True),
}
  

def main():
  run_wsgi_app(applications[os.environ['HTTP_HOST']])

if __name__ == '__main__':
  main()
