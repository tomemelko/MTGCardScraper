import xml.etree.ElementTree as ET

cardList = {}

tree = ET.parse('cards.xml')
root = tree.getroot()
print root.tag
for subtree in root:
  if subtree.tag == "cards":
    i = 1
    for child in subtree:
      i += 1
      name = child.find('name').text.lower()
      type = child.find('type').text

      try:
        text = child.find('text').text
      except:
        text = ""

      try:
        cost = child.find('manacost').text
      except:
        cost = ""

      try:
        color = child.find('color').text
      except:
        color = "Colorless"

      try:
        pt = child.find('pt').text
      except:
        pt = ""
      try:
        if "Land" in child.find('type').text:
          cardList[name] = [type]
        else:
          cardList[name] = [type, cost, color, text, pt]
      except TypeError:
        print name

f = open('updatedInventory.csv', 'w')
inv = open('inventory.csv')
inv.readline() #This eliminates the first line which contains the headers
for line in inv:
  split = line.split(',')
  count = split[0]
  name = split[1]
  if "Jor" in name:
    name = "Jor Kadeen, the Prevailer"
  try:
    f.write(count + "," + name + ',' + ','.join(cardList[name.lower()]) + "\n")
  except UnicodeEncodeError:
    print "Unicode error",name
  except TypeError:
    print "Type error",name,cardList[name.lower()]

