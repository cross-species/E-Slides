import os

def callMindMap(input, output, fileCat="html", path = os.path.dirname(os.path.abspath(__file__)) + "/static/data/"):
    # order1 =  "cd " + path
    order2 = "markmap -o \"" + path + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + path + input + ".md"
    # os.system(order1)
    os.system(order2)


def startJupyter(path = os.path.dirname(os.path.abspath(__file__)) + "/static/data/"):
    order1 = "cd " + path
    order2 = "jupyter notebook"
    status = False
    if(not status):
        os.system(order1)
        os.system(order2)
        status = True
    return status

    
def callSlides(id, output):
    order = "pandoc "+id+".md -o "+output+".html -t slidy -s"
    os.system()

md_name = "example"
callMindMap(md_name, md_name)
