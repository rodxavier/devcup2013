from django.conf.urls.defaults import url
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse

class ReturnBuilder:
    def __init__(self, prefix):
        self.prefix = prefix

    def render_to_response(self,name,context,request):
        return_render = render_to_response("%s/%s.html" % (self.prefix,name), context, RequestContext(request))
        return_render["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
        return return_render

    def redirect_safe(self, target):
        return_redirect = redirect(target)
        return_redirect["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
        return return_redirect

    def redirect(self, target):
        return_redirect = redirect(self.prefix+"."+target)
        return_redirect["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
        return return_redirect

    def HttpResponse(self, string):
        return_response = HttpResponse(string)
        return_response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
        return return_response

class UrlBuilder:
    def __init__(self, prefix):
        self.prefix = prefix

    def html(self,name,*args):
        name = name + '.html'
        page = name
        target_name = self.prefix + '.' + name
        
        param_count = len(args)
        url_regex = r'^%s' % page
        for i in range(param_count):
            url_regex += r'(?P<%s>\w+)/' % args[i]            
        return (url_regex, direct_to_template, {'template': '%s/%s' % (self.prefix,name)})

    def template(self,name,*args):
        if name == 'index':
            page = ''
        else:
            page = name + '/'
        target_name = self.prefix + '.' + name
        
        param_count = len(args)
        url_regex = r'^%s' % page
        for i in range(param_count):
            url_regex += r'(?P<%s>\w+)/' % args[i]            
        return (url_regex, direct_to_template, {'template': '%s/%s.html' % (self.prefix,name)})

    def build(self,name,*args):
        if name == 'index':
            page = ''
        else:
            page = name + '/'
        target_name = self.prefix + '.' + name
        
        param_count = len(args)
        url_regex = r'^%s' % page
        for i in range(param_count):
            url_regex += r'(?P<%s>\w+)/' % args[i]            

        return url(url_regex+'$', name, name=target_name)
