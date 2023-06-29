import re

INPUT_FILENAME = 'input.txt'


def get_shift_info(shift_string: str) -> tuple[str, int]:
    pattern = r'(.+) (\d+)'
    match = re.match(pattern, shift_string)

    if not match:
        raise ValueError(f"'{shift_string}' - This is invalid input string")

    employee_name = match.group(1)
    hours = int(match.group(2))

    return employee_name, hours


class EmployeeService:
    def __init__(self):
        self._storage: dict[str, list[int]] = dict()

    def add_shift(self, employee_name: str, hours: int):
        try:
            self._storage[employee_name].append(hours)
        except KeyError:
            self._storage[employee_name] = [hours]

    def get_sum_hours_by_name(self, employee_name: str) -> int:
        return sum(self._storage[employee_name])

    def get_info_by_name(self, employee_name: str) -> tuple[str, list[int], int]:
        return employee_name, self._storage[employee_name], self.get_sum_hours_by_name(employee_name)

    def get_info(self) -> list[tuple]:
        return [self.get_info_by_name(employee_name) for employee_name in self._storage]


def main():
    service = EmployeeService()
    # Read the input data from file
    with open(INPUT_FILENAME, "r") as file:
        for shift in file:
            # Parse input line
            shift_tuple = get_shift_info(shift)
            # Add shift to service
            service.add_shift(*shift_tuple)

    # Get required data in raw format
    info_tuples = service.get_info()
    # Format string
    info_strings = [f"{info[0]}: {', '.join(map(str, info[1]))}; sum: {info[2]}" for info in info_tuples]
    print(*info_strings, sep="\n")


if __name__ == "__main__":
    main()
