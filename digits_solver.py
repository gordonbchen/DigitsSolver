import itertools


def get_answer(num_chains, operation_chains, target):
    for num_chain in num_chains:
        for operation_chain in operation_chains:

            x = num_chain[0]
            for n_operation in range(len(operation_chain)):
                operation = operation_chain[n_operation]
                number = num_chain[1 + n_operation]
                
                if (operation == "+"):
                    x += number
                elif (operation == "-"):
                    if (x >= number):
                        x -= number
                    else:
                        break
                elif (operation == "*"):
                    x *= number
                else:
                    if (x % number == 0):
                        x /= number
                    else:
                        break

                if (x == target):
                    answer = f"{num_chain[0]}"
                    for n in range(n_operation + 1):
                        answer += str(operation_chain[n])
                        answer += str(num_chain[n + 1])
                    return answer


# Operation chains.
operation_chains = list(itertools.product(list("+-*/"), repeat=5))

# Get nums.
ans = input("Numbers (1, 2, 3): ")
nums = [int(num) for num in ans.split(", ")]

num_chains = list(itertools.permutations(nums, r=6))

# Get target.
target = int(input("Target: "))

# Find solution.
answer = get_answer(num_chains, operation_chains, target)
print(answer)