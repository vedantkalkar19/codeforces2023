def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False


def main():
  weight = int(input())
  if weight % 2 == 0:
    if is_even(weight // 2):
      print("YES")
    else:
      print("NO")
  else:
    print("NO")


if __name__ == "__main__":
  main()
