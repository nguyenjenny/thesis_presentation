import glob

import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("slides"))
template = jinja_env.get_template("base.html")

general_vars = {
    "presentation_date": "2021-09-29",
    "presentation_title": "Investigating the determinants of social communication differences in neurodevelopmental disoders",
    "subtitle": "Thesis Defense",
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
    "pink": "#E91E63",
    "light_pink": "#EB9B94",
    "red": "#FC3E00",
    "tan": "#EDE6D4",
    "peach": "#E5CEAE",
    "box_color": "#294F7C",
    "purple": "#563D7C",
    "light_purple": "#B39DDB",
    "green": "#4CAF50",
    "light_green": "#8BC34A",
    "dark_grey": "#414042",

    # Method colours
    "data_processing_color": "#93C8C9",
    "pcorr_color": "#F3A095",
    "sem_color": "#FDCB58",

    # Factor colours
    "demo_color": "#3F4077",
    "anx_color": "#47A5A2",
    "att_color": "#FDB715",
    "iq_color": "#E77E24",
    "rrb_color": "#897BB6",
    "lang_color": "#CE5F57",
    "sen_color": "#60AD45",
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

    "asd_img": "assets/images/ASDDomains.svg",
    "cliff_img": "assets/images/GapCliff.svg",
    "path_model_img": "assets/images/PathModel.svg", 
    "twelve_models_img": "assets/images/TwelveSemModels.svg", 
    "factor_img": "assets/images/Factors.svg", 

    # Method images
    "pond_img": "assets/images/logos/logo_POND.png",
    "sex_dx_plot": "assets/images/SexDx.svg",
    "measures_img": "assets/images/Measures.svg",
    "methods_img": "assets/images/Methods-03.svg", 
    "data_cleaning_img": "assets/images/DataCleaning.svg", 
    "dat_viz_img": "assets/images/DataViz.svg", 
    "pcorr_img": "assets/images/PCorr.svg", 
    "ttest_img": "assets/images/TTest.svg", 
    "sem_img": "assets/images/SEM.svg", 
    "labels_img": "assets/images/Labels.svg", 
    "distill_img": "assets/images/Distill.svg", 

    # SEM
    "sem_scq_combined_img": "assets/sem/SCQ_Combined.svg",
    "sem_abas_combined_img": "assets/sem/ABAS_Combined.svg",  
    "sem_cbcl_combined_img": "assets/sem/CBCL_Combined.svg",
    "multigroup_plot": "assets/sem/sem_multigroup.html",
    "sem_3_measures_plot": "assets/sem/sem_3_measures.html",
    "sem_scq_plot": "assets/sem/sem_scq.html",
    "sem_abas_plot": "assets/sem/sem_abas.html",
    "sem_cbcl_plot": "assets/sem/sem_cbcl.html",


    # Distribution Plots
    "sex_race_plt": "assets/plots/sex_race.svg", 
    "sc_dist_plt": "assets/plots/sc_dist.svg", 
    "factor_dist_plt": "assets/plots/factor_dist.svg", 
    "scq_soc_dist_plt": "assets/plots/scq_soc_dist.svg", 
    "scq_com_dist_plt": "assets/plots/scq_com_dist.svg", 
    "abas_soc_dist_plt": "assets/plots/abas_soc_dist.svg", 
    "abas_com_dist_plt": "assets/plots/abas_com_dist.svg", 
    "cbcl_soc_dist_plt": "assets/plots/cbcl_soc_dist.svg", 

    # gifs
    "rainbow_path": "assets/gifs/RainbowPath.mp4",
    "support_gif": "https://giphy.com/embed/eiADi71GIXWWc2Z8X8",
    "path_gif": "https://giphy.com/embed/CUehYc3mmGfUDXO6pH",
    "stair_gif": "https://giphy.com/embed/lrA5TYCRUjVUFDbJFz",
    "microscope_gif": "https://giphy.com/embed/jSO9vpciheZYmiormq",
    "measure_gif": "https://giphy.com/embed/fo4Wm6nsWAUbdaAIfD",
    "faces_gif": "https://giphy.com/embed/LRncOtkTDSjqeJEWmQ",


   





    # "_img": "assets/images/.svg", 
}

table_vars = {
    "par_char_table_full": "assets/tables/full_participant_char_table.svg",
    "par_char_table": "assets/tables/participant_char_table.svg",
    "ttest_table": "assets/tables/ttest_table.svg",
    "pcorr_table": "assets/tables/corr_table.svg",
    "fit_table": "assets/tables/fit_table.svg",

    # "_table": "assets/tables/_table.htm",
}


jinja_vars = {**general_vars, **color_vars, **home_vars, **image_vars, **table_vars}


html_str = template.render(jinja_vars)
html_file = open("index.html", "w")
html_file.write(html_str)
html_file.close()
