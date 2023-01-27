import os
import shutil

def replace_image(source, source_dir, target, target_dir):
    print("removes {}".format(target))
    print("copies in {} to {} from {}".format(source, target_dir, source_dir))
    os.remove(os.path.join(target_dir, target))
    shutil.move(os.path.join(source_dir, source), target_dir)
    return None
    
def file_in_directory(file, directory):
    if file in os.listdir(directory):
        return True
    return False
    
    
if __name__ == "__main__":

    source_parent = r"C:\Users\hpc123\Pictures"
    target_parent = r"E:\Pictures"
    
    target_dir_list = ["c u 51 31"]

    
    for dir in target_dir_list:
        target_dir = os.path.join(target_parent, dir)
        source_dir = os.path.join(source_parent, dir)
        
        print("Replacing images in {}".format(dir))
        
        image_list = os.listdir(target_dir)
    
        for image in image_list:
            if file_in_directory(image, source_dir):
                replace_image(image, source_dir, image, target_dir)
                print(image)