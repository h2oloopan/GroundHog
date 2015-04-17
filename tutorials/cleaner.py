import argparse

def main(parser):
    o = parser.parse_args()
    subtitle = o.path
    print subtitle

def get_cleaner():
    usage = """There is only one argument which is the path to the subtitle file youu want to clean"""
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('path', default='subtitle', help=('path to the subtitle file'))
    return parser

if __name__ == '__main__':
    main(get_cleaner())
