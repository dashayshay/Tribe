from Linked_list import Node, LinkedList
from Blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  
  def hash(self, key):
    key = sum(key.encode())
    return key
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    payload = Node([key, value])
    list_at_array.insert(payload)
    
    for item in list_at_array:
      if key == item[0]:
        key = item[0]
    
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    payload = self.array[array_index]
    
    for item in list_at_index:
      if key == item[0]:
        return item[1]
      else:
        return None
    
    if payload[0] == self.key:
      return payload[1]
    if payload is None:
      return None
    
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
  
print(blossom.retrieve('daisy'))