from lettuce import *
#from lettuce.django import django_url

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Given I navigate to "(.*)"')
def navigate_to_url(step, url):
    full_url = django_url(url)
    world.browser.get(full_url)
