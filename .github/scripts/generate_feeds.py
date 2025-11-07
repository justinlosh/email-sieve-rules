import os
import json
from glob import glob

def read_csv_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def collect_domains_data(domains_dir):
    domains = {}
    for domain_folder in os.listdir(domains_dir):
        folder_path = os.path.join(domains_dir, domain_folder)
        if os.path.isdir(folder_path):
            domain_data = {}
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if file.endswith('.csv'):
                    domain_data[file] = read_csv_to_list(file_path)
                elif file.endswith('.json'):
                    domain_data[file] = read_json(file_path)
            domains[domain_folder] = domain_data
    return domains

def collect_lists_data(lists_dir):
    lists = {}
    for list_folder in os.listdir(lists_dir):
        folder_path = os.path.join(lists_dir, list_folder)
        if os.path.isdir(folder_path):
            list_data = {}
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if file.endswith('.csv'):
                    list_data[file] = read_csv_to_list(file_path)
                elif file.endswith('.json'):
                    list_data[file] = read_json(file_path)
            lists[list_folder] = list_data
    return lists

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    domains_dir = os.path.join(base_dir, 'data', 'domains')
    lists_dir = os.path.join(base_dir, 'data', 'lists')
    feed_dir = os.path.join(base_dir, 'feed')
    os.makedirs(feed_dir, exist_ok=True)

    domains_data = collect_domains_data(domains_dir)
    lists_data = collect_lists_data(lists_dir)

    # Write domains.json
    with open(os.path.join(feed_dir, 'domains.json'), 'w', encoding='utf-8') as f:
        json.dump(domains_data, f, indent=2, ensure_ascii=False)

    # Write lists.json
    with open(os.path.join(feed_dir, 'lists.json'), 'w', encoding='utf-8') as f:
        json.dump(lists_data, f, indent=2, ensure_ascii=False)

    # Write feed.json (all data)
    feed = {
        'domains': domains_data,
        'lists': lists_data
    }
    with open(os.path.join(feed_dir, 'feed.json'), 'w', encoding='utf-8') as f:
        json.dump(feed, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
