def latest_financial_index(data):
  
    return data.get('financial_indices')[-1]

def calculate_average(data, key):
    
    values = [entry[key] for entry in data.get('financial_indices')]
    return sum(values) / len(values)

def calculate_minimum(data, key):
    
    values = [entry[key] for entry in data.get('financial_indices')]
    return min(values)

def calculate_maximum(data, key):
    
    values = [entry[key] for entry in data.get('financial_indices')]
    return max(values)
