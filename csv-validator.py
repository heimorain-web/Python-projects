import csv
import re
import sys

REQUIRED_COLUMNS = {"id", "name", "email"}

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def validate_csv(file_name):
    valid_count = 0
    rejected_count = 0
    seen_ids = set()

    try:
        with open(
            file_name, "r", newline="", encoding="utf-8-sig"
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV file is empty or has no header.")
                return

            headers = {
                header.strip()
                for header in reader.fieldnames
                if header
            }

            missing_columns = REQUIRED_COLUMNS - headers

            if missing_columns:
                print(
                    "Error: Missing required columns: "
                    + ", ".join(sorted(missing_columns))
                )
                return

            for line_number, row in enumerate(reader, start=2):
                row = {
                    (key.strip() if key else ""):
                    (value.strip() if value else "")
                    for key, value in row.items()
                }

                errors = []
                customer_id = row.get("id", "")
                name = row.get("name", "")
                email = row.get("email", "")

                if not customer_id:
                    errors.append("Missing ID")
                elif customer_id in seen_ids:
                    errors.append("Duplicate ID")
                else:
                    seen_ids.add(customer_id)

                if not name:
                    errors.append("Missing name")

                if not EMAIL_PATTERN.fullmatch(email):
                    errors.append("Invalid email")

                if errors:
                    rejected_count += 1
                    print(
                        f"Line {line_number}: "
                        + ", ".join(errors)
                    )
                else:
                    valid_count += 1

    except FileNotFoundError:
        print(f"Error: CSV file not found: {file_name}")
        return

    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Could not read the CSV file: {error}")
        return

    print("\nValidation Summary")
    print(f"Valid rows: {valid_count}")
    print(f"Rejected rows: {rejected_count}")


if __name__ == "__main__":
    file_name = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "sample_customers.csv"
    )
    validate_csv(file_name)
