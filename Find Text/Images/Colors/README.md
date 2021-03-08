
## How colors work

### Hue

On  the image below we can see the equivalent to Hue being from the range 0 to 1, the Saturation and Value can be any value (*py PyRun.py PyFunction.ImageToText.remove_bg img1.png 0 0 0 1 255 255*). To find the color range you want you need to rotate to the left until you find the right Hue range (0-179). We can call the hue as pure color.

<img src="https://github.com/Thecarlosmff/Scripts/blob/main/Find%20Text/Images/Hue.gif" alt="Hue Gif" class="inline" width="300" height="300"/>

[Hue Image](https://github.com/Thecarlosmff/Scripts/blob/main/Find%20Text/Images/pnghut_color-wheel-complementary-colors-scheme-analogous-of-lead.png)

### Saturation

Using the Red color as we found in the Hue let's use a Hue between 170-179 & 0-9. In the program, we use *py PyRun.py PyFunction.ImageToText.remove_bg img1.png 170 0 0 9 255 255* this should give us most of the Red, but if we want a specific part let's start by changing the Saturation. The previous image can be tricky because not much really changes if we alter the other parameters. Let's use: [Saturation Image](https://github.com/Thecarlosmff/Scripts/blob/c92781933cc3c9e91e6bf81a89226d8f2b8e6c43/Find%20Text/Images/pnghut_depth-color-wheel-photography-theory-magenta-vector-hand-drawn-ring.png).
Applying the command above we have

<img src="https://github.com/Thecarlosmff/Scripts/blob/e889f06bac5df88aee036a5d78c6b6481ee5576c/Find%20Text/Images/Saturation%20Not%20Applyed.png" alt="Hue Gif" class="inline" width="300" height="300"/>

Now changing the saturation for something bewteen 200 and 255 we got:

<img src="https://github.com/Thecarlosmff/Scripts/blob/55a3111b0d5d93fa9b3995f0a12237ad072b55c6/Find%20Text/Images/Saturation%20Applyed.png" alt="Hue Gif" class="inline" width="300" height="300"/>
We were capable of reducing the tone that were more pinkish and the less intense red by increasing the lower limit.
So saturation changes the intensity of a color, the higher the saturation more vivid is the color.

### Value

The value determites the amount of light in a color.
Use the previous configuration on another image where we have a value between 0-255 (so anything goes) and decrease the upper limit in the value for 150 the red with more light will disapear.

###### Original

<img src="https://github.com/Thecarlosmff/Scripts/blob/91dffe3e7f2fc241b602d6f8fdf001abfda1017b/Find%20Text/Images/Shades-of-red2-1.jpg" alt="Hue Gif" class="inline" width="400" height="300"/>

###### Hue and Saturation

<img src="https://github.com/Thecarlosmff/Scripts/blob/91dffe3e7f2fc241b602d6f8fdf001abfda1017b/Find%20Text/Images/Shades-of-red2-2.png" alt="Hue Gif" class="inline" width="400" height="300"/>

###### Value between 0 and 150

<img src="https://github.com/Thecarlosmff/Scripts/blob/91dffe3e7f2fc241b602d6f8fdf001abfda1017b/Find%20Text/Images/Shades-of-red2-3.png" alt="Hue Gif" class="inline" width="400" height="300"/>

