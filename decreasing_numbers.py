def main():
  print("Enter a sequence of non-decreasing numbers. ")
  curr_num = input(int("Enter num: " ))
  prev_num = curr_num

  if curr_num < prev_num:
      print("Thanks for playing!")


if __name__ == "__main__":
  main()