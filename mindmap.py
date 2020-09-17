import os

def callMindMap_once(id, output, fileCat="html"):
    
    order = "markmap -o \"D:\\E-Slides\\" + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + id + ".md"
    os.system(order)


output = "test_out"
fileCat = "txt"
id = "test"

callMindMap_once(id, output, fileCat)

