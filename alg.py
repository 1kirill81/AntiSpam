import re


def load_spam_phrases():
    with open("spam_phrases.csv", encoding="cp1251") as file:
        phrases = file.read().split("\n")
        return [phrase.strip() for phrase in phrases if phrase.strip()]


def load_spam_words():
    with open("spam_words.csv", encoding="cp1251") as file:
        words = file.read().split("\n")
        return [word.strip() for word in words if word.strip()]


def check_spam(text, spam_phrases, spam_words):
    text_lower = text.lower()
    found_phrases = [phrase for phrase in spam_phrases if phrase in text_lower]

    found_words = []
    for word in spam_words:
        if re.search(rf'\b{re.escape(word)}\b', text_lower):
            found_words.append(word)

    return found_phrases + found_words


def main():
    spam_phrases = load_spam_phrases()
    spam_words = load_spam_words()

    user_input = input("Введите текст для проверки на спам:\n")

    detected_phrases = check_spam(user_input, spam_phrases, spam_words)

    if detected_phrases:
        print("\n⚠️ Обнаружены спам-фразы:")
        for phrase in detected_phrases:
            print(f"- {phrase}")
        print("\nРекомендуется пометить как спам!")
    else:
        print("\n✅ Текст безопасен, спам-фраз не обнаружено.")


if __name__ == "__main__":
    main()