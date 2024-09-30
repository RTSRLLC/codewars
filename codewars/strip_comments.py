def strip_comments(strng: str, markers: list) -> str:
	print(f"string: {strng}\nmarkers: {markers}\n{'-'*20}")


a = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])  # , 'apples, pears\ngrapes\nbananas')
b = strip_comments('a #b\nc\nd $e f g', ['#', '$'])  # , 'a\nc\nd')
c = strip_comments(' a #b\nc\nd $e f g', ['#', '$'])  # , ' a\nc\nd')
