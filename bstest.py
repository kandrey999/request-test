from bs4 import BeautifulSoup


def get_html():
    with open("bs-test.html", "r") as f:
        return f.read()


def get_soup():
    contents = get_html()
    return BeautifulSoup(contents, 'lxml')


def main():
    root = soup.html
    #root_childs = [e.name for e in root.children]
    print(len(list(soup.recursiveChildGenerator())))


soup = get_soup()

if __name__ == '__main__':
    main()

