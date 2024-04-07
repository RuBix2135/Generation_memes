from PIL import Image, ImageDraw, ImageFont
print('Генератор мемов запущен!')
top_text = input('Введите текст, который будет отображаться сверху')
bottom_text = input('Введите текст, который будет отображаться снизу')
print('Список картинок:')
print('1. Кот в ресторане')
print('2. Кот в очках')
print('3. Гусь')
print('4. Роберт Дауни мл.')
print('5. Сквидвард')
image_number = int(input('Введите номер наиболее подходящей картинки'))
if image_number == 1:
    image_file = 'Кот в ресторане.png'
elif image_number == 2:
    image_file = 'Кот в очках.png'
elif image_number == 3:
    image_file = 'Гусь.png'
elif image_number == 4:
    image_file = 'Роберт Дауни мл.png'
elif image_number == 5:
    image_file = 'Сквидвард.png'

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size = 70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width)/2, 10), top_text, font = font, fill = 'white')

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width)/2, height - text_height - 10), bottom_text, font = font, fill = 'white')

image.save('new_meme.jpg')