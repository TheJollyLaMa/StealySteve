# Socratica.(2021). XML & ElementTree. https://www.youtube.com/watch?v=j0xr0-IAqyk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=26
import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET Module
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name,"\n")

# this lesson is about the element and the element tree
#  XML is a tree of elements.  Each element is a node in the tree.
#  Nodes are the tags.

# Display functions in ET Module
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name,"\n")
# ET.fromstring(String)  --> converts from string to XML element
# ET.parse(File)         --> gives an element tree object from a file input
# ET.tostring(Element)   --> converts from XML element to string

tree = ET.parse('hodlers.xml')
root = tree.getroot()
print(ET.tostring(root))
# OUTPUT:
# b'<crypto coin="MONEY!!!">\n  <investor>John Mattaliano</investor>\n  <investor>Andres Aitsen</investor>\n  <investor>Rich Watts</investor>\n  <investor>Will Greeson</investor>\n  <investor>Pranay S. Yadav</investor>\n  <investor>Cody Roche</investor>\n  <investor>Max Summers</investor>\n  <investor>Andrus Kukk</investor>\n  <investor>Pogo</investor>\n  <investor>Tim Pinder</investor>\n  <investor>Jack Brett</investor>\n  <investor>Dennys Antunish</investor>\n  <investor>Eric Fitzgerald</investor>\n  <investor>Chris Warren</investor>\n</crypto>'
#  the 'b' indicates a byte string
# all child elements are returned with a call to getroot()
# whitespace is returned in keyseq

# Get an attribute by calling element.get('attribute') - returns the value of the attribute of the element
coin = root.get('coin')
print("\nCrypto name = {}\n".format(coin))

# Create and Set and attribute
root.set('launched', '20210101')
root.set('address', '0xq428thrlkjrnfavkyadayadayadafd385djd99osfm5szx')
print(root.attrib)

# Save updated XML to file
tree.write('hodlers.xml')

# Add 'id' attribute to each investor
id = 1
for investor in tree.findall('investor'):
    investor.set('id', str(id))
    id += 1

# Save updated XML to file
tree.write('hodlers.xml')

# Delete attribute
for investor in tree.findall('investor'):
    del(investor.attrib['id'])

# and write it
tree.write('hodlers.xml')

# Add investors two different ways
# investor1 = ET.fromstring("<investor>Allen Duffy</investor>")
# root.append(investor1)
#
# investor2 = ET.Element("investor")
# investor2.text = "Karl Amber"
# root.append(investor2)
#
# investor3 = ET.Element("investor")
# investor3.text = "Jolly LaMa"
# root.append(investor3)

# Add ids again
id = 1
for (id, investor) in enumerate(root.findall('investor')):
    investor.set('id', str(id))

# Save it
tree.write('hodlers.xml')

# Demonstrate selecting a node (element) by path
investor = root.find(".//investor[@id='4']")
print(investor.text)
