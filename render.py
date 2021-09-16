import glob

import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("slides"))
template = jinja_env.get_template("base.html")

general_vars = {
    "presentation_date": "2021-09-16",
    "presentation_title": "Investigating the determinants of social communication difficulties in ASD",
    "subtitle": "Thesis Progress",
    "contact_text": "Contact Me",
    "presentation_width": 1300,
    "presentation_height": 700,
    "email": "nguyenpjenny@gmail.com",
}

color_vars = {
    "blue": "#5073B3",
    "aqua_blue": "#015D8E",
    "baby_blue": "#80DEEA",
    "mustard": "#E58D05",
    "pink": "#EB9B94",
    "red": "#FC3E00",
    "tan": "#EDE6D4",
    "peach": "#E5CEAE",
    "box_color": "#294F7C",
    "purple": "#563D7C",
    "light_purple": "#B39DDB",
    "green": "#4CAF50",
    "light_green": "#8BC34A",

    # Method colours
    "data_processing_color": "#93C8C9",
    "pcorr_color": "#F3A095",
    "sem_color": "#FDCB58",
}

logos = glob.glob(r"assets/images/logos/logo_*.png")
logos = [i.replace("\\", "/") for i in logos]

home_vars = {
    "logos": logos,
    "jenny_avatar": "assets/images/jennyn_theme/jenny_icon.svg",
    "mugsy_avatar": "assets/images/jennyn_theme/mugsy_icon.svg",
    "home_bg": "assets/images/jennyn_theme/geometric_orange_bg.svg",
}

image_vars = {
    # Image folder
    "image_folder": "assets/images/",

    # Introduction images
    "cliff_img": "assets/images/GapCliff.svg",
    "path_model_img": "assets/images/PathModel.svg", 
    "twelve_models_img": "assets/images/TwelveSemModels.svg", 
    "factor_img": "assets/images/Factors.svg", 

    # Method images
    "pond_img": "assets/images/logos/logo_POND.png",
    "measures_img": "assets/images/Measures.svg",
    "methods_img": "assets/images/Methods.svg", 
    "data_cleaning_img": "assets/images/DataCleaning.svg", 
    "dat_viz_img": "assets/images/DataViz.svg", 
    "pcorr_img": "assets/images/PCorr.svg", 
    "ttest_img": "assets/images/TTest.svg", 
    "sem_img": "assets/images/SEM.svg", 
    "labels_img": "assets/images/Labels.svg", 
    "distill_img": "assets/images/Distill.svg", 



    # "_img": "assets/images/.svg", 
}


jinja_vars = {**general_vars, **color_vars, **home_vars, **image_vars}


html_str = template.render(jinja_vars)
html_file = open("index.html", "w")
html_file.write(html_str)
html_file.close()
