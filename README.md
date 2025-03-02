# Pro-stock Advisor & IEEE paper chatbots

Developing an Intelligent investment assistant for equity research analysts, the objective is to streamline equity research by leveraging advanced technologies. 
[This involves implementing a Lang Chain for text processing to extract key information from news articles efficiently. Additionally, a semantic search algorithm is required to identify relevant textual chunks based on user queries while optimizing OpenAI API calls for cost-effectiveness. Leveraging OpenAI's question-answering capabilities ensures accurate responses, complemented by natural language generation for user-friendly outputs. Finally, a Streamlit-based user interface will offer a seamless and interactive experience, enhancing usability for analysts]

------------------------------------------------------------

## Technical Architecture

* Lang Chain for Text Processing:
    Cleaning and processing textual data from news articles. Extracting key information (company names, financial figures).
* Semantic Search Algorithm:
    Identify relevant chunks of text based on user queries. Optimizing OpenAI API calls for cost-effectiveness.
* OpenAI for Question Answering:
    OpenAI's language model for accurate responses. Natural language generation for user-friendly answers.
* Stream-lit for User Interface:
    A user-friendly web interface for analysts. Interactive features for enhanced user experience.

------------------------------------------------------------

#### Download or Clone the project

First Download or Clone the Project on Your Local Machine.To download the project from github press **Download Zip**

You can clone the project with git bash.To clone the project using git bash first open the git bash and write the following code
```
git clone https://github.com/Yashvanth-R/Pro-stock-Advisor.git
```
After download, Open the project using **Pycharm or VSCODE**. Then we have to create an python enviroment to run the program.

#### create enviroment 
First open the terminal or command line in the IDE.Then write the following code.
```
python -m venv venv
```
Then activate the enviroment using the code below for windows.
```
.\venv\Scripts\activate
```

#### How to run

Once you have activated the environment, install the necessary packages
```
pip install -r requirements.tsx
```

First for running the Pro-stock Advisor chatbot
```
streamlit run main.py
```

Second for running the IEEE paper chatbot 
```
streamlit run main1.py
```

If you get any error regarding the open_api key, please do enable your personal open api key through the https://platform.openai.com/api-keys platform.

-----------------------------------------------------------

## Contribute :thumbsup:
--------------------------------------
If you want to contribute in this project feel free to do that.

## Licence :scroll:
---------------------------------
MIT © [Yashvanth-R](https://github.com/Yashvanth-R)