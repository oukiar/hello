# Monkey patch to ssl certificate verification error
try:
    import ssl
    from functools import wraps

    print(('APPLYING MONKEY PATCH TO FORCE SSL '
          'PROTOCOL V1 [SSL VERSION: {}]'.format(
        ssl.OPENSSL_VERSION)))

    def sslwrap(func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)
        return bar

    # This line below is to avoid error (detected in python-2.7.12 in linux platform):
    # URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>
    # NOTE: This error causes that the tvshow's poster not to be shown/download when trying to load with kivy loader
    ssl._create_default_https_context = ssl._create_unverified_context

    ssl.wrap_socket = sslwrap(ssl.wrap_socket)
except Exception as e:
    print(('ERROR ON MONKEY PATCH SSL PROTOCOL V1: {}'.format(e)))

from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget


#import urllib.request
#import requests

'''
query = "eminem"
page = 1

url = 'https://www.youtube.com/results?search_query=' + query + '&page=' + str(page)


r = requests.get(url)
print(dir(r))

print("XXXXXX" , r.content )
'''



class Hello(FloatLayout):
    pass

if __name__ == "__main__":
    from kivy.app import App
    
    class HelloApp(App):
        def build(self):
            return Hello()

    HelloApp().run()
