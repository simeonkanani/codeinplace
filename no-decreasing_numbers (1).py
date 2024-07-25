def main():
  print("Enter a sequence of non-decreasing numbers.")

  sequence = []

  # Get the first number
  curr_num = float(input("Enter a number: "))
  sequence.append(curr_num)

  while True:
      prev_num = curr_num
      curr_num = float(input("Enter a number: "))

      if curr_num < prev_num:
          break

      sequence.append(curr_num)

  print("Thanks for playing!")
  print(f"Sequence length: {len(sequence)}")

if __name__ == "__main__":
  main()