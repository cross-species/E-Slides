import os

def callMindMap(input, output, fileCat="html"):
    
    order = "markmap -o \"D:\\E-Slides\\static\\data\\" + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + input + ".md"
    os.system(order)

def startJupyter(path = "D:\\E-Slides\\static\\data\\"):
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



