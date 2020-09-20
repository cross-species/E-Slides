import os

def callMindMap(input, output, fileCat="html", path = "D:\\E-Slides\\static\\data\\"):
    # order1 =  "cd " + path
    order2 = "markmap -o \"" + path + output + \
        "." + fileCat + "\" --enable-mathjax --enable-prism --no-open " + path + input + ".md"
    # os.system(order1)
    os.system(order2)
    return output


def startJupyter(path = "D:\\E-Slides\\static\\data\\"):
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
    order = "pandoc D:/E-Slides/static/data/" + input + ".md -o D:/E-Slides/static/data/" + output + "." + file_type + " -t " + style + " -s"
    # order = "pandoc "+input+".md -o "+output+".html -t slidy -s"
    os.system(order)
    return output

def save_md(content, input_name='example'):
    '''Save markdown into a file
    input:
        content
        input_name - The file where we wanna save the context
    Output:
        input_name
    '''
    md_name = input_name # TODO:file_name is extracted from DB
    with open("D:/E-Slides/static/data/" + md_name + ".md", "w") as f:
        f.write(content)
        f.close()
    return input_name

