score = int(input("Enter your score: "))
has_participated_in_sports = input(
    "have you participated in sports (Y/N): ").strip().lower()


if score >= 90 or score >= 75 and has_participated_in_sports == 'y':
    print("Eligible for scholarship")
else:
    print("Not eligible")
