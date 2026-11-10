import os

from dotenv import load_dotenv

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20261026", anthropic_api_key=anthropic_api_key
)


def main() -> None:
    print("Hello from langchain-course!")
    print(os.getenv("ANTHROPIC_API_KEY"))


if __name__ == "__main__":
    main()
