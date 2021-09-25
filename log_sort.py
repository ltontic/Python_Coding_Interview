def log_sort(input: list) -> None:

  # 1. Separating the input of lists into individual lists of string
  logs: list = []
  temp_number: list = []

  for i in input:

    logs.append(i.split())

  # 2. Moving lists that contain numbers (excluding the indentifier to the back)
  for i in range(0, len(logs)):

    if logs[i][2].isnumeric():
       
      # Move number logs to a temporary list, remove number logs from list
      temp_number.append(logs[i])
      logs[i] = ""
      
  # Remove empty strings from list
  logs = [x for x in logs if x != ""]
  
  # 3. Sort word logs
  Words = {}
  
  for i in logs:
    
    for j in i:
      
      if j not in Words.keys():
        
        Words[j] = i

      else:
        
        # If two logs contain the same word, the one with the faster identifier (first word) comes first
        
        if i > Words[j]:
          
          i, Words[j] = Words[j], i
          
        else:
          
          continue
          
  # Re-add number logs to list
  for i in temp_number:
    
    logs.append(i)
  
  # Concatenate previously split lists
  
  for i in logs:
  
    for j in range(1, len(i)):
      
      i[0] = i[0] + " " + i[j]
      
      
  result: list = [i[0] for i in logs]
  
  # print(result)
  
log_sort(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])