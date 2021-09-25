from collections import Counter

def group_anagrams(anagrams: list) -> None:
    
    input_list: list = anagrams
    alpha_sorted: list = []
    
    for i in input_list:
        
        alpha_sorted.append(''.join(sorted(i)))
        
    input_list = list(dict.fromkeys(alpha_sorted))
    print(input_list)
    
    for i in input_list:
        
        for j in range(0, len(alpha_sorted)):
            
            if alpha_sorted[j] == i:
                
                print(anagrams[j])
                
        print("\n")
    
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])