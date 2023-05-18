import pickle

def compare_pkl_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        obj1 = pickle.load(f1)
        obj2 = pickle.load(f2)

    return obj1 == obj2  # Compare the loaded objects

# Example usage
file1 = "C:\\Users\\willi\\.cache\\torch\\hub\\checkpoints\\shufflenetv2k30-210511-120906-animal.pkl.epoch400"
file2 = "C:\\Users\\willi\\.cache\\torch\\hub\\checkpoints\\shufflenetv2k16-210820-232500-cocokp-slurm726069-edge513-o10s-7189450a.pkl"
are_equal = compare_pkl_files(file1, file2)
print(f"Are the files equal? {are_equal}")