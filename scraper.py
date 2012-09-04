import xml.etree.ElementTree as ET

class invCard:
  pass

cardList = []

tree = ET.parse('cards.xml')
root = tree.getroot()
print root.tag
for subtree in root:
  if subtree.tag == "cards":
    i = 1
    for child in subtree:
      card = invCard()
      i += 1
      card.name = child.find('name').text
      card.type = child.find('type').text
      card.text = child.find('text').text
      try:
        card.cost = child.find('manacost').text
      except:
        card.cost = ""

      try:
        card.color = child.find('color').text
      except:
        card.color = "Colorless"

      try:
        card.pt = child.find('pt').text
      except:
        card.pt = ""

      print card.name
      print card.type
      print card.cost
      print card.color
      print card.text
      print card.pt
      print ""
      print ""
for line in open('inventory.csv'):
  
  split = line.split(',')
  #print "Count",split[0]
  #print "Name",split[1]


