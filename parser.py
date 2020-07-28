import sys

from typing import Tuple


class Parser:
    @staticmethod
    def parse_line(line: str) -> Tuple[str, dict]:
        """
        Parses a line in csv format to extract person info

        Args:
            line: Line in csv formt to be parsed
    
        Returns:
            (email, person): Tuple of person email and dictionary of person details
        """
        email, first_name, last_name, birth, gender = line.split(",")
        person = {
            "first_name": first_name,
            "last_name": last_name,
            "birth": birth,
            "gender": gender,
        }
        return email, person

    @staticmethod
    def read_file(filepath: str) -> dict:
        """
        Reads a csv file extracting people's information

        Args:
            filepath: Full path to csv file
    
        Returns:
            people: Dictionary indexed by email containing every person's details
        
        Raises:
            RuntimeError: Raises if file extension is not csv
        """
        if not filepath.endswith(".csv"):
            raise RuntimeError("File extension must be .csv")

        people = {}
        with open(filepath) as csv:
            for line in csv:
                email, person = Parser.parse_line(line.rstrip("\n"))
                if email not in people:
                    people[email] = person
                else:
                    print("Ignoring person with duplicate email {}".format(email))
        return people


def main():
    """
    Tries to parse a file. If successfull, prints the resulting entries, otherwise
    terminates with an error code.
    """

    try:
        people = Parser.read_file(sys.argv[1])
        print("\nResult:")
        for email, person in people.items():
            print("{}: {}".format(email, person))
    except RuntimeError as error:
        print(error)
        exit(1)


if __name__ == "__main__":
    main()

