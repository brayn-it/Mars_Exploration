import PIL.Image
import PIL.ImageFilter

#LES COULEURS UTILISEES TOUT AU LONG DU PROJET4

colors = {"button_bg":"#3EACC3","border":"#8BE4F7",
          "text1":"#8BE4F7","bg1":"#0C1B1E",
          "bg2":"#2B2B2B","bg3":"#003946"}

bg_img = PIL.Image.open("IHM/background_img/app_bg2.jpg")
bg_img = bg_img.resize((1920,1080))

#ICONES
power_icon = PIL.Image.open("IHM/icons/power-icon.png").resize((32,32))
home_icon = PIL.Image.open("IHM/icons/home-icon.png").resize((32,32))
datasheet_icon = PIL.Image.open("IHM/icons/datasheet-icon.png").resize((32,32))

right_arrow_icon = PIL.Image.open("IHM/icons/right-arrow-icon.png").resize((32,32))
left_arrow_icon = PIL.Image.open("IHM/icons/left-arrow-icon.png").resize((32,32))
#PIL.ImageFilter.GaussianBlur(3)
bg_img = bg_img.filter(PIL.ImageFilter.GaussianBlur(3))