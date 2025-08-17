# import modules
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QHBoxLayout, QMessageBox, QVBoxLayout, QLabel, QPushButton, QComboBox, QListWidget, QCheckBox, QFileDialog, QLineEdit
import os
from PyQt5.QtGui import QPixmap, QIcon, QFont, QFontDatabase
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt, QSize


# create a class
class PicEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.images_dir = None
        self.images_list = []
        self.original_image = None
        self.work_on_image = None
        self.image_name = None
        self.save_dir = "Edited_Images/"
        self.setObjectName("body")

        genos_font_id = QFontDatabase.addApplicationFont('fonts/Genos-VariableFont_wght.ttf')
        pacifico_font_id = QFontDatabase.addApplicationFont('fonts/Pacifico-Regular.ttf')
        zain_font_id  = QFontDatabase.addApplicationFont('fonts/Zain-Regular.ttf') 

        genos_family = QFontDatabase.applicationFontFamilies(genos_font_id)[0]
        zain_family =  QFontDatabase.applicationFontFamilies(zain_font_id)[0]
        pacifico_family =  QFontDatabase.applicationFontFamilies(pacifico_font_id)[0]

        genos_font = QFont(genos_family)
        zain_font = QFont(zain_family)
        pacifico_font = QFont(pacifico_family)



        # --- Create widgets and layouts ---

        # The main container for the glassmorphism effect
        self.glass_morphed_container = QWidget()
        self.glass_morphed_container.setObjectName('glass_morphed_container')


        # # the layout widget to hold the two containers
        self.master_row = QHBoxLayout(self)
        self.master_row.addWidget(self.glass_morphed_container)
        
        # The main layout to hold the master row
        self.main_row = QHBoxLayout(self.glass_morphed_container)

        # --- LEFT COLUMN (Column 1) Widgets and Layout ---

        # This holds the select directory button and subcol1
        self.col1 = QVBoxLayout()
        
        # This container holds the widgets in the first column
        self.subcol1_container = QWidget()
        self.subcol1_container.setObjectName('subcol1_container')
        
        # Pass the container widget to the layout constructor
        self.subcol1 = QVBoxLayout(self.subcol1_container)
        
        self.choose_directory_btn = QPushButton("Select Directory")
        self.choose_directory_btn.setObjectName('choose_directory_btn')
        self.choose_directory_btn.setFont(genos_font)
        hand_icon = QIcon('images/dir.png')
        self.choose_directory_btn.setIcon(hand_icon)
        self.choose_directory_btn.setIconSize(QSize(30,30))

        self.choose_file_label = QLabel("Select Image")
        self.choose_file_label.setFont(zain_font)
        self.choose_file_label.setObjectName('choose_file_label')
        self.image_select_list = QListWidget()
        self.choose_filter_label = QLabel("Choose a filter")
        self.choose_filter_label.setFont(zain_font)
        self.choose_filter_label.setObjectName('choose_filter_label')
        self.filter_list = QComboBox()
        self.filter_list.setObjectName('filter_list')
        self.choose_save_dir_label = QLabel("Enter directory to save image")
        self.choose_save_dir_label.setFont(zain_font)
        self.choose_save_dir_label.setObjectName('choose_save_dir_label')
        self.save_dir_input = QLineEdit()
        self.save_dir_input.setObjectName('save_dir_input')
        self.save_row = QHBoxLayout()

        self.choose_save_dir_btn = QPushButton()
        self.choose_save_dir_btn.setObjectName('choose_save_dir_btn')
        folder_icon = QIcon('images/folder.png')
        self.choose_save_dir_btn.setIcon(folder_icon)

        self.save_image_btn = QPushButton("Save Image")
        self.save_image_btn.setObjectName('save_image_btn')
        self.save_image_btn.setFont(genos_font)
        save_icon = QIcon('images/save.png')
        self.save_image_btn.setIcon(save_icon)
        self.save_image_btn.setIconSize(QSize(30,30))

        # design the left column layout
        self.subcol1.addWidget(self.choose_file_label)
        self.subcol1.addWidget(self.image_select_list)
        self.subcol1.addWidget(self.choose_filter_label)
        self.subcol1.addWidget(self.filter_list)
        self.subcol1.addWidget(self.choose_save_dir_label)
        self.save_row.addWidget(self.save_dir_input)
        self.save_row.addWidget(self.choose_save_dir_btn)
        self.subcol1.addLayout(self.save_row)
        self.subcol1.addWidget(self.save_image_btn)

        self.col1.addWidget(self.choose_directory_btn)
        self.col1.addWidget(self.subcol1_container)

        # Add the left column to the main layout
        self.main_row.addLayout(self.col1,2)
        
        # --- RIGHT COLUMN (Column 2) Widgets and Layout ---
        
        # This layout holds the main image and buttons
        self.col2 = QVBoxLayout()
        self.dark_mode = QCheckBox("Dark Mode")
        self.dark_mode.setObjectName("dark_mode")
        self.app_name = QLabel("PIC EDITOR")
        self.app_name.setFont(pacifico_font)
        self.app_name.setObjectName("appLabel")
        
        # Container and layout for the image and image name
        self.image_col_container = QWidget()
        self.image_col_container.setObjectName('image_col_container')

        # Pass the container widget to the layout constructor
        self.image_col = QVBoxLayout(self.image_col_container)
        self.image_col.setAlignment(Qt.AlignCenter)
        
        self.image_name_label = QLabel()
        self.image_name_label.setObjectName('image_name_label')
        self.image_name_label.setFont(zain_font)
        self.image_box = QLabel()
        self.image_col.addWidget(self.image_name_label)
        self.image_col.addWidget(self.image_box,9)
        
        # Container and layout for the buttons and texts
        self.button_and_text_col_container = QWidget()
        self.button_and_text_col_container.setObjectName('button_and_text_col_container')

        # Pass the container widget to the layout constructor
        self.button_and_text_col = QVBoxLayout(self.button_and_text_col_container)
        self.button_and_text_col.setAlignment(Qt.AlignHCenter)

        self.button_row = QHBoxLayout()
        self.left_button = QPushButton()
        left_button = QIcon('images/left.png')
        self.left_button.setIcon(left_button)
        self.right_button = QPushButton()
        right_button = QIcon('images/right.png')
        self.right_button.setIcon(right_button)
        self.blur_button = QPushButton()
        blur_button = QIcon('images/blur.png')
        self.blur_button.setIcon(blur_button)
        self.brightness_button = QPushButton()
        brightness_button = QIcon('images/brightness.png')
        self.brightness_button.setIcon(brightness_button)
        self.sharpness_button = QPushButton()
        sharpness_button = QIcon('images/sharpness.png')
        self.sharpness_button.setIcon(sharpness_button)
        self.contrast_button = QPushButton()
        contrast_button = QIcon('images/contrast.png')
        self.contrast_button.setIcon(contrast_button)
        self.grayscale_button = QPushButton()
        grayscale_button = QIcon('images/grayscale.png')
        self.grayscale_button.setIcon(grayscale_button)
        
        self.button_row.addWidget(self.left_button)
        self.button_row.addWidget(self.right_button)
        self.button_row.addWidget(self.sharpness_button)
        self.button_row.addWidget(self.brightness_button)
        self.button_row.addWidget(self.contrast_button)
        self.button_row.addWidget(self.blur_button)
        self.button_row.addWidget(self.grayscale_button)
        
        self.image_filter_description = QLabel()
        self.image_filter_description.setObjectName("image_filter_description")
        self.image_filter_description.setFont(zain_font)
        self.alert_label = QLabel("")
        self.alert_label.setFont(zain_font)
        
        self.button_and_text_col.addLayout(self.button_row)
        self.button_and_text_col.addWidget(self.image_filter_description)
        self.button_and_text_col.addWidget(self.alert_label)

        # Build the right column
        self.col2.addWidget(self.dark_mode)
        self.col2.addWidget(self.app_name)
        self.col2.addWidget(self.image_col_container,7)
        self.col2.addWidget(self.button_and_text_col_container)
        
        # Add the right column layout to the main layout
        self.main_row.addLayout(self.col2)

        # set app style
        self.setStyleSheet("""  
            #body{
                background-color: #2b0233;
            }                    
            #glass_morphed_container{
                background-color: rgba(255,255,255,250);
            }
                           
            #subcol1_container,#image_col_container,#button_and_text_col_container{
                background-color: #2b0233;
                border: none;
                border-radius: 15px;
            }
                           
            #dark_mode{
                margin-left: 300px;
                font-weight: 900;
            }
                           
            #appLabel{
                color: purple;
                text-align: center;
                font-size: 30px;
                font-weight: 900;
            }
            
            #choose_directory_btn{
                background-color: #2b0233;
                border-radius: 10px;
                font-size: 14px;
                font-weight: 900;
                padding: 5px 0px;
                color: white;
            }
            #choose_file_label,#choose_filter_label,#choose_save_dir_label{
                color: white;  
                font-size: 12px;              
            }
            #image_name_label{
                color: white;  
                font-size: 16px;  
                margin-left: 60px;            
            }
            #image_filter_description{
                color: white;
                font-size: 18px;
                margin-left: 60px;
            }
            #save_image_btn{
                color: white;
                background-color: #16021a;
                border-radius: 15px;
                border: 2px solid white;
                font-size: 14px;
                font-weight: 900;
                padding: 0px 5px;
            }
            QListWidget{
                color: black;
                border: 2px solid white;
                padding: 10px 10px 10px 10px;
                border-radius: 15px;
                text-align: center;
                font-size: 14px;
            }
        """)

        # event connections (unchanged)
        self.choose_directory_btn.clicked.connect(self.loadImages)
        self.image_select_list.clicked.connect(self.displayImage)
        self.right_button.clicked.connect(lambda: self.applyFilter("Rotate Right"))
        self.left_button.clicked.connect(lambda: self.applyFilter("Rotate Left"))
        self.contrast_button.clicked.connect(lambda: self.applyFilter("Contrast"))
        self.brightness_button.clicked.connect(lambda: self.applyFilter("Brightness"))
        self.sharpness_button.clicked.connect(lambda: self.applyFilter("Sharpness"))
        self.grayscale_button.clicked.connect(lambda: self.applyFilter("GrayScale"))
        self.blur_button.clicked.connect(lambda: self.applyFilter("Blur"))
        
        self.choose_save_dir_btn.clicked.connect(self.getUserSaveImageDir)
        self.save_image_btn.clicked.connect(self.saveImageInUserDir)

        self.setDefaultImage()

    # event functions (unchanged)
    def loadImages(self):
        self.image_select_list.clear()
        self.images_dir = QFileDialog.getExistingDirectory()
        if self.images_dir:
            self.extensions = ['.jpg','.png','.jpeg','.gif']
            self.images_list = self.filterFiles(os.listdir(self.images_dir),self.extensions)
            self.image_select_list.addItems(self.images_list)
            filters = ["Rotate Right","Rotate Left","Contrast","Brightness","Sharpness","GrayScale","Blur"]
            self.filter_list.addItems(filters)
        else:
            return

    def filterFiles(self,files,extensions):
        filtered_files = []
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filtered_files.append(file)
        return filtered_files
    
    def displayImage(self):
        self.button_press_num = 0
        self.image_filter_description.setText("")
        self.image_name = self.image_select_list.currentItem().text()
        self.image_fullname = os.path.join(self.images_dir,self.image_name)
        self.original_image = Image.open(self.image_fullname)
        self.work_on_image = self.original_image.copy()
        self.image_name_label.setText(self.image_name)
        self.setImage(self.image_fullname)

    def setDefaultImage(self):
        self.image_name_label.setText("Choose Image")
        image = QPixmap('images/default_image.png')
        w, h = 200,200
        image = image.scaled(w,h,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.image_box.setPixmap(image)
        self.image_box.show()

    def setImage(self,image_full_path):
        if image_full_path:
            self.image_box.hide()
            image = QPixmap(image_full_path)
            w, h = 200,200
            image = image.scaled(w,h,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.image_box.setPixmap(image)
            self.image_box.show()

    button_press_num = 1
    apply_filter_text = "Original"
    def applyFilter(self,filter):
        self.image_filter_description.clear()
        global button_press_num
        button_press_num = 1 
        global apply_filter_text
        apply_filter_text = "Original"
        if filter == apply_filter_text:
            self.work_on_image = self.original_image
        if self.image_name:
            mapping = {
                "Rotate Right": lambda image : image.rotate(-90, expand=True),
                "Rotate Left": lambda image : image.rotate(90),
                "Sharpness": lambda image : ImageEnhance.Sharpness(image).enhance(2.0),
                "Brightness": lambda image : ImageEnhance.Brightness(image).enhance(2.0),
                "Contrast": lambda image : ImageEnhance.Contrast(image).enhance(2.0),
                "GrayScale": lambda image : image.convert("L"),
                "Blur": lambda image : image.filter(ImageFilter.GaussianBlur(radius=3)),
            }
            apply_filter = mapping.get(filter)
            self.work_on_image = apply_filter(self.work_on_image)
            self.saveImage()
            edits_image_fullname = os.path.join(self.images_dir,self.save_dir,self.image_name)
            self.setImage(edits_image_fullname)
        if self.apply_filter_text == filter:
            self.button_press_num += 1
            self.image_filter_description.setText(f"{filter} {self.button_press_num}X")
        else:
            self.button_press_num = 1
            self.image_filter_description.setText(f"{filter} {self.button_press_num}X")
            self.apply_filter_text = filter 
                
    def saveImage(self):
        edits_image_path = os.path.join(self.images_dir,self.save_dir)
        if os.path.exists(edits_image_path) or os.path.isdir(edits_image_path):
            edits_image_fullname = os.path.join(edits_image_path,self.image_name)
            self.work_on_image.save(edits_image_fullname)
        else:
            os.makedirs(edits_image_path)
            edits_image_fullname = os.path.join(edits_image_path,self.image_name)
            self.work_on_image.save(edits_image_fullname)

    def getUserSaveImageDir(self):
        self.save_dir_input.clear()
        self.user_save_images_dir = QFileDialog.getExistingDirectory()
        if self.user_save_images_dir:
            self.save_dir_input.setText(self.user_save_images_dir)


    def saveImageInUserDir(self):
        save_dir_input_text = self.save_dir_input.text()
        if save_dir_input_text and self.work_on_image:
            pic_editor_images_path = save_dir_input_text + "/Pic Editor"
            self.save_dir_input.clear()
            QMessageBox.information(self, "Save Image", "Now Enter the image name", QMessageBox.Ok)
            edited_image_name, ok = QInputDialog.getText(self,"File name","Enter an image name and don't change the extension i.e .png, .jpg etc",QLineEdit.Normal,self.image_name)
            if os.path.exists(pic_editor_images_path) or os.path.isdir(pic_editor_images_path):
                pic_editor_image_fullname = os.path.join(pic_editor_images_path,edited_image_name)
                self.work_on_image.save(pic_editor_image_fullname)
                QMessageBox.information(self, "Save Image", f"Image saved successfully in {pic_editor_images_path}", QMessageBox.Ok)
            else:
                os.makedirs(pic_editor_images_path)
                pic_editor_image_fullname = os.path.join(pic_editor_images_path,self.image_name)
                self.work_on_image.save(pic_editor_image_fullname)
                QMessageBox.information(self, "Save Image", f"Image saved successfully in {pic_editor_images_path}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Save Image", "Choose an Image  and Enter a Valid Directory", QMessageBox.Ok)

# set app objects and settings
if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('Fusion')
    app.setObjectName('app')
    main = PicEditor()
    main.setWindowTitle("PIC EDITOR")
    main.setObjectName('body')
    main.resize(600,600)
    main.show()
    app.exec_()