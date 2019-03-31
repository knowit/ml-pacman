import pickle

def save_pickle(file_path_without_extension, data, feedback=True):
    """
    Save data to a pickle file
    :param file_path_without_extension: path of save location with .pkl omitted
    :param data: data to be saved
    """
    with open(file_path_without_extension + '.pkl', 'wb') as f:
        pickle.dump(data, f)

    if feedback:
        print('Done pickling %s' % file_path_without_extension)


def load_pickle(file_path, feedback=False):
    """
    Load data from pickle file
    :param file_path: path to .pkl file
    :param feedback: if True print messages indicating when loading starts and finishes
    :return: data from pickle file
    """
    if feedback:
        print('Loading %s', file_path)

    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    if feedback:
        print('Done loading pickle')

    return data