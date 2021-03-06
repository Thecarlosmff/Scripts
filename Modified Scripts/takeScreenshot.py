# To use in https://visual-novel-ocr.sourceforge.io
import mss
import mss.tools

def takeScreenshot(top, left, width, height):
    with mss.mss() as sct:
        from datetime import datetime
        # datetime object containing current date and time
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%Y-%m-%d--%H-%M-%S")
        path = 'C:/Screenshots/'
        dt_string = path + dt_string + '.png'

#---------------------------------------------------------------------------------
        # The screen part to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = "capturedImage.png".format(**monitor)
        output_screenshot = dt_string.format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)

#---------------------------------------------------------------------------------

        #saves the image for the prints...
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_screenshot)
        print(output_screenshot)
