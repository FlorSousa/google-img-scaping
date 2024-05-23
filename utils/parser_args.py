import argparse

def parser_args():
    parser = argparse.ArgumentParser(
        description='Tracks mice.'
    )

    parser.add_argument(
        '-s', type=str,help='url to scrap'
    )
    
    parser.add_argument(
        '-b', type=str,help='driver to selenium',default="chrome"
    )
    
    parser.add_argument(
        '-d', type=str,help='driver version'
    )
    
    parser.add_argument(
        '-dd', type=str,help="download driver",default="y"
    )
    
    
    return parser.parse_args()