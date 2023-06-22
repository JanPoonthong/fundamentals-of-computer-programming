tester = int(
    input("Enter a positive integer (to terminate enter a negative integer): ")
)

while tester >= 0:
    print(f"You enter number# {tester}")
    tester = int(
        input(
            "Enter a postive integer (to terminate enter a negative integer): "
        )
    )

print("Exit from a loop")
