import os
from dotenv import load_dotenv

def create_sentence(animal: str, sound: str) -> str:

    # Create sentence
    sentence = "The " + animal + " goes " + sound + "."

    return sentence

def main() -> None:

    # Read environment variables from .env file
    load_dotenv()

    # Get animal type and sound
    animal = os.environ.get("ANIMAL")
    sound = os.environ.get("SOUND")

    # Create sentence to print
    sentence = create_sentence(animal, sound)

    print(sentence)

if __name__ == "__main__":
    main()