first_name_one = "  JoHn  ."
first_name_two = "  joHn  "

first_name_one = first_name_one.lower().strip()

print(first_name_one[0:4])
first_name_two = first_name_two.strip().lower()
print(first_name_two)

sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

line_one = "The lazy dog ran so fast it hit the wall."
print(line_one.split(";"))
line_onet = len(line_one.split(";"))
print(line_onet)