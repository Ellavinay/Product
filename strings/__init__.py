# # txt = f"The price is {20 * 59} dollars"
# # print(txt)
# #
# #
# # list1 = ["a", "b" , "c"]
# # list2 = [1, 2, 3]
# #
# #
# # list2.append(list1)
# #
# # print(list1)
#
# x = -10
# y = 20
#
# if x > 5 and y < 25:
#     print("Both conditions are True")
# else:
#     print("At least one condition is False")
# # Expected Output: Both conditions are True


def voter_eligibility(age):
    return age >= 18


def main():
    try:
        age = int(input("Input your age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif voter_eligibility(age):
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please input a valid age.")


if __name__ == "__main__":
    main()