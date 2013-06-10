from jinja2 import Environment, FileSystemLoader
import os
import os.path

def gen():
    layout = os.path.dirname(__file__).join('layout')
    content = os.path.dirname(__file__).join('content')
    loader = FileSystemLoader([layout, content])
    env = Environment(loader=loader, trim_blocks=True)
    t = env.get_template('index.html')
    print t.render({})

if __name__ == '__main__':
    gen()