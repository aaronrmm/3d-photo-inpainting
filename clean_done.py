import os
import shutil


if __name__ == "__main__":
    input_dir_path = os.path.abspath("./image")
    done_dir_path = os.path.abspath("./done2")
    os.makedirs(done_dir_path, exist_ok=True)
    
    input_names = os.listdir(input_dir_path)
    print(len(input_names), "images in",input_dir_path)
    
    video_indexes = {}
    output_dir_path = os.path.abspath("./video")
    video_names = os.listdir(output_dir_path)
    for name in video_names:
        index = video_indexes.get(name[0]) or []
        index.append(name)
        video_indexes[name[0]] = index
        
    for input_name in input_names:
        video_index = video_indexes[input_name[0]]
        name_base = os.path.splitext(input_name)[0]
        for video in video_index:
            if name_base in video:
                shutil.move(
                    os.path.join(input_dir_path, input_name),
                    os.path.join(done_dir_path, input_name)
                )
                break
