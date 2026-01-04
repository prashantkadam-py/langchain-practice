import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-practice!")
    print(f"OPENAI_API_KEY : {os.environ.get('OPENAI_API_KEY')}")


if __name__ == "__main__":
    main()
