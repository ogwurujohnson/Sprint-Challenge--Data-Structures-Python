class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # store the item in a buffer at using self.current as the index
    self.storage[self.current] = item

    # in deciding what self.current should be, we need to make sure haven't exceeded the capacity of our buffer,
    # if we do, we reset reset current to 0, so we overwrite the first element and continue down
    if self.current == self.capacity - 1:
      self.current = 0
    self.current += 1

  def get(self):
    pass