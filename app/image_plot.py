import matplotlib.pyplot as plt
import matplotlib
import base64
from io import BytesIO
import cv2 
import numpy as np 
matplotlib.use('Agg')

def imageToPlot(image_path, scale=100, thresh=100):
    fig = plt.figure()
    img = cv2.imread(image_path)
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    image = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST )
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, binary = cv2.threshold(gray, thresh, thresh, cv2.THRESH_BINARY_INV)

    # GRAB EXTERNAL CONTOUR
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    data = np.vstack(contours).squeeze()
    # np.savetxt("test-test.txt", data, fmt="%d")

    x = [sub[0]/scale for sub in data]
    y = [sub[1]/scale for sub in data]

    tmpfile = BytesIO()
    plt.scatter(x,y)
    plt.plot(x,y)
    fig.savefig(tmpfile, format='png')
    plt.close(fig)
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = 'data:image/png;base64,{}'.format(encoded) 
    return [html, [x,y]]

