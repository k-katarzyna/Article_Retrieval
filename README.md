## Article Retrieval System

This is a preliminary version of article retrieval system with RAG. It indexes articles from the ["1300 Towards Data Science Medium Articles" dataset](https://www.kaggle.com/datasets/meruvulikith/1300-towards-datascience-medium-articles-dataset).

Source code and comments can be found in the *main.ipynb* notebook. The *retrieval_result.csv* file contains examples of retrieved article fragments.

### Instructions

1. Environment Setup:
```bash
# create python environment
python3 -m venv article_retrieval

# activate environment
source article_retrieval/bin/activate

# install dependencies
pip install -r requirements.txt

# create jupyter environment kernel
python -m ipykernel install --user --name=article_retrieval
```
2. Running the Project:
   * Open the *main.ipynb* notebook in Jupyter Notebook or JupyterLab.
   * Select the *article_retrieval* kernel.
   * Add your OpenAI API key to the `openai_api_key` variable in the second cell (needed only to run the last section).
   * Make sure to run the cells sequentially to ensure proper execution of the code.