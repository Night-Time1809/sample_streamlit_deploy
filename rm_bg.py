from rembg import remove

def rm_bg_fn(image):
    rm_img = remove(image)
    return rm_img