#Display the image below Where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#iterate over picture
for image in picture:
    for pixel in image:
        if pixel == 1:
            print("*", end="")
        elif pixel == 0:
            print(" ", end="")
    print(" ")