# STEP 1: Create a function for the chatbot
def chatbot_response(user_input):
    """
    This function takes user input and returns
    a predefined chatbot response.
    """

    # Convert input to lowercase to avoid case issues
    user_input = user_input.lower()

    # STEP 2: Rule-based responses
    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# STEP 3: Main program loop
def main():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        # Get input from user
        user_input = input("You: ")

        # Get chatbot response
        response = chatbot_response(user_input)

        # Display chatbot response
        print("🤖 Chatbot:", response)

        # Exit condition
        if user_input.lower() == "bye":
            break


# STEP 4: Run the chatbot
main()

