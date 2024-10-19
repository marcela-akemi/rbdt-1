from models.classifier import classify_credit

def main():
    results = classify_credit()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()