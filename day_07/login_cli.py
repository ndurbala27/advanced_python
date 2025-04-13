import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="CLI tool with two options")

    # Add two options
    parser.add_argument("-u", "--username", dest="uname", type=str, help="First option (string value)")
    parser.add_argument("-p", "--password", dest="pword", type=str, help="Second option (string value)")

    # Parse arguments
    args = parser.parse_args()

    # Display the results
    print(f"Username: {args.option_a}")
    print(f"Password: {args.option_b}")

if __name__ == "__main__":
    main()
