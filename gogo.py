import requests
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import sys
import read_google_result
import read_web_page

console = Console()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def print_result(rows):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No", )
    table.add_column("Title", style="cyan", no_wrap=False)
    table.add_column("URL", style="cyan", no_wrap=False)
    num = 0
    for r in rows:
        table.add_row(str(num), r['txt'], r['dom'])
        num += 1
    console.print(table)


def start_search():
    option ='s'
    while True:
        if option == 's':
            search = Prompt.ask("enter text to search ",default="how to install linux")
            resp = requests.get(f"https://www.google.com/search?q={search}", headers=headers)
            res = read_google_result.read_result(resp.content)
            print_result(res)
            option = Prompt.ask(f"select [b]0 to {len(res)-1}[/b] or type [b]'s'[/b] to return to search or type [b]'e'[/b] to exit",default="e")
            continue
        elif option == 'e':
            break;
        else:
            index  = int(option)
            url = res[index]['a']
            #console.print(f"fetching information from {url}")
            #title = Text(res[index]['txt'],justify='center',style='bold red')
            text = read_web_page.read_page(url)
            #console.print(Panel(title))
            console.print(Panel(text,title=res[index]['txt'],subtitle=res[index]['a']))
            option = Prompt.ask(f"select [b]0 to {len(res)-1}[/b] or type [b]'s'[/b] to return to search or type [b]'e'[/b] to exit",default="e")
            continue

start_search()

