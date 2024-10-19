# Create a Personal Assistant with LangChain
Large language models (LLM), such as ChatGPT, have been around for a relatively short amount of time yet have already changed the way we work. With a generative model in hand, many tasks can be automated to help our work.

One thing we can do with an LLM is to develop our own personal assistant, with the generative AI model performing our work, especially the tasks we do often.

In this article I will show you how to create a personal assistant with LLM facilitated by LangChain. Let’s get into it.

## Personal Assistant Development with LangChain

 
First, we need to efficiently structure our project. For our purposes, we will use the following structure:

personal_assistant_project

├── .env              
├── main.py   
├── Dockerfile  
├── utils.py                      
└── requirements.txt 

 The requirements.txt file will contain the packages necessary for the project. In this case, we would fill them with the following list:

streamlit
langchain
langchain-community
openai
Python-dotenv

 

These are the packages necessary for our project. Now, fill in the .env file with your OpenAI API key.

* OPENAI_API_KEY=”SK-YOUR_API_KEY”

 

Using a .env file is a standard way to safely secure our API keys for use in the project rather than hard-coding them in our Python file.

With the preparation ready, we would set up the utils.py file, which would become the backbone of our personal assistant project.

Initially, we will prepare all the packages we would use during the project.

https://www.kdnuggets.com/creating-a-personal-assistant-with-langchain

### Build the image

To build a container image using the Dockerfile from the you use the docker build command:

### docker build -t my_gpt:latest . ###


The -t my_gpt:latest option specifies the name and tag of the image.

The single dot (.) at the end of the command sets the build context to the current directory. This means that the build expects to find the Dockerfile and the hello.py file in the directory where the command is invoked. If those files aren't there, the build fails.

After the image has been built, you can run the application as a container with docker run, specifying the image name:

### docker run -e OPENAI_API_KEY=YourOPENAI_API_KEY my_gpt:latest ###
* Run the docker image.
To set the OPENAI_API_KEY as an env variable when you run the image.
You can use the -e flag to set or override an environment variable when running a container. You can specify multiple variables by using multiple -e flags.

