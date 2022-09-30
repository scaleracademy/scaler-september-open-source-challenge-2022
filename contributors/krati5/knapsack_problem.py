"""main function"""


def knapsack_problem(weight_arr, value_arr, w_cap, n_items):
    """
    Returns maximum output
    """

    dp_dict = [[-1 for j in range(w_cap + 1)] for i in range(n_items + 1)]

    for j in range(w_cap + 1):
        dp_dict[0][j] = 0

    for i in range(n_items + 1):
        dp_dict[i][0] = 0

    for i in range(1, n_items + 1):
        for j in range(1, w_cap + 1):

            if weight_arr[i - 1] <= j:
                dp_dict[i][j] = max(
                    value_arr[i - 1] + dp_dict[i - 1][j - weight_arr[i - 1]],
                    dp_dict[i - 1][j],
                )

            else:
                dp_dict[i][j] = dp_dict[i - 1][j]

    return dp_dict[n_items][w_cap]


if __name__ == "__main__":
    value = [60, 100, 120]
    weight = [10, 20, 30]
    N = len(value)

    W = 50  # Capacity
    print(
        "Dynamic Programming Top-Down Approach: ",
        knapsack_problem(weight, value, W, N),
    )
