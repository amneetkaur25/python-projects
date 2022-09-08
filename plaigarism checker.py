from difflib import SequenceMatcher

with open('text1.txt','r') as file1 , open('txt2.txt','r') as file2:
    file1_data=file1.read()
    file2_data=file2.read()
    similarity=SequenceMatcher(None,file1_data,file2_data).ratio()
    print(f'The contents are {similarity*100}% common')
