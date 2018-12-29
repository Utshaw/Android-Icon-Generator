from PIL import Image
import os



imgName = "ic_launcher.png"
img = Image.open(imgName)
LINE_SEPARATOR = '/'

drawable_folders = ["drawable-xxxhdpi" + LINE_SEPARATOR,  "drawable-xxhdpi" + LINE_SEPARATOR, "drawable-xhdpi" + LINE_SEPARATOR, "drawable-hdpi" + LINE_SEPARATOR, "drawable-mdpi" + LINE_SEPARATOR]
mipmap_folders = ["mipmap-xxxhdpi" + LINE_SEPARATOR,  "mipmap-xxhdpi" + LINE_SEPARATOR, "mipmap-xhdpi" + LINE_SEPARATOR, "mipmap-hdpi" + LINE_SEPARATOR, "mipmap-mdpi" + LINE_SEPARATOR]

#                 xxxhdpi       xxhdpi    xhdpi     hdpi      mdpi
drawable_sizes = [(192, 192),(144, 144),(96, 96),(72, 72),(48, 48)]
google_play_store_size = (512, 512)

icon_sizes = [(96, 96),(72, 72),(48, 48),(36, 36),(24, 24)]

res_xxxhdpi =   (192, 192) #xxxhdpi
res_xxhdpi = (144, 144)  #xxhdpi
res_xhdpi = (96, 96)  #xhdpi
res_hdpi = (72, 72)  #hdpi
res_mdpi = (48, 48)  #mdpi



current_path = os.path.dirname(os.path.abspath(__file__)) +  LINE_SEPARATOR




def make_mipmaps():
    i = 0
    for folder in mipmap_folders:
        if not os.path.exists(current_path + folder):
            os.makedirs(current_path + folder)

        img.resize(drawable_sizes[i]).save(folder + imgName)
        i+=1
    google_play_store_folder = "Google-Play-Store"
    if not os.path.exists(current_path + google_play_store_folder):
        os.makedirs(current_path + google_play_store_folder)
    img.resize(google_play_store_size).save(google_play_store_folder + LINE_SEPARATOR +  "google_play_store_launcher_512.png" )



def make_drawables():
    i = 0
    for folder in drawable_folders:

        if not os.path.exists(current_path + folder):
            os.makedirs(current_path + folder)

        img.resize(icon_sizes[i]).save(folder + imgName)
        i+=1    





def main():
    imgName = input('Enter  full image name (with extension): ')
    print('Image name: ', imgName)


    

    while True:
        drawableOrMipMap = input('Do you want to generate drawable or mipmap[D/M] ')[0]
        if (drawableOrMipMap == 'd' or drawableOrMipMap == 'D'):
            drawableOrMipMap = 'Drawable'
            break
        elif(drawableOrMipMap == 'm' or drawableOrMipMap == 'M'):
            drawableOrMipMap = 'Mipmap'
            break
    print('You need: ', drawableOrMipMap)

    while True:
        os = input('Is your operating system Windows or Unix based[W/U] ')[0]
        if (os == 'w' or os == 'W'):
            os = 'Windows'
            LINE_SEPARATOR = '\\'
            break
        elif(os == 'u' or os == 'U'):
            os = 'Unix'
            LINE_SEPARATOR = '/'
            break
    print('Your opearting system: {0} based'.format(os))

    print('Generating icons ...')
    if (drawableOrMipMap == 'Drawable'):
        make_drawables()
    else:
        make_mipmaps()

    


if __name__ == '__main__':
    main()









