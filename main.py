# %% [markdown]
# Look the files in docs folder

# %%
import os

try:
    docs = os.listdir("./docs")
except FileNotFoundError as error:
    os.mkdir('./docs')


# %% [markdown]
# Import library to convert pdf pages to images

# %%
from pdf2image import convert_from_path


# %% [markdown]
# Convert to images, this returns an PIL array

# %%
for doc in docs:

    try:
        os.mkdir('./converted/'+doc[:-4])
    except OSError as error:
        print(error)

    images = convert_from_path('./docs/'+doc)
    for i in range(len(images)):
        images[i].save('./converted/'+doc[:-4]+'/'+str(i+1)+'.png', 'PNG')



