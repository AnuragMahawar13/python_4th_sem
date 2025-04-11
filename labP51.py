#Q.51  It accepts a text file as input and returns the number of words in the file.

def count_words_in_file(file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    
# Example usage:
file_path = "/mnt/data/file-7sgottVkNjSY2bTiggMP46"
word_count = count_words_in_file(file_path)
print(f"Number of words in the file: {word_count}")