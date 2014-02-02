from lxml import etree
from store import db


def stackoverflowPosts(fName):
    tree = etree.parse(open(fName))
    for row in tree.xpath("/posts/row"):
        yield {'body': row.attrib['Body'],
               'id': row.attrib['Id']}


def insertIntoMySql(fName):
    cursor = db.cursor()
    cursor.execute("DELETE FROM posts")
    cursor.execute("DELETE FROM posts_ft")
    for post in stackoverflowPosts(fName):
        cursor.execute("INSERT INTO posts    VALUES (%s, %s)",
                       (post['id'], post['body']))
        cursor.execute("INSERT INTO posts_ft VALUES (%s, %s)",
                       (post['id'], post['body']))
