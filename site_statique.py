encoding = 'utf-8'

# importation des packages
import markdown2
import argparse
import os

# création et choix des dossiers sources
parser = argparse.ArgumentParser(usage="")
parser.add_argument("-i", "--input-directory", help = "dossier source (fichier .md)", default = './md')
parser.add_argument("-o", "--output-directory", help = "dossier final (fichier .html)", default = './html')
# parser.add_argument("-t", "--template-directory", help = "page web (fichier .html/.css)", default = './template')
args = parser.parse_args()

# code de conversion
md = os.listdir(args.input_directory)
for fichier in md:
    with open(args.input_directory + '/' + fichier, 'r+', encoding = 'utf-8') as md:
        HTML = markdown2.markdown(md.read())
        htmls = open(args.output_directory + '/' + fichier.replace(".md", ".html"), "w+", encoding="utf-8")
        htmls.write(HTML)