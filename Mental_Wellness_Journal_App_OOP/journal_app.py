class JournalEntry:
    def __init__(self, mood, note):
        self.mood = mood.lower()
        self.note = note.lower()

    def display_entry(self):
        print(f"Mood: {self.mood.capitalize()}")
        print(f"Note: {self.note}")
        print("-" * 30)

    def mood_suggestion(self):
        suggestions = {
            "sad": "Try to write about what’s bothering you or something positive that happened today.",
            "happy": "Write about what made you happy and how you can keep that positivity going.",
            "anxious": "Describe what’s making you anxious and ways you can calm down.",
            "tired": "Note down how you can rest better or what made you tired.",
            "angry": "Express what made you angry and think of ways to cool down.",
            "excited": "Write about what you are excited for and your plans.",
            "bored": "Think about what new thing you want to try or learn.",
        }
        return suggestions.get(self.mood, "Write whatever you feel or think.")

    def note_response(self):
        keywords_responses = {
            "cricket": "Sounds like you enjoy cricket! Maybe play a match or watch highlights?",
            "study": "Studying is great! Keep focusing and take breaks when needed.",
            "workout": "Awesome! Regular exercise boosts your mood and health.",
            "exercise": "Keep up the good work with your exercise routine!",
            "stress": "Try some deep breathing or meditation to reduce stress.",
            "happy": "Glad you are feeling happy! Keep spreading positivity.",
            "sad": "Sorry to hear you are sad. Writing helps, keep it up.",
            "tired": "Make sure to get enough rest and take breaks.",
            "angry": "Take a moment to cool down and breathe deeply.",
            "excited": "Excitement is great! Channel it into positive actions.",
            "bored": "Try something new or creative to beat boredom.",
            # add more keywords and responses as you like
        }

        for keyword, response in keywords_responses.items():
            if keyword in self.note:
                return response

        # Default response if no keyword found
        return "Thanks for sharing your thoughts. Keep journaling!"

class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, mood, note):
        new_entry = JournalEntry(mood, note)
        self.entries.append(new_entry)
        print("\n✅ Entry added!\n")
        print("Mood Suggestion:", new_entry.mood_suggestion())
        print("Note Suggestion:", new_entry.note_response())

    def view_entries(self):
        if not self.entries:
            print("\n📭 No entries yet.\n")
        else:
            for entry in self.entries:
                entry.display_entry()

journal = Journal()

while True:
    print("\n--- Mental Wellness Journal ---")
    print("1. Add Entry     (Write your mood and a note)")
    print("2. View Entries  (See your previous entries)")
    print("3. Exit          (Close the app)")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        mood = input("How are you feeling? (e.g. happy, sad, anxious, tired, angry, excited, bored): ")
        print("\nHere are some ideas on what you can write:")
        temp_entry = JournalEntry(mood, "")
        print(temp_entry.mood_suggestion())
        note = input("Write your note here: ")
        journal.add_entry(mood, note)

    elif choice == '2':
        journal.view_entries()

    elif choice == '3':
        print("\nGoodbye! Take care of yourself.")
        break

    else:
        print("\n❗ Invalid choice. Please try again.")




