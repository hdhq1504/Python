def convert_text(num):
  word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  text = []
  for num in str(num):
    text.append(word[int(num)])
  return " ".join(text)
  
n = int(input())

print(convert_text(n))