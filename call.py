import os

def callMindMap_once(id, output, fileCat="html"):
    
    order = "markmap -o \"D:\\E-Slides\\" + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + id + ".md"
    os.system(order)

def startJupyter():
    order1 = "cd D:\\E-Slides\\"
    order2 = "jupyter notebook"
    status = False
    if(not status):
        os.system(order1)
        os.system(order2)
        status = True
    return status

# def callJupyter(code):
    






output = "test_out"
fileCat = "txt"
id = "test"

callMindMap_once(id, output, fileCat)

