import pickle


def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def reload_object(filename):
    with open(filename, 'rb') as input:
        character = pickle.load(input)
        return character