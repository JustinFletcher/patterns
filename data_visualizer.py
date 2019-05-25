import argparse

import numpy as np

from matplotlib import pyplot as plt


def main(FLAGS):

    some_data = np.random.rand(256, 256)

    print(FLAGS.data_dir)

    plt.matshow(some_data)

    plt.show()


if __name__ == '__main__':

    # Instantiates an arg parser
    parser = argparse.ArgumentParser()

    # Establishes default arguments
    parser.add_argument("--data_dir",
                        type=str,
                        default="C:\\my\\data\\path\\",
                        help="The complete desired input filepath.")

    # Parses known arguments
    FLAGS, unparsed = parser.parse_known_args()

    # Runs the tensorflow app
    main(FLAGS)
