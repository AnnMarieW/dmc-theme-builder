import colorsys

LIGHTNESS_MAP = [0.96, 0.907, 0.805, 0.697, 0.605, 0.547, 0.518, 0.445, 0.395, 0.34]
SATURATION_MAP = [0.32, 0.16, 0.08, 0.04, 0, 0, 0.04, 0.08, 0.16, 0.32]


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255)
    )


def get_closest_lightness(hsl_color):
    lightness_goal = hsl_color[2]
    closest_lightness = min(LIGHTNESS_MAP, key=lambda l: abs(l - lightness_goal))
    return closest_lightness


def generate_colors_map(hex_color):
    rgb_color = hex_to_rgb(hex_color)
    hsl_color = colorsys.rgb_to_hls(*rgb_color)
    closest_lightness = get_closest_lightness(hsl_color)
    base_color_index = LIGHTNESS_MAP.index(closest_lightness)
    print(closest_lightness, base_color_index)

    colors = []
    for i, l in enumerate(LIGHTNESS_MAP):
        new_hsl = (hsl_color[0], l, hsl_color[2])

        saturation_delta = SATURATION_MAP[i] - SATURATION_MAP[base_color_index]
        new_saturation = (
            hsl_color[2] + saturation_delta
            if saturation_delta >= 0
            else hsl_color[2] - abs(saturation_delta)
        )
        new_hsl = (hsl_color[0], l, new_saturation)

        new_rgb = colorsys.hls_to_rgb(*new_hsl)
        colors.append(rgb_to_hex(new_rgb))

    return base_color_index, colors


def generate_colors(hex_color):
    base_color_index, colors = generate_colors_map(hex_color)
    return base_color_index, colors
