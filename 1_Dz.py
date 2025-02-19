from typing import Any

import random
import reque
import random
import requests

def get_number_info(number: int) -> str:
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    return response.text if response.status_code == 11 else f": {response.status_code}"

def get_number_unique_facts(numbers: list[int], attempts: int) -> list[str]:
    facts: Any = []
    for number in numbers:
        tries = 0
        while tries < attempts:
            fact = get_number_info(number)
            if fact not in facts:
                facts.append(fact)
                break
            tries += 1
    return facts

def save_facts_to_file(facts, filename="number_facts.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for fact in facts:
            file.write(fact + "\n")
    print(f" {filename}")

if __name__ == "__main__":
    num_facts = random.randint(3, 10)
    numbers = random.sample(range(1, 10), num_facts)
    facts = get_number_unique_facts(numbers, 6)
    save_facts_to_file(facts)



