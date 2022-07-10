import pandoc
import os
from zipfile import ZipFile
import glob
import shutil

# Extract zip with Paligo HTML output
def unzip(zipfile):
    with ZipFile(zipfile, "r") as myzip:
        myzip.extractall(path="..")

# Make a list of all HTML files in output
def get_all_html_files():
    all_html_files = glob.glob(paligo_folder + "/**/*.html", recursive=True)
    
    return all_html_files

# Use Pandoc to convert HTML files to Markdown
def transform(html_files):
    for filename in html_files:
        markdown_filename = os.path.splitext(filename)[0]+".md"
        doc = pandoc.read(format="html", file=filename)
        pandoc.write(doc, format="markdown", file=markdown_filename)

# Delete the HTML files because we're done with them
def delete_html(html_files):
    for filename in html_files:
        os.remove(filename)

# Move subdirectories to root and delete parent folder and zip
def move_directory_and_cleanup():
    source = paligo_folder + "/out/"
    destination = ".."
    shutil.copytree(source, destination, dirs_exist_ok = True)    
    shutil.rmtree(paligo_folder)
    os.remove(zipfile)

# Variables
paligo_folder = "../317-Snyk_User_Docs-html"
zipfile = paligo_folder + ".zip"

# Unzip HTML, convert to Markdown, move to root, delete unneeded files
def main():
    unzip(zipfile)
    all_html_files = get_all_html_files()
    transform(all_html_files)
    delete_html(all_html_files)
    move_directory_and_cleanup()

if __name__ == '__main__':
   main()
