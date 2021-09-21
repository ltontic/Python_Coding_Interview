def Palindrome(input: str) -> bool:

  input = input.lower()
  input_copy: str = ""
  input_reverse: str = ""

  for i in input:

    if i.isalnum():

      input_copy += i
     
  input_reverse = input_copy[::-1]
  
  # print(input_copy)
  # print(input_reverse)
  
  if input_copy == input_reverse:
    return True
  else:
    return False
