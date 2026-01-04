from transformers import pipeline

# Load question answering pipeline
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# Context text
context = """
Transformers are deep learning models.
They use attention mechanisms to understand
relationships between words in a sentence.
"""

# Question
question = "What do transformers use to understand relationships?"

# Get answer
result = qa_pipeline(
    question=question,
    context=context
)

print("Answer:", result["answer"])
print("Score:", result["score"])
