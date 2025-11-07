# Google File Search Agent - Devfest 2025 ADK Workshop

這是一個在 Google Devfest 2025 ADK 工作坊中建立的範例專案。它展示了如何使用 Google AI Developer Kit (ADK) 來建立一個可以上傳檔案並透過自然語言查詢檔案內容的 AI 代理。

## 關於此專案

這個專案的核心是一個 AI 代理，它整合了 Google 最新的生成式 AI 模型 (`gemini-2.5-flash`) 和檔案搜尋功能。您可以上傳一個或多個檔案（例如 PDF、TXT 等），然後像與真人對話一樣，向代理詢問有關這些檔案內容的問題。

## 主要功能

代理提供了兩個主要的工具：

*   `upload_file(file_path: str)`: 上傳一個本地檔案到 AI 代理的知識庫中。
*   `ask_file(question: str)`: 針對所有已上傳的檔案內容，提出一個問題，並獲得 AI 生成的答案。

## 環境準備

在開始之前，請確保您已經準備好以下環境：

1.  **Python 3.9+**: [安裝 Python](https://www.python.org/downloads/)
2.  **Google API Key**: 您需要一個有效的 Google API 金鑰來使用 Gemini 模型。
    *   前往 [Google AI for Developers](https://aistudio.google.com/app/apikey) 獲取您的 API 金鑰。
    *   設定環境變數 `GOOGLE_API_KEY`：
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```

## 安裝與執行

請依照以下步驟來安裝和執行此專案：

1.  **克隆儲存庫**
    ```bash
    git clone https://github.com/your-username/devfest-2025-adk-workshop.git
    cd devfest-2025-adk-workshop
    ```

2.  **安裝依賴套件**
    ```bash
    pip install -r requirements.txt
    ```

3.  **執行代理**
    使用 `adk` 命令列工具來執行代理：
    ```bash
    adk web
    ```
    代理將在本地啟動一個 web UI 服務。

## 使用範例

代理啟動後，您可以透過 `adk chat` 或直接與 API 互動。

1.  **上傳檔案**
    首先，請代理上傳一個檔案。例如，專案中 `files` 資料夾下的 `Cybersecurity Management Law.pdf`。

    > **User:** 請幫我上傳 `files/Cybersecurity Management Law.pdf` 這個檔案。

    代理會呼叫 `upload_file` 工具，將檔案加入知識庫。

2.  **提出問題**
    檔案上傳成功後，您可以開始提問。

    > **User:** 根據已上傳的檔案，說明什麼是網路安全？

    代理會使用 `ask_file` 工具，在檔案內容中尋找答案，並生成回覆。

---
這是一個簡單但功能強大的範例，展示了如何利用 ADK 快速打造具備 RAG (Retrieval-Augmented Generation) 功能的 AI 應用。