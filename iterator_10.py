    #using loop we can iterate value one by one but iterator means we need to iterate over all values in the collection and iterate over    all values in the collection that are not in the collection.
nums=[4,56,7,8]
print(nums[2])
for i in nums:
    print(i)
    # iter will conver the list to  iterator
it=iter(nums)
print(it)
# it will give the object value
print(it.__next__())
print(it.__next__())
# other way
print(next(it))
# it will presever the previous value
#next() will print the next   value in the iterator
# to create own iterator , object:
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
          val=self.num
          self.num += 1
          return val
        else:
            raise StopIteration
values=topten()
for i in values:
    print(i)
# print(values.__next__())
# print(values.__next__())