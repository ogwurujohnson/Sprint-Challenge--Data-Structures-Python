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
    else:
      self.current += 1

  # The get method returns all of the elements in the buffer in a list in their given order.
  # It should not return any None values in the list even if they are present in the ring buffer.
  def get(self):
    return [i for i in self.storage if i is not None]