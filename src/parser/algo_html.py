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
            return compt
        compt = compt + 1
    return -1

def get_html_line(content, html_line):
    pos = html_line.span()
    html_content = content[pos[0] + 6:]
    car_pos = get_car_pos(html_content, ';')
    if (car_pos == -1):
        car_pos = get_car_pos(html_content, '\n')
    if (car_pos == -1):
        car_pos = get_car_pos(html_content, '}')
    html_content = html_content[:car_pos]
    return html_content

def check_quote(letter, quoteCheck):
    if (letter == '"' and quoteCheck == False):
        quoteCheck = True
    elif (letter == '"' and quoteCheck == True):
        quoteCheck = False
    return letter, quoteCheck

def checkcurlBracket(letter, curlBracketCheck, checkExeption):
    if (letter == '{'):
        curlBracketCheck = curlBracketCheck + 1
    if (letter == '}'):
        curlBracketCheck = curlBracketCheck - 1
    if (curlBracketCheck <= 0):
        curlBracketCheck = 0
        checkExeption = False
    else:
        checkExeption = True
    return letter, curlBracketCheck, checkExeption

def get_end_block(html_content):
    begin = [0, False]
    end = [0, False]
    pos = 0
    compt = 0
    checkExeption = [False, False]
    curlBracketCheck = 0

    for letter in html_content:
        letter, checkExeption[0] = check_quote(letter, checkExeption[0])
        if (checkExeption[0] != True):
            letter, curlBracketCheck, checkExeption[1] = checkcurlBracket(letter, curlBracketCheck, checkExeption[1])
        if (checkExeption[0] == True or checkExeption[1] == True):
            pos = pos + 1
            continue
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
    return html_content



def html_finder(content):
    html_line = REGEXP['html line'].search(content)
    html_block = REGEXP['html block'].search(content)
    
    if (html_line):
        return get_html_line(content, html_line)
    if (html_block):
        return get_html_block(content, html_block)