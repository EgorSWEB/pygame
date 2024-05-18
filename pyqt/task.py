import datetime

def add(name, body, filepath='table.txt'):
    file = open(filepath, 'a+', encoding="utf-8")
    file.write(name + '|' + body + '|' + str(datetime.datetime.now()) + '\n')
    file.close()
    return True

def all(filepath='table.txt'):
    file = open(filepath, 'a+', encoding="utf-8")
    file.seek(0)
    results = []
    for line in file:
        arr = line.split('|')
        results.append({
            'name': arr[0],
            'body': arr[1],
            'date': arr[2]
        })
    file.close()
    return results

def find(name, filepath='table.txt'):
    file = open(filepath, 'a+', encoding="utf-8")
    found = False
    result = {}
    for line in file:
        if line.find(name + '|') == 0:
            arr = line.split('|')
            result['name'] = arr[0]
            result['body'] = arr[1]
            result['date'] = arr[2]
            found = True
            file.close()
            return result
            
    if not found:
        file.close()
        return result
    
def delete(name, filepath='table.txt'):
    file = open(filepath, 'a+', encoding="utf-8")
    file.seek(0)
    found = False
    for line in file:
        if line.find(name + '|') == 0:
            found = True
            f = open(filepath, 'r', encoding="utf-8")
            file_text = f.read()
            f.close()
            f = open(filepath, 'w', encoding="utf-8")
            f.write(file_text.replace(line, ''))
            f.close()
            file.close()
            return True

    if not found:
        file.close()
        return False
    
def edit(name, body, filepath='table.txt'):
    file = open(filepath, 'a+', encoding="utf-8")
    found = False
    for line in file:
        if line.find(name + '|') == 0:
            found = True
            f = open(filepath, 'r', encoding="utf-8")
            file_text = f.read()
            f.close()
            f = open(filepath, 'w', encoding="utf-8")
            f.write(file_text.replace(line, name + '|' + body + '|' + str(datetime.datetime.now()) + '\n'))
            f.close()
            file.close()
            return True

    if not found:
        file.close()
        return False