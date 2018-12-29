from PIL import Image
import os



imgName = "ic_launcher.png"
img = Image.open(imgName)

drawable_folders = ["drawable-xxxhdpi\\",  "drawable-xxhdpi\\", "drawable-xhdpi\\", "drawable-hdpi\\", "drawable-mdpi\\"]
mipmap_folders = ["mipmap-xxxhdpi\\",  "mipmap-xxhdpi\\", "mipmap-xhdpi\\", "mipmap-hdpi\\", "mipmap-mdpi\\"]

#                 xxxhdpi       xxhdpi    xhdpi     hdpi      mdpi
drawable_sizes = [(192, 192),(144, 144),(96, 96),(72, 72),(48, 48)]
google_play_store_size = (512, 512)

icon_sizes = [(96, 96),(72, 72),(48, 48),(36, 36),(24, 24)]

res_xxxhdpi =   (192, 192) #xxxhdpi
res_xxhdpi = (144, 144)  #xxhdpi
res_xhdpi = (96, 96)  #xhdpi
res_hdpi = (72, 72)  #hdpi
res_mdpi = (48, 48)  #mdpi


# img.resize(res_xxxhdpi).save(drawable_xxxhdpi + imgName)

current_path = os.path.dirname(os.path.abspath(__file__)) +  "\\"


#mipmaps-launcher-icon
i = 0
for folder in mipmap_folders:
    if not os.path.exists(current_path + folder):
        os.makedirs(current_path + folder)

    img.resize(drawable_sizes[i]).save(folder + imgName)
    i+=1
google_play_store_folder = "Google-Play-Store"
if not os.path.exists(current_path + google_play_store_folder):
    os.makedirs(current_path + google_play_store_folder)
img.resize(google_play_store_size).save(google_play_store_folder + "\\google_play_store_launcher_512.png" )




#drawables
# i = 0
# for folder in drawable_folders:

#     if not os.path.exists(current_path + folder):
#         os.makedirs(current_path + folder)

#     img.resize(icon_sizes[i]).save(drawable_folders[i] + imgName)
#     i+=1












