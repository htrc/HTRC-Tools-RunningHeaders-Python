from htrc.runningheaders import parse_page_structure
from htrc.tests import load_vol

if __name__ == '__main__':
    pages = parse_page_structure(load_vol("data/vol1", num_pages=10))

    for n, page in enumerate(pages):
        s = "\nPage {} (has_header: {}, has_body: {}, has_footer: {})".format(n, page.has_header, page.has_body, page.has_footer)
        print(s + "\n" + "-"*len(s))
        print("Header:\n{}".format(page.header if page.has_header else "N/A"))
        print("Body:\n{}".format(page.body if page.has_body else "N/A"))
        print("Footer:\n{}".format(page.footer if page.has_footer else "N/A"))
