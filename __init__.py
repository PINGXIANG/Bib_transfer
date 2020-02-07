from Bib_transfer import article_operator as article

# Public usages for any kinds of citation
def find_author(line: str):
    author = line[:line.find("(")].strip()
    line = line.strip(author)

    return author, line

def find_year(line):
    year = line[line.find("("):line.find(")")].strip("()")
    line = line.strip("(" + year + "). ")

    return year, line

def find_title(line):
    mid_content = line[line.find(").") + 2:line.find("doi") - 2]
    title = mid_content[:mid_content.rfind(".")].strip()
    line = line.strip(title)

    return title, line

if __name__ == "__main__":
    with open("Books.txt", "r", newline="", encoding='utf-8-sig') as file:

        for line in file:
            author, line = find_author(line)
            year, line = find_year(line)
            title, line = find_title(line)

            journal, line = article.find_journal(line)
            volume, line = article.find_volume(line)

            doi, line = article.find_doi(line)

            new_file = open("BIB_Article.txt", "a", newline="")
            new_file.write("@Article{" + author[:author.find(",")] + year + "," + "\n" +
                           "  title={" + title + "}," + "\n" +
                           "  author={" + author + "}," + "\n" +
                           "  year={" + year + "}," + "\n" +
                           "  journal={" + journal + "}," + "\n" +
                           "  volume={" + volume + "}," + "\n" +
                           "  doi={" + doi + "}," + "\n" +
                           "}" + "\n"
                           )

            new_file.close()
    file.close()
