#!/usr/bin/env python
# coding: utf-8

# In[35]:


# prompt: colour detection of an image

from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[36]:


# Load the image
image = Image.open('colorpic.jpg')


# In[37]:


# Convert the image to a NumPy array
image_array = np.array(image)

# Get the RGB values of each pixel
red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

# Calculate the average RGB values
average_red = np.mean(red_channel)
average_green = np.mean(green_channel)
average_blue = np.mean(blue_channel)

# Print the average RGB values
print('Average red:', average_red)
print('Average green:', average_green)
print('Average blue:', average_blue)

# Determine the dominant colour
if average_red > average_green and average_red > average_blue:
  print('Dominant colour: red')
elif average_green > average_red and average_green > average_blue:
  print('Dominant colour: green')
else:
  print('Dominant colour: blue')


# In[38]:


#reading csv file
image = pd.read_csv('colors.csv')


# In[39]:


image.head()


# In[40]:


image.tail()


# In[41]:


type(image)


# In[42]:


print(len(image))


# In[43]:


# Calculate average color values for each channel
average_color = np.mean(image_array, axis=(0, 1))


# In[44]:


def plot_bar_graph(average_color):
    colors = ['red', 'green', 'blue']
    plt.bar(colors, average_color, color=colors)
    plt.title('Average Color Values')
    plt.xlabel('Color Channels')
    plt.ylabel('Average Value')
    plt.show()


# In[34]:


# Plot the bar graph
plot_bar_graph(average_color)


# In[ ]:




