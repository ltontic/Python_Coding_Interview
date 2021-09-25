from collections import Counter

def most_common_word(paragraph: str, banned: str) -> str:
   
    # 1. Input string processing 
    input_string = paragraph
    input_string = input_string.replace(",", "")
    input_string = input_string.replace(".", "")
    input_string = input_string.lower()
    input_string = input_string.split()

    # 2. Counter creation
    
    Words = Counter(input_string)
    
    #3. Result
    
    if Words.most_common(1)[0][0] == banned:
    
        print(Words.most_common(2)[1][0])
        return Words.most_common(2)[0][0]
    
    else:
        
        print(Words.most_common(1)[0][0])
        return Words.most_common(1)[0][0]
            
    
most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", "hit")