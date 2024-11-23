# text = set(["terminator", "Vaqif"])
# print(type(text))


# text2 = {"terminator", "Vaqif"}

# print(type(text2))
# print(type(text))


# text  = ["Murad","Vaqif","Aytac","GPT","Rza","Ayxan"]
# print(help(text))

# text2 = ("Murad","Vaqif","Aytac","GPT",["Texnolab","Online"],"Rza","Ayxan")
# print(dir(text2))
# text2[4].append("Sethub")
# result = text2
# print(result)

# a = ["12",34, "34",("Murad")]
# print(type(a[3]))
# print(a[3].index)

# demo = tuple("necesen")
# print(demo)

# print(text.__sizeof__()  ," - List")
# print(text2.__sizeof__() ," - Tuple")





# t = ["Rza","Murad","Vaqif","Aytac","Ayxan","GPT","Abdulla"]
# q = [qw for qw in t if 'a' in qw]
# print(q)



# for x in adlar:
#     if x.lower().startswith("a"):
#         a_ile_baslayanlar.append(x)

# print(a_ile_baslayanlar)

# """ for x in adlar:
#     if "a" in x.lower():
#         a_ile_baslayanlar.append(x) """






text  = ["Murad","Vaqif","Aytac","GPT","Rza","Ayxan"]
text.sort(reverse=True)
print(text)