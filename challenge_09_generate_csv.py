"""
use Faker generate csv
"""
import csv

from faker import Faker
from faker.generator import random

fake = Faker()


def generate_age():
    return random.randint(1, 100)


def generate_gender():
    return fake.random_element(elements=("Male", "Female", "Other"))


if __name__ == '__main__':
    with open("random_data.csv", "w", newline='') as csv_file:
        fieldnames = ["Name", "Age", "Gender"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(1000):
            writer.writerow({'Name': fake.name(), 'Age': generate_age(), 'Gender': generate_gender()})
