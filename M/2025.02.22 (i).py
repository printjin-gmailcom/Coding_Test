def process_lists(a, b):
    for _ in range(3):
        a = [x + 1 if a.count(x) == 1 else x for x in a]
        b = [x for x in b if x not in a]
    return a


def allocate_servers(n, user, special_user):
    servers = [0] * n  
    users = []
    total_user_wait_time = 0  
    total_special_wait_time = 0 
    special_user.sort(key=lambda x: x[0]) 
    user.sort(key=lambda x: x[0]) 
    for arrival, use in special_user:
        users.append((arrival, use, 'special'))
    for arrival, use in user:
        users.append((arrival, use, 'user'))
    result = []
    for arrival_time, use_time, user_type in users:
        for i in range(n):
            if servers[i] <= arrival_time:
                allocated_time = max(arrival_time, servers[i])
                servers[i] = allocated_time + use_time
                wait_time = allocated_time - arrival_time
                if user_type == 'user':
                    total_user_wait_time += wait_time
                else:
                    total_special_wait_time += wait_time
                result.append([arrival_time, use_time, user_type]) 
                break
    return total_user_wait_time, total_special_wait_time


def count_valid_lists(n, k, q):
    possible_values = [[] for _ in range(k)]
    q.sort(key=lambda x: x[0])
    for x, y in q:
        for idx in range(k):
            valid_values = [num for num in range(1, n+1) if num >= x]
            possible_values[idx] = list(set(possible_values[idx]) & set(valid_values)) if possible_values[idx] else valid_values
    result = [len(values) for values in possible_values]
    return result


def search_count(data, search):
    search_keywords = search[0].split()
    pairs = [search_keywords[i:i+2] for i in range(0, len(search_keywords), 2)]
    total_count = 0
    filtered_data = data
    for keywords in pairs:
        filtered_data = [item for item in filtered_data if all(keyword in item for keyword in keywords)]
        total_count += len(filtered_data)
    return total_count