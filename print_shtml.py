from bs4 import BeautifulSoup
#hello
from rich.console import Console
from rich.rule import  Rule
from  rich.text import  Text

console = Console()

def is_bold(s):
    if s and 'b' in  s:
        return True
    return False

def parse_spans(c,text):
    for c1 in c.children:
        if c1.name == "span":
            s = c1.get("style")
            text.append(c1.text, style=s)
        else:
            text.append(c1.text)

def print_shtml(text):
    root = BeautifulSoup(text,'html.parser')
    for c in root.html.children:
        if c.name == "h" :
            s = c.get("style")
            if s is None:
                s ="bold red"
            console.print(c.text,style=s,justify="left")
        elif c.name =="p":
            text  = Text(justify="center")
            parse_spans(c,text)
            console.print("")
            console.print(text)
            console.print("")
        elif c.name == "ul":
            console.print("")
            for c1 in c.children:
                if c1.name == "li":
                    t = Text()
                    t.append("    *    ",style="red bold")
                    parse_spans(c1,t)
                    console.print(t)
            console.print("")
        elif c.name == "ol":
            index = 1
            console.print("")
            for c1 in c.children:
                if c1.name == "li":
                    t = Text()
                    t.append(f"    {index}    ", style="red bold")
                    parse_spans(c1,t)
                    console.print(t)
                    index +=1
            console.print("")
        elif c.name == "hr":
            console.print(Rule(characters="-"))

#print_shtml(open("shtml_sample.html").read())
