def main():
        filename = input("Enter the name of the file: ")
        print("Enter rows of text. Quit by entering an empty row.")
        counter = 1
        with open(filename, "w") as f:
                while True:
                        text_line = input()
                        f.write(str(counter) + " " + text_line+"\n")
                        if text_line == "":
                                break
                        counter += 1


        print(f"File {filename} has been written.")

if __name__ == "__main__":
    main()
