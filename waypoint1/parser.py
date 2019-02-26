from argparse import ArgumentParser


def do_argparse():
    """ do the argparse and return the path argument """
    parser = ArgumentParser()
    parser.add_argument('--path', help='The root directory to'
                        ' start scanning for duplicate files.')
    args = parser.parse_args()
    path = args.path
    return path