import colorgram

# Extract number of colors from an image.
# colors = colorgram.extract('data/creema-color.jpg', 6)

color_rgb = [(251, 250, 247), (188, 161, 134), (222, 228, 234), (242, 233, 238), (130, 96, 62), (244, 249, 248)]

# for num_of_color in range(len(colors)):
#     color = colors[num_of_color]
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb.append((r, g, b))

print(color_rgb[0][2])

