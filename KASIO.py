# import os

# from wand.image import Image

# with Image(filename='2.pdf', resolution=300) as img:
#     img.format = 'png'
#     img.compression_quality = 80
#     img.save(filename='output.png')

# import os
# import git
# from wand.image import Image

# # Set the repository URL and local directory
# repo_url = 'https://github.com/ZiedDhoukar/KASIO.git'
# local_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO'

# # Set the input and output directories
# input_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO/PDF'
# output_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO/receipts-images'

# # Clone the repository to the local directory
# if not os.path.exists(local_dir):
#     git.Repo.clone_from(repo_url, local_dir)

# # Convert the PDF files to images and save them in the output directory
# for filename in os.listdir(os.path.join(local_dir, input_dir)):
#     if filename.endswith('.pdf'):
#         input_path = os.path.join(local_dir, input_dir, filename)
#         output_path = os.path.join(local_dir, output_dir, filename.replace('.pdf', '.png'))
#         with Image(filename=input_path, resolution=300) as img:
#             img.format = 'png'
#             img.compression_quality = 80
#             img.save(filename=output_path)

# # Commit the changes to the local repository and push them to the remote repository
# repo = git.Repo(local_dir)
# repo.git.add(update=True)
# repo.index.commit('Converted PDF files to images')
# repo.remote().push()


# import os
# import git
# from wand.image import Image

# # Set the repository URL and local directory
# repo_url = 'https://github.com/ZiedDhoukar/KASIO.git'
# local_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO'

# # Set the input and output directories
# input_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO/PDF'
# output_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO/receipts-images'

# # Clone the repository to the local directory
# if not os.path.exists(local_dir):
#     git.Repo.clone_from(repo_url, local_dir)

# # Convert the PDF files to images and save them in the output directory
# for filename in os.listdir(os.path.join(local_dir, input_dir)):
#     if filename.endswith('.pdf'):
#         input_path = os.path.join(local_dir, input_dir, filename)
#         output_path = os.path.join(local_dir, output_dir, filename.replace('.pdf', '.jpg'))
#         with Image(filename=input_path, resolution=300) as img:
#             img.format = 'jpeg'
#             img.compression_quality = 80
#             img.save(filename=output_path)

# # Commit the changes to the local repository and push them to the remote repository
# repo = git.Repo(local_dir)
# repo.git.add(update=True)
# repo.index.commit('Converted PDF files to images')
# repo.remote().push()

import os
import git
from wand.image import Image

# Set the repository URL and local directory
repo_url = 'https://github.com/ZiedDhoukar/KASIO.git'
local_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO'

# Set the input and output directories
input_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/PDF'
output_dir = 'C:/Users/Administrator/Desktop/KASIO/AI-model/KASIO/Dataset'

# Clone the repository to the local directory
if not os.path.exists(local_dir):
    git.Repo.clone_from(repo_url, local_dir)

# Convert the PDF files to images and save them in the output directory
for root, dirs, files in os.walk(os.path.join(local_dir, input_dir)):
    for filename in files:
        if filename.endswith('.pdf'):
            input_path = os.path.join(root, filename)
            output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir).replace('.pdf', '.jpg'))
            with Image(filename=input_path, resolution=300) as img:
                img.format = 'jpeg'
                img.compression_quality = 80
                img.save(filename=output_path)

# Commit the changes to the local repository
repo = git.Repo(local_dir)
repo.git.add(update=True)
repo.index.commit('Converted PDF files to images')

# Push the changes to the remote repository
try:
    repo.remote().push()
    print('Pushed changes to remote repository')
except git.exc.GitCommandError as e:
    print('Failed to push changes to remote repository:', e)
