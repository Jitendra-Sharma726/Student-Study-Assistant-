import os

def load_document(file_path):
    """
    Load text from a file and return its content as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()

def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()                        # Break text into words
    chunks = []                                 # Store all chunks here
    step = chunk_size - overlap                 # Move this many words forward each time

    # Go through the words in steps
    for i in range(0, len(words), step):
        chunk_words = words[i:i + chunk_size]   # Take a slice of words
        chunk = " ".join(chunk_words)           # Join them back into a string
        chunks.append(chunk)                    # Add to our chunks list

    return chunks

def score_chunk(chunk, keywords):
    """
    Compute a score for a chunk based on overlapping keywords with the question.
    """
    # Convert the chunk into lowercase words
    words = chunk.lower().split()

    # Turn the list of words into a set (to remove duplicates)
    word_set = set(words)

    # Find common words between chunk and keywords
    common_words = word_set.intersection(keywords)

    # Count how many keywords are present in this chunk
    score = len(common_words)

    return score

def get_best_chunk(chunks, question, min_score):
    """
    Select the chunk that best matches the question based on keyword overlap.
    """
    # Break down the question into lowercase words
    question_words = question.lower().split()

    # Convert the list of words into a set (to remove duplicates)
    question_keywords = set(question_words)

    # Track the best chunk and highest score found
    best_chunk = None
    best_score = -1

    # Go through each chunk and calculate its score
    for chunk in chunks:
        score = score_chunk(chunk, question_keywords)

        if score > best_score:
            best_score = score
            best_chunk = chunk
    
    # NO RELEVANT CONTEXT FOUND
    if best_score < min_score:
        return None

    # Return the chunk with the highest overlap
    return best_chunk

if __name__ == "__main__":
    file_path = "document.txt"

    print("Loading document...")
    doc_content = load_document(file_path)

    print("Splitting document into chunks...")
    chunks = chunk_text(doc_content)

    question = input("Enter your question: ").lower()

    print("Finding best context chunk...")
    min_score = 2
    best_chunk = get_best_chunk(chunks, question, min_score)

    if best_chunk is None:
        print("Sorry, the answer is not present in the document.")
        exit()

    print("\nBest context chunk:")
    print(best_chunk)
    
    
    
