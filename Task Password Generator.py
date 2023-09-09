#Task: Password Generator
import random
import string
def generate_password(length, complexity):
  """Generates a random password of the specified length and complexity."""
  characters = ""
  if complexity == "low":
    characters = string.ascii_lowercase + string.digits
  elif complexity == "medium":
    characters = characters + string.ascii_uppercase
  elif complexity == "high":
    characters = characters + string.punctuation + string.ascii_letters + string.digits
  password = ""
  for _ in range(length):
    password += random.choice(characters)
  return password
def main():
  length = int(input("Enter the desired length of the password: "))
  complexity = input("Enter the desired complexity of the password (low, medium, high): ")
  password = generate_password(length, complexity)
  print("Your password is:", password)
if __name__ == "__main__":
  main()

    
      