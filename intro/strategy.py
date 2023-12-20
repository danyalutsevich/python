inputData = [1, 2, 3, 4, 5]


def calculate(data, *lambdas):
    results = []
    for lamb in lambdas:
        results.append(lamb(data))
    return min(results)


result = calculate(
    inputData,
    lambda input: sum(input),
    lambda input: max(input),
    lambda input: min(input),
)

print(result)
