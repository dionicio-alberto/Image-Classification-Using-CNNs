from pathlib import Path
import shutil
import random
import piexif

def train_test_split(data_raw: Path, data_folder_s: Path, train_size = 0.8):
    
    #Make sure we remove any existing forlders
    shutil.rmtree(str(data_folder_s.joinpath('Train','Cat')), ignore_errors=True)
    shutil.rmtree(str(data_folder_s.joinpath('Train','Dog')), ignore_errors=True)
    shutil.rmtree(str(data_folder_s.joinpath('Test','Cat')), ignore_errors=True)
    shutil.rmtree(str(data_folder_s.joinpath('Test','Dog')), ignore_errors=True)
    
    # Create new empty train and test folders
    data_folder_s.joinpath('Test','Cat').mkdir(parents=True, exist_ok=True)
    data_folder_s.joinpath('Test','Dog').mkdir(parents=True, exist_ok=True)
    data_folder_s.joinpath('Train','Cat').mkdir(parents=True, exist_ok=True)
    data_folder_s.joinpath('Train','Dog').mkdir(parents=True, exist_ok=True)
    
    # Get the numbers of cats and dogs
    list_cats = []
    for archivo in data_raw.joinpath('Cat').rglob('*'):
        if archivo.is_file():
            list_cats.append(archivo)
    
    num_cat_images = len(list_cats)
    num_cat_images_train = int(train_size * num_cat_images)
    num_cat_images_test = num_cat_images - num_cat_images_train
            
    list_dogs = []
    for archivo in data_raw.joinpath('Dog').rglob('*'):
        if archivo.is_file():
            list_dogs.append(archivo)
    num_dog_images = len(list_dogs)
    num_dog_images_train = int(train_size * num_dog_images)
    num_dog_images_test = num_dog_images - num_dog_images_train

    cat_train_images = random.sample(list_cats, num_cat_images_train)
    cat_test_images  = [img for img in list_cats if img not in cat_train_images]
    for img in cat_train_images:
        shutil.copy(str(img), dst=str(data_folder_s.joinpath('Train','Cat')))
    for img in cat_test_images:
        shutil.copy(src=str(img), dst=str(data_folder_s.joinpath('Test','Cat')))
        
    dog_train_images = random.sample(list_dogs, num_dog_images_train)
    dog_test_images  = [img for img in list_dogs if img not in dog_train_images]
    for img in dog_train_images:
        shutil.copy(str(img), dst=str(data_folder_s.joinpath('Train','Dog')))
    for img in dog_test_images:
        shutil.copy(src=str(img), dst=str(data_folder_s.joinpath('Test','Dog')))
        
    remove_exif_data(data_folder_s.joinpath('Train'))
	remove_exif_data(data_folder_s.joinpath('Test'))

# helper function to remove corrupt exif data from Microsoft's dataset
def remove_exif_data(paths: Path):
    list_cats = []
    for archivo in paths.joinpath('Cat').rglob('*'):
        if archivo.is_file():
            list_cats.append(archivo)
            
    for img in list_cats:
        try:
            piexif.remove(str(img))
        except:
            pass

    list_dogs = []
    for archivo in paths.joinpath('Dog').rglob('*'):
        if archivo.is_file():
            list_dogs.append(archivo)
            
    for img in list_dogs:
        try:
            piexif.remove(str(img))
        except:
            pass