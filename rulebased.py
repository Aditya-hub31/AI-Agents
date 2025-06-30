while True:
    question = input("Ask me anything: ").lower()
    if "course" in question:
        print("We offer AI, ML, Web Dev, and more!")
    elif "timing" in question:
        print("Classes start at 9 AM.")
    elif "bye" in question:
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't know that.")