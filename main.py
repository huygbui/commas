from fasthtml.common import *

app, rt = fast_app(pico=False)


@rt('/')
def get():
    return Titled('Hello')


serve()