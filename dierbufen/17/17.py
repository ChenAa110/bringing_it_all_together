import re

l = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

matches = re.findall("^If", l, re.MULTILINE)

print(matches)

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123?34 hel1o?"
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "_one_ _two_ __three__four"
found = re.findall("_.*?_", t)
for match in found:
    print(match)

text = """Although never is __better__ *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to ____ , it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


def mad_libs(mls):
    """

    :param mls:字符串下划线部分需要填写
    :return:
    """

    hints = re.findall("__.*?__", text)

    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
    else:
        print("invalid mls")


# mad_libs(text)


line="i love $"

m=re.findall("\\$",line,re.IGNORECASE)
print(m)
print(line)
