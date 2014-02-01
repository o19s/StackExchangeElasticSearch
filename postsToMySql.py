from lxml import etree


def stackoverflowPosts(fName):
    tree = etree.parse(open(fName))
    for row in tree.xpath("/posts/row"):
        yield {'body': row.attrib['Body'],
               'id': row.attrib['Id']}


if __name__ == "__main__":
    from sys import argv
    for post in stackoverflowPosts(argv[1]):
        print repr(post)
