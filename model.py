import json
import rules

with open('data.json') as f:
    data = json.load(f)

latest_index = rules.latest_financial_index(data)
average_value = rules.calculate_average(data, 'value')
minimum_value = rules.calculate_minimum(data, 'value')
maximum_value = rules.calculate_maximum(data, 'value')

result = {
    'latest_financial_index': latest_index,
    'average_value': average_value,
    'minimum_value': minimum_value,
    'maximum_value': maximum_value
}

print(json.dumps(result))
