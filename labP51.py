#Q.51  It accepts a text file as input and returns the number of words in the file.

def count_words_in_file(file_name):
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    
# Example usage:
file_name = "sample.txt"
word_count = count_words_in_file(file_name)
print("Number of words in the file:- ",word_count)