# square of each element
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

# sort this tuple list, based on 2nd element in the tuple
plots = [(1, 1), (4, 3), (9, 9), (10, -1)]
plots.sort(key= lambda item: item[1], reverse=False)
print(plots)
