import os
import time

def callMindMap(input, output, fileCat="html", path = os.path.dirname(os.path.abspath(__file__)) + "/static/data/"):
    # order1 =  "cd " + path
    order2 = "markmap -o \"" + path + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + path + input + ".md"
    # os.system(order1)
    os.system(order2)
    return output


def startJupyter(path = os.path.dirname(os.path.abspath(__file__)) + "/static/data/"):
    order1 = "cd " + path
    order2 = "jupyter notebook"
    status = False
    if(not status):
        os.system(order1)
        os.system(order2)
        status = True
    return status

def callSlides(input, output, file_type='html', style='slidy'):
    '''Convert markdown into html / pdf.
    Input:
        input - input file's name
        output - output file's name
        file_type - output file type ('html' / 'pdf')
        style - output file's style
    '''
    if style == 'slidy':
        order = "pandoc " + os.path.dirname(os.path.abspath(__file__)) + "/static/data/" + input + ".md -o " + os.path.dirname(os.path.abspath(__file__)) + "/static/data/" + output + "." + file_type + " -t " + style + " -s"
    if style == 'beamer':
        order = "pandoc " + os.path.dirname(os.path.abspath(__file__)) + "/static/data/" + input + ".md -s -t s5 -V s5-url=https://cdn.docbook.org/release/xsl-nons/current/slides/s5/ui/default/ -o " + os.path.dirname(os.path.abspath(__file__)) + "/static/data/" + output + "." + file_type
    # order = "pandoc "+input+".md -o "+output+".html -t slidy -s"
    os.system(order)
    return output

def save_md(content, input_name='example'):
    '''Save markdown into a file
    input:
        content
        input_name - The file where we wanna save the context
    Output:
        { input_name }_{ current time } - e.g: example_1600621720.606119
    '''
    md_name = input_name + '_' + str(time.time()) # TODO:file_name is extracted from DB
    with open(os.path.dirname(os.path.abspath(__file__)) + "/static/data/" + md_name + ".md", "w") as f:
        f.write(content)
        f.close()
    return md_name

