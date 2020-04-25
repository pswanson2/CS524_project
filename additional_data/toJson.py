# import json
# #
# #
# #
# # # Data to be written
# # class_dict = {
# #     "class_name": "sathiyajith",
# #     "gpa": 56,
# #     "professor": "[ "
# #                  "]"
# # }
# #
# # # Serializing json
# # json_object = json.dumps(class_dict, indent=4)
# #
# # # Writing to sample.json
# # with open("sample.json", "a") as outfile:
# #     outfile.write(json_object)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file1 = open('class_data.txt', 'r')
fw = open("class_data.json", "w")
n = 0  # count
length = file_len('class_data.txt')
Lines = file1.readlines()
fw.write("{\n    \"classes\":[\n")
for line in Lines:
    if n != 0:
        fw.write("    {\n")
        line_split = line.rstrip('\n').split(',')  # remove trailing new line and split
        fw.write("        \"course_num\": \"" + line_split[0] + "\",\n")
        fw.write("        \"class_name\": " +  ",\n")
        fw.write("        \"gpa\": " + line_split[1] + ",\n")
        fw.write("        \"industry_rating\": " + ",\n")
        fw.write("        \"research_rating\": " + ",\n")
        fw.write("        \"course_type\": [\n")
        fw.write("        ],\n")
        fw.write("        \"course_cat\": [\n")
        fw.write("        ],\n")
        fw.write("        \"season_offered\": [\n")
        fw.write("        ],\n")
        fw.write("        \"professor\": [\n")
        fw.write("        ]\n")
        if n == length -1:
            fw.write("    }\n")
        else:
            fw.write("    },\n")
    n = n + 1
fw.write("    ]\n}")
print(length)
print(n)