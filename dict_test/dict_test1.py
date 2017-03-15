CategoryCodeToAgentId = {
    'host': 4,
    'mid': 5,
    'task': 6,
    'db': 7,
    'app': 8,
    'net': 9,
    'test': 3,
    '': 0
}

print CategoryCodeToAgentId.get('db', -1)
print CategoryCodeToAgentId.get('', -1)
