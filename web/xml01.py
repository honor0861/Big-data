from xml.etree.ElementTree import parse
doc= parse('C:\\Users\\admin\\Desktop\\py_projects\\web\\resources\\exam1.xml')

a = doc.findall("student")

for tmp in a:
    #print(tmp)
    print(tmp.findtext("name")) # <name>a</name>
    print(tmp.findtext("age")) # <age>12</age>
    print(tmp.find("addr").attrib) # <addr id ="a">addr1</addr id ="a">
        #{"id":"a"}

# http://ihongss.com/xml/exam1.xml