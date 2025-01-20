import unittest
import sys

def main():
    suite = unittest.TestLoader().discover('tests/aius/unit_tests')
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    main()