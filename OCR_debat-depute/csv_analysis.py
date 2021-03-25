import os

#dir_path = os.path.dirname(os.path.abspath(__file__))

def launch_analysis(data_file):
    directory = os.path.dirname(__file__) # parent directory
    path_to_file = os.path.join(directory, 'data', data_file) # target sub-directory
    with open(path_to_file, 'r') as f:
        preview = f.readline()
    print("test: {} dedans".format(preview))

def main():
    launch_analysis('current_mps.csv')

if __name__ == "__main__":
    main()
