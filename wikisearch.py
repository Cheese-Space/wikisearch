import argparse
import webbrowser
import sys
parser = argparse.ArgumentParser(description="search for a wikipedia page")
lang = parser.add_mutually_exclusive_group()
lang.add_argument('--Dutch', help="sets language to Dutch", action="store_true")
lang.add_argument("--Spanish", help="sets language to Spanish", action="store_true")
lang.add_argument("--Italian", help="sets language to Italian", action="store_true")
parser.add_argument("--article", action="append", help="specify the article", required=True)
args = parser.parse_args()
if len(args.article) > 1:
    print("error: you can't specify multiple articles!")
    sys.exit(1)
article = args.article[0]
if args.Dutch:
    lang = "nl"
elif args.Spanish:
    lang = "es"
elif args.Italian:
    lang = "it"
else:
    lang = "en"
webbrowser.open(f"https://{lang}.wikipedia.org/wiki/{article}")
