from typing import List
import pandas as pd
from langchain_chroma import Chroma


def get_retriever(vector_store_database: Chroma, search_type: str, k: int):
    """
    Get set VectorStoreRetriever object.
    
    Args:
        vector_store_database: Vector database.
        search_type: Use "similarity" for vector similarity search,
                or "mmr" for optimizing both similarity and retrieved
                chunks diversity.
        k: Number of returned chunks.
    Returns:
        retriever: VectorStoreRetriever object.
    """
    return vector_store_database.as_retriever(search_type=search_type,
                                              search_kwargs={"k": k})


def print_retrieved_fragments(results: list):
    """Print retrieved article fragments prettier."""
    for doc in results:
        print(f"From article: {doc.metadata['Title']}")
        print("-"*70)
        print(doc.page_content)
        print("\n","#"*70, "\n")


def get_and_save_retrievals_to_csv(questions: List[str],
                                   path: str,
                                   db,
                                   search_type: str = "mmr",
                                   k: int = 5):
    """
    Get retrieved article chunks for many questions and save to csv file.
    
    Args:
        questions: List of strings - query questions for retrieval.
        path: Save csv file path.
        db: Vector store database.
        search_type: Use "similarity" for vector similarity search,
                or "mmr" for optimizing both similarity and retrieved
                chunks diversity.
        k: Number of returned chunks.
    Returns:
        results_df: pd.DataFrame
    """
    all_titles = []
    all_chunks = []
    all_questions = []

    for question in questions:
        retriever = get_retriever(db, search_type, k)
        results = retriever.invoke(question)
        
        titles = [doc.metadata["Title"] for doc in results]
        chunks = [doc.page_content for doc in results]
        questions = [question] * len(results)

        all_titles.extend(titles)
        all_chunks.extend(chunks)
        all_questions.extend(questions)
    
    results_dict = {
        "Title": all_titles,
        "Text_chunk": all_chunks,
        "Question": all_questions 
    }
    
    results_df = pd.DataFrame(results_dict)
    results_df.to_csv(path, index=False)

    return results_df
    