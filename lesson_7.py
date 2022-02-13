import csv

file_path = "C:/Users/Timofey/PycharmProjects/Kurses/text_files/"
text_file_title = 'text_1.txt'
csv_file_title = 'csv_2.csv'

file_title = file_path + csv_file_title
# file_title = file_path + text_file_title

# f = open(file_title, 'w')
#
# f.write('Hello World')
#
# f.close()

# print
#
# ll = ['QA', 'Automation', 'employees']
#
# # with open(file_title, 'w', encoding='utf-8') as f:
# # with open(file_title, 'x', encoding='utf-8') as f:
# with open(file_title, 'a', encoding='utf-8') as f:
#
#     # f.writelines(ll)
#     # f.write('\n'.join(ll))
#
#     for n in range(0, 10):
#         for i in ll:
#             # f.write(i)
#             # f.write('\n')
#             w_line = str(n) + '_' + i
#
#             f.writelines(w_line)
#             f.write('\n')
#
# with open(file_title, 'r') as f:
#
#     # ff = f.read()
#     # ff = f.read(10)
#     ff = f.readlines()
#
#     print(ff)
#
#     del ff[1]
#
#     with open(file_title, 'w') as wf:
#
#         wf.writelines(ff)

    # for lines in ff:
    #     #
    #     # print(ff)
    #     # print(len(ff))
    #     # print(lines)
    #     print(lines.rstrip())

users_l = [['Maxim', 30],
           ['Artiom', 32],
           ['Alexey', 35]]

# with open(file_title, 'w') as csv_f:
#     writer = csv.writer(csv_f)
#     row = ['Elena', 20]
#     row2 = ['Anna', 23]
#     writer.writerow(row)
#     writer.writerow(row2)

# with open(file_title, 'a') as csv_f:
#
#     writer = csv.writer(csv_f)
#     writer.writerow(users_l)

# with open(file_title, 'r', newline="") as csv_f:
#
#     reader = csv.reader(csv_f)
#
#     print(*reader)

# with open(file_title, 'w') as csv_f:
#
#     columns = ["Name", "Age"]
#     writer = csv.DictWriter(csv_f, fieldnames=columns)
#     writer.writeheader()
#
#     user = {"Name": "Alex",
#             "Age": 30}
#
#     writer.writerow(user)

users = [{"Name": "Alex", "Age": 30},
         {"Name": "Max", "Age": 20},
         {"Name": "Elena", "Age": 25},
         {"Name": "Vadim", "Age": 32}]

with open(file_title, 'a') as csv_f:

    columns = ["Name", "Age"]
    writer = csv.DictWriter(csv_f, fieldnames=columns, lineterminator='\n')

    writer.writerows(users)

with open(file_title, 'r') as csv_f:

    reader = csv.DictReader(csv_f)

    line_count = 0

    for rrr in reader:

        print(line_count, rrr["Name"], rrr["Age"])
        line_count += 1

