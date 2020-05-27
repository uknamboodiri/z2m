class SuperList(list):

    def __len__(self):

        count = super().__len__()
        return count


super_list1 = SuperList()
super_list1.append(5)
print(super_list1[0])
print(len(super_list1))
print(type(super_list1))

