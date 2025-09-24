import math
import os

import cv2
import numpy as np
from numpy import linspace
from scipy.interpolate import interp1d

import zebrazoom.videoFormatConversion.zzVideoReading as zzVideoReading

from ._tailTrackingBase import TailTrackingBase


class HeadEmbeddedTailTrackingTeresaNicolsonMixin(TailTrackingBase):
  @staticmethod
  def __smoothTail(points, nbTailPoints):
    y = points[0]
    x = linspace(0, 1, len(y))

    if len(x) > 3:

      points2 = []
      for i in range(0, len(points[0])-1):
        if not((points[0][i] == points[0][i+1]) and (points[1][i] == points[1][i+1])):
          points2.append([points[0][i], points[1][i]])

      i = len(points[0]) - 1
      if not((points[0][i-1] == points[0][i]) and (points[1][i-1] == points[1][i])):
        points2.append([points[0][i], points[1][i]])

      points = np.array(points2).T

      # Define some points:
      points = np.array([points[0], points[1]]).T  # a (nbre_points x nbre_dim) array

      # Linear length along the line:
      distance = np.cumsum( np.sqrt(np.sum( np.diff(points, axis=0)**2, axis=1 )) )
      distance = np.insert(distance, 0, 0)/distance[-1]

      # Interpolation for different methods:
      interpolation_method = 'quadratic'    # 'slinear', 'quadratic', 'cubic'
      alpha = np.linspace(0, 1, nbTailPoints)

      interpolated_points = {}

      interpolator =  interp1d(distance, points, kind=interpolation_method, axis=0)
      interpolated_points = interpolator(alpha)

      interpolated_points = interpolated_points.T

      newX = interpolated_points[0]
      newY = interpolated_points[1]

    else:

      newX = points[0]
      newY = points[1]

    return [newX, newY]

  def __findNextPoints(self, depth, x, y, frame, points, angle, maxDepth, steps, nbList, initialImage, debug):
    lenX = len(frame[0]) - 1
    lenY = len(frame) - 1

    thetaDiffAccept = 1 #0.4

    if depth < 0.15*maxDepth:
      thetaDiffAccept = 0.4

    if depth > 0.85*maxDepth:
      thetaDiffAccept = 0.6

    pixTotMax = 1000000
    maxTheta  = angle

    l = [i*(math.pi/nbList) for i in range(0,2*nbList) if self._distBetweenThetas(i*(math.pi/nbList), angle) < thetaDiffAccept]

    if debug:
      print("debug")

    xTot = self._assignValueIfBetweenRange(x + steps[0], 0, lenX)
    yTot = self._assignValueIfBetweenRange(y, 0, lenY)
    if yTot == 0:
      yTot = 400

    for step in steps:

      for theta in l:

        xNew = self._assignValueIfBetweenRange(int(x + step * (math.cos(theta))), 0, lenX)
        yNew = self._assignValueIfBetweenRange(int(y + step * (math.sin(theta))), 0, lenY)
        pixTot = frame[yNew][xNew]

        if debug:
          print([theta,pixTot])

        # Keeps that theta angle as maximum if appropriate
        if (pixTot < pixTotMax):
          pixTotMax = pixTot
          maxTheta = theta
          if depth < 0.4*maxDepth:
            if xNew > x:
              xTot = xNew
              yTot = yNew
          else:
            xTot = xNew
            yTot = yNew

    w = 8 # THIS IS IMPORTANT
    ym = yTot - w
    yM = yTot + w
    xm = xTot - w
    xM = xTot + w
    if ym < 0:
      ym = 0
    if xm < 0:
      xm = 0
    if yM > len(initialImage):
      yM = len(initialImage)
    if xM > len(initialImage[0]):
      xM = len(initialImage[0])

    pixSur = np.min(initialImage[ym:yM, xm:xM])
    if debug:
      print("depth:", depth, " ; maxDepth:", maxDepth, " ; pixSur:", pixSur)

    # if depth > 0.95*maxDepth:
      # pixTot = frame[y][x]
      # if (pixTot < pixTotMax):
        # pixTotMax = pixTot
        # maxTheta = theta
        # xTot = x
        # yTot = y
        # depth = maxDepth + 10

    if debug:
      print(["max:",maxTheta,pixTotMax])

    # Calculates distance between new and old point
    distSubsquentPoints = math.sqrt((xTot - x)**2 + (yTot - y)**2)

    pixSurMax = 150
    if ((pixSur < pixSurMax) or (depth < 2*0.85*maxDepth)):
      points = self._appendPoint(xTot, yTot, points)
      if debug:
        cv2.circle(frame, (xTot, yTot), 3, (255,0,0),   -1)
        self._debugFrame(frame, title='HeadEmbeddedTailTracking')

    newTheta = self._calculateAngle(x,y,xTot,yTot)

    if (distSubsquentPoints > 0) and (depth < 2*maxDepth) and (xTot < 1280 - 10) and (yTot > 10) and (yTot < 1024 - 10) and ((pixSur < pixSurMax) or (depth < 2*0.85*maxDepth)):
      (points,nop) = self.__findNextPoints(depth+distSubsquentPoints,xTot,yTot,frame,points,newTheta,maxDepth,steps,nbList,initialImage,debug)

    return (points,newTheta)

  def _headEmbededTailTrackingTeresaNicolson(self, headPosition, frame, maxDepth, tailTip, threshForBlackFrames):
    steps   = self._hyperparameters["step"]
    nbList  = 10

    x = headPosition[0]
    y = headPosition[1]

    initialImage = frame.copy()

    gaussian_blur = self._hyperparameters["headEmbededParamGaussianBlur"]
    frame = cv2.GaussianBlur(frame, (gaussian_blur, gaussian_blur), 0)
    # angle = self._hyperparameters["headEmbededParamInitialAngle"]
    angle = self._calculateAngle(x, y, tailTip[0], tailTip[1])

    points = np.zeros((2, 0))

    if np.mean(np.mean(frame)) > threshForBlackFrames:
      (points, lastFirstTheta2) = self.__findNextPoints(0,x,y,frame,points,angle,maxDepth,steps,nbList,initialImage,self._hyperparameters["debugHeadEmbededFindNextPoints"])
      points = np.insert(points, 0, headPosition, axis=1)
      if len(points[0]) > 3:
        points = self.__smoothTail(points, self._nbTailPoints)
      points[0][0] = headPosition[0]
      points[1][0] = headPosition[1]
    else:
      points = np.zeros((2, self._nbTailPoints))

    output = np.zeros((1, len(points[0]), 2))

    for idx, x in enumerate(points[0]):
      output[0][idx][0] = x
      output[0][idx][1] = points[1][idx]

    return output

  def _headEmbededTailTrackFindMaxDepthTeresaNicolson(self, frame):
    x = self._headPositionFirstFrame[0]
    y = self._headPositionFirstFrame[1]

    steps   = self._hyperparameters["step"]
    nbList  = 10

    initialImage = frame.copy()

    gaussian_blur = self._hyperparameters["headEmbededParamGaussianBlur"]
    frame = cv2.GaussianBlur(frame, (gaussian_blur, gaussian_blur), 0)

    angle = self._calculateAngle(x, y, self._tailTipFirstFrame[0], self._tailTipFirstFrame[1])

    points = np.zeros((2, 0))

    (points, lastFirstTheta2) = self.__findNextPoints(0,x,y,frame,points,angle,self._hyperparameters["headEmbededTailTrackFindMaxDepthInitialMaxDepth"],steps,nbList,initialImage, self._hyperparameters["debugHeadEmbededFindNextPoints"])

    distToTip        = np.full((200),10000)
    curTailLengthTab = np.full((200),10000)
    curTailLength  = 0
    k = 0

    distFromHeadToTip = abs(math.sqrt((x-self._tailTipFirstFrame[0])**2 + (y-self._tailTipFirstFrame[1])**2))
    while (curTailLength < 1.5*distFromHeadToTip) and (k < len(points[0])-1):
      curTailLength = curTailLength + abs(math.sqrt((points[0,k]-points[0,k+1])**2 + (points[1,k]-points[1,k+1])**2))
      distToTip[k]  = abs(math.sqrt((points[0,k]-self._tailTipFirstFrame[0])**2 + (points[1,k]-self._tailTipFirstFrame[1])**2))
      curTailLengthTab[k] = curTailLength
      k = k + 1

    minDistToTip    = 1000000
    indMinDistToTip = 0
    for idx, dist in enumerate(distToTip):
      if dist < minDistToTip:
        minDistToTip = dist
        indMinDistToTip = idx

    return (curTailLengthTab[indMinDistToTip] )

  def __getMeanOfImageOverVideo(self):
    cap = zzVideoReading.VideoCapture(self._videoPath)
    meanss = []
    ret = True
    i = 0
    while (i < 100):
      ret, frame = cap.read()
      if ret:
        if self._hyperparameters["invertBlackWhiteOnImages"]:
          frame = 255 - frame
        val = np.mean(np.mean(frame))
        meanss.append(val)
      i = i +1
    return np.mean(meanss)

  def _getThresForBlackFrame(self):
    threshForBlackFrames = 0
    if self._hyperparameters["headEmbededTeresaNicolson"] == 1:
      imagesMeans = self.__getMeanOfImageOverVideo()
      threshForBlackFrames = imagesMeans * 0.8 #0.75
    return threshForBlackFrames

  def _savingBlackFrames(self, output):
    if self._hyperparameters["headEmbededTeresaNicolson"] == 1:
      if self._hyperparameters["noBoutsDetection"] == 1:
        outputPath = os.path.join(self._hyperparameters["outputFolder"], self._hyperparameters['videoNameWithTimestamp'])
        if not os.path.exists(outputPath):
          os.makedirs(outputPath)
        with open(os.path.join(outputPath, f'blackFrames_{self._videoName}.csv'), "a") as f:
          for k in range(1,len(output[0])):
            if np.sum(output[0, k]) == 0:
              output[0, k] = output[0, k-1]
              f.write(str(k)+'\n')
