from PIL import Image

SCREEN = "./fullscreen_gray.png"
SCREEN2 = "fullscreen_half_stamina_gray.png"

# POS = (840, 140, 1060, 170) # stamina
POS = (950, 140, 1060, 170) # half stamina
# POS = (1070, 760, 1200, 850) # skill
# POS = (1075, 870, 1200, 950)
# POS = (1080, 870, 1110, 900)

def crop(output: str):
    # Check speed
    img = Image.open(SCREEN2)   
    cropped = img.crop(POS)
    cropped.save(output)

if __name__ == "__main__":
    crop("./RACE_gray.png")