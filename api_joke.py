# Import libraries
from abc import ABC, abstractmethod
import requests
import json

# Abstract class


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

# The first random joke class


class A(Joke):
    # Using the abstract function to make jokes
    def get_random_joke(self):
        # Get the link
        url = "https://official-joke-api.appspot.com/jokes/random"
        # Show the name of the joke
        print("Joke A :")
        # Get link information
        response = requests.get(url)
        # Analysis and conversion of link information
        response_dict = json.loads(response.text)
        # Access to the desired elements in the link
        setup = response_dict["setup"]
        punchline = response_dict["punchline"]
        result = setup + "\n" + punchline
        # Output from the function
        return "".join(result)


# The second random joke class


class B(Joke):
    # Using the abstract function to make jokes
    def get_random_joke(self):
        # Get the link
        url = "https://official-joke-api.appspot.com/jokes/random"
        # Show the name of the joke
        print("\nJoke B :")
        # Get link information
        response = requests.get(url)
        # Analysis and conversion of link information
        response_dict = json.loads(response.text)
        # Access to the desired elements in the link
        setup = response_dict["setup"]
        punchline = response_dict["punchline"]
        result = setup + "\n" + punchline
        # Output from the function
        return "".join(result)

# The third random joke class


class C(Joke):
    # Using the abstract function to make jokes
    def get_random_joke(self):
        url = "https://official-joke-api.appspot.com/jokes/random"
        # Show the name of the joke
        print("\nJoke C :")
        # Get link information
        response = requests.get(url)
        # Analysis and conversion of link information
        response_dict = json.loads(response.text)
        # Access to the desired elements in the link
        setup = response_dict["setup"]
        punchline = response_dict["punchline"]
        result = setup + "\n" + punchline
        # Output from the function
        return "".join(result)


# Calling joke creation functions
if __name__ == "__main__":
    print(A().get_random_joke())
    print(B().get_random_joke())
    print(C().get_random_joke())
