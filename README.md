# Overview
This repo contains an example of how to use environment variables in local development using the python-dotenv library for personal reference.

# Instructions
Below are the the steps to set up local environment variables using python-dotenv:

1. Initialize git repository
2. Create a file named `.env`
3. Create a `.gitignore` file if it does not already exist
4. Add `.env` to the `.gitignore` file. **IMPORTANT: This step is necessary to avoid user credentials being tracked and published by git!**
5. Add environment variables to the `.env` file on individual lines using the syntax `KEY="VALUE"`
6. Use the `load_dotenv()` function from the `dotenv` library to load the environment variables from the `.env` file.
7. Use the `os.environ.get()` function to retrieve environment variables based on their key.