import re

def ips_between(start: str, end: str) -> int:
    """
    Calculates the number of IP addresses between two IP addresses.

    Args:
        start (str): The start IP address.
        end (str): The end IP address.

    Returns:
        int: The number of IP addresses between the two IP addresses.

    Raises:
        ValueError: If the IP addresses are not in the correct format.

    """
    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", start):
        raise ValueError("Invalid IP address: {}".format(start))

    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", end):
        raise ValueError("Invalid IP address: {}".format(end))

    powers = [256 ** 3, 256 ** 2, 256, 1]
    return sum([j * i for j, i in zip([int(i) for i in end.split(".")], powers)]) - sum(
            [j * i for j, i in zip([int(i) for i in start.split(".")], powers)])


a = ips_between("10.0.0.0", "10.0.0.50")  # , 50)
b = ips_between("20.0.0.10", "20.0.1.0")  # , 246)

# [10, 0, 0, 0]
# [10, 0, 0, 50]
# [20, 0, 0, 10]
# [20, 0, 1, 0]
