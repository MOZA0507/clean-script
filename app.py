import os
import datetime
import shutil
from dotenv import load_dotenv
load_dotenv()

dir_path = os.getenv(r"PATH_DIR")
name_created = os.getenv("FILE_CREATED")
current_folder = os.getenv("CURRENT_FOLDER")
res = os.listdir(dir_path)


try:
  for r in res:
    if ".lnk" not in r and ".url" not in r and name_created not in r and current_folder not in r:
      #print(r)
      file_old_path = dir_path+"/"+r
      date_file = os.path.getctime(dir_path+'/'+r)
      directory = datetime.datetime.fromtimestamp(date_file).year
      new_path = dir_path + "/" + str(directory) + name_created
      #print(file_old_path)
      if os.path.exists(new_path):
        shutil.move(file_old_path, new_path)
      else:
        os.mkdir(new_path)
except:
  print("An exception occurred")


