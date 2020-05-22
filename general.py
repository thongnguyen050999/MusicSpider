import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project', directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    write_file(queue, base_url)
    write_file(crawled, '')


def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data+'\n')


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file):
    with open(file,'w') as f:
        for l in sorted(links): f.write(l+'\n')