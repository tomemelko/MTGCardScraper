import xml.etree.ElementTree as ET

class invCard:
  def __init__(self):
    1 == 1

tree = ET.parse('cards.xml')
root = tree.getroot()
print root.tag
for subtree in root:
  if subtree.tag == "cards":
    for child in subtree:
      print child.find('name').text, child.find('type').text

for line in open('inventory.csv'):
  print line[:line[:line.rfind(',')].rfind(',')]
