filename= input("Input the Filename:")
extentiondict={"py":"Python",
"java":"Java",
"cpp":"C++",
"rb":"Ruby",
"js":"JavaScript",
"r":"R",
}
# for extention in filename:
#     if extention.endswith(".py"):
#         print("The extension of the file is : 'python'")
extension=filename.split(".")
# print((extension[-1]))
print("The extension of the file is :",extentiondict[(extension[-1])])