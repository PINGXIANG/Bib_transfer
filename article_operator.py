def find_journal(line: str):
    journal = line[:line.find(",")]
    line = line.strip(journal+", ")

    return journal, line

def find_volume(line: str):
    volume = line[:line.find(".")]
    line = line.strip(volume + ". ")

    return volume, line

def find_doi(line:str):
    doi = line[line.find('doi') + 4:].strip()
    line = line.strip("doi: " + doi)

    return doi, line
