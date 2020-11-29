inp = input()
# print(inp.split())
# inp = ['dsafa', 'fsjasfj', 'wjke;lr;']
# inp = "adjfdk;afj;l jkalf;jdkl;f jksl;fjskl; f"
def concatenate(lst):
    result = "-".join(lst)
    print(result)
    return result
    # print(lst)

print(concatenate(inp.split()))