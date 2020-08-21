import webhook_quickstart


def main():
    chat_message = "Hej alle! Velkommen til gruppen. Dette chat rum bruges til at teste Google Chat API'et. " \
                   "Dette er en chat besked genereret af et Python script. :)"
    webhook_quickstart.quickstart(chat_message)


if __name__ == '__main__':
    main()
