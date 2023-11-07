with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    def console_content():
        print(file_contents)

    def word_count():
        return len(file_contents.split())
        
    def count_letters():
        letters = {}

        for char in file_contents:
            lower = char.lower()

            if lower.isalpha():
                if lower in letters:
                    letters[lower] += 1
                else:
                    letters[lower] = 1
        
        return letters
        
    def create_report():
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count()} words found in the document")
        
        letters = sorted(list(count_letters().items()), key=lambda x: x[0])
        
        for letter in letters:
            print(f"The '{letter[0]}' character was found {letter[1]} times")
    
    create_report()
    
    

