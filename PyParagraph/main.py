import re
import os
import string
#preparing the output for both files foun in Output file. If you want to test it, you should add the path of you computer 
#until "...paragraph_" and the code will do the magic.
for i in range(1,3):
    txtpath = 'C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyParagraph/Resources/Lessons_03-Python_Homework_ExtraContent_Instructions_PyParagraph_raw_data_paragraph_'+str(i)+".txt"
    output_txt = 'C:/Users/empha/Desktop/Data_Analytics/Semana_4/python-challenge/PyParagraph/Output/Output'+str(i)+'.txt'
    with open(txtpath,'r',newline='', encoding='utf-8') as txtfile:
        #paragraph = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."
        paragraph = txtfile.read()
        #What this part of the code does is that we indicate that we are using regular expression to split the paragraph.
        #positive lookbehind assertion y despues revisamos que despues de cualquier punto, singo de exclamacion o interrogacion sea el punto de partida para separarlo.
        sentences = re.split("(?<=[.!?]) +", paragraph)
        words_list = []
        total_words = 0
        suma_letras = 0
        count_points = 0
        for words in sentences: 
            words_divided = re.split(", | |-|'",words)
            for letters in words_divided:
                if "." in letters:
                    count_points += 1
                suma_letras += len(letters)
            words_list.append(len(words_divided))
            total_words += len(words_divided)

        letter_count = round((suma_letras-count_points)/total_words,2)
        sentece_length = total_words/len(sentences)

    with open(output_txt, "w", newline='',encoding='utf-8\n') as datafile:
        print("Paragraph Analysis")
        print("-----------------------")
        print(f'Approximate Word Count: {total_words}')
        print(f'Approximate Sentence Count: {len(sentences)}')
        print(f'Average Letter Count: {letter_count}')
        print(f'Average Sentence Length: {sentece_length}')
        datafile.write("Paragraph Analysis\n")
        datafile.write("-----------------------\n")
        datafile.write(f'Approximate Word Count: {total_words}\n')
        datafile.write(f'Approximate Sentence Count: {len(sentences)}\n')
        datafile.write(f'Average Letter Count: {letter_count}\n')
        datafile.write(f'Average Sentence Length: {sentece_length}\n')
        



