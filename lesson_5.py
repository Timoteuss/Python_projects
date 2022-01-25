import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num_1', type=int, required=True)
parser.add_argument('--num_2', type=int)
parser.add_argument('--action', type=str)

args = parser.parse_args()

item_1 = args.num_1
item_2 = args.num_2
act = args.action

if act == "sum":
    result = item_1 + item_2
    print("Result =", result)
elif act == "multi":
    result = item_1 * item_2
    print("Result =", result)
elif act == "div":
    result = item_1 / item_2
    print("Result =", result)
elif act == "sub":
    result = item_1 - item_2
    print("Result =", result)



# parser = argparse.ArgumentParser()
# parser.add_argument('--name', type=str)
# parser.add_argument('--age', type=int, default=27)
#
# args = parser.parse_args()
#
# print('Name =', args.name)
# print('Age =', args.age)
#
# args_dict = args.__dict__
#
# for k, v in args_dict.items():
#
#     print(k, v)


# print("Hello world!!!")
#
# params = sys.argv[1:]
#
# print('params =', params)
#
# sum_l = []
# for i in params[0:3]:
#     sum_l.append(int(i))
#
# sum_3 = sum(sum_l)
# print("sum_3 =", sum_3)