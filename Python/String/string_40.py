# 40. Count uppercase and lowercase letters separately.

text = input("Enter a string:")
lower = sum(1 for ch in text if ch.islower)
upper = sum(1 for ch in text if ch.isupper)
print(f"Lower case:{lower}Upper case:{upper}")