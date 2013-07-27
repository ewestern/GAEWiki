import webapp2
from gaewiki import handlers


application = webapp2.WSGIApplication(handlers.handlers)
