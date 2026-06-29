from backend.app.rag import answer_question

print("\n" + "═" * 70)
print("📄 DocuMind AI")
print("AI-Powered Intelligent PDF Assistant")
print("═" * 70)
print("Type 'exit' to quit.\n")

while True:

    question = input("👤 You: ")

    if question.lower() == "exit":
        print("\n👋 Thanks for using DocuMind AI!")
        break

    print("\n🤖 DocuMind AI:\n")

    result = answer_question(question)

    print(result["answer"])

    print("\n" + "─" * 70)
    print("📚 Sources")

    for source in result["sources"].split("\n"):
        print(f"• {source}")

    print("─" * 70 + "\n")