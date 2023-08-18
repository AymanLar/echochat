# EchoChat
CLI tool that simulates conversations with historical figures

Introducing `EchoChat`: A CLI tool that lets you simulate conversations with historical figures using the magic of OpenAI's ChatGPT. Step into the shoes of legends and engage in dynamic dialogues, powered by cutting-edge AI. Uncover the past, learn from the icons, and shape conversations that transcend time.
## Installation
#### Installing EchoChat from GitHub
Follow these steps to install the EchoChat app from its GitHub repository and set it up locally on your computer.
##### Step 1: Clone the Repository
Open your terminal or command prompt and navigate to the directory where you want to clone the EchoChat repository.
 ```bash
 cd /path/to/your/desired/directory
 ```
 Clone the repository using the following command:
 ```bash
 git clone https://github.com/AymanLar/echochat.git
 ```
 ##### Step 2: Install EchoChat Locally
 ```bash
 pip install -e /path/to/echochat
 ```
### OpenAI API key
EchoChat requires an OpenAI API key to function. You can obtain a key by signing up for an account at [OpenAI's website](https://platform.openai.com/account/api-keys).

Once you have your API key, set it as an environment variable:

* On macOS and Linux:

  ```bash
  export OPENAI_API_KEY="your-api-key-here"
  ```

  To avoid having to type it everyday, you can create a file with the key:

  ```bash
  echo "your-api-key" > ~/.openai-api-key.txt
  ```

  **Note:** Remember to replace `"your-api-key"` with your actual API key.

  And then, you can add this to your shell configuration file (`.bashrc`, `.zshrc`, etc.):

    ```bash
    export OPENAI_API_KEY="$(cat ~/.openai-api-key.txt)"
    ```

* On Windows:

  ```
  set OPENAI_API_KEY="your-api-key-here"
  ```
## Usage
To use EchoChat, simply type `echochat` followed by a short name of the figure of choice :
```bash
echochat tesla
```
### Exiting the Chat
type `bye` to turn the program off
 ```
   > You: bye
 ```