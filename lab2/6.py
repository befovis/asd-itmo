def find_max_crossing_subarray(prices_change, low, mid, high):
    left_sum = float('-inf')
    sum_left = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        sum_left += prices_change[i]
        if sum_left > left_sum:
            left_sum = sum_left
            max_left = i

    right_sum = float('-inf')
    sum_right = 0
    max_right = mid + 1

    for j in range(mid + 1, high + 1):
        sum_right += prices_change[j]
        if sum_right > right_sum:
            right_sum = sum_right
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(prices_change, low, high):
    if low == high:
        return low, high, prices_change[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(prices_change, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(prices_change, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(prices_change, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def analyze_stock_prices(prices, dates):
    # Вычисляем изменения цен акций по дням
    prices_change = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    # Ищем подмассив с максимальной суммой
    buy_index, sell_index, max_profit = find_maximum_subarray(prices_change, 0, len(prices_change) - 1)

    # Даты покупки и продажи
    buy_date = dates[buy_index]
    sell_date = dates[sell_index + 1]  # sell_index + 1, так как изменения цен между днями

    return buy_date, sell_date, max_profit


if __name__ == "__main__":
    # Для примера используем данные акций и даты
    company_name = "Sample Corp"
    dates = ["2024-09-01", "2024-09-02", "2024-09-03", "2024-09-04", "2024-09-05", "2024-09-06"]
    prices = [100, 102, 101, 99, 98, 105]  # Цены акций на соответствующие даты

    buy_date, sell_date, max_profit = analyze_stock_prices(prices, dates)

    # Выводим результаты в файл
    with open("output", "w") as file:
        file.write(f"Компания: {company_name}\n")
        file.write(f"Дата покупки: {buy_date}\n")
        file.write(f"Дата продажи: {sell_date}\n")
        file.write(f"Максимальная прибыль: {max_profit}\n")
