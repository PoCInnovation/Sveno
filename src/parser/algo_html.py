import regex
import numpy as np
from regex.regex import Match
from reactTypes import *

REGEXP = {
    "html line": regex.compile(r'(return).*\<'),
    "html block": regex.compile(r'return.*\(\s*\<')
}

def get_car_pos(html_content, car):
    compt = 0

    for letter in html_content:
        if (letter == car):
            break
        compt = compt + 1
    return compt

def get_html_line(content, html_line):
    pos = html_line.span()
    html_content = content[pos[0] + 6:]
    car_pos = get_car_pos(html_content, '\n')
    html_content = html_content[:car_pos]
    print(html_content)
    print("\n\n")
    return html_content

def get_end_block(html_content):
    begin = [0, False]
    end = [0, False]
    pos = 0
    compt = 0

    for letter in html_content:
        if (letter == '(' and begin[1] == False):
            begin[0] = pos + 1
            begin[1] = True
            compt = compt + 1
        if (letter == ')'):
            compt = compt - 1
        if (compt == 0 and begin[1] == True and end[1] == False):
            end[0] = pos
            end[1] = True
        pos = pos + 1
    html_content = html_content[begin[0]:end[0]]
    return html_content



def get_html_block(content, html_block):
    pos = html_block.span()
    html_content = content[pos[0]:]
    car_pos = get_car_pos(html_content, '(')
    html_content = html_content[car_pos:]
    html_content = get_end_block(html_content)
    print(html_content)
    print("\n\n")
    return



def html_finder(content):
    html_line = REGEXP['html line'].search(content)
    html_block = REGEXP['html block'].search(content)

    if (html_line):
        return get_html_line(content, html_line)
    if (html_block):
        return get_html_block(content, html_block)
        
        
    # if (html_block):
    #     print("html block")
    #     print("\n\n")
    #     return
    
    # pos = html.span();
    # html_content = content[pos[0]:]

    # compt = 0
    # for letter in html_content:
    #     if (letter == '(' and compt != 0):
    #         compt += 1
    #     if (letter == ')'):
    #         compt -= 1
    # print(compt)
    # print(html_content)
    # print("\n\n")
    # return
