from lxml import etree
import requests
import json


def createIndex():
    # The index API contains configuration for
    # 1. settings
    #      settings include custom analyzers
    # 2. mappings
    #      field types
    #
    # Must close index before updating settings
    # http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-update-settings.html
    resp = requests.put('http://localhost:9200/stackexchange')
    if resp.status_code != requests.codes.ok:
        print "ERROR: %s" % resp.status_code
    else:
        print resp.text


def createCustomAnalyzer():
    data = {
        "analysis": {
            "analyzer": {
                "html_text": {
                    "tokenizer": "standard",
                    "filter": ["standard", "lowercase", "stop", "snowball"],
                    "char_filter": ["html_strip"]
                }
            }
        }
    }
    resp = requests.put('http://localhost:9200/stackexchange/_settings',
                        data=json.dumps(data))
    if resp.status_code != requests.codes.ok:
        print "ERROR: %s" % resp.status_code
        print "ERROR: %s" % resp.text
    else:
        print resp.text


def createMappings():
    # Here "post" is a type within index stackexchange

    data = {
        "post": {
            "properties": {
                # Each type has different configuration
                # settings here, string is the most
                # important
                # mapping > types > core types
                "Body": {"type": "string",
                         "store": "yes",
                         "index_analyzer": "html_text"},
                "Id": {"type": "string",
                       "store": "yes"}
            }
        }
    }
    resp = requests.put('http://localhost:9200/stackexchange/post/_mapping',
                        data=json.dumps(data))
    if resp.status_code != requests.codes.created:
        print "ERROR: %s" % resp.status_code
        print "ERROR: %s" % resp.text
    else:
        print resp.text


def postDocument(element):
    postId = element.attrib['Id']
    doc = {"Body": element.attrib['Body'],
           "Id":  postId}
    resp = requests.put('http://localhost:9200/stackexchange/post/' + postId,
                        data=json.dumps(doc))
    if resp.status_code != requests.codes.ok:
        print "ERROR: %s" % resp.status_code
        print "ERROR: %s" % resp.text
    else:
        print resp.text


if __name__ == "__main__":
    from sys import argv
    tree = etree.parse(open(argv[1]))
    createIndex()
    requests.post('http://localhost:9200/stackexchange/_close')
    createCustomAnalyzer()
    createMappings()
    requests.post('http://localhost:9200/stackexchange/_open')
    for row in tree.xpath("/posts/row"):
        postDocument(row)
