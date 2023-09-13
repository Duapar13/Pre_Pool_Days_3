input = "This is a test. is it possible to fly? Good things come to those who never give up."
sentences = input.replace('?', '.').split('. ')
s1, s2, s3 = [sentence.split()[0] for sentence in sentences[:3]]
print(s1, s2, s3)