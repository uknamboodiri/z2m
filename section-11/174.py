from collections import Counter, OrderedDict, defaultdict

my_dict = defaultdict(lambda: 0, {
    "name": "unni",
    "age": 2,
    "place": "pune"
})

ordered_dict = OrderedDict()
ordered_dict["name"] = "unni"
ordered_dict["place"] = "pune"
ordered_dict["age"] = 2

sentence = "hello Iam in the process of learning data science"

print(ordered_dict)
print(my_dict["name"])

print(Counter(my_dict))
print(Counter(sentence))
