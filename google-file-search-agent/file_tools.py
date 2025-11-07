from google import genai
from google.genai import types
import time
import os

# This is a global variable to store the file search store name.
# This is not ideal for a production system, but for this workshop it is fine.
FILE_SEARCH_STORE_NAME = None

def get_or_create_file_search_store():
    """Gets or creates the file search store."""
    global FILE_SEARCH_STORE_NAME
    if FILE_SEARCH_STORE_NAME:
        print(f"Using existing file search store: {FILE_SEARCH_STORE_NAME}")
        return FILE_SEARCH_STORE_NAME

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")

    client = genai.Client(api_key=api_key)

    print("Creating a new file search store...")
    file_search_store = client.file_search_stores.create(config={'display_name': 'devfest-2025-file-search-store'})
    FILE_SEARCH_STORE_NAME = file_search_store.name
    print(f"File search store created: {FILE_SEARCH_STORE_NAME}")
    return FILE_SEARCH_STORE_NAME

def upload_file(file_path: str) -> str:
    """
    Uploads a file to the file search store.

    Before calling this tool, you should have already created a file.
    If you need to create a file, you can use the `write_file` tool first.

    Args:
        file_path: The path to the file to upload.

    Returns:
        A message indicating whether the file was uploaded successfully.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY environment variable not set. Please set it to your Google API key."
    client = genai.Client(api_key=api_key)

    file_search_store_name = get_or_create_file_search_store()

    print(f"Uploading file {file_path} to {file_search_store_name}...")
    operation = client.file_search_stores.upload_to_file_search_store(
        file=file_path,
        file_search_store_name=file_search_store_name
    )

    print("Waiting for file to be imported...")
    while not operation.done:
        time.sleep(5)
        operation = client.operations.get(operation)

    if operation.done:
        print("File imported successfully.")
        return f"File {file_path} uploaded and imported successfully."
    else:
        print(f"Error importing file: {operation.error}")
        return f"Error importing file {file_path}: {operation.error}"

def ask_file(question: str) -> str:
    """
    Asks a question about the files in the file search store.

    You can ask questions about the files that have been uploaded.

    Args:
        question: The question to ask.

    Returns:
        The answer to the question.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY environment variable not set. Please set it to your Google API key."
    client = genai.Client(api_key=api_key)

    file_search_store_name = get_or_create_file_search_store()
    if not file_search_store_name:
        return "File search store not created yet. Please upload a file first."

    print(f"Asking question '{question}' to file search store {file_search_store_name}...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[file_search_store_name]
                    )
                )
            ]
        )
    )

    return response.text