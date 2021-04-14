def get_mitte(l):
  '''Liefert Position und Wert des mittleren Elements von l.'''
  pos = len(l) // 2
  return pos, l[pos]

def test_get_mitte():
  l1 = [1,3,5]
  assert(get_mitte(l1) == (1,3))
  print("Alle get_mitte-Tests grün.")


def find(l, x):
  '''Rekursive binäre Suche nach x in l.
     Liefert die Position von x oder -1.'''

  # Fall 1: l ist leer
  # - Dann ist nichts zu tun,
  #   denn dann ist x auf keinen Fall in l enthalten.
  # - Also einfach -1 liefern
  if l == []:
    return -1

  # Fall 2: x steht in der Mitte von l.
  # - Dann liefern wir einfach die Position
  #   des mittleren Elements zurück.
  mpos, mvalue = get_mitte(l)
  if x == mvalue:
    return mpos

  # In Fall 1 und 2 sind wir fertig.
  # Und zwar, ohne dass noch viel getan werden muss.

  # Fall 3: x gehört nach links von der Mitte.
  # - linke Teilliste bestimmen und x darin suchen.
  # - Ergebnis der Rekursion zurückliefern.
  if x < mvalue:
    teilliste = l[:mpos]
    return find(teilliste,x)

  # Fall 4: x gehört nach rechts von der Mitte.
  # - rechte Teilliste bestimmen und x darin suchen.
  # - Ergebnis der Rekursion + Mitte + 1 liefern.

  teilliste = l[mpos+1:]
  ergebnis = find(teilliste,x)
  return -1 if ergebnis == -1 else ergebnis + mpos + 1
  #return find(l[:mpos], x) if x < l[mpos] else -1 if find(l[mpos+1:], x) == -1 else find(l[mpos+1:], x) + mpos + 1

def test_find():
  l1 = [3, 10, 15, 25, 42, 55, 66, 78, 103, 115, 125, 300]

  assert(find(l1,125) == 10)
  assert(find(l1,-10) == -1)
  assert(find(l1,400) == -1)
  assert(find(l1,30) == -1)
  assert(find(l1,42) == 4)
  assert(find(l1,3) == 0)
  assert(find(l1,300) == 11)
  assert(find([],300) == -1)
  print("Alle find-Tests grün.")

if __name__ == "__main__":
  test_find()
  test_get_mitte()