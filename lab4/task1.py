import json


def task():
    with open("input.json", "r") as f:
        d = json.load(f)

    summ = sum(item["score"] * item["weight"] for item in d)
    rounded_summ = round(summ, 3)

    return rounded_summ


if __name__ == "__main__":
    print(task())
