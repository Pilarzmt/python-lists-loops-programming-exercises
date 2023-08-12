all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(colors):
    return filter(lambda color: color["sexy"], colors)

def generate_li(color):
    return f"<li>{color['label']}</li>"
sexy_colors = filter_colors(all_colors)
li_elements = map(generate_li, sexy_colors)
html = list(li_elements)
print(html)

