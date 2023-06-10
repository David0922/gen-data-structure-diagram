from dsdiagram import save_img


class Node:

  def __init__(self, id, next=None):
    self.id = id
    self.next = next


n = 5
nodes = [Node(id) for id in range(n)]
head = nodes[0]

for id in range(n):
  nodes[id].next = nodes[(id + 1) % n]

save_img(head, 'linked-list')
