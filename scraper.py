import xml.etree.ElementTree as ET

class invCard:
  def __init__(self):
    1 == 1

cardList = []

tree = ET.parse('cards.xml')
root = tree.getroot()
print root.tag
for subtree in root:
  if subtree.tag == "cards":
    for child in subtree:
      print child.find('name').text, child.find('type').text
      if "Land" not in child.find('type').text:
        if "Artifact" not in child.find('type').text:
          if "Scheme" not in child.find('type').text:
            print "Color",child.find('color').text

for line in open('inventory.csv'):
  
  split = line.split(',')
  #print "Count",split[0]
  #print "Name",split[1]


